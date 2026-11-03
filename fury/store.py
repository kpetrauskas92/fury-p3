"""
STORE:
Keeps registered players and their scores.

Players are looked up by name and city, never by row position, so
scores always go to the right player.

When Supabase is configured the leaderboard is shared by everyone
(see supabase/schema.sql). Otherwise scores are saved on this device:
in the browser's localStorage, or in a JSON file for the terminal version.
"""
import asyncio
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

IN_BROWSER = sys.platform == "emscripten"

# Points every newly registered player starts with
BONUS_SCORE = 100

# Most points one game can give: 10 hits * 10 points * 1.3 (hard)
MAX_POINTS_PER_GAME = 130

LOCAL_STORAGE_KEY = "fury.players"


class StoreError(Exception):
    """Raised when scores can't be read or saved."""


def player_key(name, city):
    """Returns the key that identifies a player, ignoring letter case."""
    return f"{name.lower()}|{city.lower()}"


def check_points(points):
    """Rejects scores that a single game can't produce."""
    if not 0 <= points <= MAX_POINTS_PER_GAME:
        raise StoreError(f"Invalid score: {points}")


class LocalStore:
    """
    Stores players in a dictionary keyed by name and city.
    The load and save functions decide where the dictionary is kept.
    """
    shared = False

    def __init__(self, load, save):
        self._load = load
        self._save = save

    async def find(self, name, city):
        """Returns the player's record with their rank, or None."""
        players = self._load()
        record = players.get(player_key(name, city))
        if record is None:
            return None
        rank = 1 + sum(
            1 for other in players.values() if other["score"] > record["score"])
        return {**record, "rank": rank}

    async def register(self, name, city):
        """Adds a new player. Returns False if they already exist."""
        players = self._load()
        key = player_key(name, city)
        if key in players:
            return False
        players[key] = {"name": name, "city": city, "score": BONUS_SCORE}
        self._save(players)
        return True

    async def add_score(self, name, city, points):
        """Adds points to the player's total and returns the new total."""
        check_points(points)
        players = self._load()
        record = players.get(player_key(name, city))
        if record is None:
            raise StoreError("Player not found")
        record["score"] += points
        self._save(players)
        return record["score"]

    async def top(self, limit=10):
        """Returns the best players, highest score first."""
        players = sorted(
            self._load().values(), key=lambda p: p["score"], reverse=True)
        return players[:limit]


class SupabaseStore:
    """
    Stores players in a Supabase table, shared by everyone.
    Writes go through database functions that validate the scores.
    """
    shared = True

    def __init__(self, url, key):
        self._url = url.rstrip("/")
        self._headers = {
            "apikey": key,
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
        }

    async def _rpc(self, function, **params):
        return await request_json(
            "POST", f"{self._url}/rest/v1/rpc/{function}",
            self._headers, params)

    async def find(self, name, city):
        """Returns the player's record with their rank, or None."""
        rows = await self._rpc("find_player", p_name=name, p_city=city)
        return rows[0] if rows else None

    async def register(self, name, city):
        """Adds a new player. Returns False if they already exist."""
        return bool(
            await self._rpc("register_player", p_name=name, p_city=city))

    async def add_score(self, name, city, points):
        """Adds points to the player's total and returns the new total."""
        check_points(points)
        return await self._rpc(
            "add_score", p_name=name, p_city=city, p_points=points)

    async def top(self, limit=10):
        """Returns the best players, highest score first."""
        return await request_json(
            "GET",
            f"{self._url}/rest/v1/players?select=name,city,score"
            f"&order=score.desc,created_at.asc&limit={int(limit)}",
            self._headers)


async def request_json(method, url, headers, body=None):
    """
    Sends an HTTP request and returns the decoded JSON response.
    Uses the browser's fetch on Pyodide and urllib everywhere else.
    """
    data = None if body is None else json.dumps(body)
    try:
        if IN_BROWSER:
            # pylint: disable=import-outside-toplevel
            from pyodide.http import pyfetch
            response = await pyfetch(
                url, method=method, headers=headers, body=data)
            ok, status = response.ok, response.status
            text = await response.string()
        else:
            ok, status, text = await asyncio.to_thread(
                _urllib_request, method, url, headers, data)
    except Exception as err:  # pylint: disable=broad-except
        raise StoreError("Couldn't reach the leaderboard.") from err
    if not ok:
        raise StoreError(f"Leaderboard error {status}: {text[:200]}")
    return json.loads(text) if text else None


def _urllib_request(method, url, headers, data):
    request = urllib.request.Request(
        url, method=method, headers=headers,
        data=None if data is None else data.encode())
    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            return True, response.status, response.read().decode()
    except urllib.error.HTTPError as err:
        return False, err.code, err.read().decode()


def _supabase_config():
    """
    Reads the Supabase settings: web/config.js in the browser,
    FURY_SUPABASE_URL and FURY_SUPABASE_KEY in a terminal.
    """
    if IN_BROWSER:
        import js  # pylint: disable=import-outside-toplevel
        config = getattr(js, "FURY_CONFIG", None)
        if config is None:
            return None, None
        return (getattr(config, "supabaseUrl", None),
                getattr(config, "supabaseAnonKey", None))
    return (os.environ.get("FURY_SUPABASE_URL"),
            os.environ.get("FURY_SUPABASE_KEY"))


def _browser_store():
    import js  # pylint: disable=import-outside-toplevel

    def load():
        try:
            return json.loads(js.localStorage.getItem(LOCAL_STORAGE_KEY) or "{}")
        except Exception:  # pylint: disable=broad-except
            return {}

    def save(players):
        try:
            js.localStorage.setItem(LOCAL_STORAGE_KEY, json.dumps(players))
        except Exception as err:  # pylint: disable=broad-except
            raise StoreError("This browser won't let the game save.") from err

    return LocalStore(load, save)


def file_store(path):
    """Returns a LocalStore that keeps players in a JSON file."""
    path = Path(path)

    def load():
        try:
            return json.loads(path.read_text(encoding="utf8"))
        except FileNotFoundError:
            return {}
        except (OSError, ValueError) as err:
            raise StoreError(f"Couldn't read {path}") from err

    def save(players):
        try:
            path.write_text(json.dumps(players, indent=2), encoding="utf8")
        except OSError as err:
            raise StoreError(f"Couldn't write {path}") from err

    return LocalStore(load, save)


def get_store():
    """Returns the shared Supabase store if configured, else a local one."""
    url, key = _supabase_config()
    if url and key:
        return SupabaseStore(str(url), str(key))
    if IN_BROWSER:
        return _browser_store()
    return file_store(os.environ.get(
        "FURY_SCORES_FILE", Path.home() / ".fury_scores.json"))

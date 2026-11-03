"""Tests for saving players and scores, and the menus that use them."""
import asyncio
import json

import pytest

from fury import store as store_module
from fury.login import login
from fury.register import register
from fury.store import BONUS_SCORE, StoreError, file_store


@pytest.fixture
def store(tmp_path):
    return file_store(tmp_path / "scores.json")


def test_register_then_find_with_rank(store):
    assert asyncio.run(store.register("Tom", "Riga"))
    assert asyncio.run(store.register("Ann", "Oslo"))
    asyncio.run(store.add_score("Ann", "Oslo", 50))
    assert asyncio.run(store.find("tom", "RIGA")) == {
        "name": "Tom", "city": "Riga", "score": BONUS_SCORE, "rank": 2}


def test_register_twice_is_refused(store):
    assert asyncio.run(store.register("Tom", "Riga"))
    assert not asyncio.run(store.register("TOM", "riga"))


def test_scores_go_to_the_right_player_after_ranks_change(store):
    # The old version tracked players by sheet row, which moved
    # whenever the leaderboard was re-sorted.
    for name in ("Ann", "Bob", "Cat"):
        asyncio.run(store.register(name, "Oslo"))
    asyncio.run(store.add_score("Cat", "Oslo", 100))
    asyncio.run(store.add_score("Cat", "Oslo", 30))
    asyncio.run(store.add_score("Ann", "Oslo", 10))
    scores = {p["name"]: p["score"] for p in asyncio.run(store.top())}
    assert scores == {"Cat": 230, "Ann": 110, "Bob": 100}
    assert [p["name"] for p in asyncio.run(store.top(2))] == ["Cat", "Ann"]


def test_impossible_scores_are_rejected(store):
    asyncio.run(store.register("Tom", "Riga"))
    with pytest.raises(StoreError):
        asyncio.run(store.add_score("Tom", "Riga", 131))


def test_scores_survive_a_restart(tmp_path):
    path = tmp_path / "scores.json"
    asyncio.run(file_store(path).register("Tom", "Riga"))
    assert json.loads(path.read_text())["tom|riga"]["score"] == BONUS_SCORE
    assert asyncio.run(file_store(path).find("Tom", "Riga"))["rank"] == 1


def test_get_store_uses_supabase_when_configured(monkeypatch):
    monkeypatch.setenv("FURY_SUPABASE_URL", "https://example.supabase.co/")
    monkeypatch.setenv("FURY_SUPABASE_KEY", "anon-key")
    store = store_module.get_store()
    assert isinstance(store, store_module.SupabaseStore) and store.shared


def test_supabase_store_calls_the_database_functions(monkeypatch):
    calls = []

    async def fake_request(method, url, headers, body=None):
        calls.append((method, url, body))
        return 230

    monkeypatch.setattr(store_module, "request_json", fake_request)
    store = store_module.SupabaseStore("https://x.supabase.co", "key")
    assert asyncio.run(store.add_score("Tom", "Riga", 130)) == 230
    assert calls == [("POST", "https://x.supabase.co/rest/v1/rpc/add_score",
                      {"p_name": "Tom", "p_city": "Riga", "p_points": 130})]


def test_register_and_login_menus(store, typed):
    typed(["tom", "riga"])
    assert asyncio.run(register(store)) == {"name": "Tom", "city": "Riga"}
    typed(["x", "TOM", "Riga"])
    assert asyncio.run(login(store)) == {"name": "Tom", "city": "Riga"}
    typed(["Ann", "Oslo"])
    assert asyncio.run(login(store)) is None

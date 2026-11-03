"""Shared test helpers: scripted player input and a quiet screen."""
import pytest

from fury import term


@pytest.fixture
def typed(monkeypatch):
    """
    Feeds the given lines to the game as if the player typed them.
    Fails the test if the game asks for more input than was scripted.
    """
    lines = []

    async def read_line():
        if not lines:
            raise AssertionError("The game asked for more input than scripted")
        return lines.pop(0)

    monkeypatch.setattr(term, "read_line", read_line)
    monkeypatch.setattr(term, "clear_screen", lambda: None)
    for module in ("game", "login", "register", "leaderboard",
                   "main_menu", "user_menu"):
        monkeypatch.setattr(f"fury.{module}.clear_screen", lambda: None)
    return lines.extend

"""Tests for the board, the turn rules and scoring."""
import asyncio
import random

from fury import game


def board_with_tank():
    """5x5 board with one tank on A1-A2."""
    brd = game.create_brd(5)
    brd[0][0] = brd[0][1] = "T"
    return brd


def test_place_tanks_places_every_tank_without_overlap():
    random.seed(1)
    for level in game.DIFFICULTY_LEVELS.values():
        brd = game.create_brd(level["size"])
        game.place_tanks(brd, level["num_tanks"])
        cells = sum(row.count("T") for row in brd)
        assert cells == level["num_tanks"] * game.TANK_SIZES[0]


def test_hitting_every_tank_cell_wins(typed):
    typed(["a", "1", "a", "2"])
    state, player_brd, _ = asyncio.run(
        game.game_loop(5, 1, 15, enemy_brd=board_with_tank()))
    assert state["won"] and state["hits"] == 2 and state["turns"] == 2
    assert player_brd[0][:2] == ["!", "!"]


def test_repeat_shot_at_a_hit_is_not_a_miss_and_costs_no_turn(typed):
    typed(["A", "1", "A", "1", "A", "2"])
    state, player_brd, _ = asyncio.run(
        game.game_loop(5, 1, 15, enemy_brd=board_with_tank()))
    assert player_brd[0][0] == "!"
    assert state["turns"] == 2 and state["won"]


def test_off_board_shot_costs_no_turn(typed):
    # Z1 and A9 are off a 5x5 board, so only the two real shots count.
    typed(["Z", "1", "A", "9", "A", "1", "A", "2"])
    state, _, _ = asyncio.run(
        game.game_loop(5, 1, 2, enemy_brd=board_with_tank()))
    assert state["won"] and state["turns"] == 2


def test_running_out_of_turns_loses(typed):
    typed(["C", "1", "C", "2"])
    state, _, _ = asyncio.run(
        game.game_loop(5, 1, 2, enemy_brd=board_with_tank()))
    assert (state["turns"], state["hits"], state["won"]) == (2, 0, False)


def test_invalid_row_and_column_are_asked_again(typed):
    typed(["AB", "1", "A", "x", "1", "A", "2"])
    state, _, _ = asyncio.run(
        game.game_loop(5, 1, 15, enemy_brd=board_with_tank()))
    assert state["won"] and state["turns"] == 2


def test_score_uses_difficulty_multiplier():
    levels = game.DIFFICULTY_LEVELS
    assert game.calculate_score(4, levels[1]) == 40
    assert game.calculate_score(6, levels[2]) == 72
    assert game.calculate_score(10, levels[3]) == 130


def test_turn_colors_go_green_yellow_red():
    assert game.GREEN in game.get_turn_color(1, 10)
    assert game.YELLOW in game.get_turn_color(6, 10)
    assert game.RED in game.get_turn_color(10, 10)

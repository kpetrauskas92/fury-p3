"""
LEADERBOARD:
This module defines a function for displaying the top players.
"""

from fury import term
from fury.art import LEADERBOARD, LOGO_2
from fury.colors import YELLOW, RED, BOLD, DIM, RESET
from fury.store import StoreError
from fury.term import clear_screen


async def show_leaderboard(store):
    """
    Displays the leaderboard by retrieving the top 10 players
    from the store, highest score first.
    """
    print(LOGO_2)
    print(LEADERBOARD)
    try:
        players = await store.top(10)
    except StoreError as err:
        players = None
        print(f"{BOLD}{RED}⣿ {err}{RESET}")

    if players is not None:
        print(f"{YELLOW}{'Rank:':<7}{RESET}"
              f"{YELLOW}{' Name:':<15}{RESET}"
              f"{YELLOW}{'  City:':<15}{RESET}"
              f"{YELLOW}{'   Score:':<5}{RESET}")
        print("-" * 46)

        # Print the top 10 scores with rank, name, city, and score.
        for i, player in enumerate(players):
            print(f"{i + 1:<7} {player['name']:<15} {player['city']:<15} "
                  f"{player['score']:<5}")
        if not players:
            print("No scores yet. Register and be the first!")
        if not store.shared:
            print(f"\n{DIM}Scores are saved on this device only.{RESET}")

    await term.ask("\nPress ENTER to go back: ")
    clear_screen()

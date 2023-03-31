"""
LEADERBOARD:
This module defines a function for displaying a
leaderboard from a Google Sheets file.
"""

from colorama import Fore, Style
from modules.google_sheets import get_highscores_worksheet
from utils.cs import clear_screen
from art import LEADERBOARD, LOGO_2

GREEN = Fore.GREEN
CYAN = Fore.CYAN
YELLOW = Fore.YELLOW
RED = Fore.RED
BOLD = Style.BRIGHT
RESET = Style.RESET_ALL


def show_leaderboard():
    """
    Displays the leaderboard by retrieving the highscores worksheet
    from Google Sheets, sorting the rows by score,
    and printing the top 15 scores.
    """
    highscores = get_highscores_worksheet()
    rows = highscores.get_all_values()[1:]

    # Sort the rows by score, in descending order.
    sorted_rows = sorted(rows, key=lambda row: int(row[2]), reverse=True)
    print(LOGO_2)
    print(LEADERBOARD)
    print(f"{YELLOW}{'Rank:':<7}{RESET}"
          f"{YELLOW}{' Name:':<15}{RESET}"
          f"{YELLOW}{'  City:':<15}{RESET}"
          f"{YELLOW}{'   Score:':<5}{RESET}")
    print("-" * 46)

    # Print the top 10 scores with rank, name, city, and score.
    for i, row in enumerate(sorted_rows[:10]):
        name, city, score = row
        print(f"{i + 1:<7} {name:<15} {city:<15} {score:<5}")

    input("\nPress ENTER to go back to the main menu: ")
    clear_screen()

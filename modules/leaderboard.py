"""
This module defines a function for displaying a
leaderboard from a Google Sheets file.
"""
from colorama import Fore, Style
from modules.google_sheets import get_highscores_worksheet

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
    sorted_rows = sorted(rows, key=lambda row: int(row[2]), reverse=True)

    print(f"{BOLD}{GREEN}\nLeaderboard:{RESET}")
    print(f"{YELLOW}{'Rank:':<7}{RESET}"
          f"{YELLOW}{' Name:':<15}{RESET}"
          f"{YELLOW}{'  City:':<18}{RESET}"
          f"{YELLOW}{'   Score:':<7}{RESET}")
    print("-" * 50)

    for i, row in enumerate(sorted_rows[:15]):
        name, city, score = row
        print(f"{i + 1:<7} {name:<15} {city:<18} {score:<7}")

    input("\nPress ENTER to go back to the main menu: ")

""" Leaderboard module """
from colorama import Fore, Style
from modules.google_sheets import get_highscores_worksheet

GREEN = Fore.GREEN
CYAN = Fore.CYAN
YELLOW = Fore.YELLOW
RED = Fore.RED
RESET = Style.RESET_ALL


def show_leaderboard():
    """Display the leaderboard."""
    highscores = get_highscores_worksheet()
    rows = highscores.get_all_values()[1:]  # Skip the header row

    # Sort by score
    sorted_rows = sorted(rows, key=lambda row: int(row[2]), reverse=True)

    print(f"{GREEN}\nLeaderboard:{RESET}")
    print(f"{YELLOW}{'Rank:':<7}{RESET}"
          f"{YELLOW}{' Name:':<15}{RESET}"
          f"{YELLOW}{'  City:':<18}{RESET}"
          f"{YELLOW}{'   Score:':<7}{RESET}")
    print("-" * 50)

    for i, row in enumerate(sorted_rows[:15]):
        name, city, score = row
        print(f"{i + 1:<7} {name:<15} {city:<18} {score:<7}")

    input("\nPress ENTER to go back to the main menu: ")

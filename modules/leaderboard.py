""" Leaderboard module """
from colorama import Fore, Style, init
from modules.google_sheets import get_highscores_worksheet

init()


def show_leaderboard():
    """Display the leaderboard."""
    highscores = get_highscores_worksheet()
    rows = highscores.get_all_values()[1:]  # Skip the header row

    # Sort by score
    sorted_rows = sorted(rows, key=lambda row: int(row[2]), reverse=True)

    print(f"{Fore.GREEN}Leaderboard:{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}{'Rank:':<7}{Style.RESET_ALL}"
          f"{Fore.YELLOW}{' Name:':<15}{Style.RESET_ALL}"
          f"{Fore.YELLOW}{'  City:':<18}{Style.RESET_ALL}"
          f"{Fore.YELLOW}{'   Score:':<7}{Style.RESET_ALL}")
    print("-" * 50)

    for i, row in enumerate(sorted_rows[:15]):
        name, city, score = row
        print(f"{i + 1:<7} {name:<15} {city:<18} {score:<7}")

    input("\nPress ENTER to go back to the main menu: ")

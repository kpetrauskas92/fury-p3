""" Leaderboard module """
from colorama import Fore, Style, init
from modules.google_sheets import get_highscores_worksheet

init()


def show_leaderboard():
    """ leaderboard functionality """
    highscores = get_highscores_worksheet()
    rows = highscores.get_all_values()[1:]  # Skip the header row

    # Sort by score
    sorted_rows = sorted(rows, key=lambda row: int(row[2]), reverse=True)

    print(f"{Fore.GREEN}Leaderboard:{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}{'Rank:':<5}{Style.RESET_ALL}"
          f"{Fore.YELLOW}{' Name:':<20}{Style.RESET_ALL}"
          f"{Fore.YELLOW}{'  City:':<20}{Style.RESET_ALL}"
          f"{Fore.YELLOW}{'   Score:':<10}{Style.RESET_ALL}")
    print("-" * 55)

    for i, row in enumerate(sorted_rows[:15]):
        name, city, score = row
        print(f"{i + 1:<5} {name:<20} {city:<20} {score:<10}")

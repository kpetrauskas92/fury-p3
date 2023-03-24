"""Main python terminal"""

import sys
import time
from colorama import init, Fore, Style
from art import MAIN_LOGO, INTRO_TEXT
from modules.main_menu import display_main_menu
from modules.user_menu import display_user_menu_after_action
from modules.google_sheets import get_highscores_worksheet
from modules.login import login
from modules.register import register
from modules.leaderboard import show_leaderboard

init()


def typewriter(text, delay=0.05):
    """typewriter"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


if __name__ == "__main__":
    print(MAIN_LOGO)

    loading_messages = [
        "Loading game data ...",
        "Loading fury ships ...",
        "Loading battle coordinates ...\n"
    ]

    for message in loading_messages:
        typewriter(message)

    typewriter("Game has successfuly loaded!\n")
    typewriter(INTRO_TEXT)

    highscores_worksheet = get_highscores_worksheet()

    while True:
        display_main_menu()
        print("\nChoose (1, 2, or 3) and press Enter:", end=" ")
        main_menu_choice = int(input(f"{Fore.CYAN}\n>>> {Style.RESET_ALL}"))

        if main_menu_choice == 1:
            player_index = login(highscores_worksheet)
            if player_index is not None:
                display_user_menu_after_action(player_index)
        elif main_menu_choice == 2:
            player_index = register()
            if player_index is not None:
                display_user_menu_after_action(player_index)
        elif main_menu_choice == 3:
            show_leaderboard()
        else:
            print("Invalid choice. Please try again.")
            break

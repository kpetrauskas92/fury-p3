"""Main python terminal"""

import sys
import time
from colorama import Fore, Style, init
from art import MAIN_LOGO, INTRO_TEXT
from modules.main_menu import (display_main_menu,
                               process_main_menu_choice)
from modules.google_sheets import get_highscores_worksheet

init()


def typewriter(text, delay=0.05):
    """typewriter"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def continue_prompt():
    """continue prompt function"""
    while True:
        print("Do you wish to continue? (y/n):", end=" ")
        user_input = input(f"{Fore.CYAN}\n>>> {Style.RESET_ALL}").lower()
        if user_input == 'y':
            return True
        if user_input == 'n':
            return False
        print("Invalid input. Please try again.")


def load_game():
    """Load game function."""
    loading_messages = [
        f"{Fore.YELLOW}Loading game data{Style.RESET_ALL}...",
        f"{Fore.YELLOW}Loading fury ships{Style.RESET_ALL}...",
        f"{Fore.YELLOW}Loading battle coordinates{Style.RESET_ALL}..."
    ]

    for message in loading_messages:
        typewriter(message)


if __name__ == "__main__":
    print(MAIN_LOGO)

    if continue_prompt():
        load_game()

        highscores_worksheet = get_highscores_worksheet()

        while True:
            game_loaded_msg = (
                f"{Fore.GREEN}Game has loaded successfully!"
                f"{Style.RESET_ALL}"
            )
            typewriter(game_loaded_msg + "\n")
            typewriter(INTRO_TEXT)
            display_main_menu()
            print("\nChoose (1, 2, or 3) and press Enter:", end=" ")
            main_menu_choice_input = f"{Fore.CYAN}\n>>> {Style.RESET_ALL}"
            main_menu_choice = int(input(main_menu_choice_input))

            process_main_menu_choice(main_menu_choice, highscores_worksheet)

    else:
        typewriter("\nExiting the game...")
        print("Press restart button at the top to start again")

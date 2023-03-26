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
        typewriter(INTRO_TEXT)
        print(f"{Fore.CYAN}DO YOU HAVE WHAT IT TAKES?{Style.RESET_ALL} "
              f"(y/n):", end=" ")

        user_input = input(f"{Fore.CYAN}\n>>> {Style.RESET_ALL}").lower()
        if user_input == 'y':
            return True
        if user_input == 'n':
            return False
        print(f"{Fore.CYAN}Invalid input. Please try again.{Style.RESET_ALL}")


def load_game():
    """Load game function."""
    loading_messages = [
        f"\n{Fore.YELLOW}Loading game data{Style.RESET_ALL}...",
        f"{Fore.YELLOW}Loading fury tanks{Style.RESET_ALL}...",
        f"{Fore.YELLOW}Loading battle coordinates{Style.RESET_ALL}..."
    ]

    for message in loading_messages:
        typewriter(message)


if __name__ == "__main__":
    print(MAIN_LOGO)

    if continue_prompt():
        load_game()

        highscores_worksheet = get_highscores_worksheet()

        GAME_LOADED = False

        while True:
            if not GAME_LOADED:
                game_loaded_msg = (
                    f"{Fore.GREEN}Game has loaded successfully!"
                    f"{Style.RESET_ALL}"
                )
                typewriter(game_loaded_msg + "\n")
                GAME_LOADED = True

            display_main_menu()
            print("\nChoose (1, 2, 3 or 4) and press Enter:", end=" ")
            main_menu_choice_input = f"{Fore.CYAN}\n>>> {Style.RESET_ALL}"
            main_menu_choice = int(input(main_menu_choice_input))

            process_main_menu_choice(main_menu_choice, highscores_worksheet)
    else:
        typewriter(f"\n{Fore.RED}Exiting the game...{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Press RESTART GAME button at "
              f"the top to start again{Style.RESET_ALL}")

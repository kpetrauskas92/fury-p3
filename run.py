"""Main python terminal"""

import sys
import time
from colorama import Fore, Style
from art import MAIN_LOGO, INTRO_TEXT
from modules.main_menu import process_main_menu_choice
from modules.google_sheets import get_highscores_worksheet

GREEN = Fore.GREEN
CYAN = Fore.CYAN
YELLOW = Fore.YELLOW
RED = Fore.RED
BOLD = Style.BRIGHT
RESET = Style.RESET_ALL


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
        print(f"{BOLD}DO YOU HAVE WHAT IT TAKES TO {GREEN}WIN?{RESET} "
              f"(y/n):", end=" ")

        user_input = input(f"{CYAN}\n>>> {RESET}").lower()
        if user_input == 'y':
            return True
        if user_input == 'n':
            return False
        print(f"{RED}Invalid input. Please try again.{RESET}")


def load_game():
    """Load game function."""
    loading_messages = [
        f"\n{YELLOW}Loading game data{RESET}...",
        f"{YELLOW}Loading fury tanks{RESET}...",
        f"{YELLOW}Loading battle coordinates{RESET}..."
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
                    f"{BOLD}{GREEN}Game has loaded successfully!"
                    f"{RESET}"
                )
                typewriter(game_loaded_msg + "\n")
                GAME_LOADED = True

            process_main_menu_choice(highscores_worksheet)
    else:
        typewriter(f"\n{YELLOW}Shutting down the system...{RESET}")
        print(f"Press {BOLD}{RED}'RESTART GAME'{RESET} button at "
              f"the top of the screen to start again.")

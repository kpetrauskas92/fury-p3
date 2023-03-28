"""
Main Python terminal for the 'Fury' game.

This file contains the main logic and entry point for the 'Fury' game. It
imports various modules to handle game functionality such as displaying the
game logo, simulating a typewriter effect, displaying prompts to the user,
loading game data, displaying the main menu, processing user input, and
interacting with Google Sheets to store high scores.
"""

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
    """
    Simulates a typewriter effect by printing out the characters
    in the given text string one by one with a specified delay.
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def continue_prompt():
    """
    Displays a prompt asking the user if they want to continue, and returns
    True if the user enters 'y', and False if they enter 'n'.
    If the user enters an invalid input, the prompt will be repeated until
    a valid input is given.
    """
    while True:
        typewriter(INTRO_TEXT)
        print(f"{BOLD}DO YOU HAVE WHAT IT TAKES TO WIN?{RESET} "
              f"(y/n):", end=" ")

        user_input = input(f"{CYAN}\n>>> {RESET}").lower()
        if user_input == 'y':
            return True
        if user_input == 'n':
            return False
        print(f"{RED}Invalid input. Please try again.{RESET}")


def load_game():
    """
    Simulates loading game data by printing out a series of loading messages
    with a typewriter effect.
    """
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
        print(f"Press {BOLD}{RED}'RESTART GAME'{RESET} button")
        print("at the top of the screen to start again.")

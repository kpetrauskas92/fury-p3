"""
MAIN MENU:
This module defines the function for the main menu,
displaying options for playing the game, logging in,
registering a new player, and displaying the leaderboard.
"""

import time
from colorama import Fore, Style
from art import MAIN_MENU, RULES, LOGO, ERROR, LINE
from modules.login import login
from modules.register import register
from modules.leaderboard import show_leaderboard
from modules.user_menu import display_user_menu_after_action
from utils.cs import clear_screen
from game.game import play_game


GREEN = Fore.GREEN
CYAN = Fore.CYAN
YELLOW = Fore.YELLOW
RED = Fore.RED
BOLD = Style.BRIGHT
RESET = Style.RESET_ALL


def display_main_menu():
    """Displays the main menu options"""
    print(MAIN_MENU)
    print(f"{BOLD}{CYAN}1.{RESET} Play game")
    print(f"{BOLD}{CYAN}2.{RESET} Login")
    print(f"{BOLD}{CYAN}3.{RESET} Register")
    print(f"{BOLD}{CYAN}4.{RESET} Leaderboard")
    print(LINE)


def show_rules_and_start_game():
    """
    Prompts the user to see the rules and starts the game.
    If the user chooses to see the rules,
    the function prints them and waits for the user to start the game.
    Otherwise, the function starts the game immediately.
    """
    while True:
        print(LOGO)
        print(f"{BOLD}Would you like to see the "
              f"rules?{RESET} (y/n):", end=" ")
        show_rules = input(f"{BOLD}{CYAN}\n>>> {RESET}").lower()
        if show_rules.lower() == 'y':
            clear_screen()
            print("\n")
            for line in RULES.splitlines():
                print(line)
                time.sleep(0.05)
            input("\nPress ENTER to start: ")
            play_game()
            break
        if show_rules.lower() == 'n':
            play_game()
            break
        clear_screen()
        print(f"{RED}Invalid input. Please try again.{RESET}")


def process_main_menu_choice(highscores_worksheet):
    """
    Displays the main menu and processes the user's choice.
    Calls corresponding function or
    displays error message if input is invalid.
    """
    while True:
        display_main_menu()
        print("Choose (1, 2, 3 or 4) and press ENTER:", end=" ")
        try:
            choice = int(input(f"{CYAN}\n>>> {RESET}"))
            clear_screen()
            if choice == 1:
                show_rules_and_start_game()
            elif choice == 2:
                player_index = login(highscores_worksheet)
                if player_index is not None:
                    display_user_menu_after_action(player_index)
            elif choice == 3:
                player_index = register()
                if player_index is not None:
                    display_user_menu_after_action(player_index)
            elif choice == 4:
                show_leaderboard()
            else:
                print(ERROR)
                print(f"{RED}Please choose "
                      f"a number between 1 and 4.{RESET}")
        except ValueError:
            clear_screen()
            print(ERROR)
            print(f"{RED}Please enter a number between 1 and 4.{RESET}")

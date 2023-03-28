"""
USER MENU:
This module defines the user menu for the game,
displaying options to play the game,
show the leaderboard, view the rules, or log out.
"""

from colorama import Fore, Style
from game.game import play_game
from modules.leaderboard import show_leaderboard
from utils.cs import clear_screen
from art import USER_MENU
from art import RULES


GREEN = Fore.GREEN
CYAN = Fore.CYAN
YELLOW = Fore.YELLOW
RED = Fore.RED
BOLD = Style.BRIGHT
RESET = Style.RESET_ALL


def display_user_menu():
    """Displays the user menu options"""
    print(USER_MENU)
    print(f"{BOLD}{CYAN}1.{RESET} Play Game")
    print(f"{BOLD}{CYAN}2.{RESET} Leaderboard")
    print(f"{BOLD}{CYAN}3.{RESET} Rules")
    print(f"{BOLD}{CYAN}4.{RESET} Logout")


def display_user_menu_after_action(player_index):
    """
    Displays the user menu after a successful action (login or register).
    Takes a player_index argument to keep track of the
    current player's position on the leaderboard.
    Displays options to play the game, show the leaderboard,
    view the rules, or log out.
    """
    while True:
        display_user_menu()
        print("\nChoose (1, 2, 3 or 4) and press ENTER:", end=" ")
        try:
            user_choice = int(input(f"{BOLD}{CYAN}\n>>> {RESET}"))
            clear_screen()
            if user_choice == 1:
                play_game(player_index)
            elif user_choice == 2:
                show_leaderboard()
            elif user_choice == 3:
                print(RULES)
                input("\nPress ENTER to go back to the user menu: ")
                clear_screen()
            elif user_choice == 4:
                print(f"{YELLOW}You have been logged out.{RESET}")
                break
            else:
                print(f"{RED}Please choose a "
                      f"number between 1 and 4.{RESET}")
        except ValueError:
            print(f"{RED}Please enter a number between 1 and 4.{RESET}")

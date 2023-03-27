""" Main menu module """
import time
from colorama import Fore, Style
from art import MAIN_MENU, RULES
from modules.login import login
from modules.register import register
from modules.leaderboard import show_leaderboard
from modules.user_menu import display_user_menu_after_action
from game.game import play_game


GREEN = Fore.GREEN
CYAN = Fore.CYAN
YELLOW = Fore.YELLOW
RED = Fore.RED
BOLD = Style.BRIGHT
RESET = Style.RESET_ALL


def display_main_menu():
    """Displays main menu"""
    print(MAIN_MENU)
    print(f"{BOLD}{CYAN}1.{RESET} Play game")
    print(f"{BOLD}{CYAN}2.{RESET} Login")
    print(f"{BOLD}{CYAN}3.{RESET} Register")
    print(f"{BOLD}{CYAN}4.{RESET} Leaderboard")


def show_rules_and_start_game():
    """show rules and start game function."""
    while True:
        print("Would you like to see the rules? (y/n):", end=" ")
        show_rules = input(f"{BOLD}{CYAN}\n>>> {RESET}").lower()
        if show_rules.lower() == 'y':
            print("\n")
            for line in RULES.splitlines():
                print(line)
                time.sleep(0.1)
            input("\nPress ENTER to start the game: ")
            play_game()
            break
        if show_rules.lower() == 'n':
            play_game()
            break
        print(f"{RED}Invalid input. Please try again.{RESET}")


def process_main_menu_choice(highscores_worksheet):
    """Process main menu function."""
    while True:
        display_main_menu()
        print("\nChoose (1, 2, 3 or 4) and press ENTER:", end=" ")
        try:
            choice = int(input(f"{CYAN}\n>>> {RESET}"))

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
                print(f"{RED}Please choose "
                      f"a number between 1 and 4.{RESET}")
        except ValueError:
            print(f"{RED}Please enter a number between 1 and 4.{RESET}")

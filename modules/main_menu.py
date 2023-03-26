""" Main menu module """
import time
from colorama import Fore, Style, init
from art import MAIN_MENU, RULES
from modules.login import login
from modules.register import register
from modules.leaderboard import show_leaderboard
from modules.user_menu import display_user_menu_after_action
from game.game import play_game


init()


def display_main_menu():
    """Displays main menu"""
    print(MAIN_MENU)
    print(f"{Fore.CYAN}1.{Style.RESET_ALL} Play game")
    print(f"{Fore.CYAN}2.{Style.RESET_ALL} Login")
    print(f"{Fore.CYAN}3.{Style.RESET_ALL} Register")
    print(f"{Fore.CYAN}4.{Style.RESET_ALL} Leaderboard")


def show_rules_and_start_game():
    """show rules function."""
    while True:
        show_rules = input("Would you like to see the rules? (y/n): ")
        if show_rules.lower() == 'y':
            print("\n")
            for line in RULES.splitlines():
                print(line)
                time.sleep(0.1)
            return start_game_after_rules()
        if show_rules.lower() == 'n':
            play_game()
            return None
        print("Invalid input. Please try again.")


def start_game_after_rules():
    """after rules function."""
    while True:
        print("\nPress 'y' to start the game or 'n' to go back.")
        user_input = input().strip()
        if user_input.lower() == 'n':
            break
        if user_input.lower() == 'y':
            play_game()
            break
        print("Invalid input. Please try again.")


def process_main_menu_choice(choice, highscores_worksheet):
    """Process main menu function."""
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
        print("Invalid choice. Please try again.")

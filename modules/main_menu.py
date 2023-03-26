""" Main menu module """
from colorama import Fore, Style, init
from art import MAIN_MENU
from modules.login import login
from modules.register import register
from modules.leaderboard import show_leaderboard
from modules.user_menu import display_user_menu_after_action


init()


def display_main_menu():
    """Displays main menu"""
    print(MAIN_MENU)
    print(f"{Fore.CYAN}1.{Style.RESET_ALL} Login")
    print(f"{Fore.CYAN}2.{Style.RESET_ALL} Register")
    print(f"{Fore.CYAN}3.{Style.RESET_ALL} Leaderboard")


def process_main_menu_choice(choice, highscores_worksheet):
    """Process main menu function."""
    if choice == 1:
        player_index = login(highscores_worksheet)
        if player_index is not None:
            display_user_menu_after_action(player_index)
    elif choice == 2:
        player_index = register()
        if player_index is not None:
            display_user_menu_after_action(player_index)
    elif choice == 3:
        show_leaderboard()
    else:
        print("Invalid choice. Please try again.")

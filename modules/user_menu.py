"""User menu module"""

from colorama import Fore, Style, init
from game.game import play_game
from modules.leaderboard import show_leaderboard
from art import USER_MENU
from art import RULES


init()


def display_user_menu():
    """Displays user menu"""
    print(USER_MENU)
    print(f"{Fore.CYAN}1.{Style.RESET_ALL} Play Game")
    print(f"{Fore.CYAN}2.{Style.RESET_ALL} Leaderboard")
    print(f"{Fore.CYAN}3.{Style.RESET_ALL} Rules")
    print(f"{Fore.CYAN}4.{Style.RESET_ALL} Logout")


def display_user_menu_after_action(player_index):
    """Displays user menu after an action (login or register)"""
    while True:
        display_user_menu()
        print("\nChoose (1, 2, 3 or 4) and press Enter:", end=" ")
        user_choice = int(input(f"{Fore.CYAN}\n>>> {Style.RESET_ALL}"))

        if user_choice == 1:
            play_game(player_index)
        elif user_choice == 2:
            show_leaderboard()
        elif user_choice == 3:
            print(RULES)
            input("\nPress Enter to go back to the user menu: ")
        elif user_choice == 4:
            print("You have been logged out.")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 4.")

""" Main menu module """
from colorama import Fore, Style, init
from art import MAIN_MENU

init()


def display_main_menu():
    """Displays main menu"""
    print(MAIN_MENU)
    print(f"{Fore.CYAN}1.{Style.RESET_ALL} Login")
    print(f"{Fore.CYAN}2.{Style.RESET_ALL} Register")
    print(f"{Fore.CYAN}3.{Style.RESET_ALL} Leaderboard\n")

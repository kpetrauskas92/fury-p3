"""
USER MENU:
This module defines the user menu for the game,
displaying options to play the game,
show the leaderboard, view the rules, or log out.
"""

from fury import term
from fury.art import USER_MENU, RULES, ERROR, LINE
from fury.colors import CYAN, YELLOW, RED, BOLD, RESET
from fury.game import play_game
from fury.leaderboard import show_leaderboard
from fury.term import clear_screen


def display_user_menu():
    """Displays the user menu options"""
    print(USER_MENU)
    print(f"{BOLD}{CYAN}1.{RESET} Play Game")
    print(f"{BOLD}{CYAN}2.{RESET} Leaderboard")
    print(f"{BOLD}{CYAN}3.{RESET} Rules")
    print(f"{BOLD}{CYAN}4.{RESET} Logout")
    print(LINE)


async def display_user_menu_after_action(player, store):
    """
    Displays the user menu after a successful action (login or register).
    Takes the signed-in player so their scores are saved
    to the right record.
    Displays options to play the game, show the leaderboard,
    view the rules, or log out.
    """
    while True:
        display_user_menu()
        print("\nChoose (1, 2, 3 or 4) and press ENTER:", end=" ")
        user_choice = await term.ask(f"{BOLD}{CYAN}\n>>> {RESET}")
        clear_screen()

        if user_choice == '1':
            await play_game(player, store)
        elif user_choice == '2':
            await show_leaderboard(store)
        elif user_choice == '3':
            print(RULES)
            await term.ask("\nPress ENTER to go back to the user menu: ")
            clear_screen()
        elif user_choice == '4':
            print(f"{BOLD}{YELLOW}You have logged out.{RESET}")
            break
        else:
            print(ERROR)
            print(f"{RED}Please enter a number between 1 and 4.{RESET}")

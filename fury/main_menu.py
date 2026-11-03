"""
MAIN MENU:
This module defines the function for the main menu,
displaying options for playing the game, logging in,
registering a new player, and displaying the leaderboard.
"""

from fury import term
from fury.art import MAIN_MENU, RULES, LOGO, ERROR, LINE
from fury.colors import CYAN, RED, BOLD, RESET
from fury.game import play_game
from fury.leaderboard import show_leaderboard
from fury.login import login
from fury.register import register
from fury.term import clear_screen
from fury.user_menu import display_user_menu_after_action


def display_main_menu():
    """Displays the main menu options"""
    print(MAIN_MENU)
    print(f"{BOLD}{CYAN}1.{RESET} Play game")
    print(f"{BOLD}{CYAN}2.{RESET} Login")
    print(f"{BOLD}{CYAN}3.{RESET} Register")
    print(f"{BOLD}{CYAN}4.{RESET} Leaderboard")
    print(LINE)


async def show_rules_and_start_game():
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
        show_rules = (await term.ask(f"{BOLD}{CYAN}\n>>> {RESET}")).lower()
        if show_rules == 'y':
            clear_screen()
            print("\n")
            for line in RULES.splitlines():
                print(line)
                await term.pause(0.05)
            await term.ask("\nPress ENTER to start: ")
            await play_game()
            break
        if show_rules == 'n':
            await play_game()
            break
        clear_screen()
        print(f"{RED}Invalid input. Please try again.{RESET}")


async def process_main_menu_choice(store):
    """
    Displays the main menu and processes the user's choice.
    Calls corresponding function or
    displays error message if input is invalid.
    """
    while True:
        display_main_menu()
        print("Choose (1, 2, 3 or 4) and press ENTER:", end=" ")
        choice = await term.ask(f"{BOLD}{CYAN}\n>>> {RESET}")
        clear_screen()
        if choice == '1':
            await show_rules_and_start_game()
        elif choice == '2':
            player = await login(store)
            if player is not None:
                await display_user_menu_after_action(player, store)
        elif choice == '3':
            player = await register(store)
            if player is not None:
                await display_user_menu_after_action(player, store)
        elif choice == '4':
            await show_leaderboard(store)
        else:
            print(ERROR)
            print(f"{RED}Please choose "
                  f"a number between 1 and 4.{RESET}")

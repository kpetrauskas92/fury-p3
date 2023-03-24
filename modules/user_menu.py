"""User menu module"""


from game.game import play_game
from modules.leaderboard import show_leaderboard
from art import USER_MENU
from art import RULES


def display_user_menu():
    """Displays user menu"""
    print(USER_MENU)
    print("1. Play Game")
    print("2. Leaderboard")
    print("3. Rules")
    print("4. Logout")


def display_user_menu_after_action(player_index):
    """Displays user menu after an action (login or register)"""
    while True:
        display_user_menu()
        user_choice = int(input("Enter your choice (1-4): "))

        if user_choice == 1:
            play_game(player_index)
        elif user_choice == 2:
            show_leaderboard()
        elif user_choice == 3:
            print(RULES)
        elif user_choice == 4:
            print("You have been logged out.")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 4.")

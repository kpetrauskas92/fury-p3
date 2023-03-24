"""
Main python terminal
"""
# from game import play_game
from art import LOGO
from modules.main_menu import display_main_menu
from modules.user_menu import display_user_menu_after_action
from modules.google_sheets import get_highscores_worksheet
from modules.login import login


if __name__ == "__main__":
    print(LOGO)

    highscores_worksheet = get_highscores_worksheet()

    while True:
        display_main_menu()
        main_menu_choice = int(input("Enter your choice (1, 2, or 3): \n"))

        if main_menu_choice == 1:
            if login(highscores_worksheet):
                display_user_menu_after_action()
        else:
            print("Invalid choice. Please try again.")

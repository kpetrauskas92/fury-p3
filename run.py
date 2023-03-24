"""Main python terminal"""


from art import LOGO
from modules.main_menu import display_main_menu
from modules.user_menu import display_user_menu_after_action
from modules.google_sheets import get_highscores_worksheet
from modules.login import login
from modules.register import register
from modules.leaderboard import show_leaderboard

if __name__ == "__main__":
    print(LOGO)

    highscores_worksheet = get_highscores_worksheet()

    while True:
        display_main_menu()
        main_menu_choice = int(input("Enter your choice (1, 2, or 3): \n"))

        if main_menu_choice == 1:
            player_index = login(highscores_worksheet)
            if player_index is not None:
                display_user_menu_after_action(player_index)
        elif main_menu_choice == 2:
            player_index = register()
            if player_index is not None:
                display_user_menu_after_action(player_index)
        elif main_menu_choice == 3:
            show_leaderboard()
        else:
            print("Invalid choice. Please try again.")
            break

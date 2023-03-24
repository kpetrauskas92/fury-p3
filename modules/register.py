""" Player register module """
from modules.google_sheets import get_highscores_worksheet
from modules.user_menu import display_user_menu_after_action


def is_player_registered(name, city, highscores):
    """checks if user exists"""
    rows = highscores.get_all_values()
    for row in rows[1:]:  # Skip the header row
        if name.lower() == row[0].lower() and city.lower() == row[1].lower():
            return True
    return False


def register():
    """register user"""
    name = input("Please enter your name: ").title()
    city = input("Please enter your city: ").title()
    bonus_score = 10

    highscores = get_highscores_worksheet()

    if is_player_registered(name, city, highscores):
        print("Player already exists. Please choose a different name.")
        print("Or log in.")
    else:
        new_entry = [name, city, bonus_score]
        highscores.append_row(new_entry)
        print(f"Congratulations {name}!")
        print("You've been registered")
        print(f"You received {bonus_score} bonus points.")
        display_user_menu_after_action()

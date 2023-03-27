""" Player register module """
import re
from colorama import Fore, Style
from modules.google_sheets import get_highscores_worksheet


GREEN = Fore.GREEN
CYAN = Fore.CYAN
YELLOW = Fore.YELLOW
RED = Fore.RED
BOLD = Style.BRIGHT
RESET = Style.RESET_ALL


def is_player_registered(name, city, highscores):
    """checks if user exists"""
    rows = highscores.get_all_values()
    for row in rows[1:]:  # Skip the header row
        if name.lower() == row[0].lower() and city.lower() == row[1].lower():
            return True
    return False


def is_valid_input(input_str):
    """checks for valid input"""
    return bool(re.match(r'^[A-Za-z]{3,10}$', input_str))


def register():
    """register user"""
    while True:
        name = input(f"{YELLOW}Please enter your name (3-10 letters):"
                     f"{RESET} ").title()
        if is_valid_input(name):
            break
        print(RED + "Please enter a name with "
              "3 to 10 letters." + RESET)

    while True:
        city = input(f"{YELLOW}Please enter your city (3-10 letters):"
                     f"{RESET} ").title()
        if is_valid_input(city):
            break
        print(RED + "Please enter a city name with "
              "3 to 10 letters." + RESET)

    bonus_score = 10

    highscores = get_highscores_worksheet()

    if is_player_registered(name, city, highscores):
        print(f"{RED}Player already exists.{RESET}")
        print(f"{YELLOW}Please choose a different name.{RESET}")
        print(f"{GREEN}Or Log In.{RESET}")
        return None

    new_entry = [name, city, bonus_score]
    highscores.append_row(new_entry)
    player_index = len(highscores.col_values(1)) - 2

    print(f"{GREEN}Congratulations {name}!"
          f"{RESET}")
    print(f"{YELLOW}You've been registered"
          f"{RESET}")
    print(f"\nYou received /{GREEN}{bonus_score}"
          f"{RESET}/ bonus points.")

    # Return the player_index after registration
    return player_index

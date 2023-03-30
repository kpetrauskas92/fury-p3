"""
REGISTER:
This module defines functions for checking
if a player is already registered, validating user input,
and registering a new player by adding their data to Google Sheets API.
"""

import re
from colorama import Fore, Style
from modules.google_sheets import get_highscores_worksheet
from utils.cs import clear_screen
from art import REGISTER, ERROR, LOGO_2


GREEN = Fore.GREEN
CYAN = Fore.CYAN
YELLOW = Fore.YELLOW
RED = Fore.RED
BOLD = Style.BRIGHT
RESET = Style.RESET_ALL


def register():
    """
    Prompts the user to enter their name and city,
    checks if the inputs are valid,
    adds a bonus score to their score,
    and returns their index in the highscores
    worksheet after registering them.
    """
    print(LOGO_2)
    print(REGISTER)
    name = input(f"{YELLOW}Enter your name:{RESET} ").title()
    while not re.match(r'^[A-Za-z]{3,10}$', name):
        print(RED + "Please enter a name with "
              "3 to 10 letters." + RESET)
        name = input(f"{YELLOW}Enter your name:{RESET} ").title()

    # Prompt the user to enter their city
    city = input(f"{YELLOW}Enter your city:{RESET} ").title()
    while not re.match(r'^[A-Za-z]{3,10}$', city):
        print(RED + "Please enter a city name with "
              "3 to 10 letters." + RESET)
        city = input(f"{YELLOW}Enter your city:{RESET} ").title()

    bonus_score = 100

    highscores = get_highscores_worksheet()

    if is_player_registered(name, city, highscores):
        clear_screen()
        # If the given player is already registered,
        # prints a message indicating that the player already exists
        print(ERROR)
        print(f"{BOLD}{RED}⣿ Player already exists{RESET}")
        print(f"{BOLD}{YELLOW}⣿ Try again or Log In{RESET}")
        return None

    new_entry = [name, city, bonus_score]
    highscores.append_row(new_entry)
    player_index = len(highscores.col_values(1)) - 2
    clear_screen()

    print(f"\n{BOLD}{GREEN}Congratulations {name}!"
          f"{RESET}")
    print(f"{YELLOW}You've been registered"
          f"{RESET}")
    print(f"\nYou received /{BOLD}{GREEN}{bonus_score}"
          f"{RESET}/ bonus points.")

    # Return the player_index after registration
    return player_index


def is_player_registered(name, city, highscores):
    """
    Checks if a player is already registered in the highscores worksheet.
    """
    rows = highscores.get_all_values()
    for row in rows[1:]:  # Skip the header row
        if name.lower() == row[0].lower() and city.lower() == row[1].lower():
            return True
    return False

""" Player register module """
import re
from colorama import Fore, Style, init
from modules.google_sheets import get_highscores_worksheet


init()


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
        name = input(f"{Fore.YELLOW}Please enter your name (3-10 letters):"
                     f"{Style.RESET_ALL} ").title()
        if is_valid_input(name):
            break
        print(Fore.RED + "Invalid name. Please enter a name with "
              "3 to 10 letters." + Style.RESET_ALL)

    while True:
        city = input(f"{Fore.YELLOW}Please enter your city (3-10 letters):"
                     f"{Style.RESET_ALL} ").title()
        if is_valid_input(city):
            break
        print(Fore.RED + "Invalid city name. Please enter a city name with "
              "3 to 10 letters." + Style.RESET_ALL)

    bonus_score = 10

    highscores = get_highscores_worksheet()

    if is_player_registered(name, city, highscores):
        print(f"{Fore.RED}Player already exists.{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Please choose a different name.{Style.RESET_ALL}")
        print(f"{Fore.GREEN}Or log in.{Style.RESET_ALL}")
        return None

    new_entry = [name, city, bonus_score]
    highscores.append_row(new_entry)
    player_index = len(highscores.col_values(1)) - 2

    print(f"{Fore.GREEN}Congratulations {name}!"
          f"{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}You've been registered"
          f"{Style.RESET_ALL}")
    print(f"You received /{Fore.GREEN}{bonus_score}"
          f"{Style.RESET_ALL}/ bonus points.")

    # Return the player_index after registration
    return player_index

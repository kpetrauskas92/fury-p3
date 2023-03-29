"""
LOGIN:
This module defines login function for user login and highscore retrieval.
"""

import re
from operator import itemgetter
from colorama import Fore, Style
from utils.cs import clear_screen
from art import LOGIN, ERROR, LOGO_2

GREEN = Fore.GREEN
CYAN = Fore.CYAN
YELLOW = Fore.YELLOW
RED = Fore.RED
RESET = Style.RESET_ALL


def login(highscores):
    """
    Prompts the user to enter their name and city,
    retrieves the highscores from the given worksheet, and checks
    if the user's name and city already exist in the highscores.
    If found, displays the user's highscore and position on the leaderboard.
    """
    print(LOGO_2)
    print(LOGIN)
    # Prompt the user to enter their name
    player_name = input(f"{YELLOW}Enter your name:{RESET} ")
    while not re.match(r'^[A-Za-z]{3,10}$', player_name):
        print(RED + "Please enter a name with "
              "3 to 10 letters." + RESET)
        player_name = input(f"{YELLOW}Enter your name:{RESET} ")

    # Prompt the user to enter their city
    player_city = input(f"{YELLOW}Enter your city:{RESET} ")
    while not re.match(r'^[A-Za-z]{3,10}$', player_city):
        print(RED + "Please enter a city name with "
              "3 to 10 letters." + RESET)
        player_city = input(f"{YELLOW}Enter your city:{RESET} ")

    # Retrieve all records from the highscores worksheet
    records = highscores.get_all_records()

    # Sort the records by 'SCORE' in descending order
    sorted_records = sorted(records, key=itemgetter('SCORE'), reverse=True)

    # Check if the user's name and city already exist in the highscores
    clear_screen()
    for index, record in enumerate(sorted_records):
        if (record["NAME"].lower() == player_name.lower()
                and record["CITY"].lower() == player_city.lower()):
            welcome_msg = f"\nWelcome back {GREEN}{record['NAME']}!"
            print(welcome_msg + RESET)
            highscore_msg = f"You have {YELLOW}{record['SCORE']} points."
            print(highscore_msg + RESET)
            position = index + 1
            position_msg = (f"Your position is: "
                            f"/{GREEN}{position}{RESET}/ "
                            "on the leaderboard.")
            print(position_msg)
            return index

    # If the user's record was not found, display an error message
    clear_screen()
    print(ERROR)
    print(f"{RED}⣿ Player not found{RESET}")
    print(f"{YELLOW}⣿ Please try again{RESET}")
    return None

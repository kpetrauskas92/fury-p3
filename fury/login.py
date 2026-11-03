"""
LOGIN:
This module defines login function for user login and highscore retrieval.
"""

import re
from fury import term
from fury.art import LOGIN, ERROR, LOGO_2
from fury.colors import GREEN, YELLOW, RED, BOLD, RESET
from fury.store import StoreError
from fury.term import clear_screen


async def prompt_name_city():
    """
    Prompts the user for their name and city until both are
    3 to 10 letters long. Returns them in title case.
    """
    name = await term.ask(f"{YELLOW}Enter your name:{RESET} ")
    while not re.match(r'^[A-Za-z]{3,10}$', name):
        print(RED + "Please enter a name with "
              "3 to 10 letters." + RESET)
        name = await term.ask(f"{YELLOW}Enter your name:{RESET} ")

    city = await term.ask(f"{YELLOW}Enter your city:{RESET} ")
    while not re.match(r'^[A-Za-z]{3,10}$', city):
        print(RED + "Please enter a city name with "
              "3 to 10 letters." + RESET)
        city = await term.ask(f"{YELLOW}Enter your city:{RESET} ")

    return name.title(), city.title()


async def login(store):
    """
    Prompts the user to enter their name and city and looks them up.
    If found, displays the user's highscore and position on the leaderboard
    and returns the player. Returns None otherwise.
    """
    print(LOGO_2)
    print(LOGIN)
    name, city = await prompt_name_city()

    try:
        record = await store.find(name, city)
    except StoreError as err:
        clear_screen()
        print(ERROR)
        print(f"{BOLD}{RED}⣿ {err}{RESET}")
        return None

    clear_screen()
    if record is None:
        print(ERROR)
        print(f"{BOLD}{RED}⣿ Player not found{RESET}")
        print(f"{BOLD}{YELLOW}⣿ Please try again{RESET}")
        return None

    print(f"\nWelcome back {BOLD}{GREEN}{record['name']}!{RESET}")
    print(f"You have {BOLD}{YELLOW}{record['score']} points.{RESET}")
    print(f"Your position is: /{BOLD}{GREEN}{record['rank']}{RESET}/ "
          "on the leaderboard.")
    return {"name": record["name"], "city": record["city"]}

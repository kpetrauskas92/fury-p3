"""
REGISTER:
This module defines the function for registering a new player
and giving them their bonus points.
"""

from fury.art import REGISTER, ERROR, LOGO_2
from fury.colors import GREEN, YELLOW, RED, BOLD, RESET
from fury.login import prompt_name_city
from fury.store import BONUS_SCORE, StoreError
from fury.term import clear_screen


async def register(store):
    """
    Prompts the user to enter their name and city,
    registers them with a bonus score
    and returns the new player, or None if they already exist.
    """
    print(LOGO_2)
    print(REGISTER)
    name, city = await prompt_name_city()

    try:
        registered = await store.register(name, city)
    except StoreError as err:
        clear_screen()
        print(ERROR)
        print(f"{BOLD}{RED}⣿ {err}{RESET}")
        return None

    clear_screen()
    if not registered:
        # If the given player is already registered,
        # prints a message indicating that the player already exists
        print(ERROR)
        print(f"{BOLD}{RED}⣿ Player already exists{RESET}")
        print(f"{BOLD}{YELLOW}⣿ Try again or Log In{RESET}")
        return None

    print(f"\n{BOLD}{GREEN}Congratulations {name}!"
          f"{RESET}")
    print(f"{YELLOW}You've been registered"
          f"{RESET}")
    print(f"\nYou received /{BOLD}{GREEN}{BONUS_SCORE}"
          f"{RESET}/ bonus points.")
    return {"name": name, "city": city}

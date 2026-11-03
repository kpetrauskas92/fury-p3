"""
Main entry point for the 'Fury' game.

Shows the intro, simulates loading the game and then hands over to the
main menu. Run it with `python -m fury` (or `fury` once installed);
the browser version calls main() from web/app.js.
"""

import asyncio
import os
import sys
from fury import term
from fury.art import MAIN_LOGO, LOGO_2, LINE
from fury.colors import GREEN, CYAN, YELLOW, RED, BOLD, RESET
from fury.main_menu import process_main_menu_choice
from fury.store import get_store
from fury.term import clear_screen, typewriter


async def continue_prompt():
    """
    Displays a prompt asking the user if they want to continue, and returns
    True if the user enters 'y', and False if they enter 'n'.
    If the user enters an invalid input, the prompt will be repeated until
    a valid input is given.
    """
    while True:
        print(f"{BOLD}{GREEN}READY TO PLAY?{RESET} (y/n): ", end="")
        user_input = (await term.ask(f"{BOLD}{CYAN}\n>>> {RESET}")).lower()
        if user_input == 'y':
            clear_screen()
            return True
        if user_input == 'n':
            clear_screen()
            return False
        print(f"{RED}Invalid input. Please try again.{RESET}")


async def load_game():
    """
    Simulates loading game data by printing out a series of loading messages
    with a typewriter effect.
    """
    print(LOGO_2)
    print(LINE)
    loading_messages = [
        f"{YELLOW}Loading game data{RESET}...",
        f"{YELLOW}Loading fury tanks{RESET}...",
        f"{YELLOW}Loading battle coordinates{RESET}..."
    ]

    for message in loading_messages:
        await typewriter(message)


async def main():
    """Runs the game from the intro screen."""
    print(MAIN_LOGO)

    if await continue_prompt():
        await load_game()
        store = get_store()
        await typewriter(f"{BOLD}{GREEN}Game has loaded successfully!{RESET}\n")
        clear_screen()
        await process_main_menu_choice(store)
    else:
        await typewriter(f"\n{YELLOW}Shutting down the system...{RESET}\n")
        if term.IN_BROWSER:
            print(f"Press {BOLD}{RED}'RESTART GAME'{RESET} button")
            print("at the top of the screen to start again.")


def run():
    """Starts the terminal version of the game."""
    if os.name == 'nt':
        # Turns on ANSI colour support in older Windows consoles.
        os.system('')
    # The ASCII art uses braille characters, which need UTF-8.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, EOFError):
        print(f"\n{YELLOW}See you on the battlefield, soldier.{RESET}")


if __name__ == "__main__":
    run()

"""
GAME:
This module provides functionality for a turn-based tank battle game, including
grid generation, game logic, and enemy AI.
The main components of the module are:

 *Grid: Handles grid generation, rendering, and manipulation.
 *Tank: Represents player and enemy tanks,
  including their positions and status.
 *AI: Handles enemy tank movement and decision-making.
 *Game: Manages game flow, turn system, and user input.
"""

import random
from colorama import Fore, Style
from art import LOGO, LOGO_2, GAME_OVER, WINNER
from modules.google_sheets import get_highscores_worksheet
from utils.cs import clear_screen


GREEN = Fore.GREEN
CYAN = Fore.CYAN
YELLOW = Fore.YELLOW
RED = Fore.RED
BOLD = Style.BRIGHT
DIM = Style.DIM
RESET = Style.RESET_ALL

# A dictionary that defines the game difficulty levels.
DIFFICULTY_LEVELS = {
    1: {"size": 5, "num_tanks": 2, "turn_limit": 10},
    2: {"size": 7, "num_tanks": 3, "turn_limit": 15},
    3: {"size": 10, "num_tanks": 4, "turn_limit": 20},
}

# Sizes (lengths) for tanks in the game
TANK_SIZES = [2]

# A dictionary that defines the different messages
# that can be displayed during the game.
event_messages = {
    "oops": f"⣿ {YELLOW}Oops, that's not even in "
            f"the battlefield.{RESET}",
    "same": f"⣿ {RED}You've already hit that "
            f"spot. Try again!{RESET}",
    "hit": f"⣿ {GREEN}You've hit a tank!{RESET} Good job!",
    "miss": f"⣿ {YELLOW}You missed.{RESET} Better luck "
            f"next time!",
    "game_over": "\n⣿ You ran out of turns.",
    "enemy_tanks": f"⣿ {YELLOW}The enemy tanks were at:{RESET}",
    "congrats": f"\n{BOLD}{GREEN}Congratulations!{RESET}",
    "destroyed": "You destroyed all enemy tanks!",
}


def create_brd(size):
    """
    Creates a square board of the given size, initialized with "~"
    as the default value for each cell.
    """
    return [["~" for _ in range(size)] for _ in range(size)]


def print_brd(brd):
    """
    Prints the given board to the console in a stylized format.
    """
    size = len(brd)
    border = f"   +{'-' * (size * 3 + 1)}+"

    # Prints the top border
    print(border)

    # Prints row labels and board content
    for row_num, row in enumerate(brd, start=1):
        row_label = chr(row_num + 64)
        row_str = f" {row_label} | "
        for cell in row:
            if cell == "~":
                cell_color = DIM
            elif cell == "T":
                cell_color = BOLD + YELLOW
            elif cell == "X":
                cell_color = BOLD + RED
            elif cell == "!":
                cell_color = BOLD + GREEN
            else:
                cell_color = RESET
            row_str += f"{cell_color}{cell:<3}{RESET}"
        row_str += "|"

        # Prints the row string with a vertical border
        print(row_str)

    # Prints the bottom border
    print(border)

    # Prints column labels
    col_str = ("     " +
               "".join(f"{col_num:<3}" for col_num in range(1, size + 1)))
    print(col_str)


def random_row(brd):
    """
    Returns a random row index for the given board
    """
    return random.randint(0, len(brd) - 1)


def random_col(brd):
    """
    Returns a random col index for the given board
    """
    return random.randint(0, len(brd[0]) - 1)


def is_valid_tank_placement(brd, row, col, length, orientation):
    """
    Checks if a tank placement is valid on a given board
    by checking if any cells in the placement are out of bounds
    or overlap with an already placed tank.
    """
    for i in range(length):
        if orientation == "horizontal":
            if col + i >= len(brd[0]) or brd[row][col + i] == "T":
                return False
        else:
            if row + i >= len(brd) or brd[row + i][col] == "T":
                return False
    return True


def place_tank(brd, length):
    """
    Randomly places a tank on the given board with the given length.
    The tank can be placed either horizontally or vertically.
    Returns True if the placement was successful, False otherwise.
    """
    orientation = random.choice(["horizontal", "vertical"])
    if orientation == "horizontal":
        row, col = random_row(brd), random.randint(0, len(brd[0]) - length)
        if not is_valid_tank_placement(brd, row, col, length, orientation):
            return False
        for i in range(length):
            brd[row][col + i] = "T"
    else:
        row, col = random.randint(0, len(brd) - length), random_col(brd)
        if not is_valid_tank_placement(brd, row, col, length, orientation):
            return False
        for i in range(length):
            brd[row + i][col] = "T"
    return True


def place_tanks(brd, num_tanks):
    """
    Places the specified number of tanks on the given board.
    Randomly selects tank size and placement.
    Continues trying to place tanks until all tanks are placed successfully.
    """
    for _ in range(num_tanks):
        tank_length = random.choice(TANK_SIZES)
        placed = False
        while not placed:
            placed = place_tank(brd, tank_length)


def select_difficulty():
    """
    Displays the difficulty levels and prompts the user to choose one.
    Returns a tuple with the board size, number of tanks, and turn limit
    for the selected difficulty level.
    """
    print(f"{BOLD}{GREEN}Select difficulty level:{RESET}\n")
    print(f"{CYAN}1. {GREEN}Easy{RESET}")
    print(" 5x5 board with 2 Tanks - 10 turns\n")
    print(f"{CYAN}2. {YELLOW}Medium{RESET}")
    print(" 7x7 board with 3 Tanks - 15 turns\n")
    print(f"{CYAN}3. {RED}Hard{RESET}")
    print(" 10x10 board with 5 Tanks - 20 turns\n")

    while True:
        print("Choose (1, 2, or 3) and press ENTER:", end=" ")
        choice = input(f"{BOLD}{CYAN}\n>>> {RESET}")

        if choice.isdigit() and choice in ('1', '2', '3'):
            choice = int(choice)
            break

        print(f"\n{RED}Please enter a valid option "
              f"(1, 2, or 3).{RESET}")

    if choice == 1:
        return 5, 2, 10
    if choice == 2:
        return 7, 3, 15
    return 10, 4, 20


def get_turn_color(turn, total_turns):
    """
    Returns the color to represent the current turn number in the game.
    """
    mid_turn = total_turns // 2
    if turn <= mid_turn:
        return f"{GREEN}{turn}{RESET}"
    if turn <= (total_turns - mid_turn) + mid_turn - 1:
        return f"{YELLOW}{turn}{RESET}"
    return f"{RED}{turn}{RESET}"


def get_input(prompt, valid_func):
    """
    Prompts the user for input using the given prompt,
    and uses the given validation function to check if the input is valid.
    If the input is valid, returns the input value.
    """
    while True:
        value = input(prompt)
        if valid_func(value):
            return value


def valid_row(value):
    """
    Checks if the input value is a valid row identifier
    """
    if len(value) != 1 or not value.isalpha():
        print(f"{RED}Please enter a single letter.{RESET}")
        return False
    return True


def valid_col(value):
    """
    Checks if the input value is a valid col identifier
    """
    if not value.isdigit():
        print(f"{RED}Please enter a number.{RESET}")
        return False
    return True


def get_row_col(size):
    """
    Prompts the user to enter a row and column for a grid of the given size
    and returns the corresponding row and column values as a tuple.

    """
    row_input = get_input(
        f" Enter row (A-{chr(64 + size)}):{CYAN} >>> {RESET}",
        valid_row
    ).upper()
    row = ord(row_input) - 65
    col_input = get_input(
        f" Enter column (1-{size}):{CYAN} >>> {RESET}",
        valid_col
    )
    col = int(col_input) - 1
    return row, col


def update_game_state(player_brd, enemy_brd, row, col, tanks_destr):
    """
    Updates the state of the game based on the player's move
    and returns relevant information for events.
    """
    game_over = False
    if enemy_brd[row][col] == "T":
        event_message = event_messages["hit"]
        player_brd[row][col] = "!"
        enemy_brd[row][col] = "~"
        tanks_destr += 1
        if not any("T" in row for row in enemy_brd):
            game_over = True
    else:
        event_message = event_messages["miss"]
        player_brd[row][col] = "X"
    return event_message, player_brd, enemy_brd, tanks_destr, game_over


def game_loop(size, num_tanks, turn_limit):
    """
    Runs the game loop function, allowing the player to take turns,
    making moves and updating the game state until either
    all tanks have been destroyed or the turn limit has been reached.
    The function returns a dictionary with information about the game state,
    as well as the player's and enemy's game boards.
    """

    # Create game boards and place tanks on enemy board
    player_brd, enemy_brd = create_brd(size), create_brd(size)
    place_tanks(enemy_brd, num_tanks)

    # Initialize game state dictionary
    game_state = {"turns": 0, "tanks_destr": 0, "event_message": ""}

    # Main game loop
    while game_state["turns"] < turn_limit:
        clear_screen()
        print(LOGO)
        if game_state["event_message"]:
            print(game_state["event_message"])
        colored_turn = get_turn_color(game_state["turns"] + 1, turn_limit)
        if game_state["turns"] + 1 == turn_limit:
            print(f"\n Turn {colored_turn}/{turn_limit} {RED}Last!{RESET}")
        else:
            print(f"\n Turn {colored_turn}/{turn_limit}")
        print_brd(player_brd)

        # Get player's move
        row, col = get_row_col(size)

        # Handle invalid move
        if row not in range(size) or col not in range(size):
            game_state["event_message"] = event_messages["oops"]
        elif player_brd[row][col] in ("X", " !"):
            game_state["event_message"] = event_messages["same"]
        else:
            # Update game state based on player's move
            (game_state["event_message"], player_brd, enemy_brd,
             game_state["tanks_destr"], game_over) = update_game_state(
             player_brd, enemy_brd, row, col, game_state["tanks_destr"])
        if game_over:
            clear_screen()
            print(LOGO_2)
            print(WINNER)
            print(event_messages["congrats"])
            print(event_messages["destroyed"])
            break

        game_state["turns"] += 1

    return game_state, player_brd, enemy_brd


def play_game(player_index=None, signed_in=False):
    """
    This function runs the main game loop,
    handles user inputs, game states, and scoring.
    It allows the player to play multiple games in succession
    and updates the highscores if the player is signed in.
    """
    while True:
        clear_screen()
        print(LOGO)
        size, num_tanks, turn_limit = select_difficulty()
        (
            game_state,
            _,
            enemy_brd,
        ) = game_loop(size, num_tanks, turn_limit)

        # Check if the game ended due to reaching the turn limit
        if game_state["turns"] == turn_limit:
            clear_screen()
            print(LOGO_2)
            print(GAME_OVER)
            print(event_messages["game_over"])
            print(event_messages["enemy_tanks"])
            # print_brd(player_brd)
            print_brd(enemy_brd)

        # Calculate and display the player's score
        score = int(game_state["tanks_destr"] * 10 *
                    [1, 1.2, 1.3][turn_limit // 5 - 2])
        print(f"You scored: {GREEN}{score} points!{RESET}")

        # If player is signed in, update their highscore
        if player_index is not None:
            highscores = get_highscores_worksheet()
            old_score = highscores.cell(player_index + 2, 3).value
            highscores.update_cell(player_index + 2, 3, int(old_score) + score)
        elif not signed_in:

            # If player is not signed in, inform their score won't be saved
            print(f"\n⣿ Your score will {RED}not be "
                  f"saved{RESET}.")
            print(f"⣿ Please register{YELLOW} !!!{RESET}")

        play_again = prompt_play_again()
        if play_again == 'n':
            clear_screen()
            break   # Exit the loop if the player chooses not to play again


def prompt_play_again():
    """
    Prompts the player to play the game again and returns their answer.
    """
    while True:
        print(f"{YELLOW}\nPLAY AGAIN? {RESET}(y/n):", end=" ")
        play_again = input(f"{BOLD}{CYAN}\n>>> {RESET}").lower()

        if play_again in ('y', 'n'):
            return play_again
        print(f"{RED}Please ENTER 'y' or 'n'.{RESET}")

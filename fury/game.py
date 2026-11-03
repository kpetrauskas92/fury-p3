"""
GAME:
This module provides functionality for a turn-based tank battle game, including
grid generation, game logic, and scoring.
"""
import random
from fury import term
from fury.art import LOGO, LOGO_2, GAME_OVER, WINNER
from fury.colors import GREEN, CYAN, YELLOW, RED, BOLD, DIM, RESET
from fury.store import StoreError
from fury.term import clear_screen


# A dictionary that defines the game difficulty levels.
DIFFICULTY_LEVELS = {
    1: {"name": "Easy", "color": GREEN, "size": 5, "num_tanks": 2,
        "turn_limit": 15, "multiplier": 1},
    2: {"name": "Medium", "color": YELLOW, "size": 7, "num_tanks": 3,
        "turn_limit": 20, "multiplier": 1.2},
    3: {"name": "Hard", "color": RED, "size": 10, "num_tanks": 5,
        "turn_limit": 30, "multiplier": 1.3},
}

# Sizes (lengths) for tanks in the game
TANK_SIZES = [2]

# Points for each hit, before the difficulty multiplier
POINTS_PER_HIT = 10

# A dictionary that defines the different messages
# that can be displayed during the game.
event_messages = {
    "oops": f"⣿ {BOLD}{YELLOW}Oops, that's not even in "
            f"the battlefield.{RESET}",
    "same": f"⣿ {BOLD}{RED}You've already hit that "
            f"spot. Try again!{RESET}",
    "hit": f"⣿ {BOLD}{GREEN}You've hit a tank!{RESET} Good job!",
    "miss": f"⣿ {BOLD}{YELLOW}You missed.{RESET} Better luck "
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


async def select_difficulty():
    """
    Displays the difficulty levels and prompts the user to choose one.
    Returns the settings dictionary for the selected difficulty level.
    """
    print(f"{BOLD}{GREEN}Select difficulty level:{RESET}\n")
    for number, level in DIFFICULTY_LEVELS.items():
        print(f"{BOLD}{CYAN}{number}. {level['color']}{level['name']}{RESET}")
        print(f" {level['size']}x{level['size']} board with "
              f"{level['num_tanks']} Tanks - {level['turn_limit']} turns\n")
    print(f"{YELLOW}For each hit you get {POINTS_PER_HIT} points{RESET}\n")

    while True:
        print("Choose (1, 2, or 3) and press ENTER:", end=" ")
        choice = await term.ask(f"{BOLD}{CYAN}\n>>> {RESET}")

        if choice in ('1', '2', '3'):
            return DIFFICULTY_LEVELS[int(choice)]

        print(f"\n{RED}Please enter a valid option "
              f"(1, 2, or 3).{RESET}")


def calculate_score(hits, level):
    """
    Returns the score for the given number of hits,
    scaled by the difficulty level's multiplier.
    """
    return int(hits * POINTS_PER_HIT * level["multiplier"])


def get_turn_color(turn, total_turns):
    """
    Returns the color to represent the current turn number in the game.
    """
    mid_turn = total_turns // 2
    if turn <= mid_turn:
        return f"{GREEN}{turn}{RESET}"
    if turn < total_turns:
        return f"{YELLOW}{turn}{RESET}"
    return f"{RED}{turn}{RESET}"


async def get_input(prompt, valid_func):
    """
    Prompts the user for input using the given prompt,
    and uses the given validation function to check if the input is valid.
    If the input is valid, returns the input value.
    """
    while True:
        value = await term.ask(prompt)
        if valid_func(value):
            return value


def valid_row(value):
    """
    Checks if the input value is a valid row identifier
    """
    if len(value) != 1 or not value.isascii() or not value.isalpha():
        print(f"{BOLD}{RED}Please enter a single letter.{RESET}")
        return False
    return True


def valid_col(value):
    """
    Checks if the input value is a valid col identifier
    """
    if not value.isascii() or not value.isdigit():
        print(f"{BOLD}{RED}Please enter a number.{RESET}")
        return False
    return True


async def get_row_col(size):
    """
    Prompts the user to enter a row and column for a grid of the given size
    and returns the corresponding row and column values as a tuple.
    """
    row_input = (await get_input(
        f" Enter row (A-{chr(64 + size)}):{BOLD}{CYAN} >>> {RESET}",
        valid_row
    )).upper()
    row = ord(row_input) - 65
    col_input = await get_input(
        f" Enter column (1-{size}):{BOLD}{CYAN} >>> {RESET}",
        valid_col
    )
    col = int(col_input) - 1
    return row, col


def update_game_state(player_brd, enemy_brd, row, col, hits):
    """
    Updates the state of the game based on the player's move
    and returns relevant information for events.
    """
    game_over = False
    if enemy_brd[row][col] == "T":
        event_message = event_messages["hit"]
        player_brd[row][col] = "!"
        enemy_brd[row][col] = "~"
        hits += 1
        if not any("T" in row for row in enemy_brd):
            game_over = True
    else:
        event_message = event_messages["miss"]
        player_brd[row][col] = "X"
    return event_message, player_brd, enemy_brd, hits, game_over


async def game_loop(size, num_tanks, turn_limit, enemy_brd=None):
    """
    Runs the game loop function, allowing the player to take turns,
    making moves and updating the game state until either
    all tanks have been destroyed or the turn limit has been reached.
    Shots off the board or at a spot already tried don't use up a turn.
    The function returns a dictionary with information about the game state,
    as well as the player's and enemy's game boards.
    """

    # Create game boards and place tanks on enemy board
    player_brd = create_brd(size)
    if enemy_brd is None:
        enemy_brd = create_brd(size)
        place_tanks(enemy_brd, num_tanks)

    # Initialize game state dictionary
    game_state = {"turns": 0, "hits": 0, "won": False, "event_message": ""}

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
        row, col = await get_row_col(size)
        # Handle invalid move without using up a turn
        if row not in range(size) or col not in range(size):
            game_state["event_message"] = event_messages["oops"]
            continue
        if player_brd[row][col] in ("X", "!"):
            game_state["event_message"] = event_messages["same"]
            continue

        # Update game state based on player's move
        (game_state["event_message"], player_brd, enemy_brd,
         game_state["hits"], game_over) = update_game_state(
            player_brd, enemy_brd, row, col, game_state["hits"])
        game_state["turns"] += 1

        if game_over:
            game_state["won"] = True
            clear_screen()
            print(LOGO_2)
            print(WINNER)
            print(event_messages["congrats"])
            print(event_messages["destroyed"])
            break

    return game_state, player_brd, enemy_brd


async def play_game(player=None, store=None):
    """
    This function runs the main game loop,
    handles user inputs, game states, and scoring.
    It allows the player to play multiple games in succession
    and adds the score to the player's total if they are signed in.
    """
    while True:
        clear_screen()
        print(LOGO)
        level = await select_difficulty()
        game_state, _, enemy_brd = await game_loop(
            level["size"], level["num_tanks"], level["turn_limit"])

        if not game_state["won"]:
            clear_screen()
            print(LOGO_2)
            print(GAME_OVER)
            print(event_messages["game_over"])
            print(event_messages["enemy_tanks"])
            print_brd(enemy_brd)

        # Calculate and display the player's score
        score = calculate_score(game_state["hits"], level)
        print(f"You scored: {BOLD}{GREEN}{score} points!{RESET}")

        if player is not None:
            print(f"\n{YELLOW}Updating highscores... Please wait...{RESET}")
            try:
                total = await store.add_score(
                    player["name"], player["city"], score)
                print(f"⣿ Your total is now {BOLD}{GREEN}{total}{RESET} "
                      "points.")
            except StoreError as err:
                print(f"{BOLD}{RED}⣿ Couldn't save your score.{RESET} {err}")
        else:
            # If player is not signed in, inform their score won't be saved
            print(f"\n{BOLD}⣿ Your score will {RED}not be "
                  f"saved{RESET}.")
            print(f"{BOLD}⣿ Please register{YELLOW} !!!{RESET}")

        play_again = await prompt_play_again()
        if play_again == 'n':
            clear_screen()
            break   # Exit the loop if the player chooses not to play again


async def prompt_play_again():
    """
    Prompts the player to play the game again and returns their answer.
    """
    while True:
        print(f"{BOLD}{YELLOW}\nPLAY AGAIN? {RESET}(y/n):", end=" ")
        play_again = (await term.ask(f"{BOLD}{CYAN}\n>>> {RESET}")).lower()

        if play_again in ('y', 'n'):
            return play_again
        print(f"{BOLD}{RED}Please ENTER 'y' or 'n'.{RESET}")

"""
Main game
"""
import os
import random
from colorama import Fore, Style
from art import LOGO
from modules.google_sheets import get_highscores_worksheet


GREEN = Fore.GREEN
CYAN = Fore.CYAN
YELLOW = Fore.YELLOW
RED = Fore.RED
BOLD = Style.BRIGHT
DIM = Style.DIM
RESET = Style.RESET_ALL


DIFFICULTY_LEVELS = {
    1: {"size": 5, "num_tanks": 2, "turn_limit": 10},
    2: {"size": 7, "num_tanks": 3, "turn_limit": 15},
    3: {"size": 10, "num_tanks": 4, "turn_limit": 20},
}

TANK_SIZES = [2]  # Custom tank sizes

event_messages = {
    "oops": f"{YELLOW}Oops, that's not even in "
            f"the battlefield.{RESET}",
    "same": f"{RED}You've already hit that "
            f"spot. Try again!{RESET}",
    "hit": f"{GREEN}You've hit a tank! Good job!{RESET}",
    "miss": f"{YELLOW}You missed.{RESET} Better luck "
            f"next time!",
    "game_over": f"\n{RED}Game over!{RESET} You ran out "
                 f"of turns.",
    "enemy_tanks": f"{YELLOW}The enemy tanks were at:{RESET}",
    "congrats": f"{BOLD}{GREEN}Congratulations!{RESET}",
    "destroyed": "You destroyed all enemy tanks!",
}


def clear_screen():
    """clears board for new one"""
    os.system("cls" if os.name == "nt" else "clear")


def create_brd(size):
    """
    create board function
    """
    return [["~" for _ in range(size)] for _ in range(size)]


def print_brd(brd):
    """
    print board function
    """
    size = len(brd)
    border = f"   +{'-' * (size * 3 + 1)}+"

    # Print the top border
    print(border)

    # Print row labels and board content
    for row_num, row in enumerate(brd, start=1):
        row_label = chr(row_num + 64)  # Convert row number to letters
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
        print(row_str)

    # Print the bottom border
    print(border)

    # Print column labels
    col_str = "     "
    for col_num in range(1, size + 1):
        col_str += f"{col_num:<3}"
    print(col_str)


def random_row(brd):
    """
    random row function
    """
    return random.randint(0, len(brd) - 1)


def random_col(brd):
    """
    random column function
    """
    return random.randint(0, len(brd[0]) - 1)


def is_valid_tank_placement(brd, row, col, length, orientation):
    """function to check if the tank placement is valid."""
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
    place tank function
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
    place tanks function
    """
    for _ in range(num_tanks):
        tank_length = random.choice(TANK_SIZES)
        placed = False
        while not placed:
            placed = place_tank(brd, tank_length)


def select_difficulty():
    """
    select difficulty function
    """
    print(f"{BOLD}{GREEN}Select difficulty level:{RESET}\n")
    print(f"{CYAN}1. {GREEN}Easy{RESET}")
    print(" 5x5 board with 2 Tanks - 10 turns\n")
    print(f"{CYAN}2. {YELLOW}Medium{RESET}")
    print(" 7x7 board with 3 Tanks - 15 turns\n")
    print(f"{CYAN}3. {RED}Hard{RESET}")
    print(" 10x10 board with 5 Tanks - 20 turns\n")

    while True:
        print("\nChoose (1, 2, or 3) and press ENTER:", end=" ")
        choice = input(f"{CYAN}\n>>> {RESET}")

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
    """turn color function"""
    mid_turn = total_turns // 2
    if turn <= mid_turn:
        return f"{GREEN}{turn}{RESET}"
    if turn <= (total_turns - mid_turn) + mid_turn - 1:
        return f"{YELLOW}{turn}{RESET}"
    return f"{RED}{turn}{RESET}"


def get_input(prompt, valid_func):
    """get input function"""
    while True:
        value = input(prompt)
        if valid_func(value):
            return value


def valid_row(value):
    """valid row function"""
    if len(value) != 1 or not value.isalpha():
        print(f"{RED}Please enter a single letter.{RESET}")
        return False
    return True


def valid_col(value):
    """valid col function"""
    if not value.isdigit():
        print(f"{RED}Please enter a number.{RESET}")
        return False
    return True


def get_row_col(size):
    """get row col function"""
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
    """update game state function"""
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
    """game loop function"""
    player_brd, enemy_brd = create_brd(size), create_brd(size)
    place_tanks(enemy_brd, num_tanks)

    game_state = {"turns": 0, "tanks_destr": 0, "event_message": ""}

    while game_state["turns"] < turn_limit:
        clear_screen()
        print(LOGO)
        if game_state["event_message"]:
            print(game_state["event_message"])
        colored_turn = get_turn_color(game_state["turns"] + 1, turn_limit)
        if game_state["turns"] + 1 == turn_limit:
            print(f"\nTurn {colored_turn}/{turn_limit} {RED}Last!{RESET}")
        else:
            print(f"\nTurn {colored_turn}/{turn_limit}")
        print_brd(player_brd)

        row, col = get_row_col(size)

        if row not in range(size) or col not in range(size):
            game_state["event_message"] = event_messages["oops"]
        elif player_brd[row][col] in ("X", " !"):
            game_state["event_message"] = event_messages["same"]
        else:
            (game_state["event_message"], player_brd, enemy_brd,
             game_state["tanks_destr"], game_over) = update_game_state(
             player_brd, enemy_brd, row, col, game_state["tanks_destr"])
        if game_over:
            print(event_messages["congrats"])
        game_state["turns"] += 1

    return game_state, player_brd, enemy_brd


def play_game(player_index=None, signed_in=False):
    """play game function"""
    while True:
        clear_screen()
        print(LOGO)
        size, num_tanks, turn_limit = select_difficulty()
        game_state, _, enemy_brd = game_loop(size, num_tanks, turn_limit)

        if game_state["turns"] == turn_limit:
            print(event_messages["game_over"])
            print(event_messages["enemy_tanks"])
            print_brd(enemy_brd)

        score = int(game_state["tanks_destr"] * 10 *
                    [1, 1.2, 1.3][turn_limit // 5 - 2])
        print(f"You scored: {GREEN}{score} points!{RESET}")

        if player_index is not None:
            highscores = get_highscores_worksheet()
            old_score = highscores.cell(player_index + 2, 3).value
            highscores.update_cell(player_index + 2, 3, int(old_score) + score)
        elif not signed_in:
            print(f"\nYou are not signed in{RED} !!!{RESET}")
            print(f"Your score will {RED}not be "
                  f"saved{RESET}.")

        play_again = prompt_play_again()
        if play_again == 'n':
            break


def prompt_play_again():
    """play again promt"""
    while True:
        print(f"{YELLOW}\nWant to PLAY AGAIN? {RESET}(y/n):", end=" ")
        play_again = input(f"{CYAN}\n>>> {RESET}").lower()

        if play_again in ('y', 'n'):
            return play_again
        print(f"{RED}Please ENTER 'y' or 'n'.{RESET}")

"""
Main game
"""
import os
import random
from colorama import Fore, Style, init
from art import LOGO
from modules.google_sheets import get_highscores_worksheet

init()

DIFFICULTY_LEVELS = {
    1: {"size": 5, "num_ships": 2, "turn_limit": 10},
    2: {"size": 7, "num_ships": 3, "turn_limit": 15},
    3: {"size": 10, "num_ships": 4, "turn_limit": 20},
}

SHIP_SIZES = [2]  # Custom ship sizes


def clear_screen():
    """clears board for new one"""
    os.system("cls" if os.name == "nt" else "clear")


def create_board(size):
    """
    create board function
    """
    return [["~" for _ in range(size)] for _ in range(size)]


def print_board(board):
    """
    print board function
    """
    size = len(board)
    border = f"   +{'-' * (size * 3 + 1)}+"

    # Print the top border
    print(border.center(40))

    # Print row labels and board content
    for row_num, row in enumerate(board, start=1):
        row_label = chr(row_num + 64)  # Convert row number to letters
        row_str = f" {row_label} | "
        for cell in row:
            row_str += f"{cell:<3}"
        row_str += "|"
        print(row_str.center(40))

    # Print the bottom border
    print(border.center(40))

    # Print column labels
    col_str = "   "
    for col_num in range(1, size + 1):
        col_str += f"{col_num:<3}"
    print(col_str.center(40))


def random_row(board):
    """
    random row function
    """
    return random.randint(0, len(board) - 1)


def random_col(board):
    """
    random column function
    """
    return random.randint(0, len(board[0]) - 1)


def is_valid_ship_placement(board, row, col, length, orientation):
    """function to check if the ship placement is valid."""
    for i in range(length):
        if orientation == "horizontal":
            if col + i >= len(board[0]) or board[row][col + i] == "S":
                return False
        else:
            if row + i >= len(board) or board[row + i][col] == "S":
                return False
    return True


def place_ship(board, length):
    """
    place ship function
    """
    orientation = random.choice(["horizontal", "vertical"])
    if orientation == "horizontal":
        row, col = random_row(board), random.randint(0, len(board[0]) - length)
        if not is_valid_ship_placement(board, row, col, length, orientation):
            return False
        for i in range(length):
            board[row][col + i] = "S"
    else:
        row, col = random.randint(0, len(board) - length), random_col(board)
        if not is_valid_ship_placement(board, row, col, length, orientation):
            return False
        for i in range(length):
            board[row + i][col] = "S"
    return True


def place_ships(board, num_ships):
    """
    place ships function
    """
    for _ in range(num_ships):
        ship_length = random.choice(SHIP_SIZES)
        placed = False
        while not placed:
            placed = place_ship(board, ship_length)


def select_difficulty():
    """
    select difficulty function
    """
    print(f"{Fore.GREEN}Select difficulty level:{Style.RESET_ALL}\n")
    print(f"{Fore.CYAN}1. {Fore.GREEN}Easy{Style.RESET_ALL}")
    print(" 5x5 board with 2 ships - 10 turns\n")
    print(f"{Fore.CYAN}2. {Fore.YELLOW}Medium{Style.RESET_ALL}")
    print(" 7x7 board with 3 ships - 15 turns\n")
    print(f"{Fore.CYAN}3. {Fore.RED}Hard{Style.RESET_ALL}")
    print(" 10x10 board with 5 ships - 20 turns\n")

    print("\nChoose (1, 2, or 3) and press Enter:", end=" ")
    choice = int(input(f"{Fore.CYAN}\n>>> {Style.RESET_ALL}"))
    if choice == 1:
        return 5, 2, 10
    if choice == 2:
        return 7, 3, 15
    return 10, 4, 20


def get_input(prompt, valid_func):
    """get input function"""
    while True:
        value = input(prompt)
        if valid_func(value):
            return value


def valid_row(value):
    """valid row function"""
    if len(value) != 1 or not value.isalpha():
        print("Invalid input. Please enter a single letter.")
        return False
    return True


def valid_col(value):
    """get col function"""
    if len(value) != 1 or not value.isdigit():
        print("Invalid input. Please enter a single number.")
        return False
    return True


def play_game(player_index=None):
    """play game function"""
    while True:
        clear_screen()
        print(LOGO)
        size, num_ships, turn_limit = select_difficulty()
        player_board, enemy_board = create_board(size), create_board(size)
        place_ships(enemy_board, num_ships)

        game_state = {"turns": 0, "ships_sunk": 0, "event_message": ""}

        while game_state["turns"] < turn_limit:
            clear_screen()
            print(LOGO)
            if game_state["event_message"]:
                print(game_state["event_message"])
            print(f"\nTurn {game_state['turns'] + 1}/{turn_limit}")
            print_board(player_board)

            row, col = get_row_col(size)

            if row not in range(size) or col not in range(size):
                game_state["event_message"] = ("Oops, that's not even in "
                                               "the ocean.")
            elif player_board[row][col] in ("X", " !"):
                game_state["event_message"] = "You've already tried that spot."
            else:
                (game_state["event_message"], player_board, enemy_board,
                 game_state["ships_sunk"]) = update_game_state(
                 player_board, enemy_board, row, col, game_state["ships_sunk"])

            game_state["turns"] += 1

        if game_state["turns"] == turn_limit:
            print("Game over! You ran out of turns.")
            print("The enemy battleships were at:")
            print_board(enemy_board)

        score = int(game_state["ships_sunk"] * 10 *
                    [1, 1.2, 1.3][turn_limit // 5 - 2])
        print(f"You scored {score} points!")

        if player_index is not None:
            highscores = get_highscores_worksheet()
            old_score = highscores.cell(player_index + 2, 3).value
            highscores.update_cell(player_index + 2, 3, int(old_score) + score)

        play_again = input("Do you want to play again? (yes or no): ")
        if play_again.lower() == "no":
            break


def get_row_col(size):
    """get row col function"""
    row_input = get_input(
        f"Enter row (A-{chr(64 + size)}): ", valid_row
        ).upper()
    row = ord(row_input) - 65
    col_input = get_input(f"Enter column (1-{size}): ", valid_col)
    col = int(col_input) - 1
    return row, col


def update_game_state(player_board, enemy_board, row, col, ships_sunk):
    """update game state function"""
    if enemy_board[row][col] == "S":
        event_message = "Hit!"
        player_board[row][col] = "!"
        enemy_board[row][col] = "~"
        ships_sunk += 1
        if not any("S" in row for row in enemy_board):
            event_message = "Congratulations! You sunk all the battleships!"
    else:
        event_message = "You missed!"
        player_board[row][col] = "X"
    return event_message, player_board, enemy_board, ships_sunk

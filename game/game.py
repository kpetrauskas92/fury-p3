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

SHIP_SIZES = [2, 3, 4]  # Custom ship sizes


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
    # Print column labels
    print("  ", end="")
    for col_num in range(1, size + 1):
        print(f"{col_num:<3}", end="")
    print()

    # Print row labels and board content
    for row_num, row in enumerate(board, start=1):
        row_label = chr(row_num + 64)  # Convert row number to letters
        print(f"{row_label} ", end="")
        for cell in row:
            print(f"{cell:<3}", end="")
        print()


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


def place_ships(board, ship_sizes):
    """
    place ships function
    """
    for ship_size in ship_sizes:
        while not place_ship(board, ship_size):
            pass


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
    elif choice == 2:
        return 7, 3, 15
    else:
        return 10, 4, 20


def play_game(player_index=None):
    """
    Plays a game of Battleship.
    """
    while True:
        clear_screen()
        print(LOGO)
        size, num_ships, turn_limit = select_difficulty()
        player_board = create_board(size)
        enemy_board = create_board(size)
        place_ships(enemy_board, SHIP_SIZES[:num_ships])

        turns = 0
        ships_sunk = 0

        while turns < turn_limit:
            clear_screen()
            print(f"\nTurn {turns + 1}/{turn_limit}")
            print_board(player_board)

            while True:
                row_input = input(f"Enter row (A-{chr(64 + size)}): ").upper()
                if len(row_input) == 1 and row_input.isalpha():
                    row = ord(row_input) - 65
                    break
                else:
                    print("Please enter a single letter for the row.")

            while True:
                col_input = input(f"Enter column (1-{size}): ")
                if len(col_input) == 1 and col_input.isdigit():
                    col = int(col_input) - 1
                    break
                else:
                    print("Please enter a single number for the column.")

            if row not in range(size) or col not in range(size):
                print("Oops, that's not even in the ocean.")
            elif player_board[row][col] in ("X", "!"):
                print("You've already tried that spot.")
            elif enemy_board[row][col] == "S":
                print("Hit!")
                player_board[row][col] = "!"
                enemy_board[row][col] = "~"
                ships_sunk += 1
                if not any("S" in row for row in enemy_board):
                    print("Congratulations! You sunk all the battleships!")
                    break
            else:
                print("You missed!")
                player_board[row][col] = "X"

            turns += 1

        if turns == turn_limit:
            print("Game over! You ran out of turns.")
            print("The enemy battleships were at:")
            print_board(enemy_board)

        base_points = 10
        if turn_limit == 10:
            score_multiplier = 1
        elif turn_limit == 15:
            score_multiplier = 1.2
        else:
            score_multiplier = 1.3

        score = int(ships_sunk * base_points * score_multiplier)
        print(f"You scored {score} points!")

        if player_index is not None:
            highscores = get_highscores_worksheet()
            old_score = highscores.cell(player_index + 2, 3).value
            new_score = int(old_score) + score
            highscores.update_cell(player_index + 2, 3, new_score)

        play_again = input("Do you want to play again? (yes or no): ")
        if play_again.lower() == "no":
            break

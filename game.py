"""
import random lib
"""
import random


def create_board(size):
    """
    create board function
    """
    return [["~" for _ in range(size)] for _ in range(size)]


def print_board(board):
    """
    print board function
    """
    for row in board:
        print(" ".join(row))


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


def place_ship(board, length):
    """
    place ship function
    """
    orientation = random.choice(["horizontal", "vertical"])
    if orientation == "horizontal":
        row, col = random_row(board), random.randint(0, len(board[0]) - length)
        for i in range(length):
            board[row][col + i] = "S"
    else:
        row, col = random.randint(0, len(board) - length), random_col(board)
        for i in range(length):
            board[row + i][col] = "S"


def place_ships(board, num_ships):
    """
    place ships function
    """
    for _ in range(num_ships):
        place_ship(board, 3)


def select_difficulty():
    """
    select difficulty function
    """
    print("Select difficulty level:")
    print("1. Easy (5x5 board with 2 ship)")
    print("2. Medium (7x7 board with 3 ships)")
    print("3. Hard (10x10 board with 5 ships)")

    choice = int(input("Enter your choice (1, 2, or 3): "))
    if choice == 1:
        return 5, 2
    elif choice == 2:
        return 7, 3
    else:
        return 10, 4


def play_game():
    """
    Plays a game of Battleship.
    """
    print("Welcome to Battleship!")
    size, num_ships = select_difficulty()
    player_board = create_board(size)
    enemy_board = create_board(size)
    place_ships(enemy_board, num_ships)

    turn_limit = 10
    turns = 0

    while turns < turn_limit:
        print(f"Turn {turns + 1}/{turn_limit}")
        print_board(player_board)

        row = int(input(f"Enter row (1-{size}): ")) - 1
        col = int(input(f"Enter column (1-{size}): ")) - 1

        if (row < 0 or row > size - 1) or (col < 0 or col > size - 1):
            print("Oops, that's not even in the ocean.")
        elif player_board[row][col] == "X" or player_board[row][col] == "!":
            print("You've already tried that spot.")
        elif enemy_board[row][col] == "S":
            print("Hit!")
            player_board[row][col] = "!"
            enemy_board[row][col] = "~"
            if not any("S" in row for row in enemy_board):
                print("Congratulations! You sunk all the battleships!")
                break
        else:
            print("Miss!")
            player_board[row][col] = "X"

        turns += 1

    if turns == turn_limit:
        print("Game Over! You ran out of turns.")
        print("The enemy battleships were at:")
        print_board(enemy_board)

"""
import random lib
"""
import random


def random_row(board):
    """
    random row
    """
    return random.randint(0, len(board) - 1)


def random_col(board):
    """
    random column
    """
    return random.randint(0, len(board[0]) - 1)

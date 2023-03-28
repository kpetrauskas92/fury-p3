"""CLEAR SCREEN"""
import os


def clear_screen():
    """
    Clears the console screen for a new board.
    Uses the 'os' module to check the operating system,
    and then runs the appropriate console clear command.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

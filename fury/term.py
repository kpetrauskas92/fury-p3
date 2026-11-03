"""
TERMINAL:
Input/output helpers that work both in a normal terminal and in the
browser, where the game runs on Pyodide and prints to xterm.js.

Input is always awaited so the browser page never freezes while the
game waits for the player.
"""
import asyncio
import os
import sys

IN_BROWSER = sys.platform == "emscripten"


async def read_line():
    """
    Reads one line typed by the player.
    In the browser the line comes from the xterm.js page (web/app.js).
    """
    if IN_BROWSER:
        import js  # pylint: disable=import-outside-toplevel
        return str(await js.furyReadLine())
    return input()


async def ask(prompt=""):
    """Prints the prompt and waits for the player's answer."""
    print(prompt, end="", flush=True)
    return (await read_line()).strip()


async def pause(seconds):
    """Waits without blocking the browser."""
    await asyncio.sleep(seconds)


async def typewriter(text, delay=0.05):
    """
    Simulates a typewriter effect by printing out the characters
    in the given text string one by one with a specified delay.
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        await pause(delay)
    print()


def clear_screen():
    """
    Clears the console screen for a new board.
    The browser terminal understands ANSI codes; a local terminal
    uses the operating system's clear command.
    """
    if IN_BROWSER:
        print("\x1b[2J\x1b[3J\x1b[H", end="", flush=True)
    else:
        # Fixed command string, no user input reaches the shell.
        os.system('cls' if os.name == 'nt' else 'clear')

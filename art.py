"""
ASCII Art
"""
from colorama import Fore, Style, init


init()


MAIN_LOGO = f"""
⠀⠀⠀⣠⣴⠶⠶⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣰⢟⡵⠿⣿⣷⡄⢻⡶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣼⢣⣿⣿⣶⣌⣙⡇⣸⠻⣎⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⠸⡍⠻⣿⣿⠟⣰⣇⠀⢄⠑⢈⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠘⢦⣈⣉⣉⣴⡞⠁⠀⠁⠐⢿⣾⣯⠻⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠉⠛⠯⣝⡻⠦⡄⠈⣢⣾⣿⡿⠀⠀⠙⢦⡀⢀⣀⣀⣀⣠⣤⣄⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠙⠓⠚⠛⠿⣿⣿⣥⡀⠀⠀⠀⠙⢯⣭⣤⣤⣤⣤⣤⣄⠀⣽⢉⠓⠦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣌⠒⢤⡠⣀⠀⢹⣿⡌⠈⠉⠋⡇⠀⡇⣸⠙⠓⠦⣍⣓⣦⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣦⣉⣂⣑⣶⡟⢡⠀⠀⢸⠁⢰⣃⣟⣄⣀⣀⣐⣻⡼⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣠⣿⣩⣿⣿⣏⣉⣭⣥⡤⣧⡶⠒⠛⠛⠛⠛⣿⡟⠿⠿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⠞⡩⡉⢁⠀⣼⣣⠟⠉⠁⠀⡀⠀⠀⣴⢋⣦⠎⢀⣠⡶⠛⣡⢿⡶⠦⣤⣈⡙⠻⢦⣀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣴⡧⠾⠿⣷⣿⣿⡿⢁⠎⣠⢀⣾⣀⣀⣞⣿⠭⢭⣭⢿⣿⣷⢾⣧⡾⠿⠷⢾⡯⣍⣳⡦⣌⡛⠦⣄⠀⠀
⠀⠀⠀⠀⠀⢨⣟⣋⣿⣏⣻⡿⢿⠋⠹⡉⢉⠉⠉⢏⢹⡿⡾⣶⣿⡾⣿⢷⣿⡏⣴⣿⣿⣦⢻⣶⣬⣹⣶⣿⡳⣌⢻⡆
⠀⠀⠀⠀⠀⠈⢯⡈⣏⣯⣆⢹⣼⣧⠀⡄⠀⢻⣆⠀⢀⢻⣄⣸⣹⣇⣸⣦⣿⡆⢿⣷⣾⡟⣸⠛⣿⣻⣿⣿⣿⣾⠻⣇
⠀⠀⠀⠀⠀⠀⠈⢿⣏⢉⣽⣉⠹⣌⣿⣻⣶⣾⣟⣻⣿⣿⣿⡿⣽⠀⣣⠹⡌⣿⣲⣬⡥⣾⣿⣿⣿⣿⣿⣿⣿⣿⡷⣿
⠀⠀⠀⠀⠀⠀⠀⠈⢿⡚⠛⢿⠓⠿⣏⢻⣿⣿⣿⣿⣿⣿⣿⣿⡞⠳⡗⣶⢿⡉⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢻⡞⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⠾⠦⠷⠤⠼⠿⠯⠭⠿⠿⠿⠿⠽⠿⠿⠶⠤⠧⠤⠿⠧⠤⠼⠧⠤⠼⠤⠼⠧⠤⠿⠋⠀⠀

⠀⠀⠀⠀⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⠀⢀⣤⣤⣤⠀⠀⠀⣠⣤⣤⡄⠀⢠⣤⣤⣤⣤⣤⣤⣤⣤⣤⠀⢠⣤⣤⣄⠀⠀⢀⣤⣤⡤⠀⠀
⠀⠀⠀⢰⣿⣿⡿⠿⠿⠿⠿⠿⠿⠏⠀⣼⣿⣿⠇⠀⠀⢠⣿⣿⡿⠀⢀⣿⣿⣿⠿⠿⠿⢿⣿⣿⡿⠀⠈⣿⣿⣿⡀⣴⣿⡿⠋⠀⠀⠀
⠀⠀⢠⣿⣿⣿⣥⣤⣤⣤⣤⡄⠀⠀⢸⣿⣿⡟⠀⠀⠀⣾⣿⣿⠃⠀⣼⣿⣿⣧⣤⣤⣤⣼⣿⣿⠇⠀⠀⢸⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀
⠀⠀⣼⣿⣿⠟⠛⠛⠛⠛⠛⠁⠀⢀⣿⣿⣿⠁⠀⠀⣸⣿⣿⡟⠀⢠⣿⣿⡿⠛⠻⣿⣿⣿⠛⠋⠀⠀⠀⢠⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀
⠀⢰⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣷⣶⣶⣶⣿⣿⡿⠁⢀⣿⣿⣿⠃⠀⠀⢹⣿⣿⣆⠀⠀⠀⠀⣾⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀
⠀⠛⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠛⠛⠛⠛⠛⠛⠋⠁⠀⠘⠛⠛⠋⠀⠀⠀⠀⠛⠛⠛⠂⠀⠀⠘⠛⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀
  {Fore.GREEN}----\"Engage in Epic Tank Warfare!\"----{Style.RESET_ALL}
"""

INTRO_TEXT = """
Welcome to FURY!
Tank warfare: where strategy and firepower meet.
"""

LOGO = f"""
⠀⠀⠀⠀⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⠀⢀⣤⣤⣤⠀⠀⠀⣠⣤⣤⡄⠀⢠⣤⣤⣤⣤⣤⣤⣤⣤⣤⠀⢠⣤⣤⣄⠀⠀⢀⣤⣤⡤⠀⠀
⠀⠀⠀⢰⣿⣿⡿⠿⠿⠿⠿⠿⠿⠏⠀⣼⣿⣿⠇⠀⠀⢠⣿⣿⡿⠀⢀⣿⣿⣿⠿⠿⠿⢿⣿⣿⡿⠀⠈⣿⣿⣿⡀⣴⣿⡿⠋⠀⠀⠀
⠀⠀⢠⣿⣿⣿⣥⣤⣤⣤⣤⡄⠀⠀⢸⣿⣿⡟⠀⠀⠀⣾⣿⣿⠃⠀⣼⣿⣿⣧⣤⣤⣤⣼⣿⣿⠇⠀⠀⢸⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀
⠀⠀⣼⣿⣿⠟⠛⠛⠛⠛⠛⠁⠀⢀⣿⣿⣿⠁⠀⠀⣸⣿⣿⡟⠀⢠⣿⣿⡿⠛⠻⣿⣿⣿⠛⠋⠀⠀⠀⢠⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀
⠀⢰⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣷⣶⣶⣶⣿⣿⡿⠁⢀⣿⣿⣿⠃⠀⠀⢹⣿⣿⣆⠀⠀⠀⠀⣾⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀
⠀⠛⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠛⠛⠛⠛⠛⠛⠋⠁⠀⠘⠛⠛⠋⠀⠀⠀⠀⠛⠛⠛⠂⠀⠀⠘⠛⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀
  {Fore.GREEN}----\"Engage in Epic Tank Warfare!\"----{Style.RESET_ALL}
"""

MAIN_MENU = f"""
{Fore.MAGENTA}⣿ Main Menu ⣿{Style.RESET_ALL}
"""

USER_MENU = f"""
{Fore.MAGENTA}⣿ User Menu ⣿{Style.RESET_ALL}
"""


RULES = """
GAME RULES
Here are the rules you need to know before diving into the game:
   1. Your mission is to destroy all the enemy tanks hidden on the board
   within a limited number of turns.

   2. you'll choose a difficulty level: easy, medium, or hard.
   The difficulty level determines the board size, the number of tanks,
   and the turn limit.
   Once you've made your choice,
   the game will generate a hidden enemy board with randomly placed tanks.

   3. On each turn, you need to guess a row and a column on the enemy board
   where you think a tank might be.
   Rows are represented by letters (e.g., A, B, C),
   and columns are represented by numbers (e.g., 1, 2, 3).

   4. After you make your guess, the game will reveal
      whether you've hit a tank or missed:

  If you hit a tank, the cell on your player board will be marked with an "!".
  If you miss, the cell on your player board will be marked with an "X".

   5. The game will end in one of two ways:

  If you manage to destroy all the tanks, you win!
  If you reach the turn limit, the game is over.

"""

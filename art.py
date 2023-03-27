"""
ASCII Art
"""
from colorama import Fore, Style

GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
MAGENTA = Fore.MAGENTA
RED = Fore.RED
RESET = Style.RESET_ALL


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

{GREEN}⠀⠀⠀⠀⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⠀⢀⣤⣤⣤⠀⠀⠀⣠⣤⣤⡄⠀⢠⣤⣤⣤⣤⣤⣤⣤⣤⣤⠀⢠⣤⣤⣄⠀⠀⢀⣤⣤⡤{RESET}⠀⠀
{GREEN}⠀⠀⠀⢰⣿⣿⡿⠿⠿⠿⠿⠿⠿⠏⠀⣼⣿⣿⠇⠀⠀⢠⣿⣿⡿⠀⢀⣿⣿⣿⠿⠿⠿⢿⣿⣿⡿⠀⠈⣿⣿⣿⡀⣴⣿⡿⠋{RESET}⠀⠀⠀
{GREEN}⠀⠀⢠⣿⣿⣿⣥⣤⣤⣤⣤⡄⠀⠀⢸⣿⣿⡟⠀⠀⠀⣾⣿⣿⠃⠀⣼⣿⣿⣧⣤⣤⣤⣼⣿⣿⠇⠀⠀⢸⣿⣿⣿⣿⠟{RESET}⠀⠀⠀⠀⠀
{GREEN}⠀⠀⣼⣿⣿⠟⠛⠛⠛⠛⠛⠁⠀⢀⣿⣿⣿⠁⠀⠀⣸⣿⣿⡟⠀⢠⣿⣿⡿⠛⠻⣿⣿⣿⠛⠋⠀⠀⠀⢠⣿⣿⡿⠁{RESET}⠀⠀⠀⠀⠀⠀
{GREEN}⠀⢰⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣷⣶⣶⣶⣿⣿⡿⠁⢀⣿⣿⣿⠃⠀⠀⢹⣿⣿⣆⠀⠀⠀⠀⣾⣿⣿⠇{RESET}⠀⠀⠀⠀⠀⠀⠀
{GREEN}⠀⠛⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠛⠛⠛⠛⠛⠛⠋⠁⠀⠘⠛⠛⠋⠀⠀⠀⠀⠛⠛⠛⠂⠀⠀⠘⠛⠛⠋{RESET}⠀⠀⠀⠀⠀⠀⠀⠀
   {YELLOW}----/"Engage in Epic Tank Warfare!/"----{RESET}
"""

INTRO_TEXT = f"""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ {GREEN}Welcome to FURY!{RESET} ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
{YELLOW}Tank warfare: where strategy and firepower meet.{RESET}
"""

LOGO = f"""
{GREEN}⠀⠀⠀⠀⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⠀⢀⣤⣤⣤⠀⠀⠀⣠⣤⣤⡄⠀⢠⣤⣤⣤⣤⣤⣤⣤⣤⣤⠀⢠⣤⣤⣄⠀⠀⢀⣤⣤⡤{RESET}⠀⠀
{GREEN}⠀⠀⠀⢰⣿⣿⡿⠿⠿⠿⠿⠿⠿⠏⠀⣼⣿⣿⠇⠀⠀⢠⣿⣿⡿⠀⢀⣿⣿⣿⠿⠿⠿⢿⣿⣿⡿⠀⠈⣿⣿⣿⡀⣴⣿⡿⠋{RESET}⠀⠀⠀
{GREEN}⠀⠀⢠⣿⣿⣿⣥⣤⣤⣤⣤⡄⠀⠀⢸⣿⣿⡟⠀⠀⠀⣾⣿⣿⠃⠀⣼⣿⣿⣧⣤⣤⣤⣼⣿⣿⠇⠀⠀⢸⣿⣿⣿⣿⠟{RESET}⠀⠀⠀⠀⠀
{GREEN}⠀⠀⣼⣿⣿⠟⠛⠛⠛⠛⠛⠁⠀⢀⣿⣿⣿⠁⠀⠀⣸⣿⣿⡟⠀⢠⣿⣿⡿⠛⠻⣿⣿⣿⠛⠋⠀⠀⠀⢠⣿⣿⡿⠁{RESET}⠀⠀⠀⠀⠀⠀
{GREEN}⠀⢰⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣷⣶⣶⣶⣿⣿⡿⠁⢀⣿⣿⣿⠃⠀⠀⢹⣿⣿⣆⠀⠀⠀⠀⣾⣿⣿⠇{RESET}⠀⠀⠀⠀⠀⠀⠀
{GREEN}⠀⠛⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠛⠛⠛⠛⠛⠛⠋⠁⠀⠘⠛⠛⠋⠀⠀⠀⠀⠛⠛⠛⠂⠀⠀⠘⠛⠛⠋{RESET}⠀⠀⠀⠀⠀⠀⠀⠀
       {YELLOW}----/"Epic Tank Warfare!/"----{RESET}
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
"""

MAIN_MENU = f"""
{MAGENTA}⣿ Main Menu ⣿{RESET}
"""

USER_MENU = f"""
{MAGENTA}⣿ User Menu ⣿{RESET}
"""


RULES = f"""
  +⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿{GREEN} --GAME RULES-- {RESET}⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿+
  ⣿                                              ⣿
  ⣿  1. {YELLOW}Destroy all enemy tanks on the board{RESET}     ⣿
  ⣿     {YELLOW}within a limited number of turns.{RESET}        ⣿
  ⣿                                              ⣿
  ⣿  2. {YELLOW}Choose a difficulty level{RESET}                ⣿
  ⣿     {YELLOW}(easy, medium, or hard){RESET}                  ⣿
  ⣿                                              ⣿
  ⣿  3. {YELLOW}Guess a row (letter) and column (number){RESET} ⣿
  ⣿     {YELLOW}on the enemy board to target a tank.{RESET}     ⣿
  ⣿                                              ⣿
  ⣿  4. {YELLOW}A hit is marked with "!" on your board,{RESET}  ⣿
  ⣿     {YELLOW}while a miss is marked with "X".{RESET}         ⣿
  ⣿                                              ⣿
  ⣿  5. {YELLOW}Win by destroying all tanks or lose{RESET}      ⣿
  ⣿     {YELLOW}if turn limit is reached.{RESET}                ⣿
  ⣿                                              ⣿
  ⣿  6. {YELLOW}Score is based on number{RESET}                 ⣿
  ⣿     {YELLOW}of tanks destroyed{RESET}                       ⣿
  ⣿     {YELLOW}and the chosen difficulty level.{RESET}         ⣿
  ⣿                                              ⣿
  +⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿+

    {GREEN}Plan your moves CAREFULLY and enjoy the game!{RESET}
"""

"""
ASCII Art
"""
from colorama import Fore, Style

GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
MAGENTA = Fore.MAGENTA
RED = Fore.RED
BOLD = Style.BRIGHT
RESET = Style.RESET_ALL


MAIN_LOGO = f"""
{BOLD}
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
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⠾⠦⠷⠤⠼⠿⠯⠭⠿⠿⠿⠿⠽⠿⠿⠶⠤⠧⠤⠿⠧⠤⠼⠧⠤⠼⠤⠼⠧⠤⠿⠋⠀⠀{RESET}
{BOLD}{GREEN}
⠀⠀⠀⠀⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⠀⢀⣤⣤⣤⠀⠀⠀⣠⣤⣤⡄⠀⢠⣤⣤⣤⣤⣤⣤⣤⣤⣤⠀⢠⣤⣤⣄⠀⠀⢀⣤⣤⡤
⠀⠀⠀⢰⣿⣿⡿⠿⠿⠿⠿⠿⠿⠏⠀⣼⣿⣿⠇⠀⠀⢠⣿⣿⡿⠀⢀⣿⣿⣿⠿⠿⠿⢿⣿⣿⡿⠀⠈⣿⣿⣿⡀⣴⣿⡿⠋
⠀⠀⢠⣿⣿⣿⣥⣤⣤⣤⣤⡄⠀⠀⢸⣿⣿⡟⠀⠀⠀⣾⣿⣿⠃⠀⣼⣿⣿⣧⣤⣤⣤⣼⣿⣿⠇⠀⠀⢸⣿⣿⣿⣿⠟
⠀⠀⣼⣿⣿⠟⠛⠛⠛⠛⠛⠁⠀⢀⣿⣿⣿⠁⠀⠀⣸⣿⣿⡟⠀⢠⣿⣿⡿⠛⠻⣿⣿⣿⠛⠋⠀⠀⠀⢠⣿⣿⡿⠁
⠀⢰⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣷⣶⣶⣶⣿⣿⡿⠁⢀⣿⣿⣿⠃⠀⠀⢹⣿⣿⣆⠀⠀⠀⠀⣾⣿⣿⠇
⠀⠛⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠛⠛⠛⠛⠛⠛⠋⠁⠀⠘⠛⠛⠋⠀⠀⠀⠀⠛⠛⠛⠂⠀⠀⠘⠛⠛⠋{RESET}
"""

INTRO_TEXT = f"""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿  {BOLD}{GREEN}Tank Warfare{RESET}  ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
"""

LOGO = f"""
{BOLD}{GREEN}
⠀⠀⠀⠀⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⠀⢀⣤⣤⣤⠀⠀⠀⣠⣤⣤⡄⠀⢠⣤⣤⣤⣤⣤⣤⣤⣤⣤⠀⢠⣤⣤⣄⠀⠀⢀⣤⣤⡤
⠀⠀⠀⢰⣿⣿⡿⠿⠿⠿⠿⠿⠿⠏⠀⣼⣿⣿⠇⠀⠀⢠⣿⣿⡿⠀⢀⣿⣿⣿⠿⠿⠿⢿⣿⣿⡿⠀⠈⣿⣿⣿⡀⣴⣿⡿⠋
⠀⠀⢠⣿⣿⣿⣥⣤⣤⣤⣤⡄⠀⠀⢸⣿⣿⡟⠀⠀⠀⣾⣿⣿⠃⠀⣼⣿⣿⣧⣤⣤⣤⣼⣿⣿⠇⠀⠀⢸⣿⣿⣿⣿⠟
⠀⠀⣼⣿⣿⠟⠛⠛⠛⠛⠛⠁⠀⢀⣿⣿⣿⠁⠀⠀⣸⣿⣿⡟⠀⢠⣿⣿⡿⠛⠻⣿⣿⣿⠛⠋⠀⠀⠀⢠⣿⣿⡿⠁
⠀⢰⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣷⣶⣶⣶⣿⣿⡿⠁⢀⣿⣿⣿⠃⠀⠀⢹⣿⣿⣆⠀⠀⠀⠀⣾⣿⣿⠇
⠀⠛⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠛⠛⠛⠛⠛⠛⠋⠁⠀⠘⠛⠛⠋⠀⠀⠀⠀⠛⠛⠛⠂⠀⠀⠘⠛⠛⠋{RESET}
 {BOLD}“Ideals are peaceful. History is violent.”{RESET}
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
"""

MAIN_MENU = f"""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿  {BOLD}{MAGENTA}MAIN MENU {RESET} ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
"""

USER_MENU = f"""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿  {BOLD}{MAGENTA}USER MENU {RESET} ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
"""


RULES = f"""
+⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿{GREEN} --GAME RULES-- {RESET}⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿+
⣿                                              ⣿
⣿  1. {BOLD}{YELLOW}Destroy all enemy tanks on the board{RESET}     ⣿
⣿     {BOLD}{YELLOW}within a limited number of turns.{RESET}        ⣿
⣿                                              ⣿
⣿  2. {BOLD}{YELLOW}Choose a difficulty level{RESET}                ⣿
⣿     {BOLD}{YELLOW}(easy, medium, or hard){RESET}                  ⣿
⣿                                              ⣿
⣿  3. {BOLD}{YELLOW}Guess a row (letter) and column (number){RESET} ⣿
⣿     {BOLD}{YELLOW}on the enemy board to target a tank.{RESET}     ⣿
⣿                                              ⣿
⣿  4. {BOLD}{YELLOW}A hit is marked with "!" on your board,{RESET}  ⣿
⣿     {BOLD}{YELLOW}while a miss is marked with "X".{RESET}         ⣿
⣿                                              ⣿
⣿  5. {BOLD}{YELLOW}Win by destroying all tanks or lose{RESET}      ⣿
⣿     {BOLD}{YELLOW}if turn limit is reached.{RESET}                ⣿
⣿                                              ⣿
⣿  6. {BOLD}{YELLOW}Score is based on number{RESET}                 ⣿
⣿     {BOLD}{YELLOW}of tanks destroyed{RESET}                       ⣿
⣿     {BOLD}{YELLOW}and the chosen difficulty level.{RESET}         ⣿
⣿                                              ⣿
+⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿+

  Plan your moves {BOLD}{YELLOW}CAREFULLY{RESET} and enjoy the game!
"""

"""
ASCII art, created using characters from the ASCII character set.

Usage:
To print the ASCII art, simply call the `print` function on the variable.
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
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿  {BOLD}{GREEN}Tank Warfare{RESET}  ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
"""

# INTRO_TEXT = f"""
# ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿  {BOLD}{GREEN}Tank Warfare{RESET}  ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
# """

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

LOGO_2 = f"""
{BOLD}{GREEN}
⠀⠀⠀⠀⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⠀⢀⣤⣤⣤⠀⠀⠀⣠⣤⣤⡄⠀⢠⣤⣤⣤⣤⣤⣤⣤⣤⣤⠀⢠⣤⣤⣄⠀⠀⢀⣤⣤⡤
⠀⠀⠀⢰⣿⣿⡿⠿⠿⠿⠿⠿⠿⠏⠀⣼⣿⣿⠇⠀⠀⢠⣿⣿⡿⠀⢀⣿⣿⣿⠿⠿⠿⢿⣿⣿⡿⠀⠈⣿⣿⣿⡀⣴⣿⡿⠋
⠀⠀⢠⣿⣿⣿⣥⣤⣤⣤⣤⡄⠀⠀⢸⣿⣿⡟⠀⠀⠀⣾⣿⣿⠃⠀⣼⣿⣿⣧⣤⣤⣤⣼⣿⣿⠇⠀⠀⢸⣿⣿⣿⣿⠟
⠀⠀⣼⣿⣿⠟⠛⠛⠛⠛⠛⠁⠀⢀⣿⣿⣿⠁⠀⠀⣸⣿⣿⡟⠀⢠⣿⣿⡿⠛⠻⣿⣿⣿⠛⠋⠀⠀⠀⢠⣿⣿⡿⠁
⠀⢰⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣷⣶⣶⣶⣿⣿⡿⠁⢀⣿⣿⣿⠃⠀⠀⢹⣿⣿⣆⠀⠀⠀⠀⣾⣿⣿⠇
⠀⠛⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠛⠛⠛⠛⠛⠛⠋⠁⠀⠘⠛⠛⠋⠀⠀⠀⠀⠛⠛⠛⠂⠀⠀⠘⠛⠛⠋{RESET}
"""

MAIN_MENU = f"""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿  {BOLD}{MAGENTA}MAIN MENU {RESET} ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
"""

LOGIN = f"""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿  {BOLD}{MAGENTA}LOG IN {RESET} ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿

Please enter you name and city soldier.
"""

LEADERBOARD = f"""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿  {BOLD}{MAGENTA}LEADERBOARD {RESET} ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
"""

REGISTER = f"""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿  {BOLD}{MAGENTA}REGISTER {RESET} ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿

Register now and get {BOLD}{GREEN}100 extra points{RESET}!
"""

USER_MENU = f"""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿  {BOLD}{MAGENTA}USER MENU {RESET} ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
"""

ERROR = f"""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿  {BOLD}{RED}-ERROR- {RESET} ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
"""

GAME_OVER = f"""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿  {BOLD}{RED}-GAME OVER- {RESET} ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
"""

WINNER = f"""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿  {BOLD}{GREEN}WELL DONE ! {RESET} ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿

 {BOLD}Congratulations on winning the fury tank game!{RESET}
"""

LINE = f"""
{BOLD}⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿{RESET}
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

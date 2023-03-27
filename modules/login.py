""" Login module """
import re
from operator import itemgetter
from colorama import Fore, Style

GREEN = Fore.GREEN
CYAN = Fore.CYAN
YELLOW = Fore.YELLOW
RED = Fore.RED
RESET = Style.RESET_ALL


def login(highscores):
    """ Login function checks gsheets for existing data  """
    player_name = input(f"{YELLOW}Enter your name:{RESET} ")
    while not re.match(r'^[A-Za-z]{3,10}$', player_name):
        print(RED + "Invalid name. Please enter a name with "
              "3 to 10 letters." + RESET)
        player_name = input(f"{YELLOW}Enter your name:{RESET} ")

    player_city = input(f"{YELLOW}Enter your city:{RESET} ")
    while not re.match(r'^[A-Za-z]{3,10}$', player_city):
        print(RED + "Invalid city name. Please enter a city name with "
              "3 to 10 letters." + RESET)
        player_city = input(f"{YELLOW}Enter your city:{RESET} ")

    records = highscores.get_all_records()

    # Sort the records by 'SCORE' in descending order
    sorted_records = sorted(records, key=itemgetter('SCORE'), reverse=True)

    for index, record in enumerate(sorted_records):
        if (record["NAME"].lower() == player_name.lower()
                and record["CITY"].lower() == player_city.lower()):
            welcome_msg = f"\nWelcome back {GREEN}{record['NAME']}!"
            print(welcome_msg + RESET)
            highscore_msg = f"You have {YELLOW}{record['SCORE']} points."
            print(highscore_msg + RESET)
            position = index + 1
            position_msg = (f"Your position is: "
                            f"/{GREEN}{position}{RESET}/ "
                            "on the leaderboard.")
            print(position_msg)
            return index

    print(RED + "Player not found. Please try again." + RESET)
    return None

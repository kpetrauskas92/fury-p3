""" Login module """
import re
from operator import itemgetter
from colorama import Fore, Style, init

init()


def login(highscores):
    """ Login function checks gsheets for existing data  """
    player_name = input(f"{Fore.YELLOW}Enter your name:{Style.RESET_ALL} ")
    while not re.match(r'^[A-Za-z]{3,10}$', player_name):
        print(Fore.RED + "Invalid name. Please enter a name with "
              "3 to 10 letters." + Style.RESET_ALL)
        player_name = input(f"{Fore.YELLOW}Enter your name:{Style.RESET_ALL} ")

    player_city = input(f"{Fore.YELLOW}Enter your city:{Style.RESET_ALL} ")
    while not re.match(r'^[A-Za-z]{3,10}$', player_city):
        print(Fore.RED + "Invalid city name. Please enter a city name with "
              "3 to 10 letters." + Style.RESET_ALL)
        player_city = input(f"{Fore.YELLOW}Enter your city:{Style.RESET_ALL} ")

    records = highscores.get_all_records()

    # Sort the records by 'SCORE' in descending order
    sorted_records = sorted(records, key=itemgetter('SCORE'), reverse=True)

    for index, record in enumerate(sorted_records):
        if (record["NAME"].lower() == player_name.lower()
                and record["CITY"].lower() == player_city.lower()):
            welcome_msg = f"\n{Fore.GREEN}Welcome back {record['NAME']}!"
            print(welcome_msg + Style.RESET_ALL)
            highscore_msg = f"{Fore.YELLOW}Your score is {record['SCORE']}."
            print(highscore_msg + Style.RESET_ALL)
            position = index + 1
            position_msg = (f"Your position is: "
                            f"/{Fore.GREEN}{position}{Style.RESET_ALL}/ "
                            "on the leaderboard.")
            print(position_msg)
            return index

    print(Fore.RED + "Player not found. Please try again." + Style.RESET_ALL)
    return None

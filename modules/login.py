""" Login module """
from operator import itemgetter
from colorama import Fore, Style, init

init()


def login(highscores):
    """ Login function checks gsheets for existing data  """
    player_name = input("Enter your name: ")
    player_city = input("Enter your city: ")

    records = highscores.get_all_records()

    # Sort the records by 'SCORE' in descending order
    sorted_records = sorted(records, key=itemgetter('SCORE'), reverse=True)

    for index, record in enumerate(sorted_records):
        if (record["NAME"].lower() == player_name
                and record["CITY"].lower() == player_city):
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

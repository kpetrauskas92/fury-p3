""" Login module """
from operator import itemgetter


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
            print(f"Welcome back {record['NAME']}!")
            print(f"Your high score is {record['SCORE']}.")
            position = index + 1
            print(f"You are currently in position {position} on"
                  " the leaderboard.")
            return index

    print("Player not found. Please try again.")
    return None

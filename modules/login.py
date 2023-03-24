""" Login module """


def login(highscores):
    """ Login function checks gsheets for existing data  """
    player_name = input("Enter your name: ")
    player_city = input("Enter your city: ")

    records = highscores.get_all_records()

    for index, record in enumerate(records):
        if record["NAME"] == player_name and record["CITY"] == player_city:
            print(f"Welcome back {record['NAME']}!")
            print(f"Your high score is {record['SCORE']}.")
            return index

    print("Player not found. Please try again.")
    return None

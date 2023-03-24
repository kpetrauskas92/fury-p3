""" Login module """


def login(highscores):
    """ Login function checks gsheets for existing data  """
    player_name = input("Enter your name: ")
    player_city = input("Enter your city: ")

    records = highscores.get_all_records()

    for record in records:
        if record["NAME"] == player_name and record["CITY"] == player_city:
            print(f"Welcome back {player_name}!")
            print(f"Your high score is {record['SCORE']}.")
            return True

    print("Player not found. Please try again.")
    return False

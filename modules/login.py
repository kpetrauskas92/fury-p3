""" Login function """


def login(highscores):
    """ Login function checks gsheets for existing data  """
    player_name = input("Enter your name: ")
    player_city = input("Enter your city: \n")

    records = highscores.get_all_records()

    for record in records:
        if record["NAME"] == player_name and record["CITY"] == player_city:
            print(f"Welcome {player_name}!")
            print(f"Your high score is {record['SCORE']}.")
            return True

    print("Player not found. Please try again.")
    return False

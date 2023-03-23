"""
Import
"""
import gspread
from google.oauth2.service_account import Credentials
# from game import play_game
from art import LOGO


# Google Sheets API credentials
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('fury_data')
HIGHSCORES = SHEET.worksheet('highscores')


def display_main_menu():
    """ Displays main menu"""
    print("Main Menu:\n")
    print("1. Login")
    print("2. Register")
    print("3. Leaderboard")


if __name__ == "__main__":
    print(LOGO)
    display_main_menu()

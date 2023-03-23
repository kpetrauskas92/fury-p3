""" Google Sheets API initialization """
import gspread
from google.oauth2.service_account import Credentials


def get_highscores_worksheet():
    """ Access the Google Sheets and Google Drive APIs """
    scope = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = Credentials.from_service_account_file('creds.json')
    scoped_creds = creds.with_scopes(scope)
    gspread_client = gspread.authorize(scoped_creds)
    sheet = gspread_client.open('fury_data')
    highscores = sheet.worksheet('highscores')
    return highscores

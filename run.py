import gspread
from google.oauth2.service_account import Credentials
import random
from prettytable import PrettyTable

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('bank_app')

# Access the sheet
accounts_sheet = SHEET.worksheet("accounts")

from prettytable import PrettyTable

def print_database():
    """Print all accounts in the database in a formatted table."""
    accounts = accounts_sheet.get_all_records()
    if not accounts:
        print("No accounts found in the database.")
        return

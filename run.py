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


    # Create a PrettyTable instance
    table = PrettyTable()
    table.field_names = ["Name", "Account Number", "Balance (£)"]

    for account in accounts:
        table.add_row([account['Name'], account['Account Number'], account['Balance']])

    print(table)

    
# check if an amount is a numeric
def is_money(value):
    """Check if a string can be converted to a float."""
    try:
        float(value)
        return True
    except ValueError:
        return False

def find_account(account_number):
    """Find an account by account number."""
    accounts = accounts_sheet.get_all_records()
    for index, account in enumerate(accounts):
        ## convert both values to string for easy comparisim 
        if str(account['Account Number']) == str(account_number):
            return index + 2, account  # Return row number and account details
    return None, None



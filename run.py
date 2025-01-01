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

def print_database():
    """
    Print all accounts in the database in a formatted table.
    """
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
    """
    Check if a string can be converted to a float.
    """
    try:
        float(value)
        return True
    except ValueError:
        return False

def find_account(account_number):
    """
    Find an account by account number.
    """
    accounts = accounts_sheet.get_all_records()
    for index, account in enumerate(accounts):
        ## convert both values to string for easy comparisim 
        if str(account['Account Number']) == str(account_number):
            return index + 2, account  # Return row number and account details
    return None, None

def generate_account_number():
    """
    Generate a unique 10-digit account number.
    """
    while True:
        account_number = random.randint(1000000000, 9999999999)
        _, account = find_account(account_number)
        if not account:  # Ensure the account number is unique
            return account_number


def create_account(name, initial_balance):
    """
    Create a new account.
    """
    print("Creating account...")
    account_number = generate_account_number()
    accounts_sheet.append_row([name, account_number, float(initial_balance)])
    print(f"Account created successfully. Account Number is: {account_number}")

def debit_account(account_number, amount):
    """
    Debit an amount from the account.
    """
    print("debiting in progress...")
    row, account = find_account(account_number)
    if not account:
        print(f"Account with number '{account_number}' not found.")
        return


    current_balance = account['Balance']
    if current_balance < amount:
        print(f"Insufficient funds, account balance is £{current_balance}")
        return

    new_balance = account['Balance'] - amount
    accounts_sheet.update_cell(row, 3, new_balance)
    print(f"Debited £{amount}. New balance: £{new_balance}.")

def credit_account(account_number, amount):
    """
    Credit an amount to the account.
    """
    print("crediting in progress...")
    row, account = find_account(account_number)
    if not account:
        print(f"Account with number '{account_number}' not found.")
        return

    new_balance = account['Balance'] + amount
    accounts_sheet.update_cell(row, 3, new_balance)
    print(f"Credited £{amount}. New balance: £{new_balance}.")

def display_balance(account_number):
    """
    Display the balance for a specific account.
    """
    print("Wait... Getting balance...")
    _, account = find_account(account_number)
    if not account:
        print(f"Account with number '{account_number}' not found.")
        return

    print(f"Current balance for account {account_number}: £{account['Balance']}")


def main():
    print("==========================")
    print("Welcome to the Banking App")
    print("==========================")

    while True:
        print("\nSelect an option:")

        print("==========================")
        print("1. Create Account")
        print("==========================")
        print("2. Debit Account")
        print("==========================")
        print("3. Credit Account")
        print("==========================")
        print("4. Display Balance")
        print("==========================")
        print("5. Print Database")  # New option
        print("==========================")
        print("6. Exit")
        print("==========================")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter Account Name: ")
            initial_balance = input("Enter initial balance (£):)")
            if not is_money(initial_balance):
                print("Invalid balance amount.")
                continue
            create_account(name, float(initial_balance))
        elif choice == "2":
            account_number = input("Enter account number: ")
            amount = input("Enter amount to debit (£): ")
            if not is_money(amount):
                print("Invalid amount.")
                continue
            debit_account(account_number, float(amount))
        elif choice == "3":
            account_number = input("Enter account number: ")
            amount = input("Enter amount to credit (£): ")
            if not is_money(amount):
                print("Invalid amount.")
                continue
            credit_account(account_number, float(amount))
        elif choice == "4":
            account_number = input("Enter account number: ")
            display_balance(account_number)
        elif choice == "5":
            print_database()  
        elif choice == "6":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

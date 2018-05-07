class Name:
    def __init__(self, first, last, middle):
        self.first_name = first
        self.last_name = last
        self.middle_name = middle
        

class Bank_Account:
    def __init__(self, name, account_type, balance, status):
        self.name = name
        self.account_type = account_type
        self.balance = balance
        self.status = status

    def open_account(self, initial_start):
        initial_start = input("Would you like to open a bank account?: Yes or No ")
        if initial_start == "Yes":
            input("Must have $100 to open an account. Ok?")

        if initial_start == "No":
            input("Ok. Thank you.")

name = Name("James", "Harden", "The Goat")

name.open_account()
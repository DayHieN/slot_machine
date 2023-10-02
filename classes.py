from time import sleep
import random

MAX_AMOUNT = 100
MIN_AMOUNT = 1
MAX_LINES = 3
MIN_LINES = 1


class InvalidAmountException(Exception):
    pass


class Account:
    def __init__(self, name):
        self.name = name
        self.total = 0
        self.options = {

            '1': self.deposit,
            '2': Slot.bet

        }

    def viable_withdraw(self, amount):
        if amount < self.total:
            return
        else:
            raise InvalidAmountException(
                f"Couldn't withdraw ${amount} from your balance. You don't have enough money: ${self.total}"
            )

    def deposit(self):
        amount = int(input("Please, enter an amount to deposit:\n"))
        self.total = self.total + amount
        print(f" ${amount} deposited. Total balance: ${self.total}")

    def withdraw(self):
        try:
            amount = int(input("Please, enter an amount to withdraw:\n"))
            self.viable_withdraw(amount)
            self.total = self.total - amount
            print(f" $Withdraw of {amount}. Total balance: ${self.total}")
        except InvalidAmountException as err:
            print(f"Error: {err}")

    

    def show_account_info(self):
        print(f"{self.name} account.\n Balance: ${self.total}")

class Options:

    def __init__(self, acc, slot):
        self.options = {

            '1': acc.deposit,
            '2': slot.bet

        }

    def console_options(self):
        print("Options:\n 1. Deposit\n 2. Play")
        choice = input("Enter your choice:\n")
        selected_option = self.options.get(choice)
        if selected_option:
            selected_option()
        else:
            print("Invalid choice. Please, enter a valid option.")

class Slot:
    def __init__(self, lines):
        self.bet = 0
        self.winnings = 0
        self.lines = lines
        self.slots = [['A', 'B', 'C', 'D'], [
            'A', 'B', 'C', 'D'], ['A', 'B', 'C', 'D']]
        self.S1 = None
        self.S2 = None
        self.S3 = None

    def viable_bet(self, amount):
        if amount <= MAX_AMOUNT and amount >= MIN_AMOUNT:
            return
        else:
            raise InvalidAmountException(
                f"Can't bet ${amount}. Max bet amount is ${MAX_AMOUNT}. Min bet amount is ${MIN_AMOUNT}"
            )

    def bet(self):
        amount = input(f"Please, enter amount you want to bet:\n")
        self.viable_bet(amount)
        Account.viable_withdraw(amount)
        Account.withdraw(amount)
        self.bet = amount
        print(f"You bet ${amount}.")
        self.roll()

    def roll(self):
        self.S1 = random.choice(self.slots[0])
        self.S2 = random.choice(self.slots[1])
        self.S3 = random.choice(self.slots[2])
        print(f"\n( {self.s1} | {self.S2} | {self.S3} )")

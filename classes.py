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

            '1': self.deposit

        }

    def viableWithdraw(self, amount):
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
            self.viableWithdraw(amount)
            self.total = self.total - amount
            print(f" $Withdraw of {amount}. Total balance: ${self.total}")
        except InvalidAmountException as err:
            print(f"Error: {err}")

    def console_options(self):
        print("Options:\n 1. Deposit")
        choice = input("Enter your choice:\n")
        selected_option = self.options.get(choice)
        if selected_option:
            selected_option()
        else:
            print("Invalid choice. Please, enter a valid option.")

    def show_account_info(self):
        print(f"{self.name} account.\n Balance: ${self.total}")

from classes import *



def play_slot():
    new_account_name = input("Hi! Welcome to Slot Machine. Enter your name:\n")
    new_account = Account(new_account_name)
    new_account.show_account_info()
    slot = Slot(1)
    options = Options(new_account, slot)
    options.console_options()

play_slot()
from slot import Slot
from roulette import Roulette
from options import Options

from account_management import *
import json


def create_account():
    new_account_name = input("Hi! Welcome to Slot Machine. Enter your name:\n")
    new_account = Account(new_account_name)
    new_account.show_account_info()
    return new_account


def play(acc, slot, roulette):

    options = Options(acc, slot, roulette)
    while True:
        options.console_options()


if __name__ == "__main__":

    acc = create_account()
    slot = Slot(acc)
    roulette = Roulette(acc)
    play(acc, slot, roulette)

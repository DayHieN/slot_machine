from time import sleep
import random
from account_management import Account

MAX_AMOUNT = 100
MIN_AMOUNT = 1
MAX_LINES = 3
MIN_LINES = 1


class InvalidAmountException(Exception):
    pass


class Options:

    def __init__(self, acc, slot):
        self.options = {

            '1': slot.bet,
            '2': acc.show_account_info,
            '3': exit

        }

    def console_options(self):
        print("Options:\n 1. Play\n 2. Show account info\n 3. Exit")
        choice = input("Enter your choice:\n")
        selected_option = self.options.get(choice)
        if selected_option:
            selected_option()
        else:
            print("Invalid choice. Please, enter a valid option.")


class Slot:
    def __init__(self, lines, acc):
        self.account = acc
        self.betting_amount = 0
        self.winnings = 0
        self.total_winnings = 0
        self.lines = lines
        self.slots = ['7', 'A', 'B', 'C', 'D']
        self.S1_1 = None
        self.S1_2 = None
        self.S1_3 = None
        self.S2_1 = None
        self.S2_2 = None
        self.S2_3 = None
        self.S3_1 = None
        self.S3_2 = None
        self.S3_3 = None

    def viable_bet(self, amount):
        if amount <= MAX_AMOUNT and amount >= MIN_AMOUNT:
            return
        else:
            raise InvalidAmountException(
                f"Can't bet ${amount}. Max bet amount is ${MAX_AMOUNT}. Min bet amount is ${MIN_AMOUNT}"
            )

    def bet(self):
        amount = int(input(f"Please, enter amount you want to bet:\n"))
        self.viable_bet(amount)
        self.account.viable_withdraw(amount)
        self.account.withdraw(amount)
        self.betting_amount = amount
        self.total_plays = 0
        print(f"You bet ${amount}.")
        self.roll()

    def check_slots(self):
        if self.lines == 1:
            # Middle lane
            if self.S2_1 == '7' and self.S2_2 == '7' and self.S2_3 == '7':
                won_amount = self.betting_amount * 10
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
            if self.S2_1 == 'A' and self.S2_2 == 'A' and self.S2_3 == 'A':
                won_amount = self.betting_amount * 5
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
            if self.S2_1 == 'B' and self.S2_2 == 'B' and self.S2_3 == 'B':
                won_amount = self.betting_amount * 2.5
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
            if self.S2_1 == 'C' and self.S2_2 == 'C' and self.S2_3 == 'C':
                won_amount = self.betting_amount * 1.75
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
            if self.S2_1 == 'D' and self.S2_2 == 'D' and self.S2_3 == 'D':
                won_amount = self.betting_amount * 1.5
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
        if self.lines == 2:
            # Top line
            if self.S1_1 == '7' and self.S1_2 == '7' and self.S1_3 == '7':
                won_amount = self.betting_amount * 10
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
            if self.S1_1 == 'A' and self.S1_2 == 'A' and self.S1_3 == 'A':
                won_amount = self.betting_amount * 5
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
            if self.S1_1 == 'B' and self.S1_2 == 'B' and self.S1_3 == 'B':
                won_amount = self.betting_amount * 2.5
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
            if self.S1_1 == 'C' and self.S1_2 == 'C' and self.S1_3 == 'C':
                won_amount = self.betting_amount * 1.75
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
            if self.S1_1 == 'D' and self.S1_2 == 'D' and self.S1_3 == 'D':
                won_amount = self.betting_amount * 1.5
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
            # Middle line
            if self.S2_1 == '7' and self.S2_2 == '7' and self.S2_3 == '7':
                won_amount = self.betting_amount * 10
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
            if self.S2_1 == 'A' and self.S2_2 == 'A' and self.S2_3 == 'A':
                won_amount = self.betting_amount * 5
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
            if self.S2_1 == 'B' and self.S2_2 == 'B' and self.S2_3 == 'B':
                won_amount = self.betting_amount * 2.5
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
            if self.S2_1 == 'C' and self.S2_2 == 'C' and self.S2_3 == 'C':
                won_amount = self.betting_amount * 1.75
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
            if self.S2_1 == 'D' and self.S2_2 == 'D' and self.S2_3 == 'D':
                won_amount = self.betting_amount * 1.5
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
            # Bottom line
            if self.S3_1 == '7' and self.S3_2 == '7' and self.S3_3 == '7':
                won_amount = self.betting_amount * 10
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
            if self.S3_1 == 'A' and self.S3_2 == 'A' and self.S3_3 == 'A':
                won_amount = self.betting_amount * 5
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
            if self.S3_1 == 'B' and self.S3_2 == 'B' and self.S3_3 == 'B':
                won_amount = self.betting_amount * 2.5
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
            if self.S3_1 == 'C' and self.S3_2 == 'C' and self.S3_3 == 'C':
                won_amount = self.betting_amount * 1.75
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
            if self.S3_1 == 'D' and self.S3_2 == 'D' and self.S3_3 == 'D':
                won_amount = self.betting_amount * 1.5
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
        self.total_winnings = self.total_winnings + self.winnings
        if self.winnings:
            self.account.deposit_winnings(self.winnings)
            print(f"Total winnings this session: ${self.total_winnings}")
            self.winnings = 0
        else:
            print("Sorry. Better luck next time!")

    def roll(self):

        self.S1_1 = random.choice(self.slots)
        self.S1_2 = random.choice(self.slots)
        self.S1_3 = random.choice(self.slots)
        self.S2_1 = random.choice(self.slots)
        self.S2_2 = random.choice(self.slots)
        self.S2_3 = random.choice(self.slots)
        self.S3_1 = random.choice(self.slots)
        self.S3_2 = random.choice(self.slots)
        self.S3_3 = random.choice(self.slots)
        print(f"\n( {self.S1_1} | {self.S1_2} | {self.S1_3} )\n( {self.S2_1} | {self.S2_2} | {self.S2_3} )\n( {self.S3_1} | {self.S3_2} | {self.S3_3} )\n")
        self.check_slots()
        self.total_plays = self.total_plays + 1
        print(f"Plays this session: {self.total_plays}")

from time import sleep
import random
from account_management import Account

MAX_AMOUNT = 100
MIN_AMOUNT = 1
MAX_LINES = 3
MIN_LINES = 1


class InvalidAmountException(Exception):
    pass


class Slot:
    def __init__(self, lines, acc):
        self.account = acc
        self.betting_amount = 0
        self.winnings = 0
        self.total_winnings = 0
        self.play_count = 0
        self.lines = lines
        self.slots = ['💫', '​🍉​', '🍋​', '🍒', '🍏']

    def viable_bet(self, amount):
        if amount <= MAX_AMOUNT and amount >= MIN_AMOUNT:
            return
        else:
            raise InvalidAmountException(
                f"C​an't bet ${amount}. Max bet amount is ${MAX_AMOUNT}. Min bet amount is ${MIN_AMOUNT}"
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
            if self.S2_1 == '💫​' and self.S2_2 == '💫​' and self.S2_3 == '💫​':
                won_amount = self.betting_amount * 10
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
            if self.S2_1 == '🍉' and self.S2_2 == '🍉' and self.S2_3 == '🍉':
                won_amount = self.betting_amount * 5
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
            if self.S2_1 == '🍋​' and self.S2_2 == '🍋​' and self.S2_3 == '🍋​':
                won_amount = self.betting_amount * 2.5
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
            if self.S2_1 == '🍒​' and self.S2_2 == '🍒​' and self.S2_3 == '🍒​':
                won_amount = self.betting_amount * 1.75
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
            if self.S2_1 == '🍏​' and self.S2_2 == '🍏​' and self.S2_3 == '🍏​':
                won_amount = self.betting_amount * 1.5
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
        if self.lines == 2:
            # Top line
            if self.S1_1 == '💫​' and self.S1_2 == '💫​' and self.S1_3 == '💫​':
                won_amount = self.betting_amount * 10
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
            if self.S1_1 == '🍉' and self.S1_2 == '🍉' and self.S1_3 == '🍉':
                won_amount = self.betting_amount * 5
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
            if self.S1_1 == '🍋​' and self.S1_2 == '🍋​' and self.S1_3 == '🍋​':
                won_amount = self.betting_amount * 2.5
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
            if self.S1_1 == '🍒​' and self.S1_2 == '🍒​' and self.S1_3 == '🍒​':
                won_amount = self.betting_amount * 1.75
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
            if self.S1_1 == '🍏​' and self.S1_2 == '🍏​' and self.S1_3 == '🍏​':
                won_amount = self.betting_amount * 1.5
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
            # Middle line
            if self.S2_1 == '💫​' and self.S2_2 == '💫​' and self.S2_3 == '💫​':
                won_amount = self.betting_amount * 10
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
            if self.S2_1 == '🍉' and self.S2_2 == '🍉' and self.S2_3 == '🍉':
                won_amount = self.betting_amount * 5
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
            if self.S2_1 == '🍋​' and self.S2_2 == '🍋​' and self.S2_3 == '🍋​':
                won_amount = self.betting_amount * 2.5
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
            if self.S2_1 == '🍒​' and self.S2_2 == '🍒​' and self.S2_3 == '🍒​':
                won_amount = self.betting_amount * 1.75
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
            if self.S2_1 == '🍏​' and self.S2_2 == '🍏​' and self.S2_3 == '🍏​':
                won_amount = self.betting_amount * 1.5
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
            # B​ottom line
            if self.S3_1 == '💫​' and self.S3_2 == '💫​' and self.S3_3 == '💫​':
                won_amount = self.betting_amount * 10
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
            if self.S3_1 == '🍉' and self.S3_2 == '🍉' and self.S3_3 == '🍉':
                won_amount = self.betting_amount * 5
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
            if self.S3_1 == '🍋​' and self.S3_2 == '🍋​' and self.S3_3 == '🍋​':
                won_amount = self.betting_amount * 2.5
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
            if self.S3_1 == '🍒​' and self.S3_2 == '🍒​' and self.S3_3 == '🍒​':
                won_amount = self.betting_amount * 1.75
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
            if self.S3_1 == '🍏​' and self.S3_2 == '🍏​' and self.S3_3 == '🍏​':
                won_amount = self.betting_amount * 1.5
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
        if self.lines == 3:
            # Top line
            if self.S1_1 == '💫​' and self.S1_2 == '💫​' and self.S1_3 == '💫​':
                won_amount = self.betting_amount * 10
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
            if self.S1_1 == '🍉' and self.S1_2 == '🍉' and self.S1_3 == '🍉':
                won_amount = self.betting_amount * 5
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
            if self.S1_1 == '🍋​' and self.S1_2 == '🍋​' and self.S1_3 == '🍋​':
                won_amount = self.betting_amount * 2.5
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
            if self.S1_1 == '🍒​' and self.S1_2 == '🍒​' and self.S1_3 == '🍒​':
                won_amount = self.betting_amount * 1.75
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
            if self.S1_1 == '🍏​' and self.S1_2 == '🍏​' and self.S1_3 == '🍏​':
                won_amount = self.betting_amount * 1.5
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
            # Middle line
            if self.S2_1 == '💫​' and self.S2_2 == '💫​' and self.S2_3 == '💫​':
                won_amount = self.betting_amount * 10
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
            if self.S2_1 == '🍉' and self.S2_2 == '🍉' and self.S2_3 == '🍉':
                won_amount = self.betting_amount * 5
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
            if self.S2_1 == '🍋​' and self.S2_2 == '🍋​' and self.S2_3 == '🍋​':
                won_amount = self.betting_amount * 2.5
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
            if self.S2_1 == '🍒​' and self.S2_2 == '🍒​' and self.S2_3 == '🍒​':
                won_amount = self.betting_amount * 1.75
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
            if self.S2_1 == '🍏​' and self.S2_2 == '🍏​' and self.S2_3 == '🍏​':
                won_amount = self.betting_amount * 1.5
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
            # B​ottom line
            if self.S3_1 == '💫​' and self.S3_2 == '💫​' and self.S3_3 == '💫​':
                won_amount = self.betting_amount * 10
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
            if self.S3_1 == '🍉' and self.S3_2 == '🍉' and self.S3_3 == '🍉':
                won_amount = self.betting_amount * 5
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
            if self.S3_1 == '🍋​' and self.S3_2 == '🍋​' and self.S3_3 == '🍋​':
                won_amount = self.betting_amount * 2.5
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
            if self.S3_1 == '🍒​' and self.S3_2 == '🍒​' and self.S3_3 == '🍒​':
                won_amount = self.betting_amount * 1.75
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
            if self.S3_1 == '🍏​' and self.S3_2 == '🍏​' and self.S3_3 == '🍏​':
                won_amount = self.betting_amount * 1.5
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
            # D​iagonal line 1
            if self.S1_1 == '💫​' and self.S2_2 == '💫​' and self.S3_3 == '💫​':
                won_amount = self.betting_amount * 10
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
            if self.S1_1 == '🍉' and self.S2_2 == '🍉' and self.S3_3 == '🍉':
                won_amount = self.betting_amount * 5
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
            if self.S1_1 == '🍋​' and self.S2_2 == '🍋​' and self.S3_3 == '🍋​':
                won_amount = self.betting_amount * 2.5
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
            if self.S1_1 == '🍒​' and self.S2_2 == '🍒​' and self.S3_3 == '🍒​':
                won_amount = self.betting_amount * 1.75
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
            if self.S1_1 == '🍏​' and self.S2_2 == '🍏​' and self.S3_3 == '🍏​':
                won_amount = self.betting_amount * 1.5
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
            # D​iagonal line 2
            if self.S3_1 == '💫​' and self.S2_2 == '💫​' and self.S1_3 == '💫​':
                won_amount = self.betting_amount * 10
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
            if self.S3_1 == '🍉' and self.S2_2 == '🍉' and self.S1_3 == '🍉':
                won_amount = self.betting_amount * 5
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
            if self.S3_1 == '🍋​' and self.S2_2 == '🍋​' and self.S1_3 == '🍋​':
                won_amount = self.betting_amount * 2.5
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
            if self.S3_1 == '🍒​' and self.S2_2 == '🍒​' and self.S1_3 == '🍒​':
                won_amount = self.betting_amount * 1.75
                self.winnings = self.winnings + won_amount
                print(f"You won ${won_amount}!")
            if self.S3_1 == '🍏​' and self.S2_2 == '🍏​' and self.S1_3 == '🍏​':
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

        for i in range(1, random.randint(30, 75)):
            self.S1_1 = random.choice(self.slots)
            self.S1_2 = random.choice(self.slots)
            self.S1_3 = random.choice(self.slots)
            self.S2_1 = random.choice(self.slots)
            self.S2_2 = random.choice(self.slots)
            self.S2_3 = random.choice(self.slots)
            self.S3_1 = random.choice(self.slots)
            self.S3_2 = random.choice(self.slots)
            self.S3_3 = random.choice(self.slots)

            line_1 = f"\n( {self.S1_1} | {self.S1_2} | {self.S1_3} )"
            line_2 = f"\n( {self.S2_1} | {self.S2_2} | {self.S2_3} )"
            line_3 = f"\n( {self.S3_1} | {self.S3_2} | {self.S3_3} )\n"

            print(line_1, line_2, line_3, end='\r')

            sleep(i / 100)

        self.check_slots()
        self.play_count = self.play_count + 1

        print(f"Plays this session: {self.play_count}")

        self.account.save_data(self.account)

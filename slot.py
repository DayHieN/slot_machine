from time import sleep
import random
from account_management import Account
import os
from notification_sounds import Notifications

MAX_AMOUNT = 100
MIN_AMOUNT = 1
MAX_LINES = 3
MIN_LINES = 1


class InvalidAmountException(Exception):
    pass


class Slot:
    def __init__(self, acc):
        self.account = acc
        self.betting_amount = 0
        self.winnings = 0
        self.total_winnings = 0
        self.play_count = 0

        self.slots = ['💫', '​🍉​', '🍋', '🍒', '🍏']
        self.fruit_values = ['💫💫💫 *10','🍉🍉🍉 *5', '🍋🍋🍋 *2.5', '🍒🍒🍒 *1.75','🍏🍏🍏 *1.5']

    def viable_bet(self, amount):
        if amount <= MAX_AMOUNT and amount >= MIN_AMOUNT:
            return
        else:
            raise InvalidAmountException(
                f"C​an't bet ${amount}. Max bet amount is ${MAX_AMOUNT}. Min bet amount is ${MIN_AMOUNT}"
            )

    def print_fruit_value(self):
        print('\n')
        for fruit in self.fruit_values:
            print(fruit)

    def bet(self):
        self.print_fruit_value()
        amount = int(input(f"Please, enter amount you want to bet:\n"))
        self.viable_bet(amount)
        self.account.viable_withdraw(amount)
        self.account.withdraw(amount)
        self.betting_amount = amount
        self.total_plays = 0
        print(f"You bet ${amount}.")
        self.roll()

    def check_slots(self):

        # Top line
        if self.S1_1 == self.slots[0] and self.S1_2 == self.slots[0] and self.S1_3 == self.slots[0]:
            won_amount = self.betting_amount * 10
            self.winnings = self.winnings + won_amount
            print(f"You won ${won_amount} 💫!")
        if self.S1_1 == self.slots[1] and self.S1_2 == self.slots[1] and self.S1_3 == self.slots[1]:
            won_amount = self.betting_amount * 5
            self.winnings = self.winnings + won_amount
            print(f"You won ${won_amount} 🍉!")
        if self.S1_1 == self.slots[2] and self.S1_2 == self.slots[2] and self.S1_3 == self.slots[2]:
            won_amount = self.betting_amount * 2.5
            self.winnings = self.winnings + won_amount
            print(f"You won ${won_amount} 🍋!")
        if self.S1_1 == self.slots[3] and self.S1_2 == self.slots[3] and self.S1_3 == self.slots[3]:
            won_amount = self.betting_amount * 1.75
            self.winnings = self.winnings + won_amount
            print(f"You won ${won_amount} 🍒!")
        if self.S1_1 == self.slots[4] and self.S1_2 == self.slots[4] and self.S1_3 == self.slots[4]:
            won_amount = self.betting_amount * 1.5
            self.winnings = self.winnings + won_amount
            print(f"You won ${won_amount} 🍏!")
        # Middle line
        if self.S2_1 == self.slots[0] and self.S2_2 == self.slots[0] and self.S2_3 == self.slots[0]:
            won_amount = self.betting_amount * 10
            self.winnings = self.winnings + won_amount
            print(f"You won ${won_amount} 💫!")
        if self.S2_1 == self.slots[1] and self.S2_2 == self.slots[1] and self.S2_3 == self.slots[1]:
            won_amount = self.betting_amount * 5
            self.winnings = self.winnings + won_amount
            print(f"You won ${won_amount} 🍉!")
        if self.S2_1 == self.slots[2] and self.S2_2 == self.slots[2] and self.S2_3 == self.slots[2]:
            won_amount = self.betting_amount * 2.5
            self.winnings = self.winnings + won_amount
            print(f"You won ${won_amount} 🍋!")
        if self.S2_1 == self.slots[3] and self.S2_2 == self.slots[3] and self.S2_3 == self.slots[3]:
            won_amount = self.betting_amount * 1.75
            self.winnings = self.winnings + won_amount
            print(f"You won ${won_amount} 🍒!")
        if self.S2_1 == self.slots[4] and self.S2_2 == self.slots[4] and self.S2_3 == self.slots[4]:
            won_amount = self.betting_amount * 1.5
            self.winnings = self.winnings + won_amount
            print(f"You won ${won_amount} 🍏!")
        # B​ottom line
        if self.S3_1 == self.slots[0] and self.S3_2 == self.slots[0] and self.S3_3 == self.slots[0]:
            won_amount = self.betting_amount * 10
            self.winnings = self.winnings + won_amount
            print(f"You won ${won_amount} 💫!")
        if self.S3_1 == self.slots[1] and self.S3_2 == self.slots[1] and self.S3_3 == self.slots[1]:
            won_amount = self.betting_amount * 5
            self.winnings = self.winnings + won_amount
            print(f"You won ${won_amount} 🍉!")
        if self.S3_1 == self.slots[2] and self.S3_2 == self.slots[2] and self.S3_3 == self.slots[2]:
            won_amount = self.betting_amount * 2.5
            self.winnings = self.winnings + won_amount
            print(f"You won ${won_amount} 🍋!")
        if self.S3_1 == self.slots[3] and self.S3_2 == self.slots[3] and self.S3_3 == self.slots[3]:
            won_amount = self.betting_amount * 1.75
            self.winnings = self.winnings + won_amount
            print(f"You won ${won_amount} 🍒!")
        if self.S3_1 == self.slots[4] and self.S3_2 == self.slots[4] and self.S3_3 == self.slots[4]:
            won_amount = self.betting_amount * 1.5
            self.winnings = self.winnings + won_amount
            print(f"You won ${won_amount} 🍏!")
        # D​iagonal line 1
        if self.S1_1 == self.slots[0] and self.S2_2 == self.slots[0] and self.S3_3 == self.slots[0]:
            won_amount = self.betting_amount * 10
            self.winnings = self.winnings + won_amount
            print(f"You won ${won_amount} 💫!")
        if self.S1_1 == self.slots[1] and self.S2_2 == self.slots[1] and self.S3_3 == self.slots[1]:
            won_amount = self.betting_amount * 5
            self.winnings = self.winnings + won_amount
            print(f"You won ${won_amount} 🍉!")
        if self.S1_1 == self.slots[2] and self.S2_2 == self.slots[2] and self.S3_3 == self.slots[2]:
            won_amount = self.betting_amount * 2.5
            self.winnings = self.winnings + won_amount
            print(f"You won ${won_amount} 🍋!")
        if self.S1_1 == self.slots[3] and self.S2_2 == self.slots[3] and self.S3_3 == self.slots[3]:
            won_amount = self.betting_amount * 1.75
            self.winnings = self.winnings + won_amount
            print(f"You won ${won_amount} 🍒!")
        if self.S1_1 == self.slots[4] and self.S2_2 == self.slots[4] and self.S3_3 == self.slots[4]:
            won_amount = self.betting_amount * 1.5
            self.winnings = self.winnings + won_amount
            print(f"You won ${won_amount} 🍏!")
        # D​iagonal line 2
        if self.S3_1 == self.slots[0] and self.S2_2 == self.slots[0] and self.S1_3 == self.slots[0]:
            won_amount = self.betting_amount * 10
            self.winnings = self.winnings + won_amount
            print(f"You won ${won_amount} 💫!")
        if self.S3_1 == self.slots[1] and self.S2_2 == self.slots[1] and self.S1_3 == self.slots[1]:
            won_amount = self.betting_amount * 5
            self.winnings = self.winnings + won_amount
            print(f"You won ${won_amount} 🍉!")
        if self.S3_1 == self.slots[2] and self.S2_2 == self.slots[2] and self.S1_3 == self.slots[2]:
            won_amount = self.betting_amount * 2.5
            self.winnings = self.winnings + won_amount
            print(f"You won ${won_amount} 🍋!")
        if self.S3_1 == self.slots[3] and self.S2_2 == self.slots[3] and self.S1_3 == self.slots[3]:
            won_amount = self.betting_amount * 1.75
            self.winnings = self.winnings + won_amount
            print(f"You won ${won_amount} 🍒!")
        if self.S3_1 == self.slots[4] and self.S2_2 == self.slots[4] and self.S1_3 == self.slots[4]:
            won_amount = self.betting_amount * 1.5
            self.winnings = self.winnings + won_amount
            print(f"You won ${won_amount} 🍏!")

        self.total_winnings = self.total_winnings + self.winnings
        if self.winnings:
            Notifications.success_notification2()
            self.account.deposit_winnings(self.winnings)
            print(f"Total winnings this session: ${self.total_winnings}")
            self.winnings = 0
        else:
            Notifications.something_went_wrong()
            print("Sorry. Better luck next time!")

    def roll(self):
        random_number = random.randint(30, 50)
        for i in range(1, random_number):
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

            sleep(i / 300)
            if i < random_number - 1:
                os.system('cls||clear')

        self.play_count = self.play_count + 1
        self.check_slots()

        print(f"Plays this session: {self.play_count}")

        self.account.save_data(self.account)

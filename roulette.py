from time import sleep
import random
from account_management import Account


MIN_AMOUNT = 1


class InvalidAmountException(Exception):
    pass


class Roulette:
    def __init__(self, acc):
        self.account = acc
        self.betting_amount = 0
        self.winnings = 0
        self.total_winnings = 0
        self.play_count = 0
        self.numbers = {num: 'green' if num == 0 else 'red' if num %
                        2 != 0 else 'black' for num in range(37)}

    def viable_bet(self, amount):
        if amount >= MIN_AMOUNT:
            return
        else:
            raise InvalidAmountException(
                f"Can't bet ${amount}. Min bet amount is ${MIN_AMOUNT}"
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

    def check(self, choosen_number, number):
        if choosen_number == number:
            self.winnings = self.betting_amount * 35
            print(f"You won ${self.winnings}!")
        
        if self.winnings:
            self.total_winnings = self.total_winnings + self.winnings
            self.account.deposit_winnings(self.winnings)
            print(f"Total winnings this session: ${self.total_winnings}")
            self.winnings = 0
        else:
            print("Sorry. Better luck next time!")


    def roll(self):
        choosen_number = input("Please, choose your number:\n")
        random_number = random.randint(50, 75)
        for i in range(1, random_number):
            number = random.randint(0, 36)
            if i == random_number:
                print(f"    {number} {self.numbers.get(number)}\n")
            else:
                print(f"\r    {number} {self.numbers.get(number)}", end='')
            sleep(i / 150)
            
        self.check(choosen_number, number)





class InvalidAmountException(Exception):
    pass


class Account:
    def __init__(self, name):
        self.name = name
        self.total = 1000
        self.total_winnings = 0
        self.total_loses = 0
        self.profit = self.total_winnings - self.total_loses

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

    def deposit_winnings(self, winnings):
        self.total = self.total + winnings
        self.total_winnings = self.total_winnings + winnings
        print(f" ${winnings} added to your account.")

    def withdraw(self, amount):
        try:
            self.viable_withdraw(amount)
            self.total = self.total - amount
            self.total_loses = self.total_loses + amount
            print(f"Withdraw of ${amount}. Total balance: ${self.total}")
        except InvalidAmountException as err:
            print(f"Error: {err}")

    def show_account_info(self):
        print(f"{self.name} account.\n Balance: ${self.total}\n Total winnings: ${self.total_winnings}\n Total loses: ${self.total_loses}\n Profit: ${self.profit}")

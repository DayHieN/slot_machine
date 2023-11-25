import json


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

    

    def to_dict(self):
        return {'name': self.name,
                'total': self.total,
                'total_winnings': self.total_winnings,
                'total_loses': self.total_loses,
                'profit': self.profit
                }

    def save_data(self, acc):
        account = acc.to_dict()
        with open(f'save_data_{self.name}.json', 'w') as file:
            json.dump(account, file)

    @classmethod
    def from_dict(cls, data):
        return cls(data['name'], data['total'], data['total_winnings'], data['total_loses'], data['profit'])

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

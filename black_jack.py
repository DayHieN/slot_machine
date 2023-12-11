from time import sleep
import random
from account_management import Account
import os
import textwrap
from notification_sounds import Notifications


MAX_AMOUNT = 100
MIN_AMOUNT = 1
MAX_POINTS = 21


class InvalidAmountException(Exception):
    pass


class Black_jack:
    def __init__(self, acc):
        self.account = acc
        self.deck = [

            {
                'number': 'A',
                'suit': '♠️',
                'value': (1, 11)
            },
            {
                'number': '2',
                'suit': '♠️',
                'value': 2
            },
            {
                'number': '3',
                'suit': '♠️',
                'value': 3
            },
            {
                'number': '4',
                'suit': '♠️',
                'value': 4
            },
            {
                'number': '5',
                'suit': '♠️',
                'value': 5
            },
            {
                'number': '6',
                'suit': '♠️',
                'value': 6
            },
            {
                'number': '7',
                'suit': '♠️',
                'value': 7
            },
            {
                'number': '8',
                'suit': '♠️',
                'value': 8
            },
            {
                'number': '9',
                'suit': '♠️',
                'value': 9
            },
            {
                'number': '10',
                'suit': '♠️',
                'value': 10
            },
            {
                'number': 'J',
                'suit': '♠️',
                'value': 10
            },
            {
                'number': 'Q',
                'suit': '♠️',
                'value': 10
            },
            {
                'number': 'K',
                'suit': '♠️',
                'value': 10
            },

            {
                'number': 'A',
                'suit': '♥️',
                'value': (1, 11)
            },
            {
                'number': '2',
                'suit': '♥️',
                'value': 2
            },
            {
                'number': '3',
                'suit': '♥️',
                'value': 3
            },
            {
                'number': '4',
                'suit': '♥️',
                'value': 4
            },
            {
                'number': '5',
                'suit': '♥️',
                'value': 5
            },
            {
                'number': '6',
                'suit': '♥️',
                'value': 6
            },
            {
                'number': '7',
                'suit': '♥️',
                'value': 7
            },
            {
                'number': '8',
                'suit': '♥️',
                'value': 8
            },
            {
                'number': '9',
                'suit': '♥️',
                'value': 9
            },
            {
                'number': '10',
                'suit': '♥️',
                'value': 10
            },
            {
                'number': 'J',
                'suit': '♥️',
                'value': 10
            },
            {
                'number': 'Q',
                'suit': '♥️',
                'value': 10
            },
            {
                'number': 'K',
                'suit': '♥️',
                'value': 10
            },

            {
                'number': 'A',
                'suit': '♣️',
                'value': (1, 11)
            },
            {
                'number': '2',
                'suit': '♣️',
                'value': 2
            },
            {
                'number': '3',
                'suit': '♣️',
                'value': 3
            },
            {
                'number': '4',
                'suit': '♣️',
                'value': 4
            },
            {
                'number': '5',
                'suit': '♣️',
                'value': 5
            },
            {
                'number': '6',
                'suit': '♣️',
                'value': 6
            },
            {
                'number': '7',
                'suit': '♣️',
                'value': 7
            },
            {
                'number': '8',
                'suit': '♣️',
                'value': 8
            },
            {
                'number': '9',
                'suit': '♣️',
                'value': 9
            },
            {
                'number': '10',
                'suit': '♣️',
                'value': 10
            },
            {
                'number': 'J',
                'suit': '♣️',
                'value': 10
            },
            {
                'number': 'Q',
                'suit': '♣️',
                'value': 10
            },
            {
                'number': 'K',
                'suit': '♣️',
                'value': 10
            },

            {
                'number': 'A',
                'suit': '♦️',
                'value': (1, 11)
            },
            {
                'number': '2',
                'suit': '♦️',
                'value': 2
            },
            {
                'number': '3',
                'suit': '♦️',
                'value': 3
            },
            {
                'number': '4',
                'suit': '♦️',
                'value': 4
            },
            {
                'number': '5',
                'suit': '♦️',
                'value': 5
            },
            {
                'number': '6',
                'suit': '♦️',
                'value': 6
            },
            {
                'number': '7',
                'suit': '♦️',
                'value': 7
            },
            {
                'number': '8',
                'suit': '♦️',
                'value': 8
            },
            {
                'number': '9',
                'suit': '♦️',
                'value': 9
            },
            {
                'number': '10',
                'suit': '♦️',
                'value': 10
            },
            {
                'number': 'J',
                'suit': '♦️',
                'value': 10
            },
            {
                'number': 'Q',
                'suit': '♦️',
                'value': 10
            },
            {
                'number': 'K',
                'suit': '♦️',
                'value': 10
            },
        ]
        self.betting_amount = 0
        self.winnings = 0
        self.total_winnings = 0
        self.play_count = 0
        self.dealer_cards = []
        self.player_cards = []
        self.dealer_score = 0
        self.player_score = 0

    def shuffle_deck(self):
        return random.shuffle(self.deck)

    def display_cards(self, deck):

        for card in deck:

            card_img = f"""
            +-----+
            |{card['number']:<2}   |
            |  {card['suit']}  |
            |   {card['number']:>2}|
            +-----+
            """

            print(card_img, end='')

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

    def draw(self, number_of_cards, players):
        # both players
        if players == 1:
            for _ in range(1, number_of_cards + 1):
                self.dealer_cards.append(self.deck.pop(
                    random.randint(0, len(self.deck))))
            for _ in range(1, number_of_cards + 1):
                self.player_cards.append(self.deck.pop(
                    random.randint(0, len(self.deck))))
        # just dealer
        if players == 2:
            for _ in range(1, number_of_cards + 1):
                self.dealer_cards.append(self.deck.pop(
                    random.randint(0, len(self.deck))))
        # just player
        if players == 3:
            for _ in range(1, number_of_cards + 1):
                self.player_cards.append(self.deck.pop(
                    random.randint(0, len(self.deck))))

    def play(self):
        self.bet()
        self.draw(2, 1)

        self.dealer_score = sum(item['value'] for item in self.dealer_cards)
        self.player_score = sum(item['value'] for item in self.player_cards)

        print('Dealer draws!')
        self.display_cards(self.dealer_cards)
        print('Player draws!')
        self.display_cards(self.player_cards)

        print(f"Dealer's cards - {self.dealer_score} points.")
        print(f"Player's cards - {self.player_score} points.")

        if self.dealer_score >= 16:
            print("Dealer stays!")
        while self.player_score < 21 or self.dealer_score < 21:
            choice = input('Select: 1) Push 2) Stay\n')
            while choice != '1' and choice != '2':
                print("Select a valid option")
                choice = input('Select: 1) Push 2) Stay\n')
            if choice == '1':
                print("Player push!")
                print('Player draws!')
                self.draw(1, 3)
                self.player_score = sum(item['value']
                                        for item in self.player_cards)
                self.display_cards(self.player_cards)
            if choice == '2':
                print('Player stays!')

            if self.dealer_score <= 16:
                print('Dealer push!')
                print('Dealer draws!')
                self.draw(1, 2)
                self.dealer_score = sum(item['value']
                                        for item in self.dealer_cards)
                self.display_cards(self.dealer_cards)
            else:
                print('Dealer stays!\n')
            print(f"Dealer's cards - {self.dealer_score} points.")
            print(f"Player's cards - {self.player_score} points.")

        if self.dealer_score > 21 or self.player_score > 21:
            print(
                f"{'Dealer' if self.dealer_score > self.player_score else 'Player'} busted!")
        if self.dealer_score == 21:
            print("Dealer wins!")
        if self.player_score == 21:
            print("Dealer wins!")
            won_amount = self.betting_amount * 2
            self.winnings = self.winnings + won_amount
            print(f"You won ${won_amount}!")
            if self.winnings:
                Notifications.success_notification2()
                self.account.deposit_winnings(self.winnings)
                print(f"Total winnings this session: ${self.total_winnings}")
                self.winnings = 0


acc = Account('Baby')
bj = Black_jack(acc)
bj.play()

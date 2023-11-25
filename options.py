from slot import Slot
from roulette import Roulette


class Options:

    def __init__(self, acc, slot, roulette):
        self.options = {

            '1': slot.bet,
            '2': roulette.bet,
            '3': acc.show_account_info,
            '4': exit

        }

    def console_options(self):
        print(
            "Options:\n 1. Play slots\n 2. Play roulette\n 3. Show account info\n 4. Exit")
        choice = input("Enter your choice:\n")
        selected_option = self.options.get(choice)
        if selected_option:
            selected_option()
        else:
            print("Invalid choice. Please, enter a valid option.")

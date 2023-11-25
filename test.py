import curses
import time
import random

def draw_slot_machine(stdscr, slots):
    height, width = stdscr.getmaxyx()

    # Clear the screen
    stdscr.clear()

    # Draw the slot machine border
    stdscr.addch(0, 0, curses.ACS_ULCORNER)
    stdscr.addch(0, width - 1, curses.ACS_URCORNER)
    stdscr.addch(height - 1, 0, curses.ACS_LLCORNER)

    # Draw the bottom border without the lower-right corner
    for i in range(1, width - 1):
        stdscr.addch(0, i, curses.ACS_HLINE)
        stdscr.addch(height - 1, i, curses.ACS_HLINE)

    # Draw the side borders without the lower-right corner
    for i in range(1, height - 1):
        stdscr.addch(i, 0, curses.ACS_VLINE)

    # Draw the rolling slots
    for i, slot in enumerate(slots):
        for j, symbol in enumerate(slot):
            # Ensure that the drawing position is within the window boundaries
            if 1 <= j + 2 < height - 1 and 1 <= i * 10 + 2 < width - 1:
                stdscr.addch(j + 2, i * 10 + 2, symbol)

    # Draw the lower-right corner as a space using addstr
    # Draw the lower-right corner as a space
    stdscr.addch(height - 1, width - 1, ' ')
def roll_slot(slots, column):
    # Simulate rolling by shifting symbols in a slot column
    slots[column] = [chr(random.randint(33, 126)) for _ in range(3)]

def main(stdscr):
    curses.curs_set(0)  # Hide the cursor
    stdscr.clear()

    # Initialize the slot machine with random symbols
    slots = [
        [chr(random.randint(33, 126)) for _ in range(3)] for _ in range(3)
    ]

    # Animation loop
    while True:
        # Clear the screen
        stdscr.clear()

        # Roll each slot
        for i in range(3):
            roll_slot(slots, i)

        # Draw the slot machine with the updated slots
        draw_slot_machine(stdscr, slots)

        # Refresh the screen to show the changes
        stdscr.refresh()

        # Wait for a short duration (simulating rolling speed)
        time.sleep(0.1)

if __name__ == "__main__":
    curses.wrapper(main)
"""
Quick Pick Lottery Ticket Generator Program
"""
import random

NUMBER_OF_RANDOM_NUMBERS = 6
LOWEST_NUMBER = 1
HIGHEST_NUMBER = 45


def main():
    """Generate quick pick lottery ticket"""
    number_of_quick_picks = int(input("How many quick picks? "))
    quick_pick_lines = []
    draw_quick_pick_numbers(number_of_quick_picks, quick_pick_lines)
    print_quick_pick(quick_pick_lines)


def draw_quick_pick_numbers(number_of_quick_picks, quick_pick_lines):
    """Draw quick pick numbers"""
    for i in range(number_of_quick_picks):   # creating a list of lists of 6 numbers
        quick_pick_numbers = []
        for j in range(NUMBER_OF_RANDOM_NUMBERS):
            quick_pick_number = random.randint(LOWEST_NUMBER, HIGHEST_NUMBER)
            while quick_pick_number in quick_pick_numbers:   # no duplicate numbers in a single line
                quick_pick_number = random.randint(LOWEST_NUMBER, HIGHEST_NUMBER)
            quick_pick_numbers.append(quick_pick_number)
        quick_pick_lines.append(quick_pick_numbers)


def print_quick_pick(lines):
    """Print the quick pick ticket"""
    for line in lines:
        line.sort()
        for i in range(len(line)):  # removes [] from output
            print(line[i], end=" ")
        print()


main()

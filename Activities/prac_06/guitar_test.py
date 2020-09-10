"""
Guitar Test program
Student name: Julie-Anne Roder
"""

from Activities.prac_06.guitar_class import Guitar


def main():
    my_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    other_guitar = Guitar("Another Guitar", 2013, 845.29)

    print("Gibson L-5 CES get_age() - expected 98. got {}".format(my_guitar.get_age()))
    print("Another Guitar get_age() - expected 7. got {}".format(other_guitar.get_age()))

    print("Gibson L-5 CES is_vintage() - expected True. got {}".format(my_guitar.is_vintage()))
    print("Another Guitar is_vintage() - expected False. got {}".format(other_guitar.is_vintage()))


main()

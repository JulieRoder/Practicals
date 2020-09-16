"""
Guitars Program file
Student name: Julie-Anne Roder
"""

from Activities.prac_06.guitar_class import Guitar
STARTING_VALUE = 0
COUNT_START = 1
COST_VALUE_LENGTH = 10


def main():
    """Guitar Collection Program."""
    print("My guitars!")
    my_guitars = []
    guitar_name = input("Name: ")
    while guitar_name != "":
        guitar = get_guitar_details(guitar_name)
        my_guitars.append(guitar)
        print("{} ({}) : ${:,.2f} added".format(guitar.name, guitar.year, guitar.cost))
        guitar_name = input("Name: ")
    longest_guitar_name = get_longest_name(my_guitars)  # for formatting in following print statement
    print_guitar_details(my_guitars, longest_guitar_name, COST_VALUE_LENGTH)


def get_guitar_details(name):
    """Get guitar details."""
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitar = Guitar(name, year, cost)
    return guitar


def get_longest_name(guitars):
    """Get length of longest guitar name."""
    longest_name = STARTING_VALUE
    for guitar in guitars:
        if len(guitar.name) > longest_name:
            longest_name = len(guitar.name)
    return longest_name


def get_vintage_status(guitars):
    """Assign vintage status of guitar."""
    for guitar in guitars:
        if guitar.is_vintage():
            return " (vintage)"
        else:
            return ""


def print_guitar_details(guitars, longest_name, cost_length):
    """Print the details of guitars in collection."""
    for i, guitar in enumerate(guitars, COUNT_START):
        vintage_string = get_vintage_status(guitars)
        print("Guitar {}: {:<{}} ({}), worth ${:{},.2f}{}".format(i, guitar.name, longest_name, guitar.year,
                                                                  guitar.cost, cost_length, vintage_string))


main()

"""
CP1404 Practicals
Taxi Simulator program
Student name: Julie-Anne Roder
"""

from Activities.prac_08.taxi import Taxi
from Activities.prac_08.silver_service_taxi import SilverServiceTaxi
MENU = "q)uit, c)hoose taxi, d)rive"
MENU_OPTIONS = ["q", "c", "d"]


def main():
    """Taxi Simulator"""
    current_taxi = None
    taxi_bill = 0
    taxis = [Taxi("Prius", 100), Taxi("Jazz", 60), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's Drive!")
    menu_choice = get_valid_choice(MENU, ">>>", MENU_OPTIONS)
    while menu_choice != "q":
        if menu_choice == "c":
            display_taxi_list(taxis)
            taxi_choice = get_valid_number("Choose taxi:", range(len(taxis)))
            current_taxi = taxis[taxi_choice]
            display_bill(taxi_bill)
        else:
            if current_taxi is None:
                print("You have not yet selected a taxi. :(")
            else:
                drive_distance(current_taxi)
                current_fare = calculate_fare(current_taxi)
                print("Your {} trip cost you ${:.2f}".format(current_taxi.name, current_fare))
                taxi_bill += current_fare
                display_bill(taxi_bill)
        menu_choice = get_valid_choice(MENU, ">>>", MENU_OPTIONS)
    print("Total trip cost: ${:.2f}".format(taxi_bill))
    print("Taxis are now:")
    display_taxi_list(taxis)


def get_valid_choice(menu, prompt, options):
    """Get valid string from menu and options provided."""
    choice = input("{}\n{} ".format(menu, prompt)).lower()
    while choice not in options:
        print("Invalid selection")
        choice = input("{}\n{} ".format(menu, prompt)).lower()
    return choice


def get_valid_number(prompt, options):
    """Get valid number from menu and options provided."""
    number = int(input(prompt))
    while number not in options:
        print("Invalid selection")
        number = int(input(prompt))
    return number


def display_taxi_list(taxis):
    """Display the list of taxis provided."""
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


def display_bill(bill):
    """Display the bill to date."""
    print("Bill to date: ${:.2f}".format(bill))


def drive_distance(taxi):
    """Drive the taxi a distance."""
    distance = float(input("Drive how far? "))
    taxi.drive(distance)


def calculate_fare(taxi):
    """Calculate the taxi fare."""
    return taxi.get_fare()


main()

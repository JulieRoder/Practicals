"""
Program for converting temperatures to Celsius or Fahrenheit
Now using functions!! :P
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    """Convert between temperature units"""
    print(MENU)
    choice = get_valid_choice(MENU)
    while choice != "Q":
        if choice == "C":
            unit = "F"
            celsius = get_temperature("Celsius: ")
            fahrenheit = convert_celsius_to_fahrenheit(celsius)
            print_result(fahrenheit, unit)
        else:
            unit = "C"
            fahrenheit = get_temperature("Fahrenheit: ")
            celsius = convert_fahrenheit_to_celsius(fahrenheit)
            print_result(celsius, unit)
        print(MENU)
        choice = get_valid_choice(MENU)
    print("Thank you.")


def get_valid_choice(menu):
    """Get a valid menu choice"""
    choice = input(">>> ").upper()
    while choice not in menu:
        print("Invalid option")
        choice = input(">>> ").upper()
    return choice


def get_temperature(prompt):
    """Get a temperature float value"""
    return float(input(prompt))


def convert_celsius_to_fahrenheit(celsius):
    """Convert celsius temperatures to fahrenheit units"""
    return celsius * 9.0 / 5 + 32


def convert_fahrenheit_to_celsius(fahrenheit):
    """Convert fahrenheit temperatures to celsius units"""
    return 5 / 9 * (fahrenheit - 32)


def print_result(temperature, unit):
    """Prints resulting converted temperature"""
    print("Result: {:.2f} {}".format(temperature, unit))


main()

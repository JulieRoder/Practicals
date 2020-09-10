"""
CP1404 Practical 5
Student name: Julie-Anne Roder
State names in a dictionary
"""
LENGTH_OF_SHORT_STATE = 3
NAMES_OF_STATES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                   "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(NAMES_OF_STATES)


def main():
    """Accessing the Names of States dictionary."""
    state_code = input("Enter short state: ").upper()
    while state_code != "":
        if state_code in NAMES_OF_STATES:
            print("{:<{}} is {:<}".format(state_code, LENGTH_OF_SHORT_STATE, NAMES_OF_STATES[state_code]))
        else:
            print("Invalid short state")
        state_code = input("Enter short state: ").upper()

    for state in NAMES_OF_STATES:
        print("{:<{}} is {:<}".format(state, LENGTH_OF_SHORT_STATE, NAMES_OF_STATES[state]))


main()

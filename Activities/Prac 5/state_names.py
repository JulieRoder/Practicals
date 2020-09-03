"""
CP1404 Practical 5
State names in a dictionary
"""
LENGTH_OF_SHORT_STATE = 3
NAMES_OF_STATES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                   "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(NAMES_OF_STATES)

state_code = input("Enter short state: ").upper()
while state_code != "":
    if state_code in NAMES_OF_STATES:
        print(state_code, "is", NAMES_OF_STATES[state_code])
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()

for state in NAMES_OF_STATES:
    print("{:<{}} is {:<}".format(state, LENGTH_OF_SHORT_STATE, NAMES_OF_STATES[state]))

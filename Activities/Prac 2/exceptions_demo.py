"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
if user enters a non-number character
2. When will a ZeroDivisionError occur?
when user enters 0 as the denominator
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
put in a while loop that checks for 0 denominator, gives invalid message and asks for new denominator
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("invalid denominator")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
print("Finished.")

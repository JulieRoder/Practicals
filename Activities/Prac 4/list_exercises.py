"""
List Exercises program

1. Basic list operations
Pseudocode
numbers = empty list
get 5 numbers from user
display first number
display last number
display smallest number
display largest number
display average of numbers

2. Woefully inadequate security checker
Pseudocode
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
get username from user
if username in usernames list
    display Access granted
else
    display Access denied
"""
NUMBER_OF_NUMBERS = 5


def main():
    basic_list_operations()
    inadequate_security_checker()


def basic_list_operations():
    numbers = []
    for i in range(NUMBER_OF_NUMBERS):
        number = int(input("Number {}: ".format(i + 1)))
        numbers.append(number)
    print("The first number is {}".format(numbers[0]))
    print("The last number is {}".format(numbers[-1]))
    print("The smallest number is {}".format(min(numbers)))
    print("the largest number is {}".format(max(numbers)))
    print("The average of the numbers is {}".format(sum(numbers) / NUMBER_OF_NUMBERS))


def inadequate_security_checker():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    username = input("Username: ")
    if username in usernames:
        print("Access Granted")
    else:
        print("Access Denied")


main()

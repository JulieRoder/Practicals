"""
Password checker for the length of a password

Pseudocode
LENGTH = 6
get password
while password length is < LENGTH
    display password is not long enough. Try again!
    get password
display password as *
"""

LENGTH = 6
password = input("Password (>6 letters): ")
while len(password) < LENGTH:
    print("Password is not long enough. Try again!")
    password = input("Password (>6 letters): ")
print(len(password) * "*")

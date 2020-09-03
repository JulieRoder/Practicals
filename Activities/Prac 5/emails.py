"""
CP1404 Practical 5
Email list
"""

emails_and_names = {}
user_email = input("Email: ").lower()
while user_email != "":
    if user_email not in emails_and_names:
        user_name = input("Name: ").title()
        emails_and_names = {user_email: user_name}
    else:
        print("Email already entered. Please enter a new email.")
    user_email = input("Email: ").lower()
print(emails_and_names)

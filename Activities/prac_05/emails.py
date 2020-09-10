"""
CP1404 Practical 5
Student name: Julie-Anne Roder
Email list
"""


def main():
    """Create a dictionary of emails and names."""
    emails_and_names = {}
    user_email = input("Email: ").lower()
    while user_email != "":
        if user_email not in emails_and_names:
            user_name = get_name(user_email)
            emails_and_names[user_email] = user_name
        else:
            print("Email already entered. Please enter a new email.")
        user_email = input("Email: ").lower()
    for key in emails_and_names:
        print("{} ({})".format(emails_and_names[key], key))


def get_name(email):
    """Get name from email."""
    index = email.find("@")
    user_name = email[:index]
    name_pieces = user_name.split(".")
    full_name = " ".join(name_pieces).title()
    confirmation = input("Is your name {}? (Y/n) ".format(full_name)).lower()
    if confirmation == "n" or confirmation == "no":
        full_name = input("Name: ").title()
    return full_name


main()

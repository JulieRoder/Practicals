"""
CP1404 Practical
Wikipedia search & summary
Student name: Julie-Anne Roder
"""

import wikipedia


def main():
    """
    Give a summary of a wikipedia page selected by user.
    """
    search_string = input("Search wikipedia for: ")
    while search_string != "":
        get_page(search_string)
        get_summary(search_string)
        search_string = input("Search wikipedia for: ")


def get_page(string):
    try:
        search_page = wikipedia.page(string)
        print(search_page.title, search_page.url)
    except wikipedia.exceptions.PageError:
        print("'{}' does not match any pages. Try another query!".format(string))


def get_summary(string):
    try:
        search_summary = wikipedia.summary(string)
        print(search_summary)
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)


def run_tests():
    search_string = 'Barack'
    get_page(search_string)
    get_summary(search_string)
    search_string = 'Monty'  # changes to monkey, not sure why?
    get_page(search_string)
    get_summary(search_string)


# main()
run_tests()

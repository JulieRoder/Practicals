"""
Languages program
Student name: Julie-Anne Roder
"""

from Activities.prac_06.programming_language import ProgrammingLanguage


def main():
    """Programming Language comparisons?."""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)
    programming_languages = [ruby, python, visual_basic]
    print_dynamic_languages(programming_languages)


def print_dynamic_languages(programming_languages):
    """Prints the dynamically typed languages."""
    print("The dynamically typed languages are:")
    for language in programming_languages:
        if language.is_dynamic():
            print(language.name)


main()

"""
Programming Language Class Exercise
Student name: Julie-Anne Roder
"""


class ProgrammingLanguage:
    """Represents a Programming Language object."""

    def __init__(self, typing, reflection, year):
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.typing == "dynamic":
            return True
        else:
            return False

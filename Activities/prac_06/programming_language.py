"""
Programming Language Class Exercise
Student name: Julie-Anne Roder
"""


class ProgrammingLanguage:
    """Represents a Programming Language object."""

    def __init__(self, name, typing, reflection, year):
        """Initialise a ProgrammingLanguage instance.

               name: program language name
               typing: static/dynamic
               reflection: True/False
               year: year language initially created.
               """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Default print statement."""
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing, self.reflection,
                                                                           self.year)

    def is_dynamic(self):
        """Determine if language is dynamic."""
        return self.typing.lower() == "dynamic"

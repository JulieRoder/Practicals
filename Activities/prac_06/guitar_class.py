"""
Guitar Class
Student name: Julie-Anne Roder
"""
CURRENT_YEAR = 2020
VINTAGE_THRESHOLD = 50


class Guitar:
    """Represents a Guitar Object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialises a guitar instance
            name: make & model
            year: year guitar was made
            cost: guitar purchase price."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Default print statement - Name (Year) : Cost."""
        return "{} ({}) : ${:.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Get age of guitar."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if guitar is vintage."""
        return self.get_age() >= VINTAGE_THRESHOLD

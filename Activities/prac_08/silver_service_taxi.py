"""
CP1404 Practicals
Silver Service Taxi class
Student name: Julie-Anne Roder
"""

from Activities.prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that modifies fare costs based on fanciness."""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance, based on parent class."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = self.fanciness * Taxi.price_per_km
        self.current_fare_distance = 0

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return "{}, {}km on current fare, ${:.2f}/km plus flagfall of ${:.2f}".format(super().__str__(),
                                                                                      self.current_fare_distance,
                                                                                      self.price_per_km, self.flagfall)

    def get_fare(self):
        """Return the price for the taxi trip."""
        return self.price_per_km * self.current_fare_distance + self.flagfall

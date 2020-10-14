"""
CP1404 Practicals
Unreliable Car Class
Student name: Julie-Anne Roder
"""

from Activities.prac_08.car import Car
import random


class UnreliableCar(Car):
    """Specialised car class with added reliability variable."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        """Return a string like a Car with reliability added."""
        return "{}, reliability={}".format(super().__str__(), self.reliability)

    def drive(self, distance):
        """Drive like the parent Car but only if distance is less than reliability."""
        distance = random.randint(0, 100)
        if distance < self.reliability:
            super().drive(distance)
        else:
            distance = 0
        return distance

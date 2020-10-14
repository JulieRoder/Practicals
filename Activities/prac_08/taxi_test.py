"""
CP1404 Practicals
Taxi Test program
Student name: Julie-Anne Roder
"""

from Activities.prac_08.taxi import Taxi

prius_1 = Taxi("Prius 1", 100)
prius_1.drive(40)
print(prius_1)
print("Total fare is ${:.2f}".format(prius_1.get_fare()))
prius_1.start_fare()
prius_1.drive(100)
print(prius_1)
print("Total fare is ${:.2f}".format(prius_1.get_fare()))

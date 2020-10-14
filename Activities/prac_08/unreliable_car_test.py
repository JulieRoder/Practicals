"""
CP1404 Practicals
Unreliable Car test program
Student name: Julie-Anne Roder
"""

from Activities.prac_08.unreliable_car import UnreliableCar

ford_1 = UnreliableCar("Ford 1", 50, 40)
holden_1 = UnreliableCar("Holden 1", 50, 60)
hyundai_1 = UnreliableCar("Hyundai 1", 50, 10)
ford_1.drive(100)
holden_1.drive(100)
hyundai_1.drive(100)
print(ford_1)
print(holden_1)
print(hyundai_1)

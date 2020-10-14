"""
CP1404 Practicals
Silver Service Taxi test program
Student name: Julie-Anne Roder
"""

from Activities.prac_08.silver_service_taxi import SilverServiceTaxi


hummer = SilverServiceTaxi("Hummer", 200, 4)
print(hummer)
honda = SilverServiceTaxi("Honda", 50, 2)
honda.drive(18)
print(honda)
print("Total fare is ${:.2f}".format(honda.get_fare()))

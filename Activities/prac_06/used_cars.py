"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from Activities.prac_06.car import Car  # file location: Practicals/Activities/prac_06/car.py


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180)
    my_car.drive(30)
    my_car.name = "My Car"
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)  # prints class default print statement

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))

    limo = Car(100)
    limo.name = "Limo"
    limo.add_fuel(20)
    print("Limo fuel =", limo.fuel)
    limo.drive(115)
    print("Limo odo =", limo.odometer)
    print(limo)  # prints class default print statement


main()

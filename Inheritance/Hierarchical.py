class Vehicle:

    def start(self):
        print("Vehicle starting.")


class Car(Vehicle):

    pass


class Bike(Vehicle):

    pass


c = Car()
c.start()

b = Bike()
b.start()
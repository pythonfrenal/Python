
from abc import ABC, abstractmethod

# Abstract parent class
class Vehicle(ABC):

    @abstractmethod
    def calculate_rent(self, days):
        pass


# Car child class
class Car(Vehicle):
    def __init__(self):
        self.car_features = {"AC", "GPS", "Airbags"}

    def calculate_rent(self, days):
        return 2000 * days


# Bike child class
class Bike(Vehicle):
    def __init__(self):
        self.bike_features = {"Helmet", "ABS"}

    def calculate_rent(self, days):
        return 500 * days


# Main program
try:
    days = int(input("Enter rental days: "))

    if days <= 0:
        raise ValueError("Rental days must be greater than zero!")

    car = Car()
    bike = Bike()

    # Display car features
    print("\nCar Features:")
    for feature in car.car_features:
        print(feature)

    # Calculate car rent
    car_rent = car.calculate_rent(days)
    print("Car Rental Amount:", car_rent)

    if car_rent > 5000:
        car_rent = car_rent * 0.90
        print("10% discount applied to car!")
    print("Final Car Rent:", car_rent)

    # Display bike features
    print("\nBike Features:")
    for feature in bike.bike_features:
        print(feature)

    # Calculate bike rent
    bike_rent = bike.calculate_rent(days)
    print("Bike Rental Amount:", bike_rent)

    if bike_rent > 5000:
        bike_rent = bike_rent * 0.90
        print("10% discount applied to bike!")
    print("Final Bike Rent:", bike_rent)

except ValueError as e:
    print("Invalid input:", e)

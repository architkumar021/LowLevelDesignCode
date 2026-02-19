from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Starting the car")


class Bike(Vehicle):
    def start(self):
        print("Starting the bike")


class Truck(Vehicle):
    def start(self):
        print("Starting the truck")


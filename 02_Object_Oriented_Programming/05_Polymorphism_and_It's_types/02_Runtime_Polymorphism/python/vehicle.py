class Vehicle:
    def start(self):
        pass  # Base implementation (empty)


class Car(Vehicle):
    def start(self):
        print("Starting a car")


class Bike(Vehicle):
    def start(self):
        print("Starting a bike")


class Truck(Vehicle):
    def start(self):
        print("Starting a truck")


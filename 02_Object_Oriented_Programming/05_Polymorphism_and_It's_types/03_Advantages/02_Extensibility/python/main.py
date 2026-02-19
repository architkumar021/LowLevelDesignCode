import sys
sys.path.append('..')
from vehicle import Vehicle, Car, Bike, Truck


# Extensible: Add new vehicle types without changing existing code
class Bus(Vehicle):
    def start(self):
        print("Starting the bus")


vehicles = [Car(), Bike(), Truck(), Bus()]
for vehicle in vehicles:
    vehicle.start()  # Polymorphic behavior handles the new type seamlessly

"""
Output:
Starting the car
Starting the bike
Starting the truck
Starting the bus
"""


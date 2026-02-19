import sys
sys.path.append('..')
from vehicle import Car, Bike, Truck

vehicles = [Car(), Bike(), Truck()]
for vehicle in vehicles:
    vehicle.start()  # Polymorphic behavior

"""
Output:
Starting the car
Starting the bike
Starting the truck
"""


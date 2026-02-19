import sys
sys.path.append('..')
from vehicle import Car, Bike, Truck

# Flexible: Dynamically assign different types of vehicles
vehicle = Car()
vehicle.start()  # Output: Starting the car

vehicle = Bike()
vehicle.start()  # Output: Starting the bike

vehicle = Truck()
vehicle.start()  # Output: Starting the truck

"""
Output:
Starting the car
Starting the bike
Starting the truck
"""


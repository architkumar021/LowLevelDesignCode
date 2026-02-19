import sys
sys.path.append('..')
from vehicle import Vehicle, Car, Bike, Truck

# List containing various types of vehicles
vehicle_list = [Car(), Bike(), Truck(), Vehicle()]

# Debugging challenge: What type of vehicle is being started?
for vehicle in vehicle_list:
    vehicle.start()  # Runtime determines which start() method is called

"""
Output:
Starting a car
Starting a bike
Starting a truck
Starting a generic vehicle
"""


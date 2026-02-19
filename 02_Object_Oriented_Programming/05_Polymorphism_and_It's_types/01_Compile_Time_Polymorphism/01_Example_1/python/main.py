from vehicle import Vehicle

vehicle = Vehicle()

# Calls method with one argument
vehicle.start("Car")

# Calls method with two arguments (simulated overloading)
vehicle.start("Bike", 60)

"""
Output:
Starting a Car
Starting a Bike with speed: 60 km/h
"""


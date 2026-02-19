from vehicle import Vehicle

vehicle = Vehicle()

# Calls method with a string argument
vehicle.start("Truck")

# Calls method with an integer argument (simulated overloading)
vehicle.start(101)

"""
Output:
Starting a Truck
Starting a vehicle with ID: 101
"""


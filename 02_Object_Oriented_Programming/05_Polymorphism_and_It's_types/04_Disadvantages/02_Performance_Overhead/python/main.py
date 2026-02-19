import sys
import time
sys.path.append('..')
from vehicle import Car

start_time = time.time_ns()

# Dynamic method dispatch
my_vehicle = Car()
my_vehicle.start()  # Runtime resolves method implementation dynamically

end_time = time.time_ns()
print(f"Time taken for method dispatch: {end_time - start_time} nanoseconds")

"""
Output:
Starting a car
Time taken for method dispatch: XXXXX nanoseconds
"""


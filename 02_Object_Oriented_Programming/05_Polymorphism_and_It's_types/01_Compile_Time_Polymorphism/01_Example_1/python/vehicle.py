class Vehicle:
    # Python simulates method overloading using default parameters
    def start(self, vehicle_type, speed=None):
        if speed is not None:
            print(f"Starting a {vehicle_type} with speed: {speed} km/h")
        else:
            print(f"Starting a {vehicle_type}")


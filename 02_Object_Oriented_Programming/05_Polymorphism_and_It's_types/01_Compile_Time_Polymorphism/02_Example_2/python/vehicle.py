class Vehicle:
    # Python simulates method overloading by checking argument types
    def start(self, vehicle_type_or_id):
        if isinstance(vehicle_type_or_id, str):
            print(f"Starting a {vehicle_type_or_id}")
        elif isinstance(vehicle_type_or_id, int):
            print(f"Starting a vehicle with ID: {vehicle_type_or_id}")


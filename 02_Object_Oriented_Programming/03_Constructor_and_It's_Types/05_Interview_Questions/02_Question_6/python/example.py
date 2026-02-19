class Example:
    def __init__(self, value):
        self.value = 0  # Default value (equivalent to Java's int default)
        if value < 0:
            print("Invalid value! Constructor exiting early.")
            return  # Exits the constructor early
        self.value = value  # Initializes the value if valid

    def display(self):
        print(f"Value: {self.value}")


class Example:
    def __init__(self):
        self.message = "Hello, World!"

    # Static method
    @staticmethod
    def display_message():
        # In Python, 'self' is not available in static methods.
        # Attempting to access instance attributes will cause a NameError.
        # print(self.message)  # ERROR: NameError: name 'self' is not defined
        print("Cannot access instance attributes in a static method")

    def display_instance_message(self):
        print(self.message)  # Valid: 'self' refers to the current instance


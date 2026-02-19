class Person:
    def __init__(self):
        self.name = None

    def set_name(self, name):
        self.name = name
        return self  # Enables method chaining

    def display(self):
        print("Name: " + self.name)


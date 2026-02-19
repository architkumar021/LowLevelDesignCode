class Person:
    # Constructor
    def __init__(self, name):
        self.name = name  # 'self' resolves conflict between instance variable and parameter

    def display(self):
        print("Name: " + self.name)


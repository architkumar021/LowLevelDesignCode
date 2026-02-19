class Person:
    # Python doesn't support multiple constructors directly,
    # so we simulate constructor chaining with default parameters
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")


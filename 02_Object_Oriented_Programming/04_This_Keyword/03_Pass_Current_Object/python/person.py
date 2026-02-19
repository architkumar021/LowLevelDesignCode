class Person:
    def greet(self, person):
        print("Hello, " + str(person))

    def introduce(self):
        self.greet(self)  # Passes the current object

    def __str__(self):
        return "I am a Person instance."


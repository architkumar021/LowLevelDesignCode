class Movie:
    # Parameterized constructor
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def display_details(self):
        print(f"Title: {self.title}, Duration: {self.duration} mins")


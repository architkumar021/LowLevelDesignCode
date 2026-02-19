class Movie:
    # Custom default constructor
    def __init__(self):
        self.title = "Untitled"  # Default: "Untitled"
        self.duration = 90       # Default: 90

    def display_details(self):
        print(f"Title: {self.title}, Duration: {self.duration} mins")


import copy


class Movie:
    # Parameterized constructor
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    # Copy constructor equivalent using class method
    @classmethod
    def from_movie(cls, other):
        return cls(other.title, other.duration)

    # Python also supports copy via __copy__
    def __copy__(self):
        return Movie(self.title, self.duration)

    def display_details(self):
        print(f"Title: {self.title}, Duration: {self.duration} mins")


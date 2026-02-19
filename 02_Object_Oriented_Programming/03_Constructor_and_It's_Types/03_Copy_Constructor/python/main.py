import copy
from movie import Movie

original = Movie("Inception", 148)

# Copy constructor using class method
copy_movie = Movie.from_movie(original)
copy_movie.display_details()

# Copy constructor using copy module
copy_movie2 = copy.copy(original)
copy_movie2.display_details()

"""
Output:
Title: Inception, Duration: 148 mins
Title: Inception, Duration: 148 mins
"""




# 15 GGA v1
# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor
# YOUR CODE HERE
class Latlon:
    # constructor method (function)
    def __init__(self, lat, lon):
        # note: no super here, only later
        # establish base attributes to be inherited later
        self.lat = lat
        self.lon = lon

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.
# using super method for inheritance
# YOUR CODE HERE
# make a new class, a child class of latlong
class Waypoint(Latlon):
    # give it an additional name attribute
    def __init__(self, name, lat, lon):
        # note: only self. what is not inherited
        # manage inheritance with super()
        # inherited attributes
        super().__init__(lat, lon)
        # new attribute
        self.name = name
    # this allows for clean printing
    def __str__(self):
        # using fstring to manage the format of priting
        return f"Name:{self.name}, Latitude:{self.lat}, Longitude:{self.lon}"
    # read about this but did not impliment
    #def __repr__()


# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?
# YOUR CODE HERE
class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        # inherited attributes
        super().__init__(name, lat, lon)
        # new attributes
        self.difficulty = difficulty
        self.size = size
    # this allows for clean printing        
    def __str__(self):
        # using fstring to manage the format of priting
        return f"Name:{self.name}, Difficulty:{self.difficulty}, Size:{self.size}, Latitude:{self.lat}, Longitude:{self.lon}"

    #def __repr__(self)


# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521
# YOUR CODE HERE
waypoint = Waypoint("Catacombs", 41.70505, -121.51521)


# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)


# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556
# YOUR CODE HERE
geocache = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)


# Print it--also make this print more nicely
print(geocache)

import itertools

all_destinations = []
locations = {}
paths = []


class TravelPaths:
    def __init__(self):
        self._distance = 0
        self._cities = []

    def add_distance(self, distance):
        self._distance += distance

    def add_destination(self, name):
        self._cities.insert(self._cities.__len__(), name)

    def get_destinations(self):
        return self._cities

    def set_destinations(self, cities):
        self._cities = cities

    def get_destinations_string(self):
        path = ""

        for city in self._cities:
            path += city + " -> "

        return path.rstrip(" -> ")

    def get_distance(self):
        return self._distance


def handle_instruction(_instruction):
    _instruction = _instruction.split(" ")

    _city1 = _instruction[0]
    _city2 = _instruction[2]
    _distance = int(_instruction[4])

    if not _city1 in locations:
        locations[_city1] = {}

    if not _city2 in locations:
        locations[_city2] = {}

    if not _city2 in locations[_city1]:
        locations[_city1][_city2] = _distance

    if not _city1 in locations[_city2]:
        locations[_city2][_city1] = _distance


f = open('./input/day9.txt', 'r')
for line in f:
    handle_instruction(line)
f.close()

# Create unique list of cities
for city in locations:
    all_destinations.insert(0, city)

# Use permutations to get all possible routes
all_routes = list(itertools.permutations(all_destinations))

# Loop through all routes
for route in all_routes:
    travel = TravelPaths()

    for _i in xrange(0,  route.__len__() - 1):
        _source = route[_i]
        _target = route[_i + 1]

        # Add the original source, if at starting point.
        if _i == 0:
            travel.add_destination(_source)

        # Check if their is a flight from source location to destination
        if _target in locations[_source]:

            # Add the target
            travel.add_destination(_target)
            travel.add_distance(locations[_source][_target])

    paths.insert(0, travel) # Add the class to the paths variable

all_paths = {}

for travel in paths:
    all_paths[travel.get_destinations_string()] = travel.get_distance()

sorted_paths = sorted(all_paths, key=all_paths.__getitem__)
print "Shorted trip: " + sorted_paths[0] + " with a distance of " + str(all_paths[sorted_paths[0]])
print "Longest trip: " + sorted_paths[sorted_paths.__len__() - 1] + " with a distance of " + str(all_paths[sorted_paths[sorted_paths.__len__() - 1]])
print "Total amount of routes: " + str(sorted_paths.__len__())

class LocationPresents:
    def __init__(self, location, present = 0):
        self._location = location
        self._presents = present

    def add_present(self):
        self._presents += 1

    def get_presents(self):
        return self._presents

    def get_location(self):
        return self._location


f = open('day3.txt', 'r')
for line in f:
    location = [0, 0]
    locations = {}

    # Starting location gets a present.
    locations.setdefault("00", LocationPresents("00", 1))

    # Loop through all characters.
    for char in line:
        if char == '^':
            # Going North
            location[1] += 1
        elif char == '>':
            # Going East
            location[0] += 1
        elif char == 'v':
            # Going South
            location[1] -= 1
        elif char == '<':
            # Going West
            location[0] -= 1

        # Check if this location was already visited and get a reference to the object
        santaLocation = str(location[0]) + str(location[1])
        currentLocation = locations.get(santaLocation, LocationPresents(santaLocation))

        # Add present
        currentLocation.add_present()

        # Add Location to dictionary
        locations.setdefault(santaLocation, currentLocation)

    # for key in locations.keys():
    #    house = locations.get(key)
    #    print "" + getattr(house, "_location") + " has " + str(getattr(house, "_presents")) + " presents!"

    print line
    print "Amount of houses with presents " + str(locations.items().__len__()) + "\n"
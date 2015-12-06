class LocationPresents:
    def __init__(self, location, present=0):
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
    charNumber = 0          # Current character that we're processing
    santaLocation = [0, 0]  # Location of Santa (x, y)
    robotLocation = [0, 0]  # Location of Robot (x, y)
    locations = {}          # All Locations
    hasRobot = True         # Part 2 of the puzzle

    # Starting location gets a present.
    locations.setdefault("00", LocationPresents("00", 2 if hasRobot else 1)) # Assign default value for starting point.

    # Loop through all characters.
    for char in line:
        charNumber += 1     # increase the character counter
        characterLocation = robotLocation if hasRobot else santaLocation

        if charNumber % 2 is not 0 and hasRobot:
            characterLocation = santaLocation

        if char == '^':
            # Going North
            characterLocation[1] += 1
        elif char == '>':
            # Going East
            characterLocation[0] += 1
        elif char == 'v':
            # Going South
            characterLocation[1] -= 1
        elif char == '<':
            # Going West
            characterLocation[0] -= 1
        else:
            continue

        # Check if this location was already visited and get a reference to the object
        location = str(characterLocation[0]) + str(characterLocation[1])
        currentLocation = locations.get(location, LocationPresents(location))

        # Add present
        currentLocation.add_present()

        # Add Location to dictionary
        locations.setdefault(location, currentLocation)

        if charNumber % 2 is not 0 and hasRobot:
            print "Delivered by Santa at location: " + location
        elif hasRobot:
            print "Delivered by Robot Santa: " + location
        else:
            print "Delivered by Santa: " + location


    for key in locations.keys():
        house = locations.get(key)
        print "" + getattr(house, "_location") + " has " + str(getattr(house, "_presents")) + " presents!"

    print line
    print "Amount of houses with presents: " + str(locations.items().__len__())
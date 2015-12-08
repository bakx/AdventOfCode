from day3_classes import *

f = open('day3.txt', 'r')
for line in f:
    charNumber = 0              # Current character that we're processing
    santaLocation = Character(0, 0, "Santa")         # Location of Santa (x, y)
    robotLocation = Character(0, 0, "Robo Santa")   # Location of Robot (x, y)
    locations = {}              # All Locations
    hasRobot = True             # Part 2 of the puzzle

    # Starting location gets a present.
    locations[santaLocation.get_location()] = HousePresents(santaLocation.get_location(), 1)    # Add initial present

    # If the Santa Robot is active, add an additional present to the starting location
    if hasRobot:
        locations[santaLocation.get_location()].add_present();

    # Loop through all characters.
    for char in line:
        charNumber += 1     # increase the character counter
        characterLocation = robotLocation if hasRobot else santaLocation

        if charNumber % 2 is not 0 and hasRobot:
            characterLocation = santaLocation

        if char == '^':
            # Going North
            characterLocation.move_character(0, 1)
        elif char == '>':
            # Going East
            characterLocation.move_character(1, 0)
        elif char == 'v':
            # Going South
            characterLocation.move_character(0, -1)
        elif char == '<':
            # Going West
            characterLocation.move_character(-1, 0)
        else:
            continue

        # Check if this location was already visited and get a reference to the object
        location = characterLocation.get_location()
        currentLocation = locations.get(location, HousePresents(location))

        # Add present
        currentLocation.add_present()

        # Add Location to dictionary
        locations[location] = currentLocation

        print "Present delivered by " + characterLocation.get_name() + " at : " + characterLocation.get_location()

    print line
    print "Amount of houses with presents: " + str(locations.items().__len__())

f.close()

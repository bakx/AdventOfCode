f = open('day1.txt', 'r')
for line in f:
    charNumber = 0
    currentLevel = 0
    enteredBasement = ""

    # Loop through all characters.
    for char in line:
        charNumber += 1

        if char == '(':
            # Going up
            currentLevel += 1
        elif char == ')':
            # Going down
            currentLevel -= 1

        if currentLevel is -1 and enteredBasement is "":
            enteredBasement = str(charNumber)

    print line
    print "Entered basement first on character: " + enteredBasement
    print "Ended on floor: " + str(currentLevel)

f.close()

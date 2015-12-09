grid = {}
gridSize = 1000

for i in xrange(0, gridSize):
    for n in xrange(0, gridSize):
        grid[i, n] = 0


def handle_instruction(instruction):

    _range_x = [0,0]
    _range_y = [0,0]

    _ranges = instruction\
        .replace("turn off ", "") \
        .replace("turn on ", "") \
        .replace("toggle ", "") \
        .replace("through ", "") \
        .split(" ")

    _range_x[0] = int(_ranges[0].split(',')[0])
    _range_x[1] = int(_ranges[1].split(',')[0])
    _range_y[0] = int(_ranges[0].split(',')[1])
    _range_y[1] = int(_ranges[1].split(',')[1])

    # At this point, we know the ranges.
    for x in xrange(_range_x[0], _range_x[1] + 1):
        for y in xrange(_range_y[0], _range_y[1] + 1):

            if instruction.startswith("turn off"):
                grid[x, y] = 0
                continue

            elif instruction.startswith("turn on"):
                grid[x, y] = 1
                continue

            else:
                # Toggle light
                grid[x, y] = 1 if grid[x, y] == 0 else 1
                continue


f = open('day6.txt', 'r')
for line in f:

    # Trim input
    line = line.strip()

    # Handle the instruction set
    handle_instruction(line)

lightsOn = 0

for key in grid:
    if grid[key] == 1:
        #print str(key) + " is on"
        lightsOn += 1

print str(lightsOn) + " lights turned on"
f.close()

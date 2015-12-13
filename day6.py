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
    for _x in xrange(_range_x[0], _range_x[1] + 1):
        for _y in xrange(_range_y[0], _range_y[1] + 1):

            if instruction.startswith("turn off"):
                grid[_x, _y] = 0
            elif instruction.startswith("turn on"):
                grid[_x, _y] = 1
            else:
                # Toggle light
                if grid[_x, _y] == 1:
                    grid[_x, _y] = 0
                else:
                    grid[_x, _y] = 1


f = open('./input/day6.txt', 'r')
for line in f:

    # Trim input
    line = line.strip()

    # Handle the instruction set
    handle_instruction(line)

lightsOn = 0

for key in grid:
    if grid[key] == 1:
        lightsOn += 1

print str(lightsOn) + " lights turned on"
f.close()

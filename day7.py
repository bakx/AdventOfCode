instructions = []
values = {}


def handle_instruction(instruction):

    _instructions = instruction.split(" ")

    # a -> b
    if _instructions.__len__() == 3:

        # Line already has a signal
        if values.has_key(_instructions[2]):
            print _instructions[2] + " already has a signal"
            return True

        # Transferring a digit to a wire?
        if _instructions[0].isdigit():
            values[_instructions[2]] = int(_instructions[0])
            return True
        # Transfer the signal of a wire to another wire
        elif values.has_key(_instructions[0]):
            values[_instructions[2]] = values[_instructions[0]]
            return True
        else:
            return False
    # NOT a -> b
    elif _instructions.__len__() == 4:
        if values.has_key(_instructions[1]):
            values[_instructions[3]] = ~ values[_instructions[1]] & 0xffff
            return True
        else:
            return False
    # AND, OR, LSHIFT, RSHIFT e.g., hz RSHIFT 1 -> is , 1 AND cx -> cy
    elif _instructions.__len__() == 5:

        if (not _instructions[0].isdigit() and not values.has_key(_instructions[0])) or (not _instructions[2].isdigit() and not values.has_key(_instructions[2])):
            return False

        # Line already has a signal
        if values.has_key(_instructions[4]):
            print _instructions[4] + " already has a signal"
            return True

        if _instructions[1] == "AND":
            value1 = _instructions[0] if _instructions[0].isdigit() else values.get(_instructions[0])
            value2 = _instructions[2] if _instructions[2].isdigit() else values.get(_instructions[2])
            values[_instructions[4]] = int(value1) & int(value2)
            return True

        elif _instructions[1] == "OR":
            value1 = _instructions[0] if _instructions[0].isdigit() else values.get(_instructions[0])
            value2 = _instructions[2] if _instructions[2].isdigit() else values.get(_instructions[2])
            values[_instructions[4]] = int(value1) | int(value2)
            return True

        elif _instructions[1] == "LSHIFT":
            value1 = _instructions[0] if _instructions[0].isdigit() else values.get(_instructions[0])
            value2 = _instructions[2] if _instructions[2].isdigit() else values.get(_instructions[2])
            values[_instructions[4]] = value1 << int(value2)
            return True

        elif _instructions[1] == "RSHIFT":
            value1 = _instructions[0] if _instructions[0].isdigit() else values.get(_instructions[0])
            value2 = _instructions[2] if _instructions[2].isdigit() else values.get(_instructions[2])
            values[_instructions[4]] = value1 >> int(value2)
            return True

        else:
            print "Unknown command " + line

    return False


def reset_wires():

    f = open('./input/day7.txt', 'r')
    for line in f:
        instructions.insert(instructions.__len__(), line.strip())
    f.close()


# Init
reset_wires()

i = 0
reset_count = 0
part2 = True

while instructions.__len__() > 0:

    line = str(instructions[i])

    if handle_instruction(line):
        instructions.pop(i)
    else:
        i += 1

    if i >= instructions.__len__():
        i = 0

    if reset_count == 0 and values.has_key("a") and part2:

        # Reset the instructions
        instructions = []
        reset_wires()

        # Get the value from wire a
        wire_a = values.get("a")

        # Reset all values
        values.clear()

        # Add the value for wire b
        values["b"] = wire_a

        # Increase reset count to prevent endless loops
        reset_count += 1


for key in sorted(values):
    print str(key) + " has the following value: " + str(values[key])

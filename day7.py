instructions = []
values = {}
part2 = True


def handle_instruction(instruction):

    _instructions = instruction.split(" ")

    # a -> b
    if _instructions.__len__() == 3:

        # Line already has a signal
        if _instructions[2] in values:
            print _instructions[2] + " already has a signal"
            return True

        # Transferring a digit to a wire?
        if _instructions[0].isdigit():
            values[_instructions[2]] = int(_instructions[0])
            return True
        # Transfer the signal of a wire to another wire
        elif _instructions[0] in values:
            values[_instructions[2]] = values[_instructions[0]]
            return True
        else:
            return False
    # NOT a -> b
    elif _instructions.__len__() == 4:
        if _instructions[1] in values:
            values[_instructions[3]] = ~ values[_instructions[1]] & 0xffff
            return True
        else:
            return False
    # AND, OR, LSHIFT, RSHIFT e.g., hz RSHIFT 1 -> is , 1 AND cx -> cy
    elif _instructions.__len__() == 5:

        if (not _instructions[0].isdigit() and not _instructions[0] in values) or (not _instructions[2].isdigit() and not _instructions[2] in values):
            return False

        value1 = _instructions[0] if _instructions[0].isdigit() else values.get(_instructions[0])
        value2 = _instructions[2] if _instructions[2].isdigit() else values.get(_instructions[2])

        if _instructions[1] == "AND":
            values[_instructions[4]] = int(value1) & int(value2)
            return True

        elif _instructions[1] == "OR":
            values[_instructions[4]] = int(value1) | int(value2)
            return True

        elif _instructions[1] == "LSHIFT":
            values[_instructions[4]] = value1 << int(value2)
            return True

        elif _instructions[1] == "RSHIFT":
            values[_instructions[4]] = value1 >> int(value2)
            return True

        else:
            print "Unknown command " + line

    return False


def reset_wires():

    f = open('./input/day7.txt', 'r')
    for l in f:
        instructions.insert(instructions.__len__(), l.strip())
    f.close()


# Init
reset_wires()

i = 0
reset_count = 0


while instructions.__len__() > 0:

    line = str(instructions[i])

    if handle_instruction(line):
        instructions.pop(i)
    else:
        i += 1

    if i >= instructions.__len__():
        i = 0

    if reset_count == 0 and "a" in values and part2:

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

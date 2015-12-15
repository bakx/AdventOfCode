values = {}


def binary_and(value1, value2):
    return value1 & value2


def binary_or(value1, value2):
    return value1 | value2


def binary_not(decimal_value):
    return ~decimal_value & 0xffff


def binary_shift_left(decimal_value, n):
    return decimal_value << n


def binary_shift_right(decimal_value, n):
    return decimal_value >> n


def make_keys(instruction):

    _instructions = instruction\
        .replace("NOT ", "")\
        .replace("AND ", "")\
        .replace("OR ", "")\
        .replace("LSHIFT ", "")\
        .replace("RSHIFT ", "")\
        .replace("-> ", "")\
        .split(" ")

    for _key in _instructions:
        _key = _key.strip()
        if not _key.isdigit() and _key.islower() and not values.has_key(_key):
            values[_key.strip()] = 0


def handle_instruction(instruction):

    _instructions = instruction\
        .split("->")

    # Transferring a value?
    _instructions[0] = str(_instructions[0]).strip()
    _instructions[1] = str(_instructions[1]).strip()

    if values[_instructions[1]] > 0:
        print _instructions[1] + " already has a signal"
        return

    if _instructions[0].isdigit():
        _currentValue = int(_instructions[0])
        values[_instructions[1]] = _currentValue
    elif _instructions[0].startswith("NOT"):
        _variables = _instructions[0].replace("NOT ", "").strip()
        values[_instructions[1]] = binary_not(values.get(_variables))
    elif _instructions[0].__len__() < 3:
        values[_instructions[1]] = values.get(_instructions[0])
    else:
        # Determine the split mode
        _splitWord = _instructions[0].split(" ")[1]

        _variables = _instructions[0].split(_splitWord)
        _variables[0] = str(_variables[0]).strip()
        _variables[1] = str(_variables[1]).strip()

        if _splitWord == "AND":
            if _variables[0].isdigit():
                values[_instructions[1]] = binary_and(int(_variables[0]), values.get(_variables[1]))
            else:
                values[_instructions[1]] = binary_and(values.get(_variables[0]), values.get(_variables[1]))

        elif _splitWord == "OR":
            if _variables[0].isdigit():
                values[_instructions[1]] = binary_or(int(_variables[0]), values.get(_variables[1]))
            else:
                values[_instructions[1]] = binary_or(values.get(_variables[0]), values.get(_variables[1]))

        elif _splitWord == "LSHIFT":
            values[_instructions[1]] = binary_shift_left(values.get(_variables[0]), int(_variables[1]))

        elif _splitWord == "RSHIFT":
            values[_instructions[1]] = binary_shift_right(values.get(_variables[0]), int(_variables[1]))

        else:
            print "Unknown command: " + _splitWord


f = open('./input/day7.txt', 'r')
for line in f:

    # Trim input
    line = line.strip()

    # Handle the instruction set
    make_keys(line)
    handle_instruction(line)

    # print "Processed " + line

for key in values:
    if str(values[key]) is not "0":
        print str(key) + " has the following value: " + str(values[key])

print "\nKey a contains this value: " + str(values["a"])
f.close()

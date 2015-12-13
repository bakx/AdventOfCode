values = {}

# Initialize array with the alphabet
for _i in xrange(97, 97+26):
    values[chr(_i)] = 0
    for _n in xrange(97, 97+26):
        key = chr(_i) + chr(_n)
        values[key] = 0


def binary_not(decimal_value):
    decimal_value = binary_to_16bit(decimal_value)
    return int("0b" + decimal_value.replace("0", "2").replace("1", "0").replace("2", "1"), 2)


def binary_to_16bit(decimal_value):
    decimal_value = bin(decimal_value).lstrip("0b")
    decimal_value = decimal_value.rjust(16, "0")
    return decimal_value


def binary_shift_left(decimal_value, n):
    decimal_value = binary_to_16bit(decimal_value)
    return int("0b" + decimal_value, 2).__lshift__(n)


def binary_shift_right(decimal_value, n):
    decimal_value = binary_to_16bit(decimal_value)
    return int("0b" + decimal_value, 2).__rshift__(n)


def handle_instruction(instruction):

    _instructions = instruction\
        .replace("through ", "") \
        .split("->")

    # Transferring a value?
    _instructions[0] = str(_instructions[0]).strip()
    _instructions[1] = str(_instructions[1]).strip()

    if _instructions[0].isdigit():
        _currentValue = int(_instructions[0])
        values[_instructions[1]] = _currentValue
    elif _instructions[0].startswith("NOT"):
        _variables = _instructions[0].replace("NOT ", "").strip()

        values[_instructions[1]] = binary_not(values.get(_variables))

    else:

        # Determine the split mode
        _splitWord = _instructions[0].split(" ")[1]

        _variables = _instructions[0].split(_splitWord)
        _variables[0] = str(_variables[0]).strip()
        _variables[1] = str(_variables[1]).strip()

        if _splitWord == "AND":
           values[_instructions[1]] = int(binary_to_16bit(values.get(_variables[0])), 2) & int(binary_to_16bit(values.get(_variables[1])), 2)
        elif _splitWord == "OR":
            values[_instructions[1]] = int(bin(values.get(_variables[0]) | values.get(_variables[1])), 2)
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
    handle_instruction(line)

    print "Processed " + line

for key in values:
    if str(values[key]) is not "0":
        print str(key) + " has the following value: " + str(values[key])

f.close()

strLength = 0
memLength = 0
strEncodedLength = 0

f = open('./input/day8.txt', 'r')
for line in f:

    # Trim input
    line = line.strip()

    # Part 1
    strLength += line.__len__()
    memLength += str(eval(line)).__len__()

    # Part 2
    strEncodedLength += line\
        .replace("\\", "\\\\")\
        .replace("\"", "\\\"")\
        .__len__() + 2


print "Answer part 1: " + str(strLength - memLength)
print "Answer part 2: " + str(strEncodedLength - strLength)

locations = {}


f = open('./input/day9.txt', 'r')
for line in f:

    # Trim input
    line = line.strip()

    # Build up city list
    instruction = line.split(" ")

    print "{} {} {}".format(instruction[0], instruction[2], instruction[4])

    tup1 = ('physics', 'chemistry', 1997, 2000);


    #London to Dublin = 464
    #London to Belfast = 518
    #Dublin to Belfast = 141



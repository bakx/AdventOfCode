import hashlib

f = open('day4.txt', 'r')
for line in f:

    # Keep track of matches
    matches = {}

    # Trim input
    line = line.strip()

    # Debug information
    print line

    # Calculate hashes to find match
    for i in xrange(9999999):
        h = hashlib.md5()
        h.update(line + str(i))
        digest = h.hexdigest()

        if str(digest).startswith("00000") and str(digest)[5].isdigit():
            print "Found 5 digit match at " + str(i)
            print digest

        if str(digest).startswith("000000") and str(digest)[5].isdigit():
            print "Found 6 digit match at " + str(i)
            print digest
            break

    print "Done"
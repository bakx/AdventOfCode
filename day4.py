import hashlib

f = open('day4.txt', 'r')
for line in f:

    # Trim input
    line = line.strip()

    # Debug information
    print line

    # Calculate hashes to find match
    for i in xrange(99999999):
        h = hashlib.md5()
        h.update(line + str(i))
        digest = h.hexdigest()

        if digest.startswith("00000"):
            if digest[5].isdigit() and digest[5] is not "0":
                print "Found 5 digit match at " + str(i)
                print digest

        if digest.startswith("000000"):
            if digest[6].isdigit() and digest[6] is not "0":
                print "Found 6 digit match at " + str(i)
                print digest
                break

    print "Done"

f.close()


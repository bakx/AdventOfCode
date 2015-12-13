# Initialize variables
alphabet = {}
keyPhrasesRequired = {}
validWordCount = 0
invalidWordCount = 0

# Initialize array with the alphabet
for i in xrange(97, 97+27):
    key = chr(i)
    alphabet[key] = 0

# Initialize array with all key phrases that are required
for i in xrange(97, 97+26):
    for n in xrange(97, 97+26):
        key = chr(i) + chr(n)
        keyPhrasesRequired[key] = 0


def validate_word(word):

    for _i in xrange(0,  word.__len__() - 2):
        if word[_i:_i+2] == word[_i+3:_i+4]:
            return False, "Failed due overlapping"

    _hasRepeat = has_repeat_character(word)
    _hasDouble = False

    for fp in keyPhrasesRequired:
        if word.count(fp) > 1:
            _hasDouble = True

    if _hasRepeat[0] and _hasDouble:
        return True, "Ok"

    return False, ""


def has_repeat_character(word):
    for _i in xrange(0,  word.__len__() - 2):
        if word[_i] == word[_i + 2]:
            return True, "OK"

    return False, "No repeated string"


def valid_word(word):

    # Does the word contains at least one letter that appears twice in a row?
    _has_key_phrase = validate_word(word)
    if not _has_key_phrase[0]:
        return False, "Rule: Key phrase error. " + _has_key_phrase[1]

    # All rules validated
    return True, "Validated"


f = open('day5.txt', 'r')
for line in f:

    # Trim input
    line = line.strip()

    # Debug information
    checkWord = valid_word(line)

    if checkWord[0]:
        validWordCount += 1
        print line + " passed validation."
    else:
        invalidWordCount += 1
        print line + " failed validation because: " + checkWord[1]

print "Found " + str(validWordCount) + " valid words."
print "Found " + str(invalidWordCount) + " invalid words."

f.close()

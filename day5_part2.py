# Initialize variables
alphabet = {}
keyPhrasesRequired = {}
validWordCount = 0
invalidWordCount = 0

# Initialize array with the alphabet
for i in xrange(96, 96+27):
    key = chr(i)
    alphabet[key] = 0

# Initialize array with all key phrases that are required
for i in xrange(96, 96+27):
    for n in xrange(96, 96+27):
        key = chr(i) + chr(n)
        keyPhrasesRequired[key] = 0


def has_key_phrase(word, keyPhrases):
    _foundPhrases = False

    # Initial check to see if there are at least 2 items of any phrase in the word
    for fp in keyPhrasesRequired:
        if word.count(fp) > 1:
            # Initial check passes
            _foundPhrases = True

            # Is this a phrase that has identical characters?
            if fp[0] == fp[1]:

                # Check the first phrase for overlapping
                _firstMatch = word.find(fp)

                if word[_firstMatch + 2] == fp[0]:
                    return False, "Failed due overlapping " + fp[0]

                # Check the first phrase for overlapping
                _secondMatch = word.find(fp, _firstMatch)

                # Check if the second match is at the end of the string. If so, no overlapping check needed.
                # This check is mandatory since it will also prevent access errors.
                if word.__len__() - 1 >= _secondMatch + 2:
                    if word[_secondMatch + 2] == fp[0]:
                        return False, "Failed due overlapping " + fp[0]

            # It contains at least one letter which repeats with exactly one letter between them
            _hasRepeatCharacter = False

            for i in xrange(0,  word.__len__() - 1):
                if i + 2 < word.__len__() - 1:         # 3 is used here due character indexing starting at 0
                    if word[i] == word[i + 2]:      # check the the item 2 characters down from original position is matching
                        _hasRepeatCharacter = True
                        break

            if not _hasRepeatCharacter:
                return False, "No repeated characters with exactly one letter in between"

    if not _foundPhrases:
        return False, "No repeated phrase found"

    return True, "Validated"


def valid_word(word):

    # Does the word contains at least one letter that appears twice in a row?
    _has_key_phrase = has_key_phrase(word, keyPhrasesRequired)
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
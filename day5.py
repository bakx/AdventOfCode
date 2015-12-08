# Initialize variables
vowels = {"a", "e", "i", "o", "u"}
keyPhrasesRequired = {}
keyPhrasesForbidden = {"ab", "cd", "pq", "xy"}
validWordCount = 0
invalidWordCount = 0

# Initialize array with the alphabet
for i in xrange(96, 96+27):
    key = chr(i) + chr(i)
    keyPhrasesRequired[key] = 0


def has_key_phrase(word, keyPhrases):
    for fp in keyPhrasesRequired:
        if word.find(fp) > -1:
            return True

    return False


def valid_word(word):

    _vowelCount = 0

    # Does it contain at least 3 vowels?
    for c in word:
        for v in vowels:
            if c == v:
                _vowelCount += 1

    if _vowelCount < 3:
        return False, "Rule: Vowel Count. Vowels in word: " + str(_vowelCount)

    # Does the word contains at least one letter that appears twice in a row?
    if not has_key_phrase(word, keyPhrasesRequired):
        return False, "Rule: Key phrase not found"

    # Any forbidden key phrases in this word?
    for fp in keyPhrasesForbidden:
        if word.find(fp) > 0:
            return False, "Rule: Forbidden phrase. Found: " + fp

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

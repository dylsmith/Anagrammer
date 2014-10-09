import cPickle as pickle

def WordToCharCount(word):      # Maps from each char in the word to a count of its occurrences
    counts = {}                 # Make the map
    word = word.lower()         # Bring it to lowercase
    for char in word:           # For each char
        if char.isalpha():      # If it's  a letter,
            if char in counts:  # And if it exists as a key in our map
                counts[char] += 1   # Increment that char
            else:
                counts[char] = 1    # Else, create that key
    return counts

def DictionaryToObject(fileName):       # Reads from a plaintext dictionary file, writes it to a letter-counted binary one
    words = {}                          # Map from word to its letter counts
    with open(fileName, 'rt') as file:  # Open the plaintext
        for word in file:               # For each word
            word = word.rstrip()        # Remove whitespace/newlines
            words[word] = WordToCharCount(word) # Generate the char counts

    with open('Dictionary', 'wb') as out:   # Open the binary file
        pickle.dump(words, out)             # Dump the map to it

def ObjectToDictionary(fileName):       # Loads a dictionary in from a file
    with open(fileName, 'rb') as file:
        return pickle.load(file)

#DictionaryToObject('wordsEn.txt') # Uncomment to write a new dictionary file



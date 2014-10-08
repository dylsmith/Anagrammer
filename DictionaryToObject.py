import cPickle as pickle

def WordToCharCount(word):
    counts = {}
    word = word.lower()
    for char in word:
        if char.isalpha():
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
    return counts

def DictionaryToObject(fileName):
    words = {}
    with open(fileName, 'rt') as file:
        for word in file:
            words[word] = WordToCharCount(word)

    with open('Dictionary', 'wb') as out:
        pickle.dump(words, out)

def ObjectToDictionary(fileName):
    with open(fileName, 'rb') as file:
        return pickle.load(file)

def test():
    DictionaryToObject('wordsEn.txt')

    dict = ObjectToDictionary('Dictionary')
    for word in dict:
        print word
        print dict[word]




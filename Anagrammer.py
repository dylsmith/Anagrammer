from DictionaryToObject import ObjectToDictionary, WordToCharCount, test
import copy

def IsSubset(testWord, counts):
    for char in testWord:
        if char in counts:
            counts[char] -= testWord[char]
            if counts[char] == 0:
                del counts[char]
            elif counts[char] < 0:
                return 0
        else:
            return 0
    return counts

def AnagrammerR(curString, counts):
    origCounts = copy.deepcopy(counts)
    if len(counts) == 0:
        print curString
    else:
        for word in dict:
            counts = origCounts
            viable = IsSubset(dict[word], counts)
            if viable == 0:
                continue
            else:
                curString += word
                AnagrammerR(curString, viable)



def Anagrammer(string):
    AnagrammerR('', WordToCharCount(string))

dict = ObjectToDictionary('Dictionary')

#input = raw_input("Enter a sentence: ")
input = "Hello"
Anagrammer(input)

#for word in dict:
#    print word
#    print dict[word]


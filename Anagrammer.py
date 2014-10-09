from DictionaryToObject import ObjectToDictionary, WordToCharCount, test
import copy

def IsSubset(testWord, counts):     # Given a test word and a set of counts, returns 0 if that word can't be made
                                    # from those counts, or a new count set made by removing the necessary letters
    for key in testWord:    # For each char in testWord
        if key in counts:   # Check if that char is even in our count set - if not, return 0
            counts[key] -= testWord[key]    # If it is, subtract the enough letters from counts to spell the word
            if counts[key] == 0:    # If we have no more of that letter, delete it from our counts set
                del counts[key]
            elif counts[key] < 0:   # If we have too few of that letter, return 0; we can't spell this word
                return 0
        else:
            return 0
    return counts   # If we've successfully removed the necessary letters, return the count set of remaining letters

def AnagrammerR(curString, counts): # Recursive call. curString increases with recursion depth,
                                    # counts are the chars we still need to use
    if len(counts) == 0:              # If we have no letters left to use
        print 'Found: ',curString     # We have found an anagram
    else:
        for word in dict:       # For each potential word
            viable = IsSubset(dict[word], copy.copy(counts))    # Check if it's a subset of the chars we have left.
            if viable == 0:     # 0 means the word didn't fit
                continue
            else:   # Otherwise, we have a new word for our sentence!
                tempString = copy.copy(curString)   # Copy our curString
                tempString += word + ' '            # And append the new word
                AnagrammerR(tempString, copy.copy(viable))  # Recursively call Anagrammer, with this new
                                                            # curString and set of remaining chard

def Anagrammer(string): #I nitial front-facing call
    AnagrammerR('', WordToCharCount(string))    # Call the recursive version, beginning with an empty string to add words to

dict = ObjectToDictionary('Dictionary') # Load dictionary in from file
input = raw_input("Enter a sentence: ") # Prompt user for a sentence
Anagrammer(input)   # Call anagrammer


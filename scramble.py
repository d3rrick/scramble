from itertools import permutations 
import functools 
import operator 
import enchant

# enter your words
words = input("Enter scrambled word and press enter \n")

# choose language to validate the words

# check if word is in dictionary
d = enchant.Dict("en_UK")
def exists(word):
    return d.check(word)

# convert tuple to  string
def convertTuple(tup): 
    str = functools.reduce(operator.add,(tup)) 
    return str

# function to check words based on permutation
print("\n Your words \n")
def search(words):
    count=len(words)
    while count > 1:
        for i in list(permutations(words,count)): 
            conv = convertTuple(i)
            if exists(conv):
                print(conv)
        count -=1

# entry of search based on factorial algorithim pattern
def scramble(words):
    n = len(words)
    if n<=1:
        return
    else:
        search(words)
        first_words, last_char = words[:-1],words[-1:]
        count=0
        while count >= n-1:
            words = last_char+first_words
            return scramble(words)
            count+=1
    return

scramble(words)

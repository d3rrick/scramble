from itertools import permutations 
import functools 
import operator 
import enchant
import string

def main():
    # helper data structures
    all_words=[]
    words_with_sum={}
    # sorted_words
    # enter your words
    while True:
        words = input("Type you scrambled word and press enter key \n")
        if words.isalpha():
            break
        print("Please enter characters A-Z only")
    
    words = words.strip().upper()
    # choose language to validate the words

    # check if word is in dictionary
    d = enchant.Dict("en_US")
    def exists(word):
        return d.check(word)

    # convert tuple to  string
    def convertTuple(tup): 
        str = functools.reduce(operator.add,(tup)) 
        return str

    # function to check words based on permutation
    print("\n Your words with score points \n")
    def search(words):
        count=len(words)
        while count > 1:
            for i in list(permutations(words,count)): 
                conv = convertTuple(i)
                if exists(conv):
                    all_words.append(conv)
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


    def lookup(char):
        if char in ["A","E","I","L","N","O","R","S","T","U"]:
            return 1

        if char in ["D","G"]:
            return 2

        if char in ["B","C","M","P"]:
            return 3

        if char in ["F","H","V","W","Y"]:
            return 4

        if char in ["K"]:
            return 5

        if char in ["J","X"]:
            return 8

        if char in ["Q","Z"]:
            return 10


    def get_sum_of_characters():
        if all_words:
            for word in all_words:
                list_of_word = ",".join(word).split(",")
                sum = 0
                for char in list_of_word:
                    sum += lookup(char)
                words_with_sum[word]=sum

    def board():
        if words_with_sum:
            all= sorted(words_with_sum.items(), key=lambda x: x[1], reverse=True)
            for a in all:
                print(a)
    
    scramble(words)
    get_sum_of_characters()
    print(board())
    

if __name__ == "__main__":
    main()
    
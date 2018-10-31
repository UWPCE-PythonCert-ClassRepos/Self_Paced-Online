'''
Shin Tran
Python 210
Lesson 4 Assignment
'''


import string # For punctuation
import random # For a random number generator

# To store all the two word combo as keys and the following word as a value
word_dict = {}


# Opens a text file, parses though it line by line, storing two consecutive
# words as keys, and the following word as a value
def open_file():
    sentence = []
    with open('sherlock.txt', 'r') as f:
    #with open('sherlock_small.txt', 'r') as f:
        contents = f.readlines()
        #print(contents)
        for line in contents:
            unmod_sentence = line
            for c in string.punctuation:
                unmod_sentence = unmod_sentence.replace(c,'')
            sentence = unmod_sentence.split()
            for i in range(0, len(sentence)-2):
                the_key = sentence[i] + " " + sentence[i+1]
                the_value = sentence[i+2]
                if the_key not in word_dict:
                    word_dict.setdefault(the_key,[]).append(the_value)
            sentence = []
    #for key, value in word_dict.items():
    #    print(key + ": " + str(value))


# Picks a key by random initially, appends those two words to a list,
# then pulls the value and appends that to a list as well, take the 2nd
# word of the key and the value, makes that the new key and repeats
# based on the word count that's randomly generated, max of 15 words,
# the loop breaks if no key/value is found
def make_sentence():
    the_sentence = []
    first_set = random.choice(list(word_dict))
    third_word = random.choice(word_dict[first_set])
    the_sentence.extend(first_set.split())
    the_sentence.append(third_word)
    word_count = random.randint(5,14)
    temp_key = ""
    for i in range(1, word_count):
        temp_key = str(the_sentence[i]) + " " + str(the_sentence[i+1])
        next_word = word_dict.get(temp_key, 'NoKeyFound')
        if word_dict.get(temp_key):
            the_sentence.append(next_word[0])
        else:
            break
    make_proper(the_sentence)


# Takes a list as a parameter, turns that into a string using a for loop,
# capitalizes the first character,strips off the space at the end,
# and appends a period to the end so it's a sentence
def make_proper(sentence):
    s = ""
    for word in sentence:
        s += word + " "
    s = s[:-1].capitalize() + '.'
    print(s)

# Python program to use main for function call
# runs the program to make 15 sentences
if __name__ == "__main__":
    open_file()
    for j in range(0, 15):
        make_sentence()

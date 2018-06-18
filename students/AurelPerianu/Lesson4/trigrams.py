#!/usr/bin/env python3
# Lesson 4 - Trigrams
import random
import string

def main_fct():
    #input_file = input("Please enter the name of a file (with extension):\n")
    input_file='sherlock_small.txt'
    with open(input_file, 'r') as f:
        text = f.read()
    #remove unprintable characters
    filter(lambda x: x in string.printable, text)
    # lower-case everything to remove that complication:
    text = text.lower()
    # define punctuation
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    no_punct = ""
    for char in text:
        if char not in punctuations:
            no_punct = no_punct + char
        else:
            no_punct = no_punct + ' '
    text=no_punct
    #split into words
    words = text.split()
    word_dict=trigram(words)
    text_new=generate_text(word_dict)
    print (text_new)

def trigram(words):
    """build a trigram dict from the passed-in text"""
    # Dictionary for trigram results:
    # The keys will be all the word pairs
    # The values will be a list of the words that follow each pair
    word_dict = {}
    # loop through the words
    for i in range(len(words) - 2):
        pair = tuple(words[i:i+2])
        third = words[i+2]
        # use setdefault() to append to an existing key or to generate a new key
        word_dict.setdefault(pair, []).append(third)
    return word_dict

def generate_text(word_dict):
    """generate new text from the word_dict"""
    trigram_text = ''
    #generate a random number - text length will be dependent by this number
    #we cab adjust param: 10,5
    random_prop = random.randint(len(word_dict.keys())//10,len(word_dict.keys())//5)
    for i in range(random_prop):  # do thirty sentences
        #pick a word pair to start the sentence
        fragm = random.choice(list(word_dict.keys()))
        sentence=[]
        sentence.append(fragm[0])
        sentence.append(fragm[1])
        rand2=len(word_dict.keys())//10
        for j in range(1,rand2):
            value= word_dict.get(fragm)
            if value==None:
                break
            if len(value)>1:
                ln=random.randint(1,len(value))-1
            else:
                ln=len(value)-1
            #create new word key from the old key and value
            fragm=(fragm[1],value[ln],)
            sentence.append(fragm[1])
        sentence=list(sentence)
        # capitalize the first word:
        sentence[0] = sentence[0].capitalize()
        # add the period
        sentence[-1] += ". "
        sentence = " ".join(sentence)
        #add the complete sentence
        trigram_text+=sentence
    return trigram_text

if __name__=='__main__':
  main_fct()

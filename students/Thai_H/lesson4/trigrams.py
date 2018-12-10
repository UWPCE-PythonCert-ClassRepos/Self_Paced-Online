#!/usr/bin/env python3
import os
import random

#-------------------------------------------------------------------------------------
# read in words from a text file: sherlock_small.txt
def read_words():
    with open('sherlock_small.txt', 'r') as file:
        text = file.read().replace('--', ' ').replace('(',' ').replace(')', ' ').replace('(',' ').replace(',','').replace('\n', ' ')
        return text.lower().split()   #return list of words


#------------------------------------------------------------------------------------
# create a trigram from string of words
def create_trigram_from_words(words):
    trigram = {}
    for idx in range(len(words) -2):
        two_word_as_key = words[idx] + ' ' + words[idx + 1]
        third_word_as_value = words[idx + 2]
        trigram.setdefault(two_word_as_key, []).append(third_word_as_value)
    return trigram


#----------------------------------------------------------------------------
def create_new_text(trigram):
    random_key = random.choice(list(trigram)).split()
    for idx in range(2000):
        new_key = random_key[idx] + ' ' + random_key[idx + 1]
        if new_key in trigram:
            new_value = random.choice(trigram[new_key])
            random_key.append(new_value)
        else:
            break
    display_trigram(random_key)


#----------------------------------------------------
def display_trigram(new_text):
    print( ' '.join(new_text))


#----------------------------------------------------------
def main():
    words = read_words()
    trigram = create_trigram_from_words(words)
    create_new_text(trigram)


#-------------------------------------------------------------
if __name__ == "__main__":
    main()


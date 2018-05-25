#!/usr/bin/env python3
import os
import random

# read in a file and convert the words into list
def readin_words(file_name = "sherlock_small.txt"):
     with open(file_name, "r") as rf:
        # readin file and replace all the non words with space
        content = rf.read().replace('\n', ' ').replace('.','').replace(',','').replace('(',' ').replace(')', ' ').replace('--',' ')
        # convert the content into list of words
        return content.lower().split()

# create a trigram dict according to the words list generated from the input file     
def create_trigram_dict(words_list):
    trigram_dict = {}
    for i in range(len(words_list)-2):
        two_words_key=words_list[i] +' '+ words_list[i+1]
        third_word_value = words_list[i+2]
        trigram_dict.setdefault(two_words_key,[]).append(third_word_value)
    return trigram_dict

def create_new_content(trigram_dict, content_length = 100):
    # initiate from a random key in trigram_dict
    new_content = random.choice(list(trigram_dict)).split()    
    # create a new words list, the number of words are set to content_length
    for i in range(content_length):
        new_key = new_content[i]+' '+ new_content[i+1]
        if new_key in trigram_dict:
            new_word = random.choice(trigram_dict[new_key])
            new_content.append(new_word)
        else:
            break
    print( ' '.join(new_content))

if __name__ == "__main__":
    words_list = readin_words()
    trigram_dict = create_trigram_dict(words_list)
    create_new_content(trigram_dict)
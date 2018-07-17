#! /usr/bin/env python3
# Author SLammertink
# Kata assignment Lesson 04

# Will use the book 'Adventures of Sherlock Holmes by Arthur Conan Doyle'
# the .txt file can be found online at: https://www.gutenberg.org/files/48320/48320-0.txt

import re
import collections

trigram_dict = {}
#trigram_dict = collections.defaultdict(list)
text = []
first_k = 'walsall', 'where' # the tuple we start the sequence with

def read_text():
    ''' first we remove the header and footer fom a Gutenberg text with a regular expression '''
    beginning_of_text = re.compile(r"\*\*\* ?start of (this|the) project gutenberg ebook[^*]*\*\*\*")
    end_of_text = re.compile(r"\*\*\* ?end of (this|the) project gutenberg ebook[^*]*\*\*\*")
    txt = open("sherlock.txt").read().lower() # open the text
    beg = beginning_of_text.search(txt).end() # set beginning of the text
    end = end_of_text.search(txt).start() # set the end of the text
    main_text = (txt[beg:end]) # main text
    main_text = re.sub(r'[^\w\s]','',main_text).lower().replace('\n', ' ').split() # remove puncuations
    #and make main_text lower case'''

    trigrams = [main_text[i:i+3] for i in range(len(main_text)-2)] # define the trigrams
    for words in trigrams:
        word_pairs = tuple(words[:2]) # make word pairs from trigrams to add to tuple
        followup_words = words[-1] # the words following the tuple
        if word_pairs not in trigram_dict:
            trigram_dict[word_pairs] = followup_words # add folloup_words to the trigram dictionary
        else:
            trigram_dict[word_pairs] = (trigram_dict[word_pairs] , followup_words) #add follow_up words to
            # trigram dictionary if the word pair already exists in this dictionary

    for k, v in trigram_dict.items():
        next_k = (first_k[1] , v) # next key becomes fist keyword, second word and the value
        text.append(next_k) # we append the new ket to the text list
        first_k == next_k # now first key becomes next key to iterate through the list

    print(text)

if __name__ == '__main__':
    read_text()






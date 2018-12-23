#!/usr/bin/env python
# coding: utf-8

from collections import defaultdict
import random
import string
import re

def set_trigram(ent_letter, len_word, random_start):
    words = ent_letter.split()
    if(len_word > len(words)):                            # set length of words if not given
        len_word = len(words)
    kk = 0                                               # random starting point
    if random_start.lower() is not "no":
        kk = random.choice( range( 0, (len_word - 4)))
    pair_all = tuple([" ".join(words[ i:i+2]), words[ i + 2]] for i in range(kk, len_word - 2))
    pair_update = defaultdict(list)
    for k, v, in pair_all:
        pair_update[k].append(v)
    pair_update = dict(pair_update)
    return(pair_update)

def bld_trigram(ent_letter, len_word, random_start = "No"):
    pair_set = set_trigram( ent_letter = ent_letter,
                            len_word = len_word,
                            random_start = random_start)
    pair_key = list(pair_set.keys())
    pair_values = list(pair_set.values())
    pair_set2 = [[tuple(pair_key[i].split(" ")), pair_values[i]] for i in range (len(pair_key))]
    pair_set2 = dict(pair_set2)
    return(pair_set2)

# reads text file from the file path

def read_text():
    open_text = open("sherlock_small.txt")
    read_text = open_text.read()
    open_text.close()
    return(read_text)

def clean_text():
    given_text = read_text()
    translate_text = re.sub('[^A-Za-z]+', ' ', "{}".format(given_text)).lower()
    return(translate_text)


# apply the above two functions to get the output
# assumption here is given sentenses contain words only

if __name__ == "__main__":
    letter1 = clean_text()
    print("\n", letter1, "\n")
    trigrams = set_trigram(ent_letter = letter1, len_word = 10, random_start = "no")
    print("\n", trigrams, "\n")
    trigrams_fixed = bld_trigram(ent_letter = letter1, len_word = 10, random_start = "no")
    print("\n", trigrams_fixed, "\n")
    trigrams_random = bld_trigram(ent_letter = letter1, len_word = 10, random_start = "yes")
    print("\n", trigrams_random, "\n")

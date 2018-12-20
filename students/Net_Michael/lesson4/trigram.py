#!/usr/bin/env python
# coding: utf-8

from collections import defaultdict
import random

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
    pair_set = set_trigram(ent_letter = ent_letter, len_word = len_word, random_start = random_start)
    pair_key = list(pair_set.keys())
    pair_values = list(pair_set.values())

    pair_set2 = [[tuple(pair_key[i].split(" ")), pair_values[i]] for i in range (len(pair_key))]
    pair_set2 = dict(pair_set2)
    return(pair_set2)

# apply the above two functions to get the output
# assumption here is given sentenses contain words only

letter1 = 'I wish I may I wish I might'

if __name__ == "__main__":
    trigramsA = set_trigram(ent_letter = letter1, len_word = 8, random_start = "yes")
    print(trigramsA)

    trigrams = bld_trigram(ent_letter = letter1, len_word = 8, random_start = "yes")
    print(trigrams)

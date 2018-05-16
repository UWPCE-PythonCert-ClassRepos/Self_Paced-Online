#!/usr/bin/env python3

# chmod +x kata.py needs to be performed before executable

'''
    File Name: kata.py
    Author: Matt Hudgins
    Date created: 5/15/18
    Date last modified: 5/15/18
    Python Version 3.6.4
'''

import random
import math


# Starting the kata fourteen lesson
def randomkey(i):
    """ Returns random key in dictionary"""
    return random.choice(list(i.keys()))

def randvalue(i, k):
    """ This function returns a random value from values list"""
    return random.choice(i[k])


if __name__ == "__main__":
    input_file = 'sherlock.txt'
    with open(input_file, 'r') as fp:
        input = fp.read()
        fp.close()

    input = input.replace('\n', ' ').replace('\r', ' ').lower()
    punctuation = set(['--', '.', ',', '!', '(', '('])
    for p in punctuation:
        input = input.replace(p, f'{p}')
    words = input.split()
#   print(seed)

    # Trigram Dict
    trigrams = {}
    for j in range(len(words) - 1):
        key = tuple(words[j:j + 1])
        value = words[j + 1]
        if key in trigrams.keys():
            trigrams[key].append(value)
        else:
            trigrams[key] = []
            trigrams[key].append(value)

#  New Text
    key_init = randomkey(trigrams)
    value_init = randvalue(trigrams, key_init)
    out_list = list(key_init)
    out_list.append(value_init)
    for i in range(256):
        k = tuple(out_list[-2:])
        if k in trigrams:
            v = randvalue(trigrams, k)
        else:
            k = randomkey(trigrams)
            for i in list(k):
                out_list.append(i)
            v = randvalue(trigrams, k)
        out_list.append(v)
    paragraph = ' '.join(out_list)
    print(paragraph)
#!/usr/bin/env python3
"""
File Name: trigram.py
Author: Travis Brackney
Class: Python 201 - Self paced online
Date Created 4/23/2018
Python Version: 3.6.4
"""
import random


def randkey(d):
    ''' Returns random key in dictionary'''
    return random.choice(list(d.keys()))


def randvalue(d, k):
    '''Given a dictionary and key, returns random value from values list'''
    return random.choice(d[k])


input_file = 'sherlock.txt'
f = open(input_file, 'r')
input = f.read()
f.close()

input = input.replace('\n', ' ')  # removes endlines
punctuation = set(['--', '.', ',', '!', '(', ')'])
for p in punctuation:  # puts spaces around  punctuation
    input = input.replace(p, f' {p} ')
seed = input.split()

# implements trigram as a dictionary
trigrams = {}
for i in range(len(seed) - 2):
    key = tuple(seed[i:i+2])
    value = seed[i+2]
    if key in trigrams.keys():
        trigrams[key].append(value)
    else:
        trigrams[key] = []
        trigrams[key].append(value)

# Generates new text from trigrams dictionary.
key_init = randkey(trigrams)
value_init = randvalue(trigrams, key_init)
out_list = list(key_init)
out_list.append(value_init)
for i in range(256):
    k = tuple(out_list[-2:])
    if k in trigrams:
        v = randvalue(trigrams, k)
    else:
        k = randkey(trigrams)
        for i in list(k):
            out_list.append(i)
        v = randvalue(trigrams, k)
    out_list.append(v)
paragraph = ' '.join(out_list)
print(paragraph)

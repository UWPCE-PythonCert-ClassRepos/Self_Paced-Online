# ------------------------------------------------- #
# Title: Lesson 4, pt 2/2, Trigrams
# Dev:   Craig Morton
# Date:  8/25/2018
# Change Log: CraigM, 8/25/2018, Trigrams
# ------------------------------------------------- #

# !/usr/bin/env python

import string
import random

file_name = open('sherlock_small.txt', 'r')
file_content = file_name.read().lower()
file_name.close()
translation = str.maketrans(string.punctuation, ' '*len(string.punctuation))
new_text = file_content.translate(translation).split()


def trigrams(list):
    """Trigram functionality"""
    trigram_list = []
    for i in range(len(list)-2):
        trigram_list.append(('{} {}'.format(list[i], list[i+1]), list[i+2]))
    return trigram_list


def dictionary_conversion(list):
    """Converting to dictionary"""
    trigram_dictionary = dict()
    for i in list:
        if i[0] in trigram_dictionary:
            trigram_dictionary[i[0]].append(i[1])
        else:
            trigram_dictionary[i[0]] = [i[1]]

    return trigram_dictionary


dictionary_new = dictionary_conversion(trigrams(new_text))
new_text = list()
new_key = random.choice(list(dictionary_new))
new_key_split = new_key.split()
new_text.append(new_key_split[0])
new_text.append(new_key_split[1])
count = 0

while new_key in dictionary_new and count < 100:
    new_key_split = new_key.split()
    random_value = random.choice(dictionary_new[new_key])
    new_text.append(random_value)
    new_key = new_key_split[1] + " " + random_value
    count += 1
print(' '.join(new_text[0:]))

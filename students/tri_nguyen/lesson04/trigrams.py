#!/usr/bin/env python3

# ------------------------------------------- #
# Student:   Tri Nguyen
# Instructor: Natasha Aleksandrova
# Date:  28-Feb-2018
# ------------------------------------------- #

import random


def get_word_list():
    ''' this function create a list of words from 
        sherlock_small.txt '''

    word_list = []

    with open('sherlock_small.txt') as f:
        for line in f:
            line.rstrip()
            for char in line:
                line = line.replace('--', ' ')
            words = line.split()

            for word in words:
                word_list.append(word)

    return word_list


def create_word_dict():
    ''' create a dictionary that looks like the
        trigram table '''

    word_dict = {}

    txt_words = get_word_list()

    for idx in range(len(txt_words) - 2):
        word_dict.setdefault((txt_words[idx], txt_words[idx + 1]), []).append(txt_words[idx + 2])

    return word_dict


word_dict = create_word_dict()
word_list = get_word_list()
word_list_idx = list(range(len(word_list)))

start_point = random.choice(word_list_idx)

new_text = [word_list[start_point], word_list[start_point + 1]]
word_pair = (word_list[start_point], word_list[start_point + 1])

def create_new_text(rand_pair):
    ''' create new text recursively '''

    if rand_pair in word_dict:
        next_word = random.choice(word_dict[rand_pair])
        new_text.append(next_word)
        create_new_text((rand_pair[1], next_word))


# Run create_new_text recursively to get new_text
create_new_text(word_pair)

print(' '.join(new_text))

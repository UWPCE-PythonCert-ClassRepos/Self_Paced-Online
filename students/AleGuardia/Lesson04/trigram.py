#!/usr/bin/env python3

import string, random


def strip_punctuation(text):
    """Takes a string and returns the string without punctuation"""
    translator = str.maketrans('','',string.punctuation)
    return text.translate(translator)


def strip_words(text):
    """Takes a string a returns a list of words"""
    return text.split()


def creates_keys(words):
    """Takes a list of words and returns a dict of two word keys and a list of words that follows it"""
    key_value_list = {}
    for i in range(len(words)-2):
        current_key = words[i] + " " + words[i+1]
        if current_key not in key_value_list.keys():
            key_value_list.update({current_key: []})
        key_value_list[current_key].append(words[i+2])
    return key_value_list


def return_key(word_dict):
    """Takes a dictionary and returns a random key"""
    word_list = list(word_dict.keys())
    return random.choice(word_list)

def build_word(word_dict):
    """Takes a dict and returns random words"""
    text = ""
    word=return_key(word_dict)
    text += word
    while True:
        try:
            word = word_dict[word].pop()
            text += "" + word

        except (IndexError,KeyError) as e:
            return text



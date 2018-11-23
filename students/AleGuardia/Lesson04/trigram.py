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
    word_pair=return_key(word_dict)
    text += word_pair
    while True:
        try:
            word = word_dict[word_pair].pop()
            text += " " + word
            word_pair = word_pair.split()[-1] + " " + word
        except (IndexError,KeyError) as e:
            return text


def upload_book(filename):
    with open(filename) as f:
        book= f.read()
        return book


def write_new_book(book):
    f = open('trigram.txt', 'w')
    f.write(book)
    return None


def run_trigram():
    filename = input("Please enter the book's filename:")
    book = upload_book(filename)
    key_dict = creates_keys(strip_words(strip_punctuation(book)))
    new_book = build_word(key_dict)
    write_new_book(new_book)
    print('The new version of the book is on a file named trigram.txt')
    return None



#!/usr/bin/env python3
import random
import itertools
import string
from collections import defaultdict


def text_import():
    with open('sherlock_small.txt', "r") as book_text:
        book_string = book_text.read().replace('\n', ' ').lower()
        book_string = book_string.replace(string.punctuation, ' ')
        return book_string


def make_dict():
    book_list = text_import().split()
    book_dict = defaultdict(list, {})
    for i in range(len(book_list)-2):
        book_dict[(book_list[i], book_list[i+1])].append(book_list[i+2])
    return book_dict


def new_story():
    new_list = []
    book_list = text_import().split()
    book_dict = make_dict()
    lucky_number = random.randint(0, len(book_list))
    magic_key = (book_list[lucky_number], book_list[lucky_number+1],)
    new_list.append(magic_key)
    length = len(book_list) - lucky_number
    for i in range(length-2):
        try:
            new_word = random.choice(book_dict[magic_key])
            new_word = (new_word,)
            new_list.append(new_word)
            magic_key = magic_key[1:] + new_word
        except IndexError:
            return
    flat_list = list(itertools.chain(*new_list))
    machine_masterpiece = ' '.join(flat_list)
    return machine_masterpiece


new_book = new_story()
print(new_book)

new_story()

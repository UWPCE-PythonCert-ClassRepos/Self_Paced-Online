#!/usr/bin/env python3
import random
import itertools
from collections import defaultdict


def text_import():
    with open('sherlock_small.txt', "r") as book_text:
        book_string = book_text.read().replace('\n', ' ')
        book_string = book_string.replace(',', ' ')
        book_string = book_string.replace('.', ' ')
        book_string = book_string.replace('-', ' ')
        book_string = book_string.replace('(', '')
        book_string = book_string.replace(')', '')
        book_string = book_string.lower()
        return book_string


def make_dict():
    book_list = text_import().split()
    book_dict = defaultdict(list, {})
    for i in range(len(book_list)-2):
        book_dict[f'{book_list[i]} {book_list[i+1]}'].append(book_list[i+2])
    return book_dict


def new_story():
    new_list = []
    flat_list = []
    new_story = []
    book_dict = make_dict()
    key_list = book_dict.keys()
    magic_key = random.sample(key_list, 100)
    for keys in magic_key:
        new_list.append(book_dict[keys])
        flat_list = list(itertools.chain(*new_list))
    new_story = list(zip(magic_key, flat_list))
    new_master = list(itertools.chain(*new_story))
    machine_masterpiece = ' '.join(new_master)
    return machine_masterpiece


new_book = new_story()
print(new_book)

new_story()

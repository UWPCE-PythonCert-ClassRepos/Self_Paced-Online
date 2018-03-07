#!/usr/bin/env python3

from collections import defaultdict

# text_import = input("What file would you like to import?:")


def text_import():
    with open("sherlock_small.txt", "r") as book_text:
        book_string = book_text.read().replace('\n', ' ').replace(',', ' ').replace('.', ' ').replace('-', ' ')
        return book_string


def make_dict():
    book_list = text_import().split()
    book_dict = defaultdict(list, {})
    for i in range(len(book_list)-2):
        book_dict[book_list[i] + ' ' + book_list[1+1]].append(book_list[i+2])
    print(book_dict)



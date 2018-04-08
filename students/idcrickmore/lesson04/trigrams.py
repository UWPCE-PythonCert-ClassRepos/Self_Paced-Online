#!/usr/bin/env python3

import random

book_dict = dict()
line_list = list()
word_list = list()
start_pair = set()
trigram = list()
book = 'sherlock.txt'


def read_book(b):
    with open(str(b), 'r') as f:
        # 'line' var get the value of the first line of the book
        # minus the '\n' of every line ([:-1])
        line = f.readline()[:-1]
        # 'line_list' var starts with 'line'
        line_list.append(line)

        # as long as 'line' is True
        # append 'line_list' by reading new lines
        while line:
            line_list.append(f.readline()[:-1])
            # as soon as f.readline() doesn't have a line to read
            # 'line' will be null, and the while loop stops
            line = f.readline()

        # populate word list one line at a time
        for line in line_list:
            words = line.split(' ')
            for word in words:
                word_list.append(word)


def populate_dict():

    for i in range(0, len(word_list)-2):
        # define 'first_word', 'second_word' and 'third_word'
        first_word = word_list[i]
        second_word = word_list[i + 1]
        third_word = word_list[i + 2]

        # combine 'first_word' and 'second_word' to make 'word_key'
        word_key = first_word + " " + second_word

        # if the key_word isn't in the dict, add it
        if word_key not in book_dict:
            book_dict[str(word_key)] = [third_word]

        # otherwise, if check to see if the thrid_word is already
        # associated with the key_word
        # if it isn't, add it
        elif third_word not in book_dict.get(word_key):
            book_dict.get(word_key).append(third_word)


def write_trigram():
    global trigram

    # start trigram list with random word pair
    while len(trigram) < 1:
        trigram.append(random.choice(list(book_dict)))
        trigram = trigram[0].split()

    # build up the 'trigrams' list by using the last two
    # elements as a key in the 'book_dict' dictionary
    # and adding a randomly selected value
    last_two_words = trigram[-2] + " " + trigram[-1]
    while (len(trigram) < 200) and (last_two_words in book_dict):
        last_two_words = trigram[-2] + " " + trigram[-1]
        trigram.append(random.choice(book_dict[last_two_words]))

    # define a string with place holders ("{}") equal in number
    # to the length of the 'trigrams' list
    tri_string = "{} " * len(trigram)
    # then print the string using the 'trigram' list elements
    print(tri_string.format(*trigram))


read_book(book)
populate_dict()
write_trigram()

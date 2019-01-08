#!/usr/bin/env python3
"""
trigram experiment with dict - intake a book as a txt file and output a new story
Author: JohnR
Version: 1.0
Last Update: 1/8/2019
Notes: Requires that you have one or two books as text files in your working directory to choose from.
"""

import re
import random
import os


def main():
    """
    trigram exercise
    :return:
    """
    # get user selection for book to use
    # TODO: get rid of the static variables
    # TODO: eliminate the need to write a tmp file to disk
    print('Choose from the following txt files: ')
    print(os.listdir())
    original_text = input('Enter file name: ')
    tmp_text = 'tmp.txt'

    # munge through the text file and create a clean word list
    clear_non_alpha(original_text)
    word_list = create_list(tmp_text)

    # create a word dictionary and then print a new story
    word_db = create_dict(word_list)
    new_story(word_db)


def clear_non_alpha(input_text):
    """
    Open a text file, strip out any non-alpha numeric characters
    and write to a new file for later use.
    :param input_text: text file to clean
    :return: None - currently write file to disk
    """
    tmp_file = 'tmp.txt'
    old_file = open(input_text).read()
    new_file = re.sub('[^a-zA-Z0-9\n]', ' ', old_file)
    open(tmp_file, 'w').write(new_file)


def create_list(words_text):
    """
    Convert a text file of space separated words into a list
    :param words_text: any txt file
    :return: word list
    """
    with open(words_text, 'r') as f:
        words_list = f.read().split()

    return words_list


def create_dict(list_of_words):
    """
    Create dict based on short text file
    :return: db
    """
    my_dict = {}
    for word in range(len(list_of_words)-2):
        my_key = list_of_words[word] + ' ' + list_of_words[word + 1]
        if my_key not in my_dict.keys():
            my_dict.update({my_key: []})
        my_dict[my_key].append(list_of_words[word + 2])

    return my_dict


def new_story(word_dict):
    """
    Create a new story based on the new word dictionary
    :return: None
    """
    keys = list(word_dict)
    story = []
    # TODO: this works even though 'key' isn't being used; not sure why
    for key in keys:
        n = random.randint(1, len(keys) -1)
        new_key = keys[n]
        story.append(word_dict[new_key][0])

    # TODO: this prints a single line of text, need to use pprint or
    #       similar to create paragraphs with new lines
    print(*story, sep=' ')


if __name__ == '__main__':
    main()
#!/usr/bin/env python3
"""
trigram experiment with dict
Author: JohnR
Version: .2
Date: 1/5/2019
Notes:
"""

import re


def main():
    """
    trigram exercise
    :return:
    """
    # use static variables for now
    original_text = './test.txt'
    new_text = 'tmp.txt'

    # munge through the text file and create a clean word list
    clear_nonalpha(original_text)
    word_list = create_list(new_text)
    print(word_list)

    # TODO: run the new word_list through create_dict


def clear_nonalpha(input_text):
    """
    Open a text file, strip out any non-alpha numeric characters
    and write to a new file for later use.
    :param input_text: text file to clean
    :return: None - currently write file to disk
    """
    clean_file = 'tmp.txt'
    old_file = open(input_text).read()
    new_file = re.sub('[^a-zA-Z0-9\n]', ' ', old_file)
    open(clean_file, 'w').write(new_file)


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
    # create dict using each two word chunk as a key and value
    # consists of lists of following words
    pass


def new_story():
    """
    Create a new story based on the new word dictionary
    :return: None - write results to a file for now
    """
    pass


if __name__ == '__main__':
    main()
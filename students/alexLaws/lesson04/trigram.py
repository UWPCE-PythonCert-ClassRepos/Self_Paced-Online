#!/usr/bin/env python

from random import choice

# Functions


def open_file():
    """Return the text file for analysis"""
    file_to_read = input('What text file do you want to use? ')
    with open(file_to_read, 'r') as f:
        complete_text = f.read()
    return complete_text


def clean_file(text):
    no_carriage = text.replace("\n", " ")
    beginning = no_carriage.find('I.  To Sherlock Holmes she is always THE')
    end = no_carriage.find('End of the Project Gutenberg')
    return no_carriage[beginning:end]


def build_dictionary(word_list):
    """Return dictionary of word pairs and next words"""
    next_word = {}
    for i in range(len(words) - 2):
        word_pair = (words[i], words[i + 1])
        third_word = []
        if word_pair in next_word:
            next_word[word_pair].append(words[i + 2])
        else:
            third_word = [words[i + 2]]
            next_word[word_pair] = third_word
    return next_word


def trigram(search_pair, reference_dict):
    """Build the trigram output"""
    if search_pair in reference_dict:
        word_to_add = choice(reference_dict[search_pair])
        output.append(word_to_add)
        trigram((search_pair[1], word_to_add), reference_dict)


if __name__ == '__main__':
    full_text = open_file()
    prepped_text = clean_file(full_text)
    words = prepped_text.split(" ")
    while words[-1] == '':
        words.pop()
    trigram_dict = build_dictionary(words)
    # Ask the user where to start in the list
    starting_point = int(input("Pick a word to start with "
                               "(Max of {}): ".format(len(words))))
    output = [words[starting_point], words[starting_point + 1]]
    first_pair = (words[starting_point], words[starting_point + 1])
    while True:
        search_pair = (output[-2], output[-1])
        if search_pair in trigram_dict:
            word_to_add = choice(trigram_dict[search_pair])
            output.append(word_to_add)
        else:
            break
    print(" ".join(output).replace('  ', '\n\n'))
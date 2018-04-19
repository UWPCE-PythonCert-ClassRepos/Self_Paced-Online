#!/usr/bin/env python3

import random

def get_text_file():
    """
    Prompts user to for text filename.

    Args: None.
    """
    text_file = input("Plase enter the (text) filename to analyze: ")
    return text_file


def get_sample_size():
    """
    Prompts the user for size of new text sample.

    Args: None.
    """
    sample_size = input("How long (number of words) should the new text sample be: ")
    sample_size = int(sample_size)
    return sample_size


def open_text():
    """
    Opens text file and gets the returns the content.

    Args: None.
    """
    text_source = get_text_file()

    with open(text_source) as file:
        raw_text = file.read()
    return raw_text


def clean_text(raw_text):
    """
    Sanitizes the text by removing punctuation and special characters.

    Args:
    raw_text: Source text from the text file.
    """
    special_characters = ('.', ',', '?', '!', '\n', '\r', '(', ')', '"', "'", '-', ':', ';')
    scrubbed_text = ''

    for char in raw_text:
        if char in special_characters:
            char = ' '
        scrubbed_text += char

    return scrubbed_text 


def text_to_list(scrubbed_text):
    """
    Breaks the text into words and stores the words into a list.

    Args:
    scrubbed_text: Text from file with special characters removed.
    """
    text_words = scrubbed_text.split()
    text_words_list = []

    for word in text_words:
        text_words_list.append(word)

    return text_words_list


def list_to_dict(text_words_list):
    """
    Uses the list of words to build key/value pairs. 

    Args:
    text_words_list: A list of words.
    """
    trigram_dict = {}

    for word in range(len(text_words_list) - 2):
        key_1 = text_words_list[word]
        key_2 = text_words_list[word + 1]
        value = text_words_list[word + 2]
        trigram_dict.setdefault((key_1, key_2), []).append(value)
    return trigram_dict


def create_new_sample(trigram_dict):
    """
    Create a new text sample using the trigram dictionary.

    Args:
    trigram_dict:  Dictionary of trigrams.
    """
    num_words = get_sample_size()
    dict_keys = list(random.choice(list(trigram_dict.keys())))
    sample = dict_keys

    for word in range(num_words):
        dict_keys = random.choice(trigram_dict[tuple(sample[-2:])])
        sample.append(dict_keys)

    sample = ' '.join(sample)
    print()
    print(sample)


# Function calls to execute the process
pure_text = open_text()
cleansed_text = clean_text(pure_text)
word_list = text_to_list(cleansed_text)
trigrams = list_to_dict(word_list)
create_new_sample(trigrams)
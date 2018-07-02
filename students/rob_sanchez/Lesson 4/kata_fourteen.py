#!/usr/bin/env python3
import sys
import collections
import string
import re
import random


def main():
    welcome()


# Reads the contents of text file and returns a list of words
def get_book(name):
    word_list = []
    with open(name, 'r') as book:
        for txt in book:
            txt = re.sub('[-]', ' ', txt)
            raw_text = txt.translate({ord(c): None for c in string.punctuation})
            for item in raw_text.split():
                word_list.append(item.lower())
    return(word_list)


# Builds a dictionary from the list of words extracted from a text file
def build_trigram(in_list):
    new_dict = {}

    for item in range(len(in_list)-1):
        try:
            if (in_list[item], in_list[item+1]) not in new_dict:
                new_dict[in_list[item], in_list[item+1]] = [in_list[item+2]]
            else:
                new_dict[(in_list[item], in_list[item+1])].append(in_list[item+2])
        except IndexError:
            pass
        except KeyError:
            pass

    return new_dict


# Strings words together using the generated trigram and two initial words.
def string_words(word1, word2, name):
    current_words = word1, word2
    output_string = []

    book_dict = build_trigram(get_book(name))
    for i in current_words:
        output_string.append(i)

    # Loop through the dictionary and pick a random word choice based on the mapping
    for i in range(0, 200):
        try:
            last_word = random.choice(book_dict[current_words])
            output_string.append(last_word)
            current_words = output_string[-2], output_string[-1]
        except KeyError:
            pass

    form_string = "{} " * len(output_string)
    print(form_string.format(*output_string))


# Displays the initial welcome prompt
def welcome():

    # User selection
    text = input("Enter name of text file:")
    word1 = input("Enter first word:")
    word2 = input("Enter s word:")

    if(".txt" not in text):
        text = text + ".txt"

    string_words(word1, word2, text)


if __name__ == "__main__":
    main()

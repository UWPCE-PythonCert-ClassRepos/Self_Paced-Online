#!/usr/bin/env python3
import sys
import random

def read_text(file):
    """
    Reads the text from the given input text file into a list of words that were separated by whitespace
    :param file: input text file
    :returns: the list of words
    """
    text = []
    with open(file, 'r') as f:
        while True:
            line = f.readline().strip('\r')
            if not line:
                break
            text.extend(line.split())
    return text

def create_trigrams(words_list):
    """
    Creates a trigrams dictionary based on 2 word keys
    :param words_list: list of words from input file
    :returns: the trigrams created from the words list
    """
    trigrams = dict()
    for i in range(len(words_list)-2):
        key = ' '.join(words_list[i:i+2])
        if key in trigrams:
            trigrams[key].append(words_list[i+2])
        else:
            trigrams[key] = [words_list[i+2]]
    return trigrams

def create_text(trigrams):
    """
    Creates the new text using the supplied trigrams dictionary
    :param trigrams: dictionary of trigrams with two-word keys
    :returns: the new text generated from the trigrams
    """
    new_text = random.choice(list(trigrams.keys())).split(' ')

    while True:
        i = len(new_text)
        key = f"{new_text[i-2]} {new_text[i-1]}"
        if key in trigrams:
            new_text.append(random.choice(trigrams[key]))
        else:
            break
    return new_text

def write_text(out_file, text):
    """
    Writes out the supplied list of words to the given output file
    :param out_file: the file to write to
    :param text: the list of words to write to the output file, a space will be
    inserted between each word
    """
    with open(out_file, 'w') as f:
        for word in text:
            f.write(word)
            f.write(' ')

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: trigrams.py <input-file> <output-file>")
        exit()
    in_file = sys.argv[1]
    out_file = sys.argv[2]

    text = read_text(in_file)
    trigrams = create_trigrams(text)
    updated_text = create_text(trigrams)
    write_text(out_file, updated_text)

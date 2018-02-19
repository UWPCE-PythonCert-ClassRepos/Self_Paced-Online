#!/usr/bin/env python3
"""Trigrams

This module contains all the functions for the Trigrams module.
"""
import os
import pathlib
import string
import random
from collections import defaultdict


REPL_DICT = {punc: '' for punc in string.punctuation}
REPL_DICT['-'] = ' '
TRANS_TABLE = str.maketrans(REPL_DICT)


def create_trigram_dict(file_path):
    """Create a trigram dictionary from the passed text file.

    Args:
        file_path (pathlib.Path): Path to text file.

    Returns:
        dict: Dictionary contain trigram keys & values.
    """
    if not file_path.exists():
        return {}

    tri_dict = defaultdict(list)
    prv_line = ''
    with open(file_path) as corpus:
        for line in corpus:
            line = line.translate(TRANS_TABLE)
            line = f'{" ".join(prv_line.split()[-2:])} {line}'
            words = [word.lower() for word in line.split()]
            prv_line = line
            for i in range(len(words) - 2):
                tri_dict[f'{words[i]} {words[i + 1]}'].append(words[i + 2])

    return tri_dict


def create_trigram_text(tri_dict, max_len):
    """Create a trigram text based upon the passed trigram dictionary.

    Args:
        tri_dict (dict): Trigram dicionary
        max_len (int): Max number of words in trigram returned text

    Returns:
        str: Generated trigram text
    """
    if isinstance(tri_dict, defaultdict):
        tri_dict.default_factory = None

    tri_key = random.choice(list(tri_dict))
    tri_txt = list(tri_key.split())

    while tri_key in tri_dict and len(tri_txt) < max_len:
        tri_txt.append(random.choice(tri_dict[tri_key]))
        tri_key = f'{tri_txt[-2]} {tri_txt[-1]}'

    return ' '.join(tri_txt)


def main():
    """Main function."""
    corpus_path = pathlib.Path(os.path.join(os.getcwd(), 'sherlock.txt'))
    tri_dict = create_trigram_dict(corpus_path)
    tri_text = create_trigram_text(tri_dict, 200)
    print(tri_text)


if __name__ == '__main__':
    main()

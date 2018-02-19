#!/usr/bin/env python3
"""Trigrams

This module contains all the functions for the Trigrams module.
"""
import os
import pathlib
from collections import defaultdict
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


def main():
    """Main function."""
    corpus_path = pathlib.Path(os.path.join(os.getcwd(), 'sherlock.txt'))
    tri_dict = create_trigram_dict(corpus_path)


if __name__ == '__main__':
    main()

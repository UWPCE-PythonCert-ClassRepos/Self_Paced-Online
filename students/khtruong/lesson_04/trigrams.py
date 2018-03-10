#!/usr/bin/env python
from random import randint
import string
import textwrap

"""This module runs the trigrams script.
"""

l = []
d = {}


def process_book(textfile, n):
    """Open book to create key and value dict."""
    create_list(textfile)
    remove_specialchar()
    create_dict(n)
    write_book(textfile, out_line(create_ngrams(n)))


def create_list(textfile):
    """Return list of splitted words from text file."""
    with open(textfile, 'r') as infile:
        # split each line of text and extend into list
        for line in infile:
            temp = line.split(' ')
            l.extend(temp)


def remove_specialchar():
    """Return list of words without special characters and punc"""
    rm = ('\n', '(', ')', '"', '/')
    for word in l:
        l[l.index(word)] = word.translate({ord(c): None for c in rm})


def create_dict(n):
    """Return n-gram dict."""
    for i in range(0, len(l) - n + 1):
        d.setdefault(" ".join(l[i:i + n - 1]), []).append(l[i + n - 1])


def create_ngrams(n):
    """Return n-grams for given text."""
    random = randint(0, len(l))
    ngram_l = l[random:random + n - 1]  # starting point
    while True:
        key = " ".join(ngram_l[- (n - 1):])
        value = d.setdefault(key, "END")
        if value == "END":
            break
        ngram_l.append(value[-1])  # append the last element in value list
        if len(value) > 1:  # shift list to use next value next time
            value.append(value.pop(0))
        ngram_l[0] = ngram_l[0].title()  # capilize first word
    return ngram_l


def out_line(ngram_l):
    """Return list out line to write to file"""
    outstr = ''
    for word in ngram_l:
        outstr = ''.join([outstr, word, ' '])
    return outstr


def write_book(textfile, outstr):
    """Write ngram to text file"""
    out = textfile.replace('.txt', '_out.txt')
    with open(out, 'w') as outfile:
        outfile.write(textwrap.fill(outstr, 79))

if __name__ == '__main__':
    process_book("sherlock_small.txt", 3)

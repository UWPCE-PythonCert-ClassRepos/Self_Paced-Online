#!/usr/bin/env python

"""This module runs the trigrams script.
"""

text = ('I wish I may I wish I might')


def create_ngrams(text, n):
    """Return n-grams for given text."""
    d = create_dict(text, n)    
    word_list = ["I", "may"]  # starting two words
    while True:
        key = " ".join(word_list[-2:])
        value = d.setdefault(key, "END")
        if value == "END":
            break
        word_list.append(value[0])
        if len(value) > 1:  # shift list to use next value next time
            value.append(value.pop(0))
    return " ".join(word_list[:])


def create_dict(text, n):
    """Return n-gram dict."""
    splittext = text.split(' ')
    ngram_dict = {}
    for i in range(0, len(splittext) - n + 1):
        ngram_dict.setdefault(" ".join([splittext[i], splittext[i + 1]]), []
                              ).append(splittext[i + 2])
    return ngram_dict





if __name__ == '__main__':
    print(create_ngrams(text, 3))

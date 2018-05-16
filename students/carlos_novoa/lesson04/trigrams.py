#!/usr/bin/env python3

import os
import re
from collections import defaultdict

"""
Lesson4 - Kata Fourteen: Tom Swift Under Milk Wood
"""


def get_content(file_name):
    cwd = os.getcwd()
    path = os.path.join(cwd, file_name)
    with open(path, 'r') as f:
        content = f.read()
        return content


def pre_process(c):
    c = re.sub('[(),;:"]', r'', c)
    c = re.sub('([-])+', ' ', c)
    c = ' '.join(c.split()).lower()
    return c


def post_process(c):
    c = c.capitalize()
    c = re.sub('([.!?]\\s+[a-z])', lambda x: x.group(1).upper(), c)
    c = c.strip()
    return c


def make_ngrams(words, n):
    return [list(x) for x in zip(*[words[i:] for i in range(n)])]


def ngram_freqs(ngrams, words):
    """ Choose best next word """
    cfd = defaultdict(lambda: defaultdict(lambda: 0))
    for i in range(len(words) - 2):
        cfd[(words[i], words[i + 1])][words[i + 2]] += 1
    return {k: dict(v) for k, v in dict(cfd).items()}


def make_dictionary(words, best):
    word_dict = {}
    for i in range(len(words) - 2):
        key_pair = (words[i], words[i + 1])
        if key_pair not in word_dict:
            word_dict[key_pair] = max(best[key_pair])
    return word_dict


def generate_text(word_count=200, N=3, start_pair=None):
    content = get_content('sherlock.txt')
    content = pre_process(content)
    words = content.split(" ")
    ngrams = make_ngrams(words, N)
    best = ngram_freqs(ngrams, words)
    word_dict = make_dictionary(words, best)
    wc = word_count if word_count <= len(words) else len(words)
    if start_pair is not None:
        start_pair = start_pair.lower()
        key_pair = (start_pair.split(" ")[0], start_pair.split(" ")[1])
    else:
        key_pair = (words[0], words[1])
    story = "{} {} ".format(key_pair[0], key_pair[1])
    i = 2  # starting words
    while i < wc:
        if key_pair in word_dict:
            next_word = word_dict[key_pair]
            story += "{} ".format(next_word)
            key_pair = (key_pair[1], next_word)
            i += 1
        else:
            break
    story = post_process(story)
    print(story)


if __name__ == '__main__':
    start_point = input('Choose a word pair (string) as a starting point: ')
    word_count = int(input('Number of words to generate: '))
    generate_text(word_count, 3, start_point)

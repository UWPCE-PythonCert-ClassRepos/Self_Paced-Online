#!/usr/bin/env python3

import random

def make_words(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    header_size = 0
    for ind, line in enumerate(lines):
        if line.startswith("*** START OF"):
            header_size = ind
        if line.startswith("End of the Project Gutenberg"):
            footer_ind = ind
            break
    data = lines[header_size+1:footer_ind]
    text = " ".join(data)
    f.close()
    return text.split()

def build_trigrams(words, max=10000):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    count = min(len(words)-2, max)
    trigrams = {}
    for i in range(count):
        pair = (words[i], words[i+1])
        follower = words[i+2]
        if pair in trigrams.keys():
            trigrams[pair].append(follower)
        else:
            trigrams[pair] = [follower]
    return trigrams

def build_text(trigram, max=200, seed=['I',  'wish']):
    output = seed
    i = 0
    while i<max:
        i = i+1
        pair = (output[-2], output[-1])
        if pair in trigram.keys():
            follower = random.choice(trigram[pair])
        else:
            follower = list(random.choice(list(trigram.keys())))
        output.append(follower)
    output_text = " ".join(output)
    return output_text

if __name__ == "__main__":
    filename = input("Please enter filename for generating trigrams: ")

    words = make_words(filename)
    trigrams = build_trigrams(words)
    new_text = build_text(trigrams, max=300, seed=list(random.choice(list(trigrams.keys()))))
    print(new_text)
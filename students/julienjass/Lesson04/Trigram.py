#!/usr/bin/env python3

import random
import sys

def extract_words(filename):
    with open(filename) as infile:
        words = []
        for line in infile:
            if line.startswith("End of the Project Gutenberg"):
                break
            for char in ['/', '\\', '.', ',', '(', ')', ':', ';', '"', '?', '!', '-', '\'']:
                line = line.replace(char, '')
            words.extend(line.split())
    return words

def build_trigram(words):
    trig = {}
    for i in range(len(words) - 2):
        first = words[i]
        second = words[i + 1]
        third = words[i + 2]
        pair = (first, second)
        trig.setdefault(pair, []).append(third)
    return trig

def create_new_text(trigram):
    pair = random.choice(list(trigram.keys()))
    sentence = []
    sentence.extend(pair)
    for i in range(30):
        followers = trigram[pair]
        sentence.append(random.choice(followers))
        pair = tuple(sentence[-2:])
    result = ' '.join(sentence).capitalize().replace(' i ', ' I ')+"."
    return result

if __name__ == "__main__":
    all_words = extract_words("sherlock.txt")
    trigram = build_trigram(all_words)
    generated_text = create_new_text(trigram)
    print(generated_text)
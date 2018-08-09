#!/usr/bin/env python3
import random


def all_words():
    all_words = []
    text = 'great_expectations.txt'

    with open(text, 'r') as f:
        for item in f:
            words = item.split()
            for word in words:
                word = word.lower()
                word = word.replace(',', '')
                word = word.replace('.', '')
                word = word.replace('?', '')
                word = word.replace('!', '')
                word = word.replace('-', '')
                word = word.replace(' i ', ' qwerty ')
                if word == 'i':
                    word = 'I'
                all_words.append(word)
        return all_words

def make_trigram():
    words = all_words()
    d = dict()
    for i in range(len(words) - 2):
        key = tuple(words[i:i+2])
        value = words[i+2]
        d.setdefault(key, []).append(value)
    return d

def make_a_sentence():
    foo = make_trigram()
    story = []
    sentence = (random.choice(list(foo.keys())))
    for i in range(random.randint(6,16)):
        pair = sentence[-2:]
        sentence2 = list(sentence)
        sentence2.append(random.choice(foo[pair]))
        sentence = tuple(sentence2)
    sentence = " ".join(sentence)
    print(sentence[0].capitalize() + sentence[1:] + ".", end=' ') #WOW This is ugly, but it works ... isn't that what real developers say?

for i in range(int(input("How many sentences would you like me to create? "))):
    make_a_sentence()
print("\n")
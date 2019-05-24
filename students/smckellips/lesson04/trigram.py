#! /usr/bin/env python
import string

example_text = "I wish I may I wish I might"

def load_file(file):
    # TODO: Strip not text, ie TOC, Intros, title lines, etc.
    with open(file, 'r') as f:
        text = f.read().replace('\n', ' ')
    return text

def remove_punctuation(text):
    return text.translate(str.maketrans(string.punctuation, ' '*len(string.punctuation))).lower()


def build_trigram(text):
    
    words = text.split()
    word_dict = {}

    for i in range(len(words) - 2):
        key = (words[i],words[i+1])
        word_dict.setdefault(key,[]).append(words[i+2])
    return word_dict

if __name__ == "__main__":
    # file = './students/smckellips/lesson04/sherlock_small.txt'
    file = './students/smckellips/lesson04/sherlock.txt'
    trigram = build_trigram(remove_punctuation(load_file(file)))    

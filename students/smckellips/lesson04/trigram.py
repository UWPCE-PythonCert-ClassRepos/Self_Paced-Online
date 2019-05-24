#! /usr/bin/env python

example_text = "I wish I may I wish I might"


def build_trigram(text):
    words = text.split()
    word_dict = {}

    for i in range(len(words) - 2):
        key = "{} {}".format(words[i],words[i+1])
        word_dict.setdefault(key,[]).append(words[i+2])
    return word_dict

if __name__ == "__main__":
    trigram = build_trigram(example_text)    
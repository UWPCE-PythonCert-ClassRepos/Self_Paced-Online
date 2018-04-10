#!/usr/bin/python
import os
import random


def openfile(file):
    text_ = []
    f = open(file)
    for word in f.read().split():
        text_.append(word)
    for i, word in enumerate(text_):
        if "." in word:
            text_[i] = word.replace(".", "")
        if "," in word:
            text_[i] = word.replace(",", "")
        if "(" in word:
            text_[i] = word.replace("(", "")
        if ")" in word:
            text_[i] = word.replace(")", "")
    return text_


def create_dict(data):
    trigram_dict_ = {}
    for i in range(0, len(data) - 2):
        trigram_dict_[(data[i], data[i+1])] = data[i+2]
    return trigram_dict_


if __name__ == '__main__':

    file_path = os.path.dirname(__file__)
    filename = file_path + '/sherlock_small.txt'

    text = openfile(filename)
    trigram_dict = create_dict(text)

    first_word_in = random.randint(0, len(text)-1)
    first_word = text[first_word_in]
    second_word = text[first_word_in + 1]


    def create_story(first_, second_, story_, dict_=trigram_dict):
        if (first_, second_) in dict_:
            story_.append(dict_[first_, second_])
            if len(story_) == 1:
                create_story(second_, story_[0], story_)
            else:
                create_story(story_[-2], story_[-1], story_)
        return story_

    story__ = []
    story = create_story(first_word, second_word, story__, trigram_dict)
    print(' '.join(story))

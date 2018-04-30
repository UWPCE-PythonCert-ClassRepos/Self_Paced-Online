#!/usr/bin/env python3

from random import choice
# Text processing


def prep_text(text_name):
    """open file, read text, strip  characters, and split into words """
    with open(text_name, 'r') as fin:
        text_file = fin.read()
        text_file = text_file.replace(',', '').replace('\n', ' ').strip()
        text_file = text_file.replace(';', '').replace(':', '')
        word_list = text_file.replace('.', '').replace('_', '').split()
    return(word_list)


def trigrams(word_list):
    """form tuples of trigrams and enter them as key-val pairs in dictionary"""
    tri_dict = {}
    for index in range(len(word_list) - 2):
        tpl = tuple(word_list[index:index + 3])
        key = tpl[0:2]
        val = tpl[2]
        if key in tri_dict:
            tri_dict.setdefault(key, [])
            tri_dict[key].append(val)
        else:
            tri_dict.update({key: [val]})
    return(tri_dict)


def new_text(tri_dict):
    """generate random starter and alternative keys, append key and val to new
     text, with random choice of value for all keys with multiple values"""
    new_text = []
    random_key = choice(list(tri_dict.keys()))
    new_text.append(random_key[0])
    new_text.append(random_key[1])
    for n in range(250):
        try:
            new_text.append(choice(tri_dict[(new_text[-2], new_text[-1])]))
        except KeyError:
            alt_key = choice(list(tri_dict.keys()))
            new_text.append(alt_key[0])
            new_text.append(alt_key[1])
    print(new_text)


def epic_poem_format(new_text):
    """arrange text in 8-word verse lines with initial capitals"""
    pass


def main():
    """generate the trigram dictionary then used to derive new text """
    text_name = './Milton_sample.txt'
    word_list = prep_text(text_name)
    tri_dict = trigrams(word_list)
    new_text(tri_dict)


if __name__ == "__main__":
    main()

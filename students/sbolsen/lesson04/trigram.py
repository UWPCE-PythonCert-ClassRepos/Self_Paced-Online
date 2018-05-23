#!/usr/bin/env python3

import random

def read_file():
    with open('text.txt', 'r') as fp:
        split_text = fp.read().split()
        return split_text


def create_new_file(split_text):
    new_dict = {}
    for item in range(0, len(split_text)-2):
        new_dict.setdefault('{} {}'.format(split_text[item], split_text[item+1]), [])
        new_dict['{} {}'.format(split_text[item], split_text[item+1])].append('{}'.format(split_text[item+2]))
        chapter = random.choice(list(new_dict)).split()
    try:
        while True:
            for word in range(0, len(chapter)-1):
                chapter.append(random.choice(new_dict[' '.join(chapter[-2:])]))
    except KeyError:
        with open('new_chapter.txt', 'w') as newfp:
            newfp.write(' '.join(chapter))


def main():
    a = read_file()
    create_new_file(a)

if __name__ == '__main__':
    main()

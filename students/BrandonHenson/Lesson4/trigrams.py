#!/usr/bin/env python3
# Brandon Henson
# 4/16/18
# Lesson04
# Trigram

import random
tridict = {}
list1 = []


def readdata():
    with open('./s.txt', 'r') as fileobj:
        read_data = fileobj.read()
        words = read_data.replace('\n', ' ').replace('--', ' ')\
            .replace('!', ' ').replace("'", ' ')\
            .replace(',', ' ').replace('.', ' ').replace('  ', ' ').split(' ')
        for word in words:
            if not word == '':
                list1.append(word)
    inlist()


def inlist():
    for x, y in enumerate(list1):
        if x < len(list1) - 3:
            first = y
            second = list1[x + 1]
            key = (first, second)
            if key not in tridict:
                tridict[key] = [list1[x + 2]]
            else:
                tridict[key].append(list1[x + 2])
    print(tridict)

if __name__ == '__main__':
    readdata()

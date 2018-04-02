#!/usr/bin/env python3

trigram = {}
collection = []

with open('./sherlock_small.txt', 'r') as f:
    read_data = f.read()
    split_words = read_data.replace('\n', ' ').split(' ')
    for word in split_words:
        if not word == '':
            collection.append(word.translate({ord(c): None for c in '()'}))

for i, el in enumerate(collection):
    if i < len(collection) - 3:
        first = el
        second = collection[i + 1]
        key = (first, second)
        if key not in trigram:
            trigram[key] = [collection[i + 2]]
        else:
            trigram[key].append(collection[i + 2])

print(trigram)

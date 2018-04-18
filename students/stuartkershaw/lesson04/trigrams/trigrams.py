#!/usr/bin/env python3

import random
from collections import defaultdict

collection = []
trigram = defaultdict(list)

with open('./sherlock_small.txt', 'r') as f:
    read_data = f.read()
    for el in ['\n', '--']:
        read_data = read_data.replace(el, ' ')
    split_words = read_data.split(' ')
    for word in split_words:
        if not word == '':
            collection.append(word.translate({ord(c): None for c in '()'}))

for i, el in enumerate(collection):
    if i < len(collection) - 3:
        first = el
        second = collection[i + 1]
        key = (first, second)
        trigram[' '.join(key)].append(collection[i + 2])

random_story = []
random_start = random.randint(0, len(collection) - 1)

while random_start <= len(collection) - 3:
    random_key = (collection[random_start], collection[random_start + 1])
    random_value = trigram.get(' '.join(random_key))
    if random_value is not None:
        random_story.append(random_value[0])
    random_start += 2

print(' '.join(random_story) + '.')

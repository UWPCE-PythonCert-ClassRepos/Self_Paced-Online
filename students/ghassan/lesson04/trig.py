#!/usr/bin/env python3

import random
from pprint import pprint

with open('data.txt', 'r') as datafh:
    data = datafh.read().split()


z = {}


for item in range(0, len(data)-2):
    z.setdefault('{} {}'.format(data[item], data[item+1]), [])
    z['{} {}'.format(
        data[item], data[item+1])].append('{}'.format(data[item+2]))

key = random.choice(list(z))


new_file = key.split()


try:
    while True:
        for word in range(0, len(new_file)-1):
            new_file.append(random.choice(z[' '.join(new_file[-2:])]))
except KeyError:
    with open('new_book.txt', 'w') as newfh:
        newfh.write(' '.join(new_file))

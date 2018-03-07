#!/usr/bin/env python3

from pprint import pprint

with open('data.txt', 'r') as datafh:
    data = datafh.read().split()

z = {}


for item in range(0, len(data)-2):
    z.setdefault('{} {}'.format(data[item], data[item+1]), [])
    z['{} {}'.format(
        data[item], data[item+1])].append('{}'.format(data[item+2]))

key = 'I should'

new_file = [x for x in key.split()]


try:
    while True:
        for word in range(0, len(new_file)-1):
            for y in z[' '.join(new_file[:])]:
                new_file.append(y)
            print(new_file)
except KeyError:
    with open('new_book.txt', 'w') as newfh:
        newfh.write(' '.join(new_file))

#!/usr/bin/env python3

from pprint import pprint

with open('data.txt', 'r') as datafh:
    data = datafh.read().split()

z = {}


for item in range(0, len(data)-2):
    z.setdefault('{} {}'.format(data[item], data[item+1]), [])
    z['{} {}'.format(data[item], data[item+1])].append('{}'.format(data[item+2]))

pprint(z)



#!/usr/bin/env python3

import pathlib

d = {
    "name": "Chris",
    "city": "Seattle",
    "cake": "Chocolate"
}

print(d)

del d['cake']

print(d)

d['fruit'] = 'Mango'

print(d)

for key in d:
    print(key)

for key, value in d.items():
    print(value)

print('cake' in d)
print('Mango' in d.values())

d_with_ts = {}

for key, value in d.items():
    d_with_ts[key] = value.lower().count('t')

print(d_with_ts)

s2 = set(range(0, 21, 2))
s3 = set(range(0, 21, 3))
s4 = set(range(0, 21, 4))

print(s2, s3, s4)

print(s3.issubset(s4))
print(s4.issubset(s2))

py_set = set(list('Python'))

print(py_set)

py_set.add('i')

print(py_set)

m_set = frozenset(list('marathon'))

print(m_set)

print(py_set.union(m_set))
print(py_set.intersection(m_set))

pth = pathlib.Path('./')

for f in pth.iterdir():
    print(f)

with open('./house.bmp', 'rb') as infile, \
 open('./house_copy.bmp', 'wb') as outfile:
    outfile.write(infile.read())

with open('./dict_lab.py', 'rb') as infile, \
 open('./dict_lab_copy.py', 'wb') as outfile:
    outfile.write(infile.read())

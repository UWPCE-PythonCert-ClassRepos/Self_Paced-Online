#!/usr/bin/env python3
"""
File Name: dict_lab.py
Author: Travis Brackney
Class: Python 201 - Self paced online
Date Created 4/17/2018
Python Version: 3.6.4
"""

# Dictonaries 1
d1 = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
print(d1)

# Remove cake
d1.pop('cake')
print(d1)

# Add Fruit
d1['fruit'] = 'Mango'
print(d1)

# Print keys
for x in d1:
    print(x)

# Print Values
for i in d1.values():
    print(i)

print('cake' in d1.items())
print('Mango' in d1.values())

# Dictonaries 2
d2 = {}
for x, y in d1.items():
    d2[x] = y.lower().count('t')
print(d2)

# Sets 1
s1 = set(range(21))

s2 = set()
for i in s1:
    if i % 2 == 0:
        s2.update([i])

s3 = set()
for i in s1:
    if i % 3 == 0:
        s3.update([i])

s4 = set()
for i in s1:
    if i % 4 == 0:
        s4.update([i])
print('s2')
print(s2)
print('s3')
print(s3)
print('s4')
print(s4)

print('S3 is a subset of S2')
print(s3.issubset(s2))

print('S4 is a subset of S2')
print(s4.issubset(s2))

# Sets 2
s2_1 = set('python')
s2_1.add('i')
fs = frozenset('marathon')
print(s2_1.intersection(fs))
print(s2_1.union(fs))

#!/usr/bin/env python3

### Dictionaries 1 ###
print("*" * 5 + " Dictionaries 1 " + "*" * 5)
d = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
print(d)

d.pop('cake')
print(d)

d['fruit'] = 'Mango'
print(d)

print(d.keys())
print(d.values())

print("Is 'cake' a key in the dictionary?", 'cake' in d)
print("Is 'Mango' a value in the dictionary?", 'Mango' in d.values())
print()

### Dictionaries 2 ###
print("*" * 5 + " Dictionaries 2 " + "*" * 5)
print("Dictionary from part 1:", d)
for key in d.keys():
    d[key] = d.get(key).lower().count('t')

print("How many 't's in each value:", d)
print()

### Sets 1 ###
print("*" * 5 + " Sets 1 " + "*" * 5)
s2, s3, s4 = set(), set(), set()

for i in range(21):
    if i % 2 == 0:
        s2.add(i)
for i in range(21):
    if i % 3 == 0:
        s3.add(i)
for i in range(21):
    if i % 4 == 0:
        s4.add(i)

print("s2:", s2)
print("s3:", s3)
print("s4:", s4)
print()

print("Is s3 a subset of s2?", s3.issubset(s2))
print("Is s4 a subset of s2?", s4.issubset(s2))
print()

### Sets 2 ###
print("*" * 5 + " Sets 2 " + "*" * 5)
py_set = set()
marathon_set = set()
str_1 = "Python"
str_2 = "marathon"

for c in str_1:
    py_set.add(c)
py_set.add('i')

for c in str_2:
    marathon_set.add(c)
frozen_marathon_set = frozenset(marathon_set)

print("Python set:", py_set)
print("Frozen marathon set:", frozen_marathon_set)
print("Union of two sets:", py_set.union(frozen_marathon_set))
print("Intersection of two sets:", py_set.intersection(frozen_marathon_set))

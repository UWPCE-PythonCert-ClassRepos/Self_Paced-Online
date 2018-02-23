#!/usr/bin/env python3

import os

# Dictionaries 1
'''
person = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
print(person)
person.pop('cake')
person['fruit'] = 'Mango'
print(person)

print(person.keys())
print(person.values())
print('cake' in person)
print('Mango' in person.values())

# Dictionaries 2

num_Ts = {}
for i in person:
    num_Ts[i] = person[i].lower().count('t')

print(num_Ts)

# Sets 1

s2 = set(filter(lambda x: x % 2 == 0, range(21)))
s3 = set(filter(lambda x: x % 3 == 0, range(21)))
s4 = set(filter(lambda x: x % 4 == 0, range(21)))

print(s2)
print(s3)
print(s4)

print(s3.issubset(s2))
print(s4.issubset(s2))

# Sets 2

char_Set = set("python")
char_Set.add("i")
print(char_Set)

froz_set = frozenset("marathon")
print(froz_set)

print(char_Set.union(froz_set))
print(char_Set.intersection(froz_set))

# File Practice

'''
def print_dir():
    for i in os.listdir():
        print(i)


def copy_file(file, dest=None):
    buffer = 256
    copy = "{}\{}_copy{}".format(dest, file[:-4], file[-4:])
    f = open(file, 'rb')
    j = open(copy, 'wb')
    while True:
        temp = f.read(buffer)
        if len(temp) > 0:
            j.write(temp)
        else:
            break
    j.close()
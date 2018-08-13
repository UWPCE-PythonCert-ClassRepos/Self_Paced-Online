#!/usr/bin/env python3
"""Dictionary and sets exercises."""


# region dictionaries 1
# create a dictionary
dict1 = {'name' : 'Chris', 'city' : 'Seattle', 'cake' : "Chocolate"}

# print dictioanry
print("{name} from {city} who likes {cake}".format(**dict1))
print()

# delete the entry for cake
dict1.pop('cake')
print()

# print the dictionary again
for k in dict1:
    print("{} : {}".format(k, dict1[k]))
print()

# add fruit:Mango and display the dictionary
dict1['fruit'] = 'Mango'
print(dict1.items())
print()

# display the dictionary keys
print(dict1.keys())
print()

# display the dictionary values
print( dict1.values())
print()

# check if cake is in the dictionary
print('cake' in dict1)
print()

# check if Mango is one of the values
print('Mango' in dict1.values())
print()
# endregion


# region dictionaries 2

dict2 = dict()
for k in dict1:
    if k not in dict2:
        dict2[k] = dict1[k].lower().count('t')
print(dict2.items())
print()
# endregion


# region set1
# create a set of numbers divisible by 2, 3 or 4 up to 20
s2 = set()
s3 = set()
s4 = set()
for i in range(21):
    if i % 2 == 0:
        s2.add(i)
    if i % 3 == 0:
        s3.add(i)
    if i % 4 == 0:
        s4.add(i)
print(s2)
print(s3)
print(s4)

# print if subsets
print(s3.issubset(s2))
print(s4.issubset(s2))
print()
# endregion

# region sets2
# create a set from Python string then add a i to it
set_python = set()
string_python = 'Python'
for s in string_python:
    set_python.add(s)
print(set_python)
set_python.add('i')
print(set_python)
print()

# implementation of a set out of string and immutable sets
str4  = 'marathon'
set4 = set()
for c in str4:
    set4.add(c)
print(set4)
set4_frozenset = frozenset(set4)
print(set4_frozenset)

# print the union and intersection of the last 2 sets
union_set = set4 | set_python
print('Union set: {}'.format(union_set))
intersection_set = set4 & set_python
print('Intersection set: {}'.format(intersection_set))
# endregion


if __name__ == '__main__':
    print()

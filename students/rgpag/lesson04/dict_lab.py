#!/usr/bin/env python3
import os

# Activity 1: Dictionary and Set Lab
# Dictionary1
"""
Create a dictionary containing “name”, “city”, and “cake” for “Chris” from\
“Seattle” who likes “Chocolate” (so the keys should be: “name”, etc, and\
values: “Chris”, etc.)
Display the dictionary.
Delete the entry for “cake”.
Display the dictionary.
Add an entry for “fruit” with “Mango” and display the dictionary.
Display the dictionary keys.
Display the dictionary values.
Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
Display whether or not “Mango” is a value in the dictionary (i.e. True).
"""

dict1 = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
print(dict1)
del dict1['cake']
print(dict1)
dict1['fruit'] = 'Mango'
print(dict1)
print(dict1.keys())
print(dict1.values())
print('cake' in dict1)
print('Mango' in dict1.values())


# Dictionary2
"""
Using the dictionary from item 1: Make a dictionary using the same keys but\
with the number of ‘t’s in each value as the value (consider upper and lower\
case?).
"""
dict2 = dict1.copy()
for i in dict2.keys():
    val = dict2.get(i).lower()
    t = val.count('t')
    dict2[i] = t
print(dict2)

# Sets1
"""
Create sets s2, s3 and s4 that contain numbers from zero through twenty, \
divisible by 2, 3 and 4.

Display the sets.
Display if s3 is a subset of s2 (False)
and if s4 is a subset of s2 (True).
"""
s2 = set()
for i in range(21):
    if i % 2 == 0:
        s2.update([i])

s3 = set()
for i in range(21):
    if i % 3 == 0:
        s3.update([i])

s4 = set()
for i in range(21):
    if i % 4 == 0:
        s4.update([i])

print(s2, s3, s4)
print(s3.issubset(s2))
print(s4.issubset(s2))


# Sets2
py_set = set()
for i in ('Python'):
    py_set.update([i])
py_set.update(['i'])

print(py_set)

fs_marathon = frozenset('marathon')
print(fs_marathon)
print(py_set.union(fs_marathon))
print(py_set.intersection(fs_marathon))

# Activity 2: File Lab
"""
Write a program which prints the full path for all files in the current\
directory, one per line

Write a program which copies a file from a source, to a destination (without\
using shutil, or the OS copy command).

Advanced: make it work for any size file: i.e. don’t read the entire contents\
of the file into memory at once.
This should work for any kind of file, so you need to open the files in binary\
 mode: open(filename, 'rb') (or 'wb' for writing). Note that for binary files,\
  you can’t use readline() – lines don’t have any meaning for binary files.

Test it with both text and binary files (maybe jpeg or something of your \
chosing).
"""

for i in (os.listdir()):
    print(os.path.realpath(i))


def cp(source, destination):
    source_basename = os.path.basename(source)
    copy_file = open(source)
    new_file = copy_file.read()
    copy_file.close()
    os.chdir(destination)
    paste_file = open(source_basename, 'w')
    paste_file.write(new_file)
    paste_file.close()

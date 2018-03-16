#!/usr/bin/env python3
#########################Dictionaries 1#########################################
#Create a dictionary containing “name”, “city”, and “cake” for “Chris” from
#“Seattle” who likes “Chocolate” (so the keys should be: “name”, etc,
#and values: “Chris”, etc.)
d = {}
d['name'] = 'Chris'
d['city'] = 'Seattle'
d['cake'] = 'Chocolate'
#Display the dictionary.
print(d)
#Delete the entry for “cake”.
del d['cake']
#Display the dictionary.
print(d)
#Add an entry for “fruit” with “Mango” and display the dictionary.
d['fruit'] = 'Mango'
print(d)
#Display the dictionary keys.
print(d.keys())
#Display the dictionary values.
print(d.values())
#Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
print('cake' in d.keys())
#Display whether or not “Mango” is a value in the dictionary (i.e. True).
print('Mango' in d.values())

#########################Dictionaries 2#########################################
"""Using the dictionary from item 1: Make a dictionary using the same keys
but with the number of ‘t’s in each value as the value (consider upper and lower case?)."""
d2 = {}
for value in d.values():
    d2[value] = value.lower().count('t')
print(d2)

#########################Sets 1#################################################
"""Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible by 2, 3 and 4."""
s2 = set()
s3 = set()
s4 = set()

for num in range(21):
    if num%2 == 0:
        s2.add(num)
    if num%3 == 0:
        s3.add(num)
    if num%4 == 0:
        s4.add(num)
"""Display the sets."""
print(s2)
print(s3)
print(s4)
"""Display if s3 is a subset of s2 (False)"""
print(s3.issubset(s2))
"""and if s4 is a subset of s2 (True)."""
print(s4.issubset(s2))

#########################Sets 2#################################################
"""Create a set with the letters in ‘Python’ and add ‘i’ to the set."""
set1 = set("Python")
set1.add("i")
print(set1)
"""Create a frozenset with the letters in ‘marathon’."""
set2 = frozenset("marathon")
print(set2)
"""display the union and intersection of the two sets."""
print(set1.union(set2))
print(set1.intersection(set2))

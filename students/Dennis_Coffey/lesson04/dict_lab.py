# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 21:06:45 2018

@author: denni
"""

#Dictionaries 1
#Create a dictionary containing “name”, “city”, and “cake” for “Chris” from “Seattle” who likes “Chocolate” (so the keys should be: “name”, etc, and values: “Chris”, etc.)
#Display the dictionary.
dict1 = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
print('Print full dictionary')
print(dict1)

#Delete the entry for “cake”.
#Display the dictionary.
dict1.pop('cake')
print('\nPrint dictionary after removing cake entry')
print(dict1)

#Add an entry for “fruit” with “Mango” and display the dictionary. 
dict1['fruit'] = 'Mango'
print('\nPrint dictionary after adding fruit with Mango')
print(dict1)

#Display the dictionary keys.
print('\nPrint the dictionary keys')
print(dict1.keys())

#Display the dictionary values.
print('\nPrint the dictionary values')
print(dict1.values())

#Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
print(f'\nCake is a key in the dictionary? ')
print('cake' in dict1.keys())

#Display whether or not “Mango” is a value in the dictionary (i.e. True).
print(f'\nMango is a value in the dictionary? ')
print('Mango' in dict1.values())


#Dictionaries 2
#Using the dictionary from item 1: Make a dictionary using the same keys 
#but with the number of ‘t’s in each value as the value (consider upper and lower case?).
for item in dict1.keys():
    dict1[item] = dict1[item].lower().count('t')
print(f'\nDictionary with value as number of t')
print(dict1)
    
#Sets 1
#Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible by 2, 3 and 4.
#Display the sets.
#Display if s3 is a subset of s2 (False)
#and if s4 is a subset of s2 (True).

#Function to create set within range defined by start and stop, incremented by passed value
def create_sets(start,stop,increment):
    set1 = set()
    for i in range(stop+1):
        if i%increment == 0:
            set1.update([i])
    return set1

s1 = create_sets(0,20,1)
s2 = create_sets(0,20,2)
print(f'\nDisplay s2, set that is divisible by 2')
print(s2)
s3 = create_sets(0,20,3)
print(f'\nDisplay s3, set that is divisible by 3')
print(s3)
s4 = create_sets(0,20,4)
print(f'\nDisplay s4, set that is divisible by 4')
print(s4)

print(f'\nIs s3 a subset of s2?')
print(s3.issubset(s2))

print(f'\nIs s4 a subset of s2?')
print(s4.issubset(s2))


#Sets 2
#Create a set with the letters in ‘Python’ and add ‘i’ to the set.
#Create a frozenset with the letters in ‘marathon’.
#display the union and intersection of the two sets.
s5 = set(['P','y','t','h','o','n'])
s5.update(['i'])
print(s5)
fs1 = frozenset(('m','a','r','a','t','h','o','n'))
print(f'\nThe union of s5 and fs1')
print(s5.union(fs1))
print(f'\nThe intersection of s5 and fs1')
print(s5.intersection(fs1))


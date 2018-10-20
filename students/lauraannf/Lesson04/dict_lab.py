# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 09:55:33 2018

@author: Laura.Fiorentino
"""

dictionary_one = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
print('Dictionary One: {}'.format(dictionary_one))
print()
print('Delete the entry for cake:')
dictionary_one.pop('cake')
print('Dictionary One: {}'.format(dictionary_one))
print()
print('Add fruit:')
dictionary_one['fruit'] = 'Mango'
print('Dictionary One: {}'.format(dictionary_one))
print()
print(('dictionary_one keys: ') + ('{} '*len(dictionary_one)).format
      (*dictionary_one.keys()))
print(('dictionary_one values: ') + ('{} '*len(dictionary_one)).format
      (*dictionary_one.values()))
print()
print('Is cake a key in dictionary_one?')
print('cake' in dictionary_one)
print()
print('Is Mango a value?')
print('Mango' in dictionary_one.values())
print()
dictionary_two = dictionary_one.copy()
print('Dictionary Two: {}'.format(dictionary_two))
for it in dictionary_two:
    dictionary_two[it] = dictionary_two[it].count('t')
print()
print('Replace dicitonary_two values with the number of t''s in the value')
print('Dictionary Two: {}'.format(dictionary_two))
print()
print('Sets One')
print('Create sets s2,s3,s4 that contain numbers 0-20, divisible by 2,3,4')
s2 = set()
s3 = set()
s4 = set()
for it in range(21):
    if it % 2 == 0:
        s2.update([it])
    if it % 3 == 0:
        s3.update([it])
    if it % 4 == 0:
        s4.update([it])
print('s1: {}, s2: {}, s3: {}'.format(s2, s3, s4))
print()
print('Is s3 a subset of s2?')
print(s3.issubset(s2))
print()
print('Is s4 a subset of s2?')
print(s4.issubset(s2))
print()
print('Sets Two')
print('Set with the letters in Python')
python_set = set('Python')
print('python set: {}'.format(python_set))
print()
print('add i')
python_set.add('i')
print('python set: {}'.format(python_set))
print()
print('Frozenset marathon')
marathon_set = frozenset(('marathon'))
print('marathon set: {}'.format(marathon_set))
print()
print('Union of python and marathon sets')
print(python_set.union(marathon_set))
print()
print('Intersection of python and marathon sets')
print(python_set.intersection(marathon_set))

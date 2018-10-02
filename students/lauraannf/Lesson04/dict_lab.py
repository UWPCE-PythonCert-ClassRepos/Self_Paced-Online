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

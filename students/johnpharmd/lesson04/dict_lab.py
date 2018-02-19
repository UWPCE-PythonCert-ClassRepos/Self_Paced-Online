#!/usr/bin/env python3

# Dictionaries01
dict1 = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
print(dict1)

dict1.pop('cake')
print(dict1)

dict1['fruit'] = 'Mango'
print(dict1)

print(dict1.keys())
print(dict1.values())
print('"cake" is in dictionary:', 'cake' in dict1)
print('"Mango" is in dictionary:', 'Mango' in dict1.values())

# Dictionaries02
dict2 = dict1.copy()
print('dict1:', dict1)
print('dict2:', dict2)
print('dict 1 == dict2?:', dict1 == dict2)
print ('dict1 is dict2?:', dict1 is dict2)

for k, v in dict1.items():
	dict2[k] = v.lower().count('t')

print('dict1:', dict1)
print('dict2:', dict2)

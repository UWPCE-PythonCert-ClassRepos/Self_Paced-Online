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
print('"cake" is a key in the dictionary:', 'cake' in dict1)
print('"Mango" is a value in the dictionary:', 'Mango' in dict1.values())
print()

# Dictionaries02
dict2 = dict1.copy()
print('dict1:', dict1)
print('dict2:', dict2)

for k, v in dict1.items():
	dict2[k] = v.lower().count('t')

print('dict1:', dict1)
print('dict2:', dict2)
print()

# Sets01
sets_dict = {'s2': set(), 's3': set(), 's4': set()}

for i in range(21):
	for k, v in sets_dict.items():
		if i % int(k[1]) == 0:
			v.update([i])

for k, v in sets_dict.items():
	print(k, type(v), v)

print('s3 is a subset of s2?:', sets_dict['s3'].issubset(sets_dict['s2']))
print('s4 is a subset of s2?:', sets_dict['s4'].issubset(sets_dict['s2']))
print()

#Sets02
pyset = set()
for l in 'Python':
	pyset.update(l)

print('pyset:', type(pyset), pyset)
pyset.update('i')
print('pyset with letter "i" added:', pyset)

marset = set()
for l in 'marathon':
	marset.update(l)

fs = frozenset(marset)
print('fs:', fs)
print('Note: Python sets do not allow duplicates.')
print('pyset U fs:', pyset.union(fs))
print('pyset intersection fs:', pyset.intersection(fs))

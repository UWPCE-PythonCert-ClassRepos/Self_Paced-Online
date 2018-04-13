#!/usr/bin/env python3

# Dictionaries 1
d = {'name': 'Chris', 'city': 'Seattle', 'cake':  'chocolate'}
print(d)
del d['cake']
print(d)
d['fruit'] = 'Mango'
print(d)

print('\ndictionary keys...')
for k in d:
    print(k)

print('\ndictionary values...')
for v in d.values():
    print(v)

print('\ncake is a key...')
print('cake' in d)


print('\nMango is a value...')
print('Mango' in d.values())


# Dictionaries 2
# loop through d, count lowercase t and writing value to new k_dict
k_dict = {}
for k, v in d.items():
    k_dict[k] = d[k].lower().count('t')

print(k_dict)


# sets 1
# use range's 'step' parameter to filter out unwanted values
s2 = set(range(0, 21, 2))
s3 = set(range(0, 21, 3))
s4 = set(range(0, 21, 4))

print(s2)
print(s3)
print(s4)

print(s3.issubset(s2))
print(s4.issubset(s2))


# sets2
p = set('Python')
p.update('i')
m = frozenset('marathon')
print(p.union(m))
print(p.intersection(m))

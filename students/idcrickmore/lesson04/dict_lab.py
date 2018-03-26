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
k_dict = {}
for k, v in d.items():
    k_dict[k] = d[k].lower().count('t')
    
print(k_dict)


# sets 1 this sh*t is broken
s2 = set(range(1,21))
for s in s2:
    if (s % 3) != 0:
        del s
    
print(s2)
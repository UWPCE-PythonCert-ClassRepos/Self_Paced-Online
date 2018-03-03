#!/usr/bin/env python3

# dictionaries1
cakes = {
    'name': 'Chris',
    'city': 'Seattle',
    'cake': 'Chocolate'
}

print(cakes)
cakes.pop('cake')
print(cakes)
cakes['fruit'] = 'Mango'
print(cakes)
print(cakes.keys())
print(cakes.values())
print('cake' in cakes.keys())
print('Orange' in cakes.values())

# dictionaries2
t_cakes = {}
for k, v in cakes.items():
    count = 0
    for letter in v:
        if letter == 't':
            count += 1
    t_cakes[k] = count
print(t_cakes)

# sets1
s2 = set(s for s in range(0, 21) if s % 2 == 0)
s3 = set(s for s in range(0, 21) if s % 3 == 0)
s4 = set(s for s in range(0, 21) if s % 4 == 0)
print(s2)
print(s3)
print(s4)
print(s3.issubset(s2))
print(s4.issubset(s2))

# sets2
s1 = set('Python')
s1.add('i')
s2 = frozenset('marathon')
print(s1.union(s2))
print(s1.intersection(s2))

#!/usr/bin/env python3

# Activity One

d = {
    "name": "Chris",
    "city": "Seattle",
    "cake": "Chocolate"
}

print(d)

del d['cake']

print(d)

d['fruit'] = 'Mango'

print(d)

for key in d:
    print(key)

for key, value in d.items():
    print(value)

print('cake' in d)
print('Mango' in d.values())

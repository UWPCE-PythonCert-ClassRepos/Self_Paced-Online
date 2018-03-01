#!/usr/bin/env python3

def dict1():
    d = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
    print(d)
    del d['cake']
    print(d)
    d['fruit'] = 'Mango'
    print(d.keys())
    print(d.values())
    print('cake' in d.keys())
    print('Mango' in d.values())

def dict2():
    d = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
    for x in d.keys():
        d[x] = d[x].lower().count('t')
    print(d)

if __name__ == "__main__":
    print('\n\nDictionary 1')
    dict1()
    print('\n\nDictionary 2')
    dict2()
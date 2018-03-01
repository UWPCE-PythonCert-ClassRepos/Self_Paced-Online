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
    for item in d:
        d[item] = d[item].lower().count('t')
    print(d)

def set1():
    s2 = set(range(0, 21, 2))
    s3 = set(range(0, 21, 3))
    s4 = set(range(0, 21, 4))
    print(s2, s3, s4, sep='\n')
    print(s3.issubset(s2))
    print(s4.issubset(s2))

def set2():
    s = set('Python')
    s.update('i')
    f = frozenset('marathon')
    print(s.union(f))
    print(s.intersection(f))

if __name__ == "__main__":
    print('\n\nDictionary 1')
    dict1()
    print('\n\nDictionary 2')
    dict2()
    print('\n\nSet 1')
    set1()
    print('\n\nSet 2')
    set2()
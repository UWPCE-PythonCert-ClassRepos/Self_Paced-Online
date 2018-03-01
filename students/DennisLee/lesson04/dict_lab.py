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

if __name__ == "__main__":
    dict1()
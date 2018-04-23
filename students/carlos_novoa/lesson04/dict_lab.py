#!/usr/bin/env python3

import os

"""
Lesson4, Activities
"""


def dictionaries_1():
    d = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
    print(d)
    d.pop('cake')
    print(d)
    d['fruit'] = 'Mango'
    print(d)
    print(d.keys())
    print(d.values())
    print('cake' in d)
    print('Mango' in d.values())


def dictionaries_2():
    d = {'name': 'Chris', 'city': 'Seattle', 'fruit': 'Mango'}
    print(d)
    for k, v in d.items():
        d[k] = v.count('t')
    print(d)


def sets1():
    s2 = set(range(0, 21, 2))
    s3 = set(range(0, 21, 3))
    s4 = set(range(0, 21, 4))
    print(s2)
    print(s3)
    print(s4)
    print(s3.issubset(s2))
    print(s4.issubset(s2))


def sets2():
    s = set('Python')
    s.add('i')
    fs = frozenset('marathon')
    print(s.union(fs))
    print(s.intersection(fs))


def get_file_paths(files_dir):
    return [os.path.join(path, file)
            for path, dirs, files in os.walk(files_dir)
            for file in files]


def activity_2():
    # print paths
    cwd = os.getcwd()
    files_dir = cwd + '/files/'
    files = get_file_paths(files_dir)
    print(*files, sep="\n")

    # copy file
    f_orig = files_dir + 'uw.png'
    f_copy = files_dir + 'uw2.png'
    with open(f_copy, 'wb+') as ofile, open(f_orig, 'rb') as ifile:
        data = ifile.read(1024)
        while data:
            ofile.write(data)
            data = ifile.read(1024)

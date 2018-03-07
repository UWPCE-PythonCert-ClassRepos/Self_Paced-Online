#!/usr/bin/env python3

import collections
import random

# infile = './sherlock_small.txt'
infile = './sherlock.txt'
oneline = './oneline.txt'
pool = collections.defaultdict(list)


def create_oneline(f):
    '''
    Remove line breaks from file given as an input argument and write 
    output to another file ('oneline')
    
        ARGS:
    f: file with the line breaks you want to remove.
    '''
    with open(f, 'r') as myfile:
        a = ' '.join(l.strip() for l in myfile)
        with open(oneline, 'w') as o:
            o.write(a)


def create_biglist(f):
    '''
    Create a list out of the single words of a given file.
    
        ARGS:
    f: file to read
    '''
    with open(f, 'r') as ofile:
        biglist = ofile.readline().split()

    for i in get_stuff_generator(0, biglist):
        # print(i)
        create_dict(i)


def get_stuff_generator(n, l):
    '''
    Iterate over a list of arbitrary length and get a slice of 3 elements out
    of it with every iteration. The slice and it's predecessor overlap by 
    2 elements (the last 2 elements of one slice are the first 2 of the 
    following slice). Return the slice.
    '''
    try:
        while n >= 0:
            e = n + 3
            k = l[n:e]
            y = l[e] 
            x = ' '.join(k)
            yield k
            n += 1
    except IndexError:
        return


def create_dict(l):
        k = ' '.join(l[0:2])
        v = l[2]
        pool[k].append(str(v))    # put key and value in dictionary


def show_dict(d):
    for i in d:
        print('{} --> {}'.format(i, d[i]))

def new_text(d):
    '''
    Given a dictionary which values are lists (defaultdict(list)), by random
    choose one single value out of the value list of each key. Print the key 
    and the choosen value.
    '''
    for i in d:
        print('{} {}'.format(i, random.choice(d[i])))

def main():
    create_oneline(infile)
    create_biglist(oneline)
    # get_stuff()
    # create_dict()
    # show_dict(pool)
    new_text(pool)

if __name__ == '__main__':
    main()

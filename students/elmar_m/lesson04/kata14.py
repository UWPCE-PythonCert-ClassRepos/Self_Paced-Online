#!/usr/bin/env python3

'''
file: kata14.py
elmar_m / 22e88@mailbox.org
Lesson04: Kata Fourteen: Tom Swift Under Milk Wood
'''

import collections
import random


def cleanup(x):
    '''
    Substitute certain characters in a string by whitespace. 
    Return the cleaned string. 
    
        ARGS:
    x: a string object
    '''
    x = x.replace('-', ' ')
    x = x.replace('.', ' ')
    x = x.replace(',', ' ')
    x = x.replace('"', ' ')
    x = x.replace("'", ' ')
    x = x.replace(":", ' ')
    x = x.replace('?', ' ')
    x = x.replace('!', ' ')
    x = x.lower()
    return x 


def make_oneline(x):
    '''
    Remove line breaks from a file. 
    Return the files content as a string respectively one long line.
    
        ARGS:
    x: the file to operate on
    ''' 
    with open(x, 'r') as myfile:
        l = ' '.join(l.strip() for l in myfile)
        return l


def create_biglist(x):
    '''
    Create a list out of a string by breaking it up on 
    whitespace.
    Return the list.
   
        ARGS:
    x: the string to break up 
    '''
    y = x.split()
    return y


def get_stuff_generator(x):
    '''
    Generator to iterate over a list of arbitrary length. Get a slice of 3 elements out
    of the list with every iteration. The slice and it's predecessor overlap by 
    2 elements (the last 2 elements of one slice are the first 2 of the 
    following slice). 
    Return the slice.
    
        ARGS:
    x: the list to operate on
    '''
    n = 0
    end = len(x) - 3
    while n <= end:
        e = n + 3
        s = x[n:e]
        yield s
        n += 1


def append_to_dict(x, y):
    '''
    Append items to a dictionary. 

        ARGS:
    x: the dictionary to append to
    y: the item. Item is expected to be a list of 3 elements. The  
       first two are joined by whitespace and built the new key. 
       The third element then builts the value of that key.
    '''
    k = ' '.join(y[0:2])
    v = y[2]
    x[k].append(str(v))    # put key and value in dictionary


def show_dict(x):
    '''
    Show key and values of a dictionary. Helper function for debugging.

        ARGS:
    x: the dictionary to show
    '''
    for i in x:
        print('{} --> {}'.format(i, x[i]))


def make_new_text(x):
    '''
    Print every key of a dictionary and one of it's (randomly chosen)
    values. 
    
        ARGS:
    x: a dictionary. Each key is expected to have a list of values.
    '''
    for i in x:
        print('{} {}'.format(i, random.choice(x[i])), end = ' ')     
            

#######################################################################

def main():
    infile = './sherlock.txt'
    mydict = collections.defaultdict(list)
    oneline = make_oneline(infile)
    cleaner_oneline = cleanup(oneline)
    biglist = create_biglist(cleaner_oneline)

    for slice in get_stuff_generator(biglist):
        append_to_dict(mydict, slice)
    
    # show_dict(mydict)
    make_new_text(mydict)
    
#######################################################################


if __name__ == '__main__':
    main()


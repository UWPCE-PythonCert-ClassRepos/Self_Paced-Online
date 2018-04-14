#!/usr/bin/env python3

import time

def simple():
    print('simple')
    return False

def react_correct():
    response = input('Please type yes or no\n')

    try:
        if response == 'yes':
            # print('answer was yes')
            print('JAAA')
            # print('answer was yes, will return secondfunc()')
            # return 'JAAA' 
            # return secondfunc()
            return True
        elif response == 'no':
            print('NOOO')
            # return 'NOOO'
            return False
        else:
            print('BULLSHIT')
            return 'BULLSHIT'
    except ValueError:
        print('ValueError exception raised !!')


def secondfunc():
    print('this is secondfunc() executed...')
    ts = time.strftime('%Y%m%d-%H%M%S')
    filename = 'foo.{}.txt'.format(ts)
    try:
        with open(filename, 'w') as f:
            f.write('helloworld\n')
    except:
        print('f**king exception caught')
    # return 'HAHAHA'
    # return None


def thirdfunc(a, b):
    c = a + b
    return c
    

def fourthfunc():
    print('i am fourthfunc and your value was > 10')
    return True
    # return False


def funcfive(x):
    if x > 10:
        return fourthfunc()
    else:
        return False

def funcsix():
    return funcseven()
    

def funcseven():
    opinion = input('Tell me what you think...')

def main():
    print('starting my program...')
    simple()
    react_correct()
    response = input('And now: give a value bigger / smaller 10:\n')
    funcfive(int(response)) 
    funcsix()
    print('end of my program.')


if __name__ == '__main__':
    main()


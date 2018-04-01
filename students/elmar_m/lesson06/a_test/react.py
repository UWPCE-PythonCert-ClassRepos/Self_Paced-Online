#!/usr/bin/env python3

def react_correct():
    response = input('Please type yes or no\n')

    try:
        if response == 'yes':
            # print('answer was yes')
            print('JAAA')
            # print('answer was yes, will return secondfunc()')
            # return 'JAAA' 
            return secondfunc()
        elif response == 'no':
            print('NOOO')
            return 'NOOO'
        else:
            print('BULLSHIT')
            return 'BULLSHIT'
    except ValueError:
        print('ValueError exception raised !!')


def secondfunc():
    print('this is secondfunc() executed...')
    return 'HAHAHA'

def main():
    print('starting my program...')
    react_correct()
    print('end of my program.')


if __name__ == '__main__':
    main()


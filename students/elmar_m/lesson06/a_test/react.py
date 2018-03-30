#!/usr/bin/env python3

def react_correct():
    response = input('Please type yes or no\n')

    try:
        if response == 'yes':
            # print('answer was yes')
            print('JAAA')
            return 'JAAA' 
        elif response == 'no':
            print('answer was no')
            return 'NOOO'
        else:
            print('BULLSHIT')
            return 'BULLSHIT'
    except ValueError:
        print('ValueError exception raised !!')


def main():
    print('starting my program...')
    react_correct()
    print('end of my program.')


if __name__ == '__main__':
    main()


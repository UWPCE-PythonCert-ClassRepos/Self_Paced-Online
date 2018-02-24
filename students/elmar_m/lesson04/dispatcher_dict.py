#!/usr/bin/env python3

# file: dispatcher_dict.py


def one():
    print('executed one')
    return 'executed one'

def two():
    print('executed two')
    return 'executed two'

def efunc():
    # return 'exiting.\n'
    return 'exiting'

prompt = 'please give an option, a or b, or q to exit menu: > '

dispdict = {
    'a' : one,
    'b' : two,
    # 'q' : 'exit menu',
    'q' : efunc,
    }

def menusel(p, dd):
    while True:
        response = input(p)
        if dd[response]() == 'exiting':
            break


if __name__ == '__main__':
    menusel(prompt, dispdict)


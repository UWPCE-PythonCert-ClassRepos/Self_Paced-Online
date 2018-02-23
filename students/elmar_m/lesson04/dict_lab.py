#!/usr/bin/env python3

'''
file: dict_lab.py
elmar_m / 22e88@mailbox.org
Lesson04: Dictionary and Set Lab
'''


nccdict = {
    'name' : 'Chris',
    'city' : 'Seattle',
    'cake' : 'Chocolate',
    }


def status(d):
    '''
    Display key value pairs of a dictionary
    '''
    print('Current dictionary:')
    # for i in d:
    #     print(i, ':', d[i])
    for a, b in d.items():
        print('{} : {}'.format(a, b))


def dict1():
    '''
    Dictionaries 1 exercise
    '''
    status(nccdict)
    print('\nDeleting item "cake"...')
    del nccdict['cake']
    status(nccdict)
    print('Item "cake" deleted!')
    print('\nAdding "fruit" : "mango" ...')
    nccdict['fruit'] = 'mango'
    status(nccdict)
    # print(nccdict.keys())
    # print(nccdict.values())
    
    if 'cake' in nccdict:
        print('key "cake" available in dictionary')
    else: 
        print('key "cake" NOT available in dictionary')

    if 'mango' in nccdict.values():
        print('value "mango" available in dictionary')
    else: 
        print('value "mango" NOT available in dictionary')
        

def dict2():
    '''
    Dictionaries 2 exercise
    '''
    pass

if __name__ == '__main__':
    dict1() 


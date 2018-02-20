#!/usr/bin/env python3

'''
file: list_lab.py
elmar_m / 22e88@mailbox.org
Lesson03: List Lab Exercise
'''

def print_list(l):
    '''
    prints the elements of a list in one line, ending with a 
    single line feed
    '''
    for i in l:
        print(i, '', end='')     
    print()

def series1():
    '''
    series 1
    '''
    fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
    print_list(fruits)
    response = input('Please add a fruit: > ')
    fruits.append(response)
    print_list(fruits)
    response = input('Please enter a number to see the fruit having that number: ')
    print('Fruit number', response, 'is:', fruits[int(response) -1])

    print('This is fruitlist now:')

    print_list(fruits)
    
    anotherfruit = input('Please type in another fruit, this will be added at the beginning using "+": > ')
    fruits = [anotherfruit] + fruits  
    print('This is fruitlist now:')
    print_list(fruits)

    thirdfruit = input('Type in a 3rd fruit to add it at the beginning using insert(): >')
    fruits.insert(0, thirdfruit)
    print('See fruitlist once again:')
    print_list(fruits)
    print(thirdfruit, 'have been added successfully too.')

def series2():
    ''' 
    series 2
    '''
    fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
    print('original list:')
    print_list(fruits)
    input('Please press enter to remove the last fruit from the list...')
    fruits.pop()
    print("Here's the result:")
    print_list(fruits)
    response = input("Please type in a fruit to remove: >")
    fruits.remove(response)
    print("Here's the list now:")
    print_list(fruits)
    print('Multiplied times two:')
    fruits = fruits + fruits
    print_list(fruits)

    rmfruit = input('Please type in a fruit to remove: >')

    while rmfruit not in fruits:
        print(rmfruit, 'is not in the list')
        print('current list is: ')
        print_list(fruits)
        rmfruit = input('Please choose a fruit which is available in the list: >')

    while rmfruit in fruits:
        fruits.remove(rmfruit)

    print('OK,', rmfruit, 'was removed.')
    print('Now this is still in the list:')
    print_list(fruits)


def series3():
    '''
    series 3
    '''
    fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
    print('original list:')
    print_list(fruits)
    for i in fruits[:]:
        print('Do you like', i, '?', 'Type "yes" or "no": >')
        answer = input()
        while (answer != 'yes') and (answer != 'no'):
            answer = input('Please type either "yes" or "no": >\n')
        if (answer == 'no'):
            print('removing', i, '...')
            fruits.remove(i)
        else:
            print('keeping', i, '...')
            
    print('These are the fruits you like:')   
    print_list(fruits)


def series4():
    '''
    series 4
    '''
    fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
    print('original list:')
    print_list(fruits)

    cfruits = []
    for i in fruits:
        item = i[::-1]
        cfruits.append(item)
    print('original list items with reversed letters:')    
    print_list(cfruits)

    print('original list, last item removed:')
    fruits.pop()
    print_list(fruits)


if __name__ == '__main__':
    print('This file contains functions for the list lab exercises, please import it to use them')

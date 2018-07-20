# Description: 
# Author: Andy Kwok
# Last Updated: 07/14/2018
# ChangeLog: 
# v1.0 - Initialization

import os 

#!/usr/bin/env python

list = ['Apples', 'Pears', 'Oranges', 'Peaches']

#Series 1
def series_one(list):
    """ Function to display and add item to list
    list: list of fruit
    new_list = list after mod in fruit
    new_fruit: new element to add to list
    id: index value
    new_fruit_2: another new element to add to list
    selection: list item scan
    """ 
    print(list)
    new_fruit = input('Please enter another fruit > ')
    list = list + [new_fruit]
    print(list)
    id = input('Number on the list to display? ')
    print('Number {} on the list is {}'.format(id, list[int(id)-1]))
    new_fruit_2 = input('Please enter another fruit > ')    
    list = [new_fruit_2] + list
    print('Add: ', list)
    list.insert(0,new_fruit_2)
    print('Add & insert', list)
    new_list = []
    for selection in list:
        if selection[0] == 'P':
            new_list += [selection]
    print('Fruit with P: ', new_list)    
    return list

#Series 2    
def series_two(list):
    """ Function to remove item from list
    list: input list
    fruit: fruit from list
    respond: fruit to delete
    """
    print('Series 2: ', list)
    list.remove(list[-1])
    print('Removed Last: ', list)
    double_list = list.copy()
    list += double_list
    print(list)
    respond = input('What fruit do you want to delete from the list? ')
    while respond in list:
        list.remove(respond)
    print(list)


#Series 3
def series_three(list):
    """Function to remove dislike fruit
    list: input list
    mod_list: list with removed fruit
    fruit: fruit from list
    respond: fruit to delete
    """
    mod_list = list.copy()
    for fruit in list:
        print('Do you like {}?'.format(fruit.lower())) 
        respond = None
        while respond != 'no' and respond != 'yes':
            respond = input('yes or no? ')
            if respond == 'no':
                mod_list.remove(fruit)
    print('Modified List: ' , mod_list)
    print('Existing list: ' , list)

#Series 4
def series_four(org_list):
    """Function to modify existing list and 
    org_list: input list
    copy_list: list with letters of each fruit reversed
    mod_list: rebuild list
    fruit: fruit from list
    """
    copy_list = org_list.copy()
    mod_list = []
    for fruit in copy_list:
        mod_list += [fruit[::-1]]
    copy_list = mod_list.copy()
    org_list.remove(org_list[-1])
    print('Orginal list contains > ', org_list)
    print('Copied list contains > ', copy_list)
    input("Enter to continue...")
    

# Run all tasks in the program
list_one = series_one(list)
series_two(list_one)
series_three(list_one)
series_four(list_one)
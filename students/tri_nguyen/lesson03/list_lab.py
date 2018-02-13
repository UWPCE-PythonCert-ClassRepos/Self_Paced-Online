#!/usr/bin/env python3

# ------------------------------------------- #
# Student:   Tri Nguyen
# Instructor: Natasha Aleksandrova
# Date:  09-Feb-2018
# ------------------------------------------- #

from copy import deepcopy

# Define functions
def print_series(n):
    ''' this function is an indicator of each Series '''
    print('--Series {0} of Python List exercise--{1}'.upper().format(n, '\n'))


def display_list():
    ''' this function will display the fruit_list '''
    
    fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']
    
    print('Below is the current list of fruits.')
    
    for idx, fruit in enumerate(fruit_list):
        print(idx + 1, '-', fruit)
        
    print() #  print extra space below
 
def add_new_fruit():
    ''' Ask the user for a new fruit then add to the end 
        of fruit_list
    '''
    
    fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']
    
    user_input = input('Please add another fruit: ')
    
    fruit_list.append(user_input.title())
    
    print('Below is a newly updated list of fruits.')
    
    for idx, fruit in enumerate(fruit_list):
        print(idx + 1, '-', fruit)
        
    print() #  print extra space below
    
def pick_a_number():
    ''' this function will take a number and return the
        corresponding fruit '''
    
    fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']
    
    num_from_user = int(input('Please pick a number to get back the corresponding fruit: '))
    num_from_user = num_from_user - 1
    
    print(num_from_user + 1, '-', fruit_list[num_from_user] + '\n')

def add_to_front(a_fruit):
    ''' Add another fruit to the beginning of the
        list using '+' and display the list '''
        
    fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']
    
    fruit_list = [a_fruit.title()] + fruit_list
    
    print(a_fruit.title(), 'has been added to the beginning of the list. See below for the list.')
    
    for idx, fruit in enumerate(fruit_list):
        print(idx + 1, '-', fruit)
        
    print()
    
def insert_front(a_fruit):
    ''' this function adds another fruit
        to the beginning of the list 
        using insert() and display the list '''
        
    fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']
    
    fruit_list.insert(0, a_fruit.title())
    
    print(a_fruit.title(), 'has been added to the beginning of the list. See below for the list.')
    
    for idx, fruit in enumerate(fruit_list):
        print(idx + 1, '-', fruit)
        
    print()
    
def fruit_with_letter(letter):
    ''' this function displays all the 
        fruits that begins with 'P' using for loop '''

    fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']
    
    print('Below is the list of fruits that begin with "P".')
    for fruit in fruit_list:
        if fruit.startswith(letter.title()):
            print(fruit)
    
    print()
    
def remove_last_fruit():
    ''' this function removes the last fruit
        from the list '''
        
    fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']

    print('The last fruit ({}) from the list has been removed.'.format(fruit_list[len(fruit_list) - 1]))

    fruit_list.pop()

    for idx, fruit in enumerate(fruit_list):
        print(idx + 1, '-', fruit)

    print()

def delete_fruit():
    ''' this function asks the user for a fruit to delete '''
    
    fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']
    
    to_be_deleted = input('Enter a fruit to delete ').title()
    
    if to_be_deleted in fruit_list:
        fruit_list.remove(to_be_deleted)
    
    print('Below is a newly updated list of fruits.')    
    
    for idx, fruit in enumerate(fruit_list):
        print(idx + 1, '-', fruit)

    print()

def like_or_not():
    ''' this function asks the user
        whether she/he likes a fruit '''

    fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']

    like_fruit_list = []

    for fruit in fruit_list:
        like_answer = input(f'Do you like {fruit.lower()}? ')
        
        while like_answer.lower() not in ('yes', 'no'):
            like_answer = input('Please answer "yes" or "no" ')

        if like_answer == 'yes':
            like_fruit_list.append(fruit)

    print(like_fruit_list)
    print()
  
# End of function definition  

# ------------------------------------------- #
# Series 1:  
 
# Presentation of Series 1
print_series(1)
display_list()
add_new_fruit()
pick_a_number()
add_to_front('watermelon')
insert_front('pinnaples')
fruit_with_letter('p')

# End of presentation of Series 1
# ------------------------------------------- #

# ------------------------------------------- #
# Series 2:

# Presentation of Series 2

print_series(2)
display_list()
remove_last_fruit()
delete_fruit()

# End of presentation of Series 2
# ------------------------------------------- #

# ------------------------------------------- #
# Series 3:

# Presentation of Series 3

print_series(3)
like_or_not()

# End of presentation of Series 3
# ------------------------------------------- #

# ------------------------------------------- #
# Series 4:

# Presentation of Series 4

print_series(4)

fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']

copied_fruit_list = deepcopy(fruit_list)

reversed_letters = []

for fruit in copied_fruit_list:
    reversed_letters.append(fruit[::-1])

fruit_list.pop()

print('The original list of fruits minus the last fruit:')

for idx, fruit in enumerate(fruit_list):
    print(idx + 1, '-', fruit)

print('\nThe copied list of fruits with reversed letters:')

for idx, fruit in enumerate(reversed_letters):
    print(idx + 1, '-', fruit)

# End of presentation of Series 4
# ------------------------------------------- #

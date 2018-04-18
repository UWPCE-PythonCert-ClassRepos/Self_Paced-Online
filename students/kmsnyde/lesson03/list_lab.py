#! /usr/bin/env python3
"""
Created on Thu Apr  5 17:42:17 2018

@author: Karl M. Snyder
"""

#SERIES 1

fruit = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruit, '\n')
add_fruit = input('What fruit would you like to add? ')
fruit.append(add_fruit)
print(fruit, '\n')
fruit_num = int(input('Provide a number: '))
print(fruit[fruit_num - 1], '\n')
fruit += ['Red Grape']
print(fruit, '\n')
fruit.insert(0, 'Prickly Pear')
print(fruit, '\n')
for i in fruit:
    if i[0] == 'P':
        print(i)

#SERIES 2

#reset fruit to original
fruit = ['Apples', 'Pears', 'Oranges', 'Peaches'] 
print('\n', fruit,'\n')
fruit.pop()
print(fruit)
del_fruit = input('What piece of fruit do you want to remove? ')
fruit.remove(del_fruit)
print(fruit, '\n')


#SERIES 3

#reset fruit to original
fruit = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruit,'\n')
new_fruit = fruit[:]
for i in fruit:
    user_input = input('Do you like ' + i + ': ')
    while user_input not in ['yes', 'no']:
        user_input = input('Do you like ' + i + ':' + ("'yes' or 'no'"))
    if user_input == 'no':
        new_fruit.remove(i)
print(new_fruit, '\n')

#SERIES 4

#reset fruit to original
fruit = ['Apples', 'Pears', 'Oranges', 'Peaches']
fruit_join = ','.join(fruit[:])
fruit_rev1 = fruit_join[::-1]
fruit_reord = fruit_rev1.split(',')
fruit_reord.reverse()
fruit.pop()
print(fruit, '\n', fruit_reord)

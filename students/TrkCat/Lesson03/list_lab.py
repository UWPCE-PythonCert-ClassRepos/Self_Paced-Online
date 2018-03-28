#!/usr/bin/env python3

#Series 1
fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruits)

fruit_to_add = input('\nWhat fruit should be added? > ')
fruits.append(fruit_to_add)
print(fruits)

fruit_to_disp = int(input('\nWhat fruit to view (1 to 5)? >'))
print(fruit_to_disp,fruits[fruit_to_disp-1],'\n')

fruits = ['Pineapples'] + fruits
print(fruits,'\n')

fruits.insert(0, 'Bananas')
print(fruits,'\n')

for fruit in fruits:
    if fruit[0] == 'P':
        print(fruit)



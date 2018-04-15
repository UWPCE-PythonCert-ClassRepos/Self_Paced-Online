#!/usr/bin/env python3
"""
File Name: list_lab.py
Author: Travis Brackney
Class: Python 201 - Self paced online
Date Created 3/18/2018
Python Version: 3.6.4
"""

# Series 1
print('Series 1')
fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruits)
new_fruit = input('Enter the name of a fruit: ')
fruits.append(new_fruit)
print(fruits)
num = int(input(f'Enter a number from 1 to {len(fruits)}: '))
print(f"You have selected {num} for {fruits[num-1]}")
print("Adding a fruit with +")
print(fruits)
print("Adding a fruit with .insert")
fruits.insert(0, "Passionfruit")
print(fruits)
print("Fruits that start with P")
for fruit in fruits:
    if (fruit[0] == 'P'):
        print(fruit)
print("\n")

# Series 2
print('Series 2')
fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruits)
fruits.pop()
print(fruits)
fruit_to_remove = input(f"Enter the name of a fruit you want to remove: ")
fruits = fruits * 2
for fruit in fruits:
    if fruit == fruit_to_remove:
        fruits.remove(fruit)
print(fruits)
print("\n")

# Series 3
print('Series 3')
fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
fruits[:]
for fruit in fruits[:]:
    response = ''
    while response != 'yes' and response != 'no':
        response = input(f'Do you like {fruit}: ').lower()
        if response == 'no':
            fruits.remove(fruit)
print(fruits)
print("\n")

# Series 4
print('Series 4')
fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
copy = []
for f in fruits:
    copy.append(f[::-1])
fruits.pop()
print(fruits)
print(copy)

#!/usr/bin/env python3
# NEIMA SCHAFI, LESSON 3 Assignment - list_lab
#SERIES 1
fruit = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruit)
response = input("Please enter another fruit: ")
fruit.append(response.title())
print(fruit)
response2 = int(input("Please enter a number above zero: "))
print(fruit[response2-1])
fruit = ['Lemon'] + fruit
print(fruit)
fruit.insert(0, 'Banana')
print(fruit)
for item in fruit:
    if item[0][0] == 'P':
        print(item)

#SERIES 2
print(fruit)
fruit = fruit[:-1]
print(fruit)
response3 = input("Please enter a fruit to delete: ")
if response3.title() in fruit:
    fruit.remove(response3.title())
print(fruit)

#SERIES 3
fruit = ['Apples', 'Pears', 'Oranges', 'Peaches']
fruit2 = ['Apples', 'Pears', 'Oranges', 'Peaches']
for n in fruit:
    response4 = input("Do you like {}? ".format(n.lower()))
    while not response4.lower() in ['yes', 'no']:
        response4 = input('Please enter yes or no:\n')
    if response4.lower() == 'no':
        fruit2.remove(n)
fruit = fruit2
print(fruit)

#SERIES 4
fruit = ['Apples', 'Pears', 'Oranges', 'Peaches']
fruit2 = []
for item in fruit:
    fruit2.append(item[::-1])
fruit = fruit[:-1]
print(fruit)
print(fruit2)

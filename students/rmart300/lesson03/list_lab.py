#!/usr/bin/env python3

#series 1
"""
Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
Display the list (plain old print() is fine…).
Ask the user for another fruit and add it to the end of the list.
Display the list.
Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis). Remember that Python uses zero-based indexing, so you will need to correct.
Add another fruit to the beginning of the list using “+” and display the list.
Add another fruit to the beginning of the list using insert() and display the list.
Display all the fruits that begin with “P”, using a for loop.
"""

fruit_list = ['Apples','Pears','Oranges','Peaches']
print(fruit_list)
fruit_to_add = input("enter the name of a fruit > ")
fruit_list.append(fruit_to_add)
print(fruit_list)

list_index = -1
while list_index < 0 or list_index > len(fruit_list):
    list_index = int(input("choose a position in the fruit list > "))
    list_index -= 1

print(fruit_list[list_index])

fruit_to_add = input("enter the name of another fruit > ")
fruit_list = [fruit_to_add] + fruit_list
print(fruit_list)

fruit_to_add = input("enter the name of another fruit > ")
fruit_list.insert(0,fruit_to_add)
print(fruit_list)

print("Here's your P fruits:")
for fruit in fruit_list:
    if fruit.startswith('P'):
        print(fruit)




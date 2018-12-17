#!/usr/bin/env python3
# list_lab.py
# Coded by LouReis

# Beginning of Series 1.
# Create a list that contains Apples, Pears, Oranges, and Peaches.
fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']
# Display the list using print statement.
print(fruit_list)
# Ask the user for another fruit.
response = [input("Enter the name of another fruit> ")]
# Add the fruit to the end of the list.
fruit_list = fruit_list + response
# Display the list using the print statement.
print(fruit_list)
#
# fruit_list.append(response)
#
# Ask the user for a number representing one in the list (on a 1 is first basis).
pick = input("Enter a number to pick a fruit in the list> ")
pick_int = int(pick)
# Convert from zero-based indexing to 1 based.
pick_int = pick_int - 1
# Display the number back to the user along with the corresponding fruit.
print((pick_int+1),fruit_list[pick_int])
# Add another fruit to the beginning of the list using "+".
fruit_list = ['Bananas'] + fruit_list
# Display the new list.
print(fruit_list)
# Add another fruit to the beginning of the list using insert().
fruit_list.insert(0, 'Kiwi')
# Display the new list.
print(fruit_list)
# The following lines & loop display the fruits that begin with the letter P.
num_fruit = len(fruit_list)
print("The below fruit in the list start with the letter P:")
for x in range(0,num_fruit):
    pick=fruit_list[x]
    if pick[:1] == 'P' or pick[:1] == 'p':
        print(pick)

# Beginning of Series 2
# Display the list.
print(fruit_list)
# Remove the last item in the list.
fruit_list.pop()
print(fruit_list)
# Ask the user for a fruit to delete, find it and delete it. First fruit is 1.
pick = input("Enter a number to pick a fruit in the list to remove> ")
pick_int = int(pick)
# Convert from zero-based indexing to 1 based.
pick_int = pick_int - 1
# Remove the selected fruit from the list.
del fruit_list[pick_int]
print(fruit_list)
# Double the list by multiplying by 2.
fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches', 'Bananas', 'Kiwis']
fruit_list = fruit_list*2
print(fruit_list)
# The below code didn't seem to work properly.
# response = [input("Enter the name of a fruit to remove> ")]
# print(response)
# fruit_list.remove(response)
# print(fruit_list)
#
# Ask the user for a fruit to remove
for x in range(0,len(fruit_list)):
    if x == 0:
        response = [input("Enter a fruit to remove:")]
    if (x < len(fruit_list)) and ([fruit_list[x]] == response):
        print("match for index", x, "will remove from list")
        del fruit_list[x]
print(fruit_list)

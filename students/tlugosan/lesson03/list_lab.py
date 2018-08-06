#!/usr/bin/env python3

# region series1
"""Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”"""
fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]

"""Display the list"""
print(fruit_list)

"""Ask for another fruit and add it to the end"""
response1 = input("Please provide another fruit: ").lower().capitalize()
fruit_list.append(response1)

"""Display list."""
print(fruit_list)
print()

"""Ask for a number and display the number and the corresponding fruit on a 1-is basis."""
response2 = input("Please provide a number between 1 and %s: " % len(fruit_list))
while True:
    if not response2.isnumeric() or int(response2) < 1 or int(response2) > len(fruit_list):
        response2 = input("Try again a number between 1 and %s: " % len(fruit_list))
    else:
        break
print("%d : %s" % (int(response2), fruit_list[int(response2) - 1]))
print()

"""Add another fruit at the beginning of the list using +  then print the list"""
response3 = input("Please provide another fruit: ").lower().capitalize()
fruit_list = [response3] + fruit_list
print(fruit_list)
print()

""" Add another fruit at the beginning at the list using insert() function"""
response4 = input("Please provide another fruit: ").lower().capitalize()
fruit_list.insert(0, response4)
print(fruit_list)
print()

"""Display all the fruits that start with P using a for loop"""
print("Fruit that start with letter P: ", end=" ")
for item in fruit_list:
    if item.startswith("P"):
        print(item, end=" ")
print()
print("---------------------------------")
# endregion

# region series2
"""Display the fruit list."""
print(fruit_list)

"""Remove the last fruit from the list."""
fruit_list.pop()
print("Last fruit from the list was removed")

"""Display list."""
print(fruit_list)
print()

"""Prompt the user to delete for a fruit to delete, find it and remove it."""
response5 = input("Pick a fruit from the list to delete: ").lower().capitalize()
if response5 in fruit_list:
    fruit_list.remove(response5)
print(fruit_list)
print()

""" Multiply the list times two. Keep asking until a match is found.
Once found, delete all occurrences."""
fruit_list += fruit_list
print(fruit_list)
response6 = input("Pick another fruit from the list to delete: ").lower().capitalize()
while True:
    if response6 in fruit_list:
        while response6 in fruit_list:
            fruit_list.remove(response6)
        break
    else:
        response6 = input("This fruit doesn't exist in the list. Please try again: ").lower().capitalize()
print(fruit_list)
print("---------------------------------")
# endregion

# region series3
"""Given a fruit list ask the user if they like it or not.
 For no remove the fruit from the list then display the leftover list."""

fruit_list3 = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruit_list3)
YES = "yes"
NO = "no"
temp_fruit_list = []
for item in fruit_list3:
    response7 = input("Do you like %s? Please answer with yes or no: " % item.lower()).lower()
    while response7 not in (YES, NO):
        response7 = input("Please answer only with yes or no: ").lower()
    if response7 == YES:
        temp_fruit_list.append(item)
fruit_list3 = temp_fruit_list
print("The fruit that you like are: %s" % fruit_list3)
print("---------------------------------")
# endregion

# region series4
"""Make a copy of the list and reverse the letters in each fruit in the copy.
Delete the last item of the original list. Display the original list and the copy."""

fruit_list4 = ["Apples", "Pears", "Oranges", "Peaches"]
print("Original list: %s" % fruit_list4)
print()

reversed_fruit_list = []
for item in fruit_list4:
    reversed_fruit_list.append(item[::-1])
print("Copy of reversed items list: %s" % reversed_fruit_list)
print()

fruit_list4.pop()
print("Original list once the last item was removed: %s" % fruit_list4)
print("Copy of reversed items list: %s" % reversed_fruit_list)
# endregion

#!/usr/bin/env python3


'''
    File Name: list_lab.py
    Author: Matt Hudgins
    Date created: 5/5/18
    Date last modified: 5/5/18
    Python Version 3.6.4
'''

# Series 1

print("Starting Series 1!")

# Fruit List
fruit = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruit)

# User will add a new fruit
new_fruit = input("What fruit would you like to add?")
fruit.append(new_fruit)
print("This is the new list", fruit)

# User will pick a number
pick_a_number = int(input("Pick a number between 1-4:"))
print(pick_a_number, fruit[pick_a_number - 1])

# User will add a fruit to the beginning of the list
add_a_fruit = input("What fruit would you like to add to the beginning of the list?")
fruit = [add_a_fruit] + fruit
print(fruit)

# User will insert fruit into list at the beginning
insert_a_fruit = input("What fruit would you like to add to the beginning?")
fruit.insert(0, insert_a_fruit)
print("Updated List:", fruit)

# Searching for fruits that start with the letter P
for n in fruit:
    if n.startswith("P"):
        print("Here's all of the fruit that start with the letter P:", n)


# Series 2


print("Starting Series 2!")

# This prints and updated list for the user
print("This is the most upto date list:", fruit)

# This removes the last furit from the list
del fruit[6]
print("This is an updated list with the last fruit removed:", fruit)

# User deletes a fruit from the list
new_fruit = input("Which fruit would you like to delete?")
if new_fruit in fruit:
    fruit.remove(new_fruit)
    print(new_fruit, "has been deleted from the list")

print("This is the new list:", fruit)


# Series 3


print("Staring Series 3!")

fruit = ["Apples", "Pears", "Oranges", "Peaches"]
fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]

print("Please answer the following questions with yes or no")
for i in fruit_list:
    x = input(f"Do you like {i.lower()} ?")
    while (x != "yes") and (x != "no"):
        x = input("Invalid input please enter a yes or no:")
    if x == "no":
        fruit.remove(i)
    if x == "yes":
        print("I like this fruit too!")
print("This is an updated list with only the fruits you like:", fruit)

# Series 4

print("Alright lets start Series 4!")

fruit = ["Apples", "Pears", "Oranges", "Peaches"]
fruit_reserve = list(range(len(fruit)))

for i in range(len(fruit)):
    fruit_reserve = [fruit[i][::-1]]
    print("Original List:", fruit)
    print("Reversed Order:", fruit_reserve)

del fruit[-1]
print("This is a list of the last fruit deleted:", fruit)
fruit.insert(3,"Peaches")
print("This is the original list:", fruit)

Print ("This is the end of the list-lab exercise!")

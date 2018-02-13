#!/usr/bin/env python3
# Lesson 3 - List Lab Excercise

### Series 1 #########################################################
# Create/dipslay list of fruit
print("*" * 5 + "Series 1" + "*" * 5)
fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
print("Original list:", fruit_list)

# Prompt user for another fruit, add to list
response = input("Please enter a fruit: ")
fruit_list.append(response)
print(fruit_list)

# Ask user for a number, print number and fruit corresponding to number
response = input("Please enter a number: ")
print("You chose:", response + "... That corresponds to:", fruit_list[int(response) - 1])

# Add fruit to beginning using "+" and display. Add fruit to beginning using 'insert()' and display
fruit_list = ["Bananas"] + fruit_list
print("Adding fruit using '+':", fruit_list)
fruit_list.insert(0, "Strawberries")
print("Adding fruit using 'insert':", fruit_list)

# Display all fruits beginning with "P" using a 'for' loop
p_fruits = []
for item in fruit_list:
    if item[0] == "P":
        p_fruits.append(item)

print("All fruits beginning with 'P':", p_fruits)


### Series 2 ##########################################################
print("*" * 5 + "Series 2" + "*" * 5)
fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
print("Starting with the list from Series 1:", fruit_list)

# Remove last fruit from list and display
fruit_list.pop()
print("List after removing last element:", fruit_list)

# Ask for fruit to delete, find and delete. List multiplied by 2.
fruit_list *= 2
response = input("Which fruit would you like to delete: ")

while True:
    if response in fruit_list:
        for item in fruit_list:
            if item == response:
                fruit_list.remove(item)
        break
    else:
        response = input("Sorry, that fruit isn't in the list, please try again: ")

print("Doubled list with fruit removed:", fruit_list)


### Series 3 #########################################################
print("*" * 5 + "Series 3" + "*" * 5)
fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
print("Starting with the list from Series 1:", fruit_list)

# Ask user if they like each fruit, check answer, remove if 'no'
for item in fruit_list[:]:
    response = input("Do you like {}? ".format(item.lower()))
    if response.lower() == "yes":
        continue
    elif response.lower() == "no":
        fruit_list.remove(item)
    else:
        while True:
            response = input("That's not a valid answer, 'yes' or 'no' please... ")
            if response.lower() == "yes":
                break
            elif response.lower() == "no":
                fruit_list.remove(item)
                break
            else:
                continue

print("Here's the fruit you like:", fruit_list)


### Series 4 #########################################################
print("*" * 5 + "Series 4" + "*" * 5)
fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
print("Starting with the list from Series 1:", fruit_list)

# Make copy of list, reverse letters of each fruit
copy_fruit_list = fruit_list[:]
for i, item in enumerate(copy_fruit_list):
    copy_fruit_list[i] = item[::-1]

# Remove last item of original list, print both lists
fruit_list.pop()
print("Original list with last item removed:", fruit_list)
print("Copied, reversed list:", copy_fruit_list)

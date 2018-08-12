#!/usr/bin/env python3
# Lesson 03, Series lab

# Series 1
# Print out initial list of fruit
fruits = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruits)

# Prompt for another fruit and append it to the end of list, then print
fruits.append(input("\nPlease enter a fruit to add -> "))
print(fruits)

# Prompt for index of fruit to display and display it
index = int(input("\nEnter index of fruit to display -> "))
if index > 0 and index <= len(fruits):
    print(index, fruits[index-1])
else:
    print("There are ", len(fruits), " fruits, enter a number in that range")
    
# Using two different methods, add another fruit to beginning
fruits = ["Banana"] + fruits
print("....\n", fruits)
fruits.insert(0, "Kumquats")
print("....\n", fruits)

# Iterate through the list and display all fruits that start with 'P'
print("....")
for fruit in fruits:
    if fruit[0] == "P" or fruit[0] == "p":
        print(fruit)
#!/usr/bin/env python3
# Lesson 03, Series lab

# Series 1
# Print out initial list of fruit
fruits = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruits)

# Prompt for another fruit and append it to the end of list, then print
fruits.append(input("\nPlease enter a fruit to add -> "))
print(fruits)

# Prompt for index of fruit to display and display it (make them enter a number in range)
index = 0
while index < 1 or index > len(fruits):
    index = int(input("\nEnter index of fruit (between 1 and " + str(len(fruits)) + ") to display -> "))
print("Fruit number {} is {}".format(index, fruits[index-1]))
    
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
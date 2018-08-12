#!/usr/bin/env python3
# Lesson 03, Series lab

# Series 1
print("\nSERIES 1\n")

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
fruits = ["Bananas"] + fruits
print("....\n", fruits)
fruits.insert(0, "Kumquats")
print("....\n", fruits)

# Iterate through the list and display all fruits that start with 'P'
print("....")
for fruit in fruits:
    if fruit[0] == "P" or fruit[0] == "p":
        print(fruit)
        
# Series 2
print("\nSERIES 2\n")

# Make a copy of the list for use in Series 2, since instructions for Series 3 say to use list from Series 1
fruits2 = fruits[:]

# Print the list of fruits
print(fruits2)

# Remove last fruit from list and print again
fruits2.pop()
print(fruits2)

# Double the fruit list (for BONUS!) and display again
fruits2 *= 2
print(fruits2)

# Prompt for fruit to delete (prompt until a match is found)
fruit_to_delete = ""
while fruit_to_delete not in fruits2:
    fruit_to_delete = input("\nEnter fruit to delete -> ")

# Delete all occurrences of the entered fruit
while fruit_to_delete in fruits2:
    fruits2.remove(fruit_to_delete)
    
# Display the list to show fruit was removed
print(fruits2)

# Series 3
# Start with ending list from Series 1, display it to start
print("\nSERIES 3\n")

# Again make a copy of the list for use in Series 3, since instructions for Series 4 say to use list from Series 1
fruits3 = fruits[:]
 
print(fruits3)

# make a copy of the list to iterate
fruits_copy = fruits3[:]
for fruit in fruits_copy:
    while True:
        response = input("Do you like " + fruit.lower() + " (yes or no)? ")
        if response == "yes":
            break
        elif response == "no":
            fruits3.remove(fruit)
            break

# Display new list with fruit they hate removed
print(fruits3)

# Series 4
print("\nSERIES 4\n")

# Make a new copy of the list for manipulation in this series
fruits4 = fruits[:]

# Iterate the copy list and reverse the letters in each fruit
for i, fruit in enumerate(fruits4):
    fruits4[i] = fruit[::-1]
    
# Remove last fruit on original list
fruits.pop()

# Display both lists
print("Original:", fruits)
print("Copy:    ", fruits4)


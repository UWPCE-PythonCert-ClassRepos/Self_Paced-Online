#!/usr/bin/env python3

# Series 1 - create a list, display and ask user for number input
# create list of fruit
fruit = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruit)
# request response from user and append to list
response = input("Choose a fruit > ")
fruit.append(response)
print(fruit)
fruit_count = len(fruit)
print(fruit_count)
# prompt for number and display fruit by index
response = input("Select a number > ")
numval = int(response)
#numval = numval -1
print("index ", numval, "is ", fruit[numval-1])




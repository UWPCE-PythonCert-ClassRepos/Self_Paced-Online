#!/usr/bin/env python3

# Series 1 - create a list, display and ask user for number input
# create list of fruit
fruit = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruit)
response = input("Choose a fruit > ")
print(response)
fruit.append(response)
print(fruit)


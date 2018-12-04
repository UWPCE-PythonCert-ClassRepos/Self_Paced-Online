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
# print fruit by index adjusting by "-1"
print("index ", numval, "is ", fruit[numval-1])
# prompt for another fruit and add to beginning of list using "+" method
prompt = input("Chose another fruit > ")
new_list = []
new_list.append(prompt)
fruit = new_list + fruit
print(fruit)
#new_list1 = list[prompt]
#fruit = new_list + fruit
#print(fruit)
#print(new-list)
#print(new_list1)




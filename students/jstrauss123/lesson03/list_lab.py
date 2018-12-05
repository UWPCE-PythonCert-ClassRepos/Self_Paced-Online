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
prompt = input("Choose another fruit > ")
new_list = []
new_list.append(prompt)
# concatenate lists
fruit = new_list + fruit
print(fruit)
# prompt for another fruit and add to beginning of list using insert
prompt = input("Choose another fruit > ")
# append new fruit idx 0
fruit.insert(0, prompt)
print(fruit)
# print all fruit that starts with P using for loop.
for i in fruit:
    for elem in i:
        if elem == "P":
            print(i)
print(" ")
            
# series 2
# display list of fruit, delete last fruit in list, prompt user to choose a fruit to delete
response = input("Press enter to continue with series 2 > ")
fruit = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruit)
# delete last fruit from list
fruit.pop()
print(fruit)
# ask user for a fruit to delete, delete fruit and show list again
response = input("Choose a fruit to delete > ")
fruit.remove(response)
print(fruit)
print(" ")

# series 3
# loop through fruit list and prompt user by fruit name if they like it or not. remove if answer is no
response = input("Press enter to continue with series 3 > ")
fruit = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruit)
# loop through list and prompt user for yes, keep the item for no, delete it
for i in fruit:
    response = input("Do you like {} (yes/no) ? ".format(i.lower()))
    print(response)
    while response != "yes" or response != "no":
        print("Please enter yes or no")
        response = input("Do you like {} (yes/no) ? ".format(i.lower()))
        if response == "no":
            fruit.remove(i)
print(fruit)
print(" ")

    
    







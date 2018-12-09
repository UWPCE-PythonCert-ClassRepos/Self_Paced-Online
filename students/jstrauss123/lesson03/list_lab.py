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
fruit1 = list(fruit)
print(fruit)
# loop through list and prompt user for yes, keep the item. for no, delete it
for i in fruit1:
    response = input("Do you like {} (yes/no) ? ".format(i.lower()))
    while True:
        if response == 'no':
            print("removing ", i)
            fruit.remove(i)
            break
        elif response == 'yes':
            break
        else:
            print("Please enter yes or no")
            response = input("Do you like {} (yes/no) ? ".format(i.lower()))
print(fruit)
print(" ")


# series 4
# make copy of list, reverse letters in each fruit, delete last item in original list. display both lists
response = input("Press enter to continue with series 4 > ")
fruit = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruit)    
# reverse letter in each fruit and add to list oopy
str1 = ""
fruit1 = list()
# copy list reversing fruit letters
for i in fruit:
    str = ""
    for elem in i:
        str1 = elem + str1
    fruit1.append(str1)
    str1 = ""   
# delete last fruit in original list
fruit.pop()
print(fruit)
print(fruit1)


    







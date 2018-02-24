#!/usr/bin/env python3

fruitlist = ['Apples', 'Pears', 'Oranges','Peaches']

print(fruitlist)
response = input("Please enter a fruit to add to the list > ")
fruitlist.append(response)
print(fruitlist)

response = input("Please enter the number of the fruit of the list to display > ")
print("fruit " + response + " : " + fruitlist[int(response)-1])

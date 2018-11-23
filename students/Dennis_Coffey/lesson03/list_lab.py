#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 21:07:54 2018

@author: denni
"""

"""Lesson 3 - List Lab assignment - Series of 4 steps modifying a list of fruits"""

#Series 1:
#Create list of fruits
fruits = ['Apples','Pears','Oranges','Peaches']
print(fruits)
#Copy original fruits list for use in Series 4
fruits_original = fruits.copy()

#Prompt user for new fruit and then add to list
response = input("Please enter a fruit > ")
fruits.append(response)
print(fruits)

#Prompt user for number and display that number and corresponding fruit in list
response = input("Please enter a number between 1 and " + str(len(fruits)) + " > ")
print(response + ": " + fruits[int(response)-1])

#Add another fruit to the beginning of the list using “+” and display the list.
fruits = ["Banana"] + fruits
print(fruits)

#Add another fruit to the beginning of the list using insert() and display the list.
fruits.insert(0,"Papaya")
print(fruits)

#Display all the fruits that begin with “P”, using a for loop.
for fruit in fruits:
    if fruit.lower().startswith('p'):
        print(fruit)
#Copy Series 1 fruits list result for use in later results
series1_fruits = fruits.copy()

#Series 2:
#Display the list from Series 1
print(fruits)
#Remove the last fruit from the list and display. 
del fruits[-1] 
print(fruits)  

#Ask the user for a fruit to delete, find it and delete it.
response = input("Enter a fruit to delete > ") 
fruits.remove(response)
print(fruits)

#Series 3:
#Again, using the list from series 1:
#Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the fruit all lowercase).
#For each “no”, delete that fruit from the list.
#For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here)
#Display the list.
series3_fruits = series1_fruits.copy()
for fruit in series1_fruits:
    response = input("Do you like " + fruit + "? ")
    while response.lower() not in ['yes','no']:
        response = input("Please answer with a yes or no > ")
    if response.lower() == "no":
        series3_fruits.remove(fruit)
print(series3_fruits)

#Series 4:
#Make a copy of the list from series 1 and reverse the letters in each fruit in the copy.
#Delete the last item of the original list. Display the original list and the copy.
series4_fruits = []
for fruit in series1_fruits:
#    series4_fruits.append(''.join(sorted(fruit)))
    series4_fruits.append(fruit[::-1])

#Delete last item from original series 1 list.  The last item from the original
#list is Peaches
fruits_original.pop()

print("Print of resultant series 1 fruit list with letters for each fruit reversed")
print(series4_fruits)
print("Print of original series 1 fruit list with last fruit from list (Peaches) deleted")
print(fruits_original)
    
                
        
        
        
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

#Series 2:
        
        
        
        
        
        
"""
Author: Alyssa Hong
Date: 10/22/2018
Lesson3 Assignments > List Lab Exercise
"""


#!/usr/bin/env python3
#
#Series 1
#

fruits = ["Apples","Pears", "Oranges","Peaches"]
print(fruits)

response = input("What would you like to add a fruit? ")
fruits.append(response)
print(fruits)

response = input("What number of fruit would you like to see(the number is 1~5 and you can choose just one)? ")
print(fruits[int(response)-1])

print(["Mangos"] + fruits)

fruits.insert(0, 'Blueberries')
print(fruits)

for x in fruits:
    if x.startswith('P'):
         print("the fruit that begin with “P” is ", x)

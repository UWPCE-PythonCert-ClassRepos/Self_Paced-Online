#!/usr/bin/env python3
"""Assignmet 3 List Lab
Ian Sahlberg
Python 210
12/26/2018
"""

"""Series 1
Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
Display the list (plain old print() is fine…).
Ask the user for another fruit and add it to the end of the list.
Display the list.
Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis). Remember that Python uses zero-based indexing, so you will need to correct.
Add another fruit to the beginning of the list using “+” and display the list.
Add another fruit to the beginning of the list using insert() and display the list.
Display all the fruits that begin with “P”, using a for loop."""


fruit_basket = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruit_basket)

user_fruit = input("Tell me another fruit to add to your basket...")
fruit_basket.append(user_fruit)
print(fruit_basket)
user_number = int(input("Can you give me a number 1 thru " + str(len(fruit_basket)) + " ?"))
print("Your number is", user_number, "and the corresponding fruit is", fruit_basket[user_number - 1])

#!/usr/bin/env python3
# Russell Felts
# Assignment 3 - List Lab Exercise

def series1():
    """
    Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
    Display the list (plain old print() is fine…).
    Ask the user for another fruit and add it to the end of the list.
    Display the list.
    Ask the user for a number and display the number back to the user and the
    fruit corresponding to that number (on a 1-is-first basis). Remember that
    Python uses zero-based indexing, so you will need to correct.
    Add another fruit to the beginning of the list using “+” and display the
    list.
    Add another fruit to the beginning of the list using insert() and display the list.
    Display all the fruits that begin with “P”, using a for loop.

    """

    fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
    print(fruit_list)

    response = input("Please enter another fruit: ")
    #print(response)

    fruit_list.append(response)
    print(fruit_list)

    response = input("Please enter a number: ")
    #print(response)

    print(str(response) + " " + fruit_list[int(response)-1])


series1()


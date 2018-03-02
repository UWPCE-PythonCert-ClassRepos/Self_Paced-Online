#!/usr/bin/env python3
"""
Lesson 3 - List Lab
"""

def main():
    fruits = series1()
    

def series1():
    """ Performs a series of actions based off an exisiting list of fruits. """
    fruits = ["Apples", "Pears", "Oranges", "Peaches"]
    print(" ".join(item for item in fruits))  # Test printing these in one line.

    # Prompt user for fruit and append to list.
    fruits.append(str(input("Please enter a fruit: ")))
    print(" ".join(item for item in fruits))

    #   Prompt user for number and display the fruit in it's position.  
    # Note: user input of 1 == index[0]
    # Note: if not int --> default to 1 for easy testing.
    try:
        user_fruit = int(input("Please enter a number: "))
    except ValueError:
        user_fruit = 1
    print( "You have selected number {}.  The fruit at this position is {}"
           .format(user_fruit, fruits[user_fruit-1]))  # -1 to get index pos.
    
    # Add fruit to beginning of the list with '+'.
    fruits = ['Tangerine'] + fruits
    print(" ".join(item for item in fruits))

    # Add fruit to beginning of list with 'insert()'.
    fruits.insert(0, "Pomelo")
    print(" ".join(item for item in fruits))

    # Display all fruits that start with 'P'.
    for item in fruits:
        if item[0].upper() == "P":
            print(item)
    
    return fruits


main()
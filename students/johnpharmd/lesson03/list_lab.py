#!/usr/bin/env python3


def get_fruits():
    """
    Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
    """
    fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
    return fruits


def series1():
    # Call get_fruits to create the fruits list.
    fruits = get_fruits()
    # Create an additional fruit list and fruit string.
    one_fruit = ['Cherries']
    another_fruit = 'Grapes'
    
    # Display the list.
    print('List contains: ', fruits)
    
    # Ask the user for another fruit and add it to the end of the list.
    response = input('Add another fruit: ')
    while not response.isalpha():
        response = input('Only words, please. Add another fruit: ')
    response.lower()
    fruits.append(response.capitalize())
    
    # Display the list
    print('List contains: ', fruits)
    
    """
    Ask the user for a number and display the number back to the user and
    the fruit corresponding to that number (on a 1-is-first basis).
    """
    response = input('Enter a number within the list count: ')
    while not response.isdigit():
        response = input('Only numbers. Enter a number within the list count: ')
    while int(response) not in range(len(fruits) + 1):
        response = input('Enter a number within the list count: ')
    print('You entered', response)
    print('Here is the fruit for that number from the list: ')
    print(fruits[int(response) - 1])
    
    # Add another fruit to the beginning of the list using “+” and
    # display the list.
    fruits = one_fruit + fruits
    print('Adding a fruit to start of list using concatenation:')
    print(fruits)
    
    # Add another fruit to the beginning of the list using insert() and
    # display the list.
    print('Adding a fruit to start of list using insert method:')
    fruits.insert(0, another_fruit)
    print(fruits)
    
    # Display all the fruits that begin with “P”, using a for loop.
    p_fruits = []
    for item in fruits:
        if item[0] == 'P':
            p_fruits.append(item)
    print('These are the fruits that start with "P":', p_fruits)


def series2():
    # Call get_fruits to create the fruits list.
    fruits = get_fruits()
    # Display the list.
    print('List contains:', fruits)
    
    # Remove the last fruit from the list.
    fruits.pop()
    # Display the list.
    print('Popped last item. List now contains:', fruits)
    
    # Ask the user for a fruit to delete, find it and delete it.
    response = input('Enter a fruit to be removed: ')
    while not response.isalpha():
        response = input('Only words, please. Remove which fruit?: ')
    response.lower()
    response.capitalize()
    while response not in fruits:
        response = input('Enter a fruit from the list: ')
        response.lower()
        response.capitalize()
    fruits.remove(response)
    print(response, 'removed. List now contains:', fruits)


def series3():
    # Call get_fruits to create the fruits list.
    fruits = get_fruits()
    
    # Create copy of fruits list, iterate over copy, mutate original.
    """
    Ask the user for input displaying a line like “Do you like apples?”
    for each fruit in the list (making the fruit all lowercase).
    """
    new_fruits = fruits
    for item in new_fruits:
        print('Do you eat {:s}?'.format(item).lower())
        response = input('Enter "y" for yes or "n" for no: ')
        
        # For each “no”, delete that fruit from the list.
        if response == 'n':
            fruits.remove(item)
        """
        For any answer that is not “yes” or “no”, prompt the user to answer
        with one of those two values (a while loop is good here).
        """       
        # while response is not 'y' or 'n':
        #    response = input('Choose "y" for yes or "n" for no: ')
        #    if response == 'y' or 'n':
        #        break
    # Display the list.    
    print('List now contains:', fruits)

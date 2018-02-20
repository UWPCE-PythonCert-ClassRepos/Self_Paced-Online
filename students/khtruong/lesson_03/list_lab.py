#!/usr/bin/env python

"""Sample module docstrings text
"""


def fruit_list():
    '''Return fruit list.'''
    return ['Apples', 'Pears', 'Oranges', 'Peaches']


def add_fruit():
    '''Return user input for type of fruit to add.'''
    return input('Enter a type of fruit to add to list> ')


def remove_fruit(l):
    '''Return user input for type of fruit to delete.'''
    keepgoing = True
    while keepgoing:
        del_item = input('Enter a type of fruit to remove from list> ')
        # looking for valid item...keeps asking user until do
        for item in l:
            if item == del_item:
                keepgoing = False
                break
        else:
            print('{} is not found...try again!'.format(del_item))

        # actually delete the item in list for all occurrences
        for item in l:
            if item == del_item:
                l.remove(item)


def series1():
    """Return a series of action for 'series 1' assignment."""
    # Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
    l = fruit_list()
    # Display the list (plain old print() is fine…).
    print(l)
    # Ask the user for another fruit and add it to the end of the list.
    l.append(add_fruit())
    # Display the list.
    print(l)
    # Ask the user for a number and display the number back to the user and the
    # fruit corresponding to that number (on a 1-is-first basis). Remember that
    # Python uses zero-based indexing, so you will need to correct.
    while True:
        answer = int(input("Enter an integer between "
                           "1 and {:d}!> ".format(len(l))))
        if 1 <= answer <= 5:
            break
    print(answer, l[answer-1])
    # Add another fruit to the beginning of the list using “+” and display
    # the list.
    l = [add_fruit()] + l
    print(l)
    # Add another fruit to the beginning of the list using insert() and display
    # the list.
    l.insert(0, add_fruit())
    print(l)
    # Display all the fruits that begin with “P”, using a for loop.
    for item in l:
        if item[0] == 'P':
            print(item)


def series2():
    """Return a series of action for 'series 2' assignment."""
    # Using the list created in series 1 above:
    l = fruit_list()
    # Display the list.
    print(l)
    # Remove the last fruit from the list.
    del l[-1]
    # Display the list.
    print(l)
    # Ask the user for a fruit to delete, find it and delete it.
    remove_fruit(l)
    print(l)
    # (Bonus: Multiply the list times two. Keep asking until a match is found.
    # Once found, delete all occurrences.)
    l = 2*l
    print(l)
    remove_fruit(l)
    print(l)


def series3():
    """Return a series of action for 'series 3' assignment."""
    # Again, using the list from series 1:
    l = fruit_list()
    # Ask the user for input displaying a line like “Do you like apples?”
    # for each fruit in the list (making the fruit all lowercase).
    # For each “no”, delete that fruit from the list.
    # For any answer that is not “yes” or “no”, prompt the user to answer with
    # one of those two values (a while loop is good here)
    for item in l[:]:
        while True:
            answer = input('Do you like {}? yes or no?> '.format(item.lower()))
            if answer == 'yes':
                break
            elif answer == 'no':
                l.remove(item)
                break
            else:
                string = ' '.join([answer, 'is not a valid response,'
                                           ' please pick yes or no!'])
                print(string)
    # Display the list.
    print(l)


def series4():
    """Return a series of action for 'series 4' assignment."""
    # Once more, using the list from series 1:
    l = fruit_list()
    # Make a copy of the list and reverse the letters in each fruit
    # in the copy.
    mod_l = []
    for item in l:
        mod_l.append(item[::-1])
    # Delete the last item of the original list.
    l.pop()
    # Display the original list and the copy.
    print(l)
    print(mod_l)

series1()
series2()
series3()
series4()

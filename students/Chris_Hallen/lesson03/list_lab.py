#!/usr/bin/env python3

#  Series 1

#  This is the original fruit list we'll begin with
fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']


def show_fruit():
    """ This function prints a list of fruit """
    print(fruits)


show_fruit()  # This function call asks a function - show_fruit - to print out a fruit list


#  This function asks the user for a fruit to add to the existing fruit list and stores it in a variable
another_fruit = input("Please enter another fruit to add to the list: ")


def add_fruit_to_list(another_fruit):
    """ This functions adds a fruit to the end of a fruit list and returns the fruit list """
    fruits.append(another_fruit)
    return fruits


fruits = add_fruit_to_list(another_fruit)  # This function call asks the user for another fruit to add to the end of an existing fruit list


show_fruit()  # This function call asks a function - show_fruit - to print out a fruit list


def ask_for_fruit_num():
    """ This function asks the user for a number of a fruit on a list with an index starting with one """
    num = input("Please enter a number of a fruit on the list: ")
    return num


fruit_num = ask_for_fruit_num()  # This function call asks for a number of fruit from the user based on an index starting with one

# This function changes the user input from a string to an integer and adjusts the user's index beginning from
# one to an index that begins with zero
index_num = int(fruit_num) - 1


def show_added_index_and_fruit(fruit_num, index_num):
    """ This function tells the user what fruit number she picked - based on an index starting with one - and what fruit it is. """
    print(f'You picked fruit number {fruit_num}.  The fruit you picked are the {fruits[index_num]}.')


show_added_index_and_fruit(fruit_num, index_num)
# This function call shows what fruit was added to the fruit list and its index number - based on an index staring with one.


def add_fruit_with_a_plus(fruits):
    """ This functions adds a fruit to the end of a fruit list and returns the fruit list """
    another_fruit = [input("Please enter another fruit to add to the list: ")]
    return another_fruit + fruits


fruits = add_fruit_with_a_plus(fruits)
# This function call asks for a fruit to be added to the end of the fruit list


show_fruit()  # This function call asks a function - show_fruit - to print out a fruit list


def add_fruit_with_insert(fruits):
    """ This functions takes a list of fruit and adds a fruit to the beginning of the list """
    another_fruit = input("Please enter another fruit to add to the list: ")
    fruits.insert(0, another_fruit)
    return fruits


fruits = add_fruit_with_insert(fruits)
# This function call asks for a fruit to be added to the beginning of the fruit list


show_fruit()  # This function call asks a function - show_fruit - to print out a fruit list


def show_words_with_P_to_start(fruits):
    """ This function prints out all the lists of fruit that begins with the letter 'P' """
    print("Here are all the fruits that begin with 'P': ")
    for fruit in fruits:
        if str(fruit).startswith('P'):
            print(fruit)


show_words_with_P_to_start(fruits)  # This function call asks for fruits starting with the letter 'P' to be printed


# Series 2

show_fruit()  # This function call asks a function - show_fruit - to print out a fruit list


def remove_last_fruit_from_list(fruits):
    """ This function takes the fruit list, removes the last fruit from the list, and returns the modified fruit list """
    del fruits[-1]
    return fruits


fruits = remove_last_fruit_from_list(fruits)  # This function call deletes the last fruit from the list and returns the fruit list


show_fruit()  # This function call asks a function - show_fruit - to print out a fruit list


def ask_user_to_delete_a_fruit(fruits):
    """
        This function takes a list of fruit, asks the user to delete a fruit from an index
        starting with one, and returns the modified list of fruit.
    """
    fruit_num = input("Please enter a number of a fruit to delete from 1 to {:d}: ".format(len(fruits)))
    zero_index_fruit_num = int(fruit_num) - 1
    del fruits[zero_index_fruit_num]
    return fruits


fruits = ask_user_to_delete_a_fruit(fruits)  # This function call asks the use to delete a fruit from the list based on an index starting with one

# Series 3


def edit_fruit_list(fruits):
    """
        This function takes a list of fruits, asks the user which fruit(s) from the list
        she wants to delete, deletes them, and returns a modified fruit list.  If a user
        enters a response other than 'yes' or 'no' or 'YeS' or 'nO' (the casing doesn't matter),
        her response will be rejected until she enters 'yes' or 'no'.
    """
    for fruit in reversed(fruits):
        yes_or_no = input("Do you like" + " {}? ".format(fruit).lower())
        yes_or_no = yes_or_no.lower()
        while yes_or_no != 'no' and yes_or_no != 'yes':
            print("Please enter either 'yes' or 'no' to the question.")
            yes_or_no = input("Do you like" + " {}? ".format(fruit).lower())
            yes_or_no = yes_or_no.lower()
        if yes_or_no == 'no':
            fruits.remove(fruit)
    return fruits


fruits = edit_fruit_list(fruits)   # This function call asks for the user to edit the existing fruit list, returns the modified fruit list, and stores it in a variable


show_fruit()  # This function call asks a function - show_fruit - to print out a fruit list

# Series 4


def copy_fruit_list_and_reservse_copy(fruits):
    """
        This function makes a copy of a fruit list, prints out the original fruit
        list with the last item removed, and prints the copy of the original full
        fruit list with the letters in each fruit being reversed.
    """
    fruits_copy = fruits[:]
    del fruits[-1]
    print("Here's the original list with the last item deleted: ")
    print(fruits)
    print("Here the original list with each fruit's letters reversed: ")
    i = 0
    while i < len(fruits_copy):
        fruits_copy[i] = fruits_copy[i][::-1]
        i += 1
    print(fruits_copy)


copy_fruit_list_and_reservse_copy(fruits)


#  The function call above asks to print out a fruit list with the last item removed and
#  a copy of the original fruit list with each fruit's letters in reverse.

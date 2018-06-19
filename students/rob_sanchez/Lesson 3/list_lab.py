#!/usr/bin/#!/usr/bin/env python3
import sys
import time


# Returns a list of fruits based on different scenarios
def series_1():
    fruits = ["Apples", "Pears", "Oranges", "Peaches"]

    print("*** Series 1 ***")
    print("List of fruits:"), fruits
    new_fruit = input('Enter name of new fruit > ')
    fruits.append(new_fruit)
    print (fruits)
    print()
    number = input('Enter a number > ')
    print('You selected: {} - {}...'.format(number, fruits[int(number)-1]))
    print()
    time.sleep(1)
    # Adding a new fruit to the list using '+'
    new_list = ["Plums"] + fruits
    print(new_list[0], "have been added to the beginning of the list...")
    print(new_list)
    time.sleep(1)
    # Adding a new fruit to the beginnning of the list using insert()
    yet_another_fruit = "Pineapples"
    new_list.insert(0, yet_another_fruit)
    print()
    print(yet_another_fruit, "have been added to the beginning of the list...")
    print(new_list)
    time.sleep(1)
    print()
    # Filter all fruits from the list that begin with the letter "P"
    length = len(new_list)
    filtered_items = get_items_with_p(new_list)

    print("These {} fruits begin with 'P':".format(length))
    print(filtered_items)


def series_2():
    # Print initial list
    fruits = ["Apples", "Pears", "Oranges", "Peaches"]
    print(fruits)
    print()
    time.sleep(1)
    # Remove the last fruit from the list
    print('Removing last item ({})...'.format(fruits.pop()))
    print(fruits)
    print()
    time.sleep(1)
    # Remove fruit based on user input
    fruit_to_remove = input('Enter name of fruit to be removed > ')
    print()
    print('{} was removed...'.format(fruit_to_remove))
    fruits.remove(fruit_to_remove)
    print(fruits)
    print()
    time.sleep(1)

    # Double list
    bigger_list = fruits * 2
    print("List x2")
    print(bigger_list)
    print()

    # Prompt for value to be removed
    value_to_delete = input('Enter name of occurrence to be removed > ')

    # Keep prompting user until a matching value is found
    while value_to_delete not in bigger_list:
        value_to_delete = input('Enter name of occurrence to be removed > ')

    # Return a new list where all occurrences have been removed
    new_list = remove_all_instances(bigger_list, value_to_delete)

    print()
    print("All ocurrences of {} have been deleted...".format(value_to_delete))
    print(new_list)


def series_3():
    # Print initial list
    fruits = "Apples", "Pears", "Oranges", "Peaches"
    print (fruits)


def series_4():
    fruits = ["Apples", "Pears", "Oranges", "Peaches"]
    print (fruits)


# ***Helper Functions***
# Returns a filtered list of items that begin with the letter "P"
def get_items_beginning_with_p(list_of_values):
    filtered_list = []
    for item in list_of_values:
        if item.startswith('P') or item.startswith('p'):
            filtered_list.append(item)
    return filtered_list


# Removes all instances from a list
def remove_all_instances(list_of_values, instance):
    filtered_list = []
    for item in list_of_values:
        if instance not in item:
            filtered_list.append(item)
    return filtered_list

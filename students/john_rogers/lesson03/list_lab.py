#!/usr/bin/env python3
"""
Series 2 completed.
Author: JohnR
Version: 2.0
Date: 12/9/2018
Notes: Series 2 completed, but need to add some testing around the inputs
        to insure they're valid (e.g., number when expecting a number).
"""


def main():
    """
    Core script logic.
    :return: Return each function.
    """
    fruit = series_1()
    series_2(fruit)


def series_1():
    """
    Create a list of fruits, then add fruits based on user input.
    :return: Return final list of fruits back to main().
    """
    fruit_list = ['Apples',
                  'Pears',
                  'Oranges',
                  'Peaches',
                ]
    print(fruit_list)

    new_fruit = input('Please enter name of a fruit: ')
    new_fruit = new_fruit.capitalize()
    fruit_list.append(new_fruit)
    print(fruit_list)

    # TODO: Need to check if the number is an integer and within range
    number = int(input('Please enter a number between 1 and 5: '))
    list_length = len(fruit_list) + 2 # this does not work
    if number <= 0 or number >= list_length:
        print('Number is out of range.')
    else:
        print(str(number) + ' is ' + fruit_list[number - 1])

    second_fruit = input('Enter another fruit: ')
    second_fruit = second_fruit.capitalize()
    fruit_list = [second_fruit] + fruit_list
    print(fruit_list)

    third_fruit = input('Enter a third fruit: ')
    third_fruit = third_fruit.capitalize()
    fruit_list.insert(0, third_fruit)
    print(fruit_list)

    for fruit in fruit_list:
        if fruit[0] == 'P':
            print(fruit)

    return fruit_list


def series_2(fruit):
    """
    Display the list, remove the last fruit, display list, ask user input
    for a fruit to delete and then delete it.
    Multiply the list * 2. Keep asking until a match is found, once found
    delete all occurrences.
    :param fruit: The list of fruit to display and work with from series_1.
    :return: No need to return values to main(), series_3 will use the same
            list generated in series_1.
    """
    print('*' * 20)
    print('Series 2 starts here:')
    print('*' * 20)
    print(fruit)

    fruit.pop()
    print(fruit)

    delete_fruit = input('Enter a fruit to delete: ')
    delete_fruit = delete_fruit.capitalize()
    fruit.remove(delete_fruit)
    print(fruit)

    new_list = fruit * 2
    print(new_list)
    delete_me = input('Enter another fruit to delete: ')
    delete_me = delete_me.capitalize()
    if delete_me not in new_list:
        print('Sorry, that item is not in the list.')
    else:
        while delete_me in new_list:
            new_list.remove(delete_me)

    print(new_list)


if __name__ == '__main__':
    main()

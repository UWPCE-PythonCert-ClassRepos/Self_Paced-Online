#!/usr/bin/env python3
"""
Series 3 of 4 completed.
Author: JohnR
Version: 2.6
Date: 12/9/2018
Notes: Series_3 completed.
"""


def main():
    """
    Core script logic.
    :return: Return each function.
    """
    fruit = series_1()
    s2_fruit = fruit[:]
    s3_fruit = fruit[:]
    series_2(s2_fruit)
    series_3(s3_fruit)


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

    number = int(input('Please enter a number between 1 and 5: '))
    if number <= 0 or number > len(fruit_list):
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
    :return: None
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


def series_3(fruit):
    """
    For any answer not yes or no prompt user to answer with correct value
    Remove items when answer is 'no'
    :param fruit:  Use fruit list from series_1
    :return: None
    """
    print('*' * 20)
    print('Start of series 3:')
    print('*' * 20)

    for item in fruit[:]:
        answer = ''
        while answer not in ['yes', 'no']:
            answer = input('Do you like {}?'.format(item.lower()))
        if answer == 'yes':
            print('Me too!')
        else:
            fruit.remove(item)

    print(fruit)


if __name__ == '__main__':
    main()

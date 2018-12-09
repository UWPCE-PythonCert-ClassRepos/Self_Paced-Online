#!/usr/bin/env python3
"""
Series 1 completed.
Author: JohnR
Version: 1.0
Date: 12/9/2018
Notes: Completed series 1 of list lab. For series 2 will need to break
        the below into a separate function and be able to pass the results
        into a second function.
"""


def main():
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

    number = input('Please enter a number between 1 and 5: ')
    number = int(number)
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


if __name__ == '__main__':
    main()

#!/usr/bin/env python3

"""
Lesson3, List Lab Excercises
"""


def is_int(str):
    """Helper function to check that input can be cast into int"""
    try:
        int(str)
        return True
    except ValueError:
        return False


def series1():
    print("::: Series 1 :::::::")

    # print intial list
    fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
    print(fruits)

    # add fruit to end and print
    af = input('Type a fruit to add to the end of the list: ')
    fruits.append(af)
    print(fruits)

    # print fruit at inputted index
    fruit_number = 0
    while not 1 <= fruit_number <= len(fruits):
        try:
            fruit_number = int(input("Enter a number: "))
        except ValueError:
            print("Not a valid number: ")
    print(fruits[fruit_number - 1])

    # concat lists
    fruits = ['Grapes'] + fruits
    print(fruits)

    # insert item
    fruits.insert(0, 'Mango')
    print(fruits)

    # print items starting with 'P'
    for fruit in fruits:
        if fruit[:1] == 'P':
            print(fruit)

    series2(fruits)  # run next series


def series2(fruits):
    print("::: Series 2 :::::::")

    # print list from series1
    print(fruits)

    # remove last fruit
    fruits = fruits[:len(fruits) - 1]
    print(fruits)

    # remove inputted fruit
    rf = input('Type a fruit name to delete: ')
    prompt = "Type the exact fruit name from this list {}: "
    found = False
    while not found:
        if rf in fruits:
            fruits.remove(rf)
            print(fruits)
            found = True
        else:
            rf = input(prompt.format(fruits))

    # multiply list and remove every instance of inputted fruit
    fruits = fruits * 2
    print(fruits)
    rf = input('Type another fruit name to delete: ')
    found = False
    while not found:
        if rf in fruits:
            while rf in fruits:
                fruits.remove(rf)
            found = True
        else:
            rf = input(prompt.format(fruits))
    print(fruits)

    series3(fruits)  # run next series


def series3(fruits):
    print("::: Series 3 :::::::")

    # create copy of list
    fcopy = fruits[:]
    print(fcopy)

    # do you like x
    for fruit in fcopy:
        answer = input('Do you like {}?: '.format(fruit.lower()))
        while answer != 'no' and answer != 'yes':
            question = 'Do you like {}? (Type "yes" or "no"):'
            answer = input(question.format(fruit.lower()))

        # delete unliked fruits
        if answer == 'no':
            fruits.remove(fruit)

    print(fruits)
    series4(fruits)  # run next series


def series4(fruits):
    print("::: Series 4 :::::::")
    # reverse letters in each item of copy
    fcopy = fruits[:]
    for i, fruit in enumerate(fcopy):
        fcopy[i] = fruit[::-1]

    # remove last item from original
    fruits = fruits[:len(fruits) - 1]

    print(fruits)
    print(fcopy)


series1()  # start everything

#!/usr/bin/env python3
# list_lab
# Brandon Henson
# 4/6/18


def series_one():
    print("__________________SERIES 1_______________")
    # Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”
    list1 = ["Apples", "Pears", "Oranges", "Peaches"]
    # Display the list
    print(list1)
    # Ask the user for another fruit
    newfruit = input("Please enter another fruit \n")
    # add it to the end of the list
    list1.append(newfruit)
    # Display the list
    print(list1)
    # Ask the user for a number
    num1 = input("Please enter a number\n ")
    num2 = int(num1) - 1
    # display the number and fruit back to the user
    print(int(num1), list1[num2])
    # Add another fruit to the beginning of the list using “+” and display
    addafruit = input("What fruit do you want to add to the beginning ? \n")
    list2 = [addafruit] + list1
    print(list2)
    # Add another fruit to the beginning of the list using insert() and display
    addafruit2 = input("What fruit do you want to add to the beginning? \n")
    list2.insert(0, addafruit2)
    print(list2)
    # Display all the fruits that begin with “P”, using a for loop
    for i in list2:
        if i.startswith('P'):
            print(i)


def series_two():
    print("__________________SERIES 2_______________")
    list1 = ["Apples", "Pears", "Oranges", "Peaches"]
    # Display the list
    print(list1)
    # Remove the last fruit from the list
    list1.pop()
    # Display the list
    print("This is the list without the last fruit", list1)
    # Ask the user for a fruit to delete, find it and delete it
    delfruit = input("What fruit do you want to delete?\n")
    for i in list1:
        if i.upper() == delfruit.upper():
            list1.remove(i)
        else:
            continue
    print(list1)


def series_three():
    print("__________________SERIES 3_______________")
    list1 = ["Apples", "Pears", "Oranges", "Peaches"]
    print (list1)
    list2 = []
    for i in (list1):
        # Ask the user for input displaying a line like “Do you like apples?”
        while True:
            askiflikefruit = input("Do you like {}?\n".format(i))
            if askiflikefruit.lower() == "no":
                print("okay. i will remove it")
                break
            elif askiflikefruit.lower() == "yes":
                list2.append(i)
                break
            print("Enter 'yes' or 'no' \n")
    list1 = list2
    # Display the list
    print(list1)


def series_4():
    print("__________________SERIES 4_______________")
    list1 = ["Apples", "Pears", "Oranges", "Peaches"]
    # Make a copy of the list
    list2 = list1.copy()
    print (list2)
    for i, fruit in enumerate(list2):
        list2[i] = fruit[::-1]
    # Delete the last item of the original list.
    del list1[-1]
    #  Display the original list and the copy.
    print(list2)
    print()
    print(list1)

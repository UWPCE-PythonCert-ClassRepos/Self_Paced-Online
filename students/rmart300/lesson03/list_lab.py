#!/usr/bin/env python3

def series1():
    """
    Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
    Display the list (plain old print() is fine…).
    Ask the user for another fruit and add it to the end of the list.
    Display the list.
    Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis). Remember that Python uses zero-based indexing, so you will need to correct.
    Add another fruit to the beginning of the list using “+” and display the list.
    Add another fruit to the beginning of the list using insert() and display the list.
    Display all the fruits that begin with “P”, using a for loop.
    """

    fruit_list = ['Apples','Pears','Oranges','Peaches']
    print(fruit_list)
    fruit_to_add = input("enter the name of a fruit > ")
    fruit_list.append(fruit_to_add)
    print(fruit_list)

    list_index = -1
    while list_index < 0 or list_index > len(fruit_list):
        list_index = int(input("choose a position in the fruit list > "))
        list_index -= 1

    print(fruit_list[list_index])

    fruit_to_add = input("enter the name of another fruit > ")
    fruit_list = [fruit_to_add] + fruit_list
    print(fruit_list)

    fruit_to_add = input("enter the name of another fruit > ")
    fruit_list.insert(0,fruit_to_add)
    print(fruit_list)

    print("Here's your P fruits:")
    for fruit in fruit_list:
        if fruit.startswith('P'):
            print(fruit)

    return fruit_list

def series2(fruit_list):
    """
    Using the list created in series 1 above:

    Display the list.
    Remove the last fruit from the list.
    Display the list.
    Ask the user for a fruit to delete, find it and delete it.
    (Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)
    """
    print(fruit_list)
    fruit_list.pop()
    print(fruit_list)
    fruit_to_remove = None
    while fruit_to_remove not in fruit_list:
        fruit_to_remove = input("enter name of fruit to remove from list > ")

    fruit_list = fruit_list*2

    while fruit_to_remove in fruit_list:
        fruit_list.remove(fruit_to_remove)
    print(fruit_list)

def series3(fruit_list):
    """
    Again, using the list from series 1:

    Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the fruit all lowercase).
    For each “no”, delete that fruit from the list.
    For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here)
    Display the list.
    """
    valid_answer = ('Yes','yes','y','Y','No','no','n','N')
    for fruit in fruit_list:
        answer = input("Do you like " + fruit.lower() + " > ")
        while answer not in valid_answer:
            answer = input("Do you like " + fruit.lower() + " (y/n) > ")
        if answer.lower().startswith('n'):
            fruit_list.remove(fruit)

    print("Here's the fruit you like: ")
    print(fruit_list)
        

if __name__ == '__main__':
    fruit_list = series1()
    #fruit_list_copy = fruit_list[:]
    #series2(fruit_list_copy)
    fruit_list_copy = fruit_list[:]
    series3(fruit_list_copy)
    #fruit_list_copy = fruit_list[:]
    #series4(fruit_list_copy)


#!/usr/bin/env python3

#Series 1
def series1():
    fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
    print(fruits)
    add_fruit = input("What fruit do you want to add?\n")
    fruits.append(add_fruit)
    print(fruits)
    num = int(input("Enter a number to choose which fruit you want:\n"))
    while num > len(fruits):
        num = int(input("Enter a number less or equal than {}\n".format(len(fruits))))

    print("The fruit you chose is {}".format(fruits[num-1]))
    some_fruit = input("Add another fruit:\n")
    fruits = [some_fruit] + fruits
    print(fruits)
    another_fruit = input("Add another fruit again:\n")
    fruits.insert(0,another_fruit)
    print(fruits)
    for i in range(len(fruits)):
        if fruits[i][0] == 'P':
            print(fruits[i], end=" ")

#Series 2
def series2():
    fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
    print(fruits)
    fruits.pop()
    print("Fruit list after pop() is {}".format(fruits))
    to_delete = input("Which fruit do you want to delete? \n")
    for f in fruits:
        if f.lower() == to_delete.lower():
            fruits.remove(f)
    print("{} are left in your list".format(fruits))

#Series #3
def series3():
    fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
    fruit_list = fruits[:]
    print([f.lower() for f in fruits])
    for f in fruits:
        ans = input("Do you like {}?\n".format(f))

        while ans.lower() != 'yes' and ans != 'no':
            ans = input("Please answer yes or no.\n")
        if ans.lower() == 'no':
            fruit_list.remove(f)

    print("Here are the fruits you like {}".format(fruit_list))

#Series #4
def series4():
    fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
    new_fruits = fruits[:]
    for i in range(len(new_fruits)):
        new_fruits[i] = new_fruits[i][-1::-1]
    fruits.pop()
    print(new_fruits)
    print(fruits)

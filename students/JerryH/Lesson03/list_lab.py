#!/usr/bin/env python3

fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
#Series 1
def series1():
    print(fruits)
    addFruit = input("What fruit do you want to add?\n")
    fruits.append(addFruit)
    print(fruits)
    num = int(input("Enter a number:\n"))
    print(num)
    print("The fruit is {}".format(fruits[num-1]))
    someFruit = input("Add another fruit:\n")
    fruits = [someFruit] + fruits
    print(fruits)
    anotherFruit = input("Add another fruit again:\n")
    fruits.insert(0,anotherFruit)
    print(fruits)
    for i in range(len(fruits)):
        if fruits[i][0] == 'P':
            print(fruits[i], end=" ")

#Series 2
def series2():
    print(fruits)
    fruits.pop()
    print(fruits)
    toDelete = input("Which fruit do you want to delete? /n")
    for f in fruits:
        if f == toDelete:
            fruits.remove(toDelete)
    print(fruits)

#Series #3
def series3():
    print([f.lower() for f in fruits])
    ans = input("Do you like apples?\n")
    ans = ans.lower()
    while ans != 'yes' and ans != 'no':
        ans = input("Please answer yes or no.\n")

    if ans == 'no':
        fruits.remove('Apples')
    print(fruits)

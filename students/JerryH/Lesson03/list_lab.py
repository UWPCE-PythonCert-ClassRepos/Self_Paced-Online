#!/usr/bin/env python3

#Series 1
fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
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

#!/usr/bin/env python3

# Series 1
fruits = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruits)
fruits.append(input("Enter a fruit: "))
print(fruits)
strInput = input("Enter a number corresponding to a fruit in the list: ")
print(strInput)
print(fruits[int(strInput)-1])
strInput = input("Enter a fruit to add to the beginning of the list: ")
fruits = [strInput] + fruits
print(fruits)
strInput = input("Enter another fruit to add to the beginning of the list: ")
fruits.insert(0, strInput)
print(fruits)
for fruit in fruits:
    if fruit[0].lower() == 'p':
        print(fruit)
    else:
        continue

# Series 2
fruits = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruits)
del fruits[-1]
print(fruits)
fruits.remove(input("Enter a fruit to delete: "))
print(fruits)

# Series 2 Bonus
fruits = ["Apples", "Pears", "Oranges", "Peaches"]
double_fruits = fruits * 2
for fruit in fruits:
    strInput = input('Do you want to delete ' + fruit + '? [yes/no] ')
    if strInput.lower() == 'yes':
        while fruit in double_fruits:
            double_fruits.remove(fruit)
    else:
        continue
print(double_fruits)

# Series 3
fruits = ["Apples", "Pears", "Oranges", "Peaches"]
for fruit in fruits[:]:
    while True:
        strInput = input('Do you like ' + fruit.lower() + '? [yes/no] ')
        if strInput.lower() == 'no':
            fruits.remove(fruit)
            break
        elif strInput.lower() == 'yes':
            break
        else:
            print('Please enter a yes or no answer!')
            continue
print(fruits)

# Series 4
fruits = ["Apples", "Pears", "Oranges", "Peaches"]
fruits_copy = fruits[:]
for i in range(len(fruits_copy)):
    fruits_copy[i] = fruits_copy[i][::-1]
fruits.remove(fruits[-1])
print(fruits)
print(fruits_copy)

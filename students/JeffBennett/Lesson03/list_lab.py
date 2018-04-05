#!/usr/bin/env python3

# Series 1
fruits = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruits)
new_fruit = input("Enter a fruit: ")
fruits.append(new_fruit)
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
for fruit in fruits:  # not functioning
    print(fruit)

# Series 2
fruits = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruits)
del fruits[-1]
print(fruits)
fruit_to_delete = input("Enter a fruit to delete: ")
fruits.remove(fruit_to_delete)

# Series 3
fruits = ["Apples", "Pears", "Oranges", "Peaches"]
for fruit in fruits:
    while True:
        strInput = print(input('Do you like' + fruit.lower() + '? [yes/no]'))
        if strInput.lower() == 'no':
            del fruit
            break
        elif strInput.lower() == 'yes':
            break
        else:
            print('Please enter a yes or no answer!')
            continue
print(fruits)

# Series 4
fruits = ["Apples", "Pears", "Oranges", "Peaches"]
# Three ways to make a copy:
fruits_copy1 = fruits.copy()
fruits_copy2 = list(fruits)
fruits_copy3 = fruits[:]
for i in range(len(fruits_copy2)):
    fruits_copy2[i] = fruits_copy2[i][::-1]
fruits.remove(fruits[-1])
print(fruits)
print(fruits_copy2)

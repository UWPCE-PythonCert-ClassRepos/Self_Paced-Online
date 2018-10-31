#!/usr/bin/env python3
"""
Created on Sun Sep  9 19:00:58 2018

@author: Laura.Fiorentino
"""
# Series 1
print('------Series 1------')
fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']
for it in range(len(fruit_list)):
    print(fruit_list[it])
new_fruit = input("Name another fruit > ")
fruit_list = fruit_list + [new_fruit]
for it in range(len(fruit_list)):
    print(fruit_list[it])
fruitnumber = input("Pick a number between 1 and 5 > ")
print(fruit_list[int(fruitnumber) - 1])
new_fruit = input("Name another fruit > ")
fruit_list.insert(0, new_fruit)
for it in range(len(fruit_list)):
    print(fruit_list[it])
new_fruit = input("Name another fruit > ")
fruit_list = [new_fruit] + fruit_list
for it in range(len(fruit_list)):
    print(fruit_list[it])
print()
print('Fruits that start with P:')
for it in range(len(fruit_list)):
    if fruit_list[it][0] == 'P':
        print(fruit_list[it])
for it in range(3):
    print()

# Series 2
print('------Series 2------')
fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']
for it in range(len(fruit_list)):
    print(fruit_list[it])
print()
print('Remove last fruit')
del fruit_list[-1]
for it in range(len(fruit_list)):
    print(fruit_list[it])
badfruit = input("Name fruit to get rid of > ")
fruit_list.remove(badfruit)
for it in range(len(fruit_list)):
    print(fruit_list[it])
fruit_list = fruit_list*2
print()
print('Double the fruit')
for it in range(len(fruit_list)):
    print(fruit_list[it])
badfruit = input("Name another fruit to get rid of > ")
while badfruit in fruit_list:
    fruit_list.remove(badfruit)
for it in range(len(fruit_list)):
    print(fruit_list[it])
for it in range(3):
    print()

# Series 3
print('------Series 3------')
fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']
new_fruit_list = fruit_list[:]
for fruit in fruit_list:
    yesorno = input("Do you like {} ?>".format(fruit.lower()))
    while yesorno != 'yes' and yesorno != 'no':
        yesorno = input('Please answer yes or no>')
    if yesorno == 'yes':
        print('Ok, keeping {}'.format(fruit.lower()))
    elif yesorno == 'no':
        print('Ok, removing {}'.format(fruit.lower()))
        new_fruit_list.remove(fruit)
print()
print('Ok, here''s your fruit')
for it in range(len(new_fruit_list)):
    print(new_fruit_list[it])

# Series 4
print('------Series 4------')
fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']
new_fruit_list = fruit_list[:]
for it in range(len(fruit_list)):
    new_fruit_list[it] = fruit_list[it][-1::-1]
fruit_list.remove(fruit_list[-1])
print('Old List')
for it in range(len(fruit_list)):
    print(fruit_list[it])
print()
print('New List')
for it in range(len(new_fruit_list)):
    print(new_fruit_list[it])

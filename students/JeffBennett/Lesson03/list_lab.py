#!/usr/bin/env python3


"""
Series 1

Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
Display the list (plain old print() is fine…).
Ask the user for another fruit and add it to the end of the list.
Display the list.
Ask the user for a number and display the number back to the user and the fruit
corresponding to that number (on a 1-is-first basis). Remember that Python uses
zero-based indexing, so you will need to correct.
Add another fruit to the beginning of the list using “+” and display the list.
Add another fruit to the beginning of the list using insert() and display the
list.
Display all the fruits that begin with “P”, using a for loop.
"""
print('Series 1:\n')
fruits = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruits)
fruits.append(input("Enter another fruit: "))
print(fruits)
strInput = input("Enter a number corresponding to a fruit in the list: ")
print(f"Number {strInput} corresponds to {fruits[int(strInput)-1]}")
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

"""
Series 2

Using the list created in series 1 above:

Display the list.
Remove the last fruit from the list.
Display the list.
Ask the user for a fruit to delete, find it and delete it.
"""
print('\nSeries 2:\n')
fruits = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruits)
del fruits[-1]
print(fruits)
fruits.remove(input("Enter a fruit to delete: "))
print(fruits)

"""Series 2 Bonus

Multiply the list times two. Keep asking until a match is
found.  Once found, delete all occurrences.
"""
print('\nSeries 2 Bonus:\n')
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

"""
Series 3

Again, using the list from series 1:

Ask the user for input displaying a line like “Do you like apples?” for each
fruit in the list (making the fruit all lowercase).
For each “no”, delete that fruit from the list.
For any answer that is not “yes” or “no”, prompt the user to answer with one
of those two values (a while loop is good here).
Display the list.
"""
print('\nSeries 3:\n')
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

"""
Series 4

Once more, using the list from series 1:

Make a copy of the list and reverse the letters in each fruit in the copy.
Delete the last item of the original list. Display the original list and
the copy.
"""
print('\nSeries 4:\n')
fruits = ["Apples", "Pears", "Oranges", "Peaches"]
fruits_copy = fruits[:]
for i in range(len(fruits_copy)):
    fruits_copy[i] = fruits_copy[i][::-1]
fruits.remove(fruits[-1])
print(fruits)
print(fruits_copy)

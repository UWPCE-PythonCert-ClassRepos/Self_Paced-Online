## Ian Letourneau
## 04/30/2018
## A script to run various functions utilizing lists

#!/usr/bin/env python3

#Series One: Print List. rompt user for a fruit to add. Display fruit based on index given by user. Insert two fruits using '+' and .insert.
#Display fruits with first letter 'P'.
fruits = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruits)
fruitAdd = input("Please add another fruit: ")
fruits.append(fruitAdd)
print(fruits)
number = int(input("Please give a number to display: "))
print(str(number) + " - " + fruits[number-1])
fruits = ["Bananas"] + fruits
print(fruits)
fruits.insert(0, "Avocados")
print(fruits)
for fruit in fruits:
    if fruit[0].lower() == 'p':
        print(fruit)

#Series Two: Remove last entry of fruit list. Multiply list by 2 and remove every instance of user prompted fruit. Display fruit list.
fruits2 = fruits.copy()
print(fruits2)
fruits2.pop()
print(fruits2)
#removeFruit = input("Please enter a fruit to remove: ")
#fruits2.remove(removeFruit)
fruits2 = fruits2*2
print(fruits2)
removeFruit = input("Please enter a fruit to remove: ")
if removeFruit in fruits2:
    while removeFruit in fruits2:
        fruits2.remove(removeFruit)
print(fruits2)

#Series Three: Ask user if they like each fruit in fruit list. If answer is 'no', remove fruit from list. If answer is neither 'yes' nor 'no',
#prompt user for a valid answer until valid answer is given. Display fruit list between each iteration.
fruits3 = fruits.copy()
count = 0
while count < len(fruits3):
    response = input("Do you like " + fruits3[count].lower() + '? ')
    while response != 'yes' and response != 'no':
        response = input("Invalid answer. Do you like " + fruits3[count].lower() + '? ')
    if response == 'no':
        fruits3.remove(fruits3[count])
    else:
        count += 1
    print(fruits3)

#Series Four: Copy fruit list into a new list. Reverse new list. Remove last entry of original list. Display lists.
new_fruits = fruits.copy()
for fruit in range(0,len(new_fruits)):
    new_fruits[fruit] = ''.join(reversed(new_fruits[fruit]))
fruits.pop()
print(fruits)
print(new_fruits)

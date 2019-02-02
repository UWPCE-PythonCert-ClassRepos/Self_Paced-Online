#!/usr/bin/env python3
###Series 1####

fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruits)

response_fruit = input("Which fruit do you want to add?")
if response_fruit is not '':
    fruits.append(response_fruit)

print(fruits)

try:
    response_no = int(input("Which Number of Fruit do you want?"))
    print(fruits[response_no - 1])
except ValueError:
    print("expecting an integer value")

response_fruit = input("Which fruit do you want to add at the beginning?")
if response_fruit is not '':
    fruits = [response_fruit] + fruits
print(fruits)

response_fruit_0 = input("Another fruit do you want to add at the beginning?")
if response_fruit is not '':
    fruits.insert(0,response_fruit_0)
print(fruits)

for fruit in fruits:
    if fruit[0] == 'P':
        print(fruit)

###Series 2####

print(fruits)
fruits.remove(fruits[-1])
print(fruits)
remove_response_fruit = input("Which fruit do you want to delete?")
try:
    fruits.remove(remove_response_fruit)
    print(fruits)
except ValueError:
    print("This fruit is not in the list")



###Series 3###
print(fruits)
print(len(fruits))
fruits_remove = []
for fruit in range(len(fruits)):
    response_from_user = input("Do you like" + ' ' + fruits[fruit].lower() + "?")
    while response_from_user not in ['yes', 'no']:
        response_from_user = input("Do you like" + ' ' + fruits[fruit].lower() + "?")
    if response_from_user == 'no':
        fruits_remove.append(fruits[fruit])
print("Fruits to be removed " + fruits_remove)
for fruit in fruits_remove:
    fruits.remove(fruit)
print("Fruits after removing the not liked ones " + fruits)

###Series 5###
# Once more, using the list from series 1:
#
#     Make a copy of the list and reverse the letters in each fruit in the copy.
#     Delete the last item of the original list. Display the original list and the copy.

fruits_series = ['Apples', 'Pears', 'Oranges', 'Peaches']
fruits_series_copy = fruits_series
fruits_series_copy_rev = []
print(fruits_series_copy)
for fruit in range(len(fruits_series_copy)):
    fruit_rev = fruits_series_copy[fruit]
    fruits_series_copy_rev.append(fruit[::-1])

print("Fruits to be removed " + fruits_remove)
for fruit in fruits_remove:
    fruits.remove(fruit)
print("Fruits after removing the not liked ones " + fruits)
fruit1 = fruits_series[0]
print(fruit1[::-1])

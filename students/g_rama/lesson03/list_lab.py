#!/usr/bin/env python3
fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruits)

response_fruit = input("Which fruit do you want to add?")
if response_fruit is not '':
    fruits.append(response_fruit)

print(fruits)

response_no = int(input("Which Number of Fruit do you want?"))
print(fruits[response_no-1])

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

#!/usr/bin/env python3

#Series 1
fruit = ["Apples", "Pears", "Oranges", "Peaches"]
response = input("Add another fruit: ")
fruit.append(response)
print(fruit)

number = int(input("Input a number: "))
print(number, fruit[number-1])

first = input("And another one: ")
first_list = [first]
fruit = first_list + fruit
print(fruit)

first = input("And another one: ")
fruit.insert(0, first)
print(fruit)
j=0
p_fruit=[]
for i in fruit:
    if fruit[j][0]=="P":
        p_fruit.append(fruit[j])
    j=j+1
print(p_fruit)
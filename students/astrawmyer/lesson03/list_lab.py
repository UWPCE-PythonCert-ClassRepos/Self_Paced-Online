#!/usr/bin/env python3

# Series 1
""" fruit = ["Apples", "Pears", "Oranges", "Peaches"]
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

# Series 2
# Made fruit2 so list from first sequence unchanged for series 3 and 4.
fruit2 = fruit
print(fruit2)
fruit2.pop()
print(fruit2)
response = input("Type a fruit to delete:")
fruit2.remove(response)
print(fruit2) """

# Series 3
fruit = ["Apples", "Pears", "Oranges", "Peaches"]
fruit3 = fruit
for i in fruit3:
    response = input("Do you like " + i.lower() + "?")
    if response == "no":
        fruit3.remove(i)
print(fruit3)

# look into how enumerate woorks to fix this/make it easier.
#!/usr/bin/env python3

print("Series 1")
fruit = ["Apples", "Pears", "Oranges", "Peaches"]

print(fruit)
fruit.append(input("Please name a fruit: "))
print(fruit)
val = int(input("Please enter a number: "))
print("Fruit " + str(val) + " is " + fruit[val-1])
fruit = ["Melons"] + fruit
print(fruit)
fruit.insert(0, "Apricots")
print(fruit)
for item in fruit:
    if item[0] == "P":
        print(item)

print("Series 2")
print(fruit)
fruit.pop()
print(fruit)
fruit.remove(input("Please select a fruit from the list to be removed: "))

print("Series 3")
for item in fruit:
    ans = input("Do you like " + item + "?")
    while ans.lower() != "yes" and ans.lower() != "no":
        ans = input("Please answer yes or no.")
    if ans.lower() == "no":
        fruit.remove(item)
print(fruit)

print("Series 4")
reverse = list()
for item in fruit:
    reverse.append(item[::-1])
fruit.pop()
print(fruit)
print(reverse)

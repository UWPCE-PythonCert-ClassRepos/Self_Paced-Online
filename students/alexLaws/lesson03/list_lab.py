#!/usr/bin/env python3

# Series 1

fruit = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruit)

fruit.append(input("Enter a fruit to add to the list: "))
print(fruit)

num = input("Enter a number: ")
print("You chose number ", num, ". The corresponding fruit is " + fruit[int(num)-1])

fruit = ["Strawberries"] + fruit
print(fruit)

fruit.insert(0, "Blueberries")
print(fruit)

for fr in fruit:
    if fr[0] == "P":
        print(fr)

# Series 2

fr_two = fruit[:]
print(fr_two)
fr_two.pop()
print(fr_two)

while True:
    rm = input("Pick a fruit to remove: ")
    if rm in fr_two:
        fr_two = list(filter(lambda x: x != rm, fr_two))
        break
    else:
        fr_two += fr_two
        print("That fruit isn't in the list.")

print(fr_two)

# Series 3

print(fruit)

fr_three = fruit[:]
for fr in fruit:
    while True:
        if fr == "Apples":
            like = input("How do you like them %s: " % fr.lower())
        else:
            like = input("Do you like %s: " % fr.lower())
        if like.lower() == "yes":
            break
        elif like.lower() == "no":
            fr_three.remove(fr)
            break
        else:
            print("Please respond with a Yes or No.")

print(fr_three)

# Series 4

fr_four = []
for fr in fruit:
    fr_four.append(fr[::-1])
print(fr_four)
fruit.pop()

print(fruit)
print(fr_four)

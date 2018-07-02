#!/usr/bin/env python3

#SERIES 1
print ("~~~~~~~~~~~~~~~SERIES 1~~~~~~~~~~~~~~~")
fruit = ["Apple", "Pears", "Oranges", "Peaches"]
print (fruit)
another = input("What other fruit would you like: ")
fruit.append(another)
print(fruit)
a = int(input("What number fruit would you like? "))
if a > 5:
	a = int(input("Please provide a number between 1 and 5: "))
print (fruit[a - 1])
fruit = fruit + ["Kiwi"]
print (fruit)
fruit.insert(0, "Dragon")
print(fruit)
for i in fruit:
	if i[0] == "P":
		print(i)

#SERIES 2
print ("~~~~~~~~~~~~~~~SERIES 2~~~~~~~~~~~~~~~")
print (fruit)
del fruit [0]
print (fruit)
b = input("Which fruit would you like to delete? ")
fruit.remove(b)
print(fruit)
fruit = fruit * 2
print(fruit)
c = input ("Which fruit would you like to delete? ")
for i in fruit:
	if i == c:
		fruit.remove(c)
print(fruit)

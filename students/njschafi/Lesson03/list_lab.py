#!/usr/bin/env python3

##SERIES 1
fruit =['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruit)
response = input("Please enter another fruit: ")
fruit.append(response)
print(fruit)
response2 = int(input("Please enter a number above 0: "))
print(fruit[response2-1])
fruit = ['Lemon'] + fruit
print(fruit)
fruit.insert(0,'banana')
print(fruit)
for item in fruit:
	if item[0] == 'P': ##or try item[0:1] or use CONTAINS
		print(item[0])
		


##SERIES 2		
print(fruit)
fruit = fruit[:-1]
print(fruit)
response3 = input("Please enter a fruit to delete: ")
if response3.title() in fruit:
	fruit.remove(response3.title())
print(fruit)
##Bonus Round
while m in fruit:
	if m == fruit[p]:
		fruit.remove(fruit[p])
	else:
		p += 1

##SERIES 3
fruit =['Apples', 'Pears', 'Oranges', 'Peaches']
response4 = input("Do you like apples?") ##make dynamic in a for loop


###SERIES 4
fruit =['Apples', 'Pears', 'Oranges', 'Peaches']
fruit2 =[]
for item in fruit:
	fruit2.append(item[::-1])
fruit = fruit[:-1]
print(fruit)
print(fruit2)

			
	
	
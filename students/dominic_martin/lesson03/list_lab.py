#!/usr/bin/env Python 3

fruit = ['Apples', 'Pears', 'Oranges', 'Peaches', 'Strawberries',
		'Bananas', 'Tangerines', 'Kiwis', 'Grapes']
print(fruit)

choice = int(input("What would you like to do? \nAdd Fruit - 1\n"
		"Choose Fruit - 2\nDelete Fruit - 3\nLike Fruit - 4\n"
		"Reverse Fruit - 5\nEnter Response:"))


def addFruit(choice):
	if choice == 1:
		newFruit = input("Type the name of a fruit to add to the list:")
		fruit.append(newFruit)
		print(fruit)

def whichFruit(choice):
	if choice == 2:
		c = int(input("Starting with the leftmost fruit, type \n"
		"a number to display the desired fruit:"))
		print(fruit[c])

def delFruit(choice): 

	print(fruit)
	if choice == 3:
		fruit.pop(-1)
		print()
		print("The last item has been removed.\n",fruit)
		pick1 = input("Type the name of fruit you wish to remove:")
		a = fruit.index(pick1)
		fruit.pop(int(a))
		print(fruit)


def likeFruit(choice):
	''' This function needs a way to cycle through the index.  Everything
	works except function skips over indices.'''
	print(fruit)
	if choice == 4:
		running = True
		while running:
			for i in fruit[:]:
				a = int(input("How do you like them " + i + "?\n"
				"'I like them!' - 1\n'I hate them!' - 2\n"
				"Enter your response:"))
				if a == 1:
					print()
					print("We'll keep it on the list!")
				else:
					print()
					fruit.remove(i)
					print("That's too bad, so sad.")
					print("This is what remains:", fruit)
					

def copyFruit(fruit):
	if choice == 5:
		fruitCopy = fruit[:]
		fruitCopy = [x[::-1] for x in fruitCopy][:]
		print(fruitCopy)
		print()
		fruit.pop(-1)
		print(fruit)
		fruitCopy = fruit


addFruit(choice)
whichFruit(choice)
delFruit(choice)
likeFruit(choice)
copyFruit(fruit)
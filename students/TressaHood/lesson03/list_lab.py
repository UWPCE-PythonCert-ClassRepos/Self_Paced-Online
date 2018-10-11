#!/usr/bin/env python3

#lesson 03, Lists exercise



def series_one():
	"""
	Start with a default list and get user input to create new lists
	Return l: the modified list
	"""
	#series one
	l = ["Apples", "Pears", "Oranges", "Peaches"]

	#print the default list
	print(l)

	#ask the user for another fruit
	response = input("Please give me another fruit: ")

	#add that new fruit to the list
	l.append(response)
	print(l)

	#ask the user for a number
	response = int(input("Please give me a number: "))

	#display number back and give the fruit, accounting for 0 index
	num = response-1
	print("Your number was: {}".format(response) + ", your chosen fruits are {}".format(l[num]))

	#ask the user for another fruit
	response = input("Please give me another fruit: ")

	#add that new fruit to the list with + 
	l = [response] + l
	print(l)

	#ask the user for another fruit
	response = input("Please give me another fruit: ")

	#add that new fruit to the list with insert
	l.insert(0, response)
	print(l)

	#display all fruits beginning with "P", using a for loop
	for item in l:
		if item[0] == "P":
			print(item)

	#return your list
	return l

def series_two(l):
	"""
	Start with the list from other step and remove items based on user input
	:param l: the list from step 1
	"""
	#series two
	print("Here is your list {}".format(l))

	#remove the last item from the list
	l.pop()
	print("Removed last item, new list: ", l)

	#ask for a fruit to remove
	response = input("Please give me a fruit to remove: ")

	#remove it
	l.remove(response)
	print(l)

def series_three(l):
	"""
	Start with the list from the first step and remove items based on user input
	:param l: the list from step 1
	"""
	#series three
	l_copy = l.copy()
	
	#set up the for loop to ask the questions
	for item in l:
		print("Do you like {}?".format(item.lower()))
		#set up the while loop with a flag
		response = None
		while response != "yes" and response != "no":
			response = input("yes or no: ")

			#now the if statement for no
			if response == "no":
				l_copy.remove(item)


	print("Here is your final list {}".format(l_copy))

def series_four(l):
	"""
	Start with the list from the first step and copy it, then revers the letters, then delete the last item
	of the original list, displaying both
	:param l: the list from step 1
	"""
	#series four
	l_copy = l.copy()

	#use a bank list to add the items
	rev_list = []

	#create a for loop to get to each item for reversing the letters (iterate over copy)
	for item in l_copy:
		rev_list += [item[::-1]]

	print("Reversing items in copy!")
	print("Deleting last item from list!")
	l.remove(l[-1])

	print("Final reversed items in copy: {}".format(rev_list))
	print("Final original copy, with last item removed {}".format(l))





#define the main function
def main():
	"""
	This is the main function that calls the program
	"""

	print("Starting Series One")
	print()
	fruit_list = series_one()
	print("Starting Series Two")
	print()
	series_two(fruit_list)
	print("Starting Series Three")
	print()
	series_three(fruit_list)
	print("Starting Series Four")
	print()
	series_four(fruit_list)


#call the main function
main()

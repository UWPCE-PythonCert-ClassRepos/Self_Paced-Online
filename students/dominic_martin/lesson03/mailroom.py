#!usr/bin/env Python 

dnd = {'Ted Bayer': 500, 'Panfila Alvarez': 700, 'JR Reid': 330, 'Simon Laplace': 440, 'Jennifer Meyers': 800}

a = int(input("What would you like to do?\nSend a Thank You? - (1)\nCreate a Report? - (2)\nQuit? - (3)\nEnter your response:"))


def choices(a):
	'''	This function presents the user with choices.'''
	global dnd
	if a == 1:
		thanks(a)
	if a == 2:
		genReport(a)
	if a == 3:
		quitAll(a)


def thanks(a):
	'''	This function gives the option to enter a name already on the list, or enter a new name. If the user enters a new name, another function is called.  If a current name is entered, a function is called.  If the user wants to see a list of names, a list is printed.'''
	global dnd 
	b = str(input("Who would you like to send a thanks to?\n"
		"Type 'list' or enter a name:")) 
	if b in dnd.items():
		print()
		print(b)
		donamt(b)
	if b == 'list':
		print()
		for x in dnd.keys():
			print(x)	
	else:
		newDonor(b)


def newDonor(b):
	'''	If a new name is entered, the dictionary is updated with the name and a default donation of $0.'''
	print()
	dnd.update({b:0})
	newDonat = 0
	for name, donat in dnd.items():
		if donat == newDonat:
			print(name)
			print()
			donamt(b)
			a == None


def donamt(b):
	'''	This function allows the user to enter a donation amount for either a new or current name.  The function updates the current donation amount for the name.'''
	global dnd
	print()
	d = int(input("Enter a donation amount:"))
	print()
	e = int(dnd[b]) + d
	dnd.update({b:e})
	for name, donat in dnd.items():
		if b == name:
			print(b + " has donated: " + str(e))
	tyemail(b)


def tyemail(b):
	'''	This function sends a thank you message to the previously chosen name.'''
	global dnd
	print()
	for name, donat in dnd.items():
		if b == name:
 			print(name + ", thank you so much for your donation.  It's going to a wonderful cause to help lessen the greenhouse emissions from our production plant.  Thanks again and Happy Holidays!")
 			a == None
 			

def genReport(a):
	'''	This function generates a report that shows a list of names and their associated donations.'''
	global dnd
	print()
	width1 = 27
	p = ('Name:', 'Amount:')
	print(f'{p[0]:{width1}}{p[1]:{width1}}')
	for name, donat in dnd.items():
		print(f'{name:{width1}}{"$"+str(donat):{width1}}')
		

def quitAll(a):
	'''	This function quits the program.'''
	print()
	print("Thanks for using The Mailroom Application!  Goodbye!")

choices(a)



#!usr/bin/env Python3

# donation_list = {'name': ('Ted Bayer', 'Panfila Alvarez', 'JR Reid', 'Simon Laplace', 'Jennifer Meyers'), 'donation': (500, 700, 330, 440, 800)}
donation_list1 = {'Ted Bayer': 500, 'Panfila Alvarez': 700, 'JR Reid': 330, 'Simon Laplace': 440, 'Jennifer Meyers': 800}
names = ['Ted Bayer', 'Panfila Alvarez', 'JR Reid', 'Simon Laplace', 'Jennifer Meyers']
donations = [500, 700, 330, 440, 800]
namesDonations = {name: donation for name, donation in zip(names, donations)}


def choices(a):
	global namesDonations # new 
	switch_dict = {1:thanks, 2:genReport, 3:writeLetters, 4:quitAll}
	switch_dict.get(a, quitAll)()	
	print()

def thanks():
	global namesDonations # new
	b = int(input("Who would you like to send a thanks to?\n(1) - Ted Bayer\n(2) - Panfila Alvarez\n(3) - JR Reid\n(4) - Simon Lapalce\n(5) - Jennifer Meyers\n(6) - Enter a new name\nEnter your choice:"))	
	nameIdx = (int(b - 1))
	if nameIdx < 5:
		donamt(nameIdx)
	if nameIdx == 5:
		newDonor(nameIdx)

def newDonor(nameIdx):
	global names
	global donations
	try:
		newName = str(input("Enter a new name:"))
		nameCheck = any(str.isdigit(c) for c in newName)
		if nameCheck == True:
			print("Please use letters only. Try again.")
			print()
			newName = str(input("Enter a new name:"))
	except:
		pass
	print()
	names.append(newName)
	donations.append(0)
	print()
	donamt(nameIdx)

def donamt(nameIdx):
	global names
	global donations
	print()
	newDonation = int(input("Enter a donation amount:"))
	enumerate(donations.append[nameIdx](newDonation))
	print()
	print(str(names[nameIdx]) + " has donated " + "$" + str(newDonation))
	tyemail(nameIdx)


def tyemail(nameIdx):
	global names
	print()
	print(str(names[-1]) + ", thank you so much for your donation.  It's going to a wonderful cause to help lessen the greenhouse emissions from our production plant.  Thanks again and Happy Holidays!")
	

def genReport():
	global namesDonations
	print()
	width1 = 27
	p = ('Name:', 'Amount:')
	print(f'{p[0]:{width1}}{p[1]:{width1}}')
	# for name, donation in donation_list1.items():
	for name, donation in namesDonations.items(): # new
		print(f'{name:{width1}}{"$"+str(donation):{width1}}')
			

def writeLetters():
	global namesDonations
	for key in namesDonations.keys():
		with open('%s.txt'%(key,), 'w') as f:
			f.write(key  + "\n\nThanks for your donation!\n\nAll the Best,\n\nThe Mailroom Team") 		
		

def quitAll():
	print()
	print("Thanks for using The Mailroom Application!  Goodbye!")


while True:
	try:
		a = int(input("What would you like to do?\n(1) - Send a Thank You?\n(2) - Create a Report?\n(3) - Send Letters to Everyone?\n(4) - Quit?\nEnter your response:"))
		if a in range(0,4):
			choices(a)
	except TypeError:
	
		print("\nIncorrect Input.  Try again.")
	else:
		break
		

	



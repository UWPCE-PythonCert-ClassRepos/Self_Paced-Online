#!usr/bin/env Python3

donation_list = {'name': ('Ted Bayer', 'Panfila Alvarez', 'JR Reid', 'Simon Laplace', 'Jennifer Meyers'), 'donation': (500, 700, 330, 440, 800)}
donation_list1 = {'Ted Bayer': 500, 'Panfila Alvarez': 700, 'JR Reid': 330, 'Simon Laplace': 440, 'Jennifer Meyers': 800}


a = int(input("What would you like to do?\n(1) - Send a Thank You?\n(2) - Create a Report?\n(3) - Send Letters to Everyone?\n(4) - Quit?\nEnter your response:"))


def choices(a):
	global donation_list
	switch_dict = {1:thanks, 2:genReport, 3:writeLetters, 4:quitAll}
	switch_dict.get(a, quitAll)()	
	print()

def thanks():
	global donation_list
	b = int(input("Who would you like to send a thanks to?\n(1) - Ted Bayer\n(2) - Panfila Alvarez\n(3) - JR Reid\n(4) - Simon Lapalce\n(5) - Jennifer Meyers\n(6) - Enter a new name\nEnter your choice:"))	
	nameIdx = (int(b - 1))
	if nameIdx < 5:
		donamt(nameIdx)
	if nameIdx == 5:
		newDonor(nameIdx)

def newDonor(nameIdx):
	global donation_list
	newName = str(input("Enter a new name:"))
	print()
	donation_list['name'][nameIdx] = newName
	donation_list['donation'][nameIdx] = 0
	print()
	donamt(nameIdx)

def donamt(nameIdx):
	global donation_list
	print()
	newDonation = int(input("Enter a donation amount:"))
	print()
	print(str(donation_list['name'][nameIdx]) + " has donated " + "$" + str(donation_list['donation'][nameIdx]))
	tyemail(nameIdx)


def tyemail(nameIdx):
	global donation_list
	print()
	print(str(donation_list['name'][nameIdx]) + ", thank you so much for your donation.  It's going to a wonderful cause to help lessen the greenhouse emissions from our production plant.  Thanks again and Happy Holidays!")
 
def genReport():
	global donation_list1
	print()
	width1 = 27
	p = ('Name:', 'Amount:')
	print(f'{p[0]:{width1}}{p[1]:{width1}}')
	for name, donation in donation_list1.items():
		print(f'{name:{width1}}{"$"+str(donation):{width1}}')
			

def writeLetters():
	global donation_list
	for name in donation_list['name']:
		with open('%s.txt'%(name,), 'w') as f:
			f.write(name  + "\n\nThanks for your donation!\n\nAll the Best,\n\nThe Mailroom Team") 		
		

def quitAll(a):
	print()
	print("Thanks for using The Mailroom Application!  Goodbye!")

choices(a)



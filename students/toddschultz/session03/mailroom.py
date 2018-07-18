#!/usr/bin/env python3

global donors
donors = ["Imp", 100.00, "Fred Flintstone", 50.00, 50.00, "Mighty Mouse", 420, 1.00, 1.00, "Road Runner", 999.00, "Papa Smurf", 1000.00, 1000.00, 1000.00]

def prompt():
	action = input("Would you like to (S)end a Thank You, (C)reate a Report or (Q)uit? ")
	if action.lower() == "s":
		thank_you()
	elif action.lower() == "c":
		create_report
	elif action.lower() == "q":
		print("Have a nice day!")
	else:
		print("Please enter S, C, or Q.")
		prompt()

def thank_you():
	person = (input("Who would you like to send a Thank You to? "))
	if person.lower() == "list":
		try_again()
	elif person in donors: 
		donation = float(input("How much was the donation? "))
		location = donors.index(person)
		donors.insert((location + 1),donation)
		print("\n\n" + person + ":\n")
		print("\tThank you very much for your generouse donation.")
		print(f'Your donated ${donors[location+1]:.2f} will allow us to continue our efforts.')
		print("Our charity would not exist without your support.\n")
		print("Sincerely:\n\nLeadership Team at Charity X.\n\n")
		prompt()
	else:
		try_again()

def try_again():
		donors_list = []
		for i in donors:
			if type(i) is str:
				donors_list.append(i)
		print(donors_list) #todo: Make this appear not in bracket, join?
		print("Please select from the names above, be sure to spell them correctly.")
		thank_you()

def create_report():
	print('This is where the report will go.')
'''
		all_donations = []
		while type(donors[current]) is float:
			all_donations.append(donors[current])
			current += 1
'''

prompt()
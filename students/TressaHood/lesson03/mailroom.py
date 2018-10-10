#!/usr/bin/env python3

#lesson 03, Mailroom Assignment

def menu_selection():
	"""
   	This function gives the user a menu selection, and prompts them for the correct
	submission. Depending on their selection either exits or returns the response.
	:return response: the user's response returned to main function
	"""
	#Start prompts for mailroom
	print("Welcome to the mailroom, please choose an action: \n\tSend a Thank You: Press 1\n\t Create a Report: Press 2 \n\t\t    Quit: Press 3")
	response = input("\nWhat action would you like to choose?")

	#create the selection
	while True:
		if response == "1" or response == "2":
			return response
		elif response == "3":
			print("Goodbye")
			break
		else:
			response = input("You did not select 1, 2, or 3. Please choose again:")

#define the function for thank yous
def thank_you():
	"""
	Prompt the user for more information to create the thank you, then call the email function to write it
	"""
	print("\nYou have choosen to create a Thank You Note")
	response = input("Please give me the full name of the donor or type 'list' to see all current donors: ")

	#create the selection
	while True:
		if response == "list":
			#print the list of donors
			print("\n" + ", ".join(donors[0::2]) + "\n")
			response = input("Please give me the full name of the donor: ")
		elif response in donors[0::2]:
			#find their donation amount
			index = donors.index(response)
			amount = float(input("How much did they donate? "))
			email(response, amount)

			#add the new donation to the total and average
			donors[index+1][0] = donors[index+1][0] + amount
			donors[index+1][1] = donors[index+1][1] + 1
			donors[index+1][2] = donors[index+1][0] / donors[index+1][1]
			break		

		else:
			#there is a new donor
			print("Great! A new donor! Adding to {} database now...".format(response)) 
			amount = float(input("How much did they donate? "))
			donors.append(response)
			donors.append([amount, 1, amount])
			
			#call the email
			email(response, amount)
			break


#define the email function
def email(name, donation):
	"""
	Print the email with the donor name and amount included
	"""
	print("\nCreating the email: ")
	print("Dear {}, \nThank you for your generous donation of ${:.2f}. We appreciate all that you do for us!\n\nBest, \nMailroom Assitant\n".format(name, donation))



#define the function for the reports
def report():
	"""
	Print a formatted report of all donations thus far
	"""
	#print the headers
	print("\n{:<20}| {:<20}| {:<20}| {:<20}".format("Donor Name", "Total Given", "Num Gifts", "Average Gifts"))
	print("----------"*8)

	#go through the sorted list
	for entry in sorted(donors[1::2], reverse = True):
		index = donors.index(entry)
		#print it
		print("{:<20} ${:<20.2f} {:<20d} ${:<20.2f}\n".format(donors[index-1], donors[index][0], donors[index][1], donors[index][2]))


#define the main function
if __name__ == '__main__':
	"""
	This is the main function that calls the program and sets up the donor starting list
	"""
	donors = ["Sarah Sanderson", [3000, 3, 1000], "Amy Anderson", [300, 2, 150], "Erin Eckoff", [12536.26, 1, 12536.26], 
				"Cassandra Cooper", [234.34, 2, 117.17], "Debbie Danger", [9809.56, 3, 3269.85]]

	while True:
		#get the user info by prompting with a menu selection
		user_response = menu_selection()

		#decide on next step
		if user_response == "1":
			thank_you()
		elif user_response == "2":
			report()
		else:
			break









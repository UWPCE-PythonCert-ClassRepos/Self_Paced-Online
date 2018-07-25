'''
Shin Tran
Python 210
Lesson 3 Assignment
'''

masterList = []
nameList = []


# Creates the masterList where it has 12 donations pre-populated
def initialize():
	global masterList
	d1 = ["James Smith", 91561.25]
	d2 = ["Mary Johnson", 5811.05]
	d3 = ["John Williams", 41113.42]
	d4 = ["Patricia Brown", 19184.81]
	d5 = ["Robert Jones", 51227.53]
	d6 = ["Jennifer Miller", 53514.94]
	d7 = ["Michael David", 31051.46]
	d8 = ["Mary Johnson", 71646.16]
	d9 = ["William Rodriguez", 69244.21]
	d10 = ["Mary Johnson", 12689.07]
	d11 = ["Michael David", 57145.50]
	d12 = ["Patricia Brown", 81679.15]
	masterList = [d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12]

# Prompts the user to enter an option
def mainPrompt():
	response = input("Choose from one of 3 actions:\n\
		1) Send a Thank You\n\
		2) Create a Report\n\
		3) Quit\n\
		Please type 1, 2, or 3: ")
	return response

# Takes in a user input as a parameter, enters a donation, prints a report,
# prints list, exit, prompts again if the input is bad
# If the user types exit it'll go back to the main prompt
def action(userInput):
	tempList = []
	createNameList()
	if userInput == 'list':
		for i in range(0,len(nameList)):
			print(nameList[i])
		action(mainPrompt())
	elif userInput == '1':
		donorName = input("Enter a full name: ")
		if (donorName != 'exit'):
			tempList.append(donorName)
			donationAmt = input("Enter a donation amount: ")
			if (donationAmt != 'exit'):
				tempList.append(float(donationAmt))
				masterList.append(tempList)
				printEmail(tempList)
		action(mainPrompt())
	elif userInput == '2':
		printReport()
		action(mainPrompt())
	elif userInput == '3':
		quit()
	else:
		action(mainPrompt())

# Creates a list of names of distinct donors
def createNameList():
	global masterList
	global nameList
	for i in range(0,len(masterList)):
		nameList.append(masterList[i][0])
	nameList = list(set(nameList))

# Prints a thank you email to a donator
# Donor name and amount is passed in as a parameter
def printEmail(currentDonation):
	print("Dear {:s},\n\
		Thank you for the generous donation of {:.2f}.\n\
		Sincerely,\n\
		Your Local Charity".format(*currentDonation))

# Prints a report of all the previous donators
# Report includes name, total donated, count of donations, average gift
# Report is also formatted with a certain spacing
def printReport():
	global masterList
	global nameList
	donationTotal = []
	for x in range(0,len(nameList)):
		donationSum = 0
		counter = 0
		for y in range(0, len(masterList)):
			if masterList[y][0] == nameList[x]:
				donationSum += masterList[y][1]
				counter += 1
		donationTotal.append([nameList[x], round(donationSum,2), counter, round(donationSum/counter,2)])
	donationTotal.sort(key=lambda l: l[1], reverse = True)
	print("Donor Name          |   Total Given  |  Num Gifts |  Average Gift")
	print("-----------------------------------------------------------------")
	for z in range(0, len(donationTotal)):
		print('{:20} ${:13.2f}{:14}  ${:13.2f}'.format(*donationTotal[z]))

# Python program to use main for function call
if __name__ == "__main__":
	initialize()
	theInput = mainPrompt()
	action(theInput)
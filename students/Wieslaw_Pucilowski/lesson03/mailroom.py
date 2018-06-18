#!/usr/bin/env python3
__author__="Wieslaw Pucilowski"

donors_hist = [
            ['Richard Lionheart', 100.5, 36.30, 230],
            ['Andreas Bolen', 220, 1000],
            ['Ivan Smirnoff', 1200],
            ['Karl Marx', 345.2, 140.20],
            ['Alvaro Speedy', 330, 850, 100.50],
			['Ilunga Mulungma', 350, 550],
            ['Denis Donuts', 68],
			['Haruto Asai', 45, 997.50],
			['Great Gatsby', 0.5],
        ]

def greetings(donator):
	print("""
	
	Ex Programmers Charity
	1999 Heartbeat Avenue
	11111 Fresh Spring, Alaska
	
	Dear {},
	
	Thank you for your generous donation of {} USD
	
	Sincerely
	Rob Steven

	""".format(donator[:1][0], donator[-1:][0]))

def print_main_menu():
	print("\n{:-^31}\n".format(" Main Menu "))
	choices = (("Send a Thank You", "1"),("Create a Report","2"),("Quit","3"))
	for i in range(len(choices)):
		print("{:.<30}{}".format(*choices[i]))
		
def main_menu ():
	while True:
		print_main_menu()
		response=input("Please choose one of three options:")
		if response == '1':
			send_thank_you()
		elif response == '2':
			create_report()
		elif response == '3':
			print("\nGoodbye.\n")
			return

def main_menu_1 ():
	print_main_menu()
	response=''
	while response not in ['1', '2', '3']:
		response=input("Please choose one of three options:")
	if response == '1':
		send_thank_you()
	elif response == '2':
		create_report()
	elif response == '3':
		print("\nGoodbye.\n")
		return
		
def send_thank_you():
	print("Sending thank you mail...")
	donors = [ x[0] for x in donors_hist]
	name = input("Type donor name or 'list' to print all donors, or 'quit' to go back:")
	while name.lower() == "list":
		print("Donors list: "+", ".join(["{}"]*(len(donors))).format(*donors))
		name = input("Type donor name or 'list' to print all donors, or 'quit' to go back:")
	if name.lower() == 'quit':
		return ## go to main_menu() at the bottom
	elif name not in donors:
		new_donor=[]
		new_donor.append(name)
		donation=input("Donation in USD: ")
		while not donation.isdigit():
			donation=input("Donation in USD: ")
		new_donor.append(float(donation))
		donors_hist.append(new_donor)
		greetings(new_donor)
	else:
		donation=input("Donation in USD: ")
		while not donation.isdigit():
			donation=input("Donation in USD: ")
		indx=donors.index(name)
		donors_hist[indx].append(float(donation))
		greetings(donors_hist[indx])
	return # main_menu()
	
def create_report():
	print("Creating a report...")
	print( "{:<30}| {:<18}| {:<8}| {:<18}".format('Donor Name','Total Given','Num Gifts','Average Gift'))
	print("{:-<80}".format(''))
	for i in donors_hist:
		print('{:<30}{}{:>18.2f}{:>11}{}{:>17.2f}'.format(i[:1][0], ' $', sum(i[1:]), len(i[1:]), ' $', sum(i[1:])/len(i[1:])))
	return

def main():
	main_menu ()

if __name__ == "__main__":
	main()
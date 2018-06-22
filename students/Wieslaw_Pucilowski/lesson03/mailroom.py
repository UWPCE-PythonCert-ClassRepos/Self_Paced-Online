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
			return   # to quit program

		
def send_thank_you():
	print("Sending thank you mail...")
	donors = [ x[0] for x in donors_hist]
	name = input("Type donor name or 'list' to print all donors, or 'quit' to go back:")
	while name.lower() == "list":
		print("Donors list: "+", ".join(["{}"]*(len(donors))).format(*donors))
		name = input("Type donor name or 'list' to print all donors, or 'quit' to go back:")
	if name.lower() == 'quit':
		return # go back to main_menu()
	elif name not in donors:
		new_donor=[name]
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
	#return 

def custom_key(x):
    return sum(x[1:])

def create_report():
    print("Creating a report...\n")
    print( "{:<30}| {:<18}| {:<8}| {:<18}".format('Donor Name','Total Given','Num Gifts','Average Gift'))
    print("{:-<80}".format(''))
    for x in sorted(donors_hist, key=custom_key,reverse=True):
        print('{:<30}{}{:>18.2f}{:>11}{}{:>17.2f}'.format(x[:1][0], ' $', sum(x[1:]), len(x[1:]), ' $', sum(x[1:])/len(x[1:])))
    


if __name__ == "__main__":
	main_menu ()

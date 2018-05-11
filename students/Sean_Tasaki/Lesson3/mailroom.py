"""
Sean Tasaki
5/11/2018
Lesson03.mailroom_part_1
"""

donor_full_list = [['Bob Dylan', 120000.00, 3, 40000.00], ['Leonard Cohen', 600.00, 2, 300.00], ['Soren Kierkegaard', 1000.00, 2, 500.00], ['Italo Calvino', 20000.00, 4, 5000.00], ['Florence Feist', 300.00, 3, 100.00]]
donor_name_list = []
for x in donor_full_list:
	donor_name_list.append(x[0])


def main_menu():
	response = input("Enter 1-3 from the following options: (1) Send a Thank You, (2) Create a Report, (3) Quit\n >")
	if response == '1':
		thank_you()
	elif response == '2':
		create_report()
	elif response =='3':
		exit()
	else:
		print("Invalid data. Enter 1-3 from the following options: (1) Send a Thank You, (2) Create a Report, (3) Quit\n> ")
		main_menu()

		

def thank_you():
	name = input("Enter the first and last name of the donor or enter 'list' to see a list of previous donor names or enter Q to exit to main menu\n> ")
	if name.lower() == 'list':
		print(donor_name_list)
		thank_you()
	elif name.upper() == 'Q':
		main_menu()
	elif name.title() in donor_name_list:
		for x in donor_full_list:
			if x[0].casefold() == name.casefold():
				amount = input(f"{name.title()} is a previous donor. Enter the donation amount.\n> ")
				if amount.lower() == 'q':
					thank_you()
				else:
					x[1] += float(amount)
					x[2] += 1
					x[3] = float(x[1]/x[2])
					thank_you()
			else:
				continue
	elif name.title() not in donor_name_list:
		amount = input(f"{name.title()} is a new donor. Enter the donation amount.\n> ")
		if amount.lower() == 'q':
			thank_you()
		else:
			donor_name_list.append(name.title())
			new_list = ['null', 0.00, 0, 0.00]
			new_list[0] = (name.title())
			new_list[1] = (float(amount))
			new_list[2] += 1
			new_list[3] = (float(amount))
			donor_full_list.append(new_list)
			thank_you()
	
	print()
	main_menu()

def create_report():
	donor_full_list.sort(key = lambda x: x[1], reverse = True)
	print("Donor Name           |   Total Given   |   Num Gifts  |    Average Gift")
	print("-----------------------------------------------------------------------")
	for x in donor_full_list:
		print(f"{x[0]:20} ${x[1]:>17.2f}    {x[2]:>6}     ${x[3]:>16.2f}")  
	main_menu()

if __name__ == '__main__':
	main_menu()


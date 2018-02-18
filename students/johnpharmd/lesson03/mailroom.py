#!/usr/bin/env python3

# Data
donors_amts = [['Gates', 150000, 3], ['Brin', 150000, 3],
              ['Cerf', 50000, 2], ['Musk', 100000, 1],
              ['Berners-Lee', 50000, 2],
              ['Wojcicki', 125000, 1], ['Avey', 200000, 2]]
donors = []

# Processing
for donor in donors_amts:
	donors.append(donor[0])


def send_ty():
	global donors_amts, donors
	while True:
		print()
		response = input('Enter full last name of Donor,'
			+ ' "list" for List of Donors'
			+ ', or "e" to Exit back to Main Menu: ')
		print()
		if response == 'e':
			break	
		if response.isalpha():
			if response == 'list':
				print('Here is the list of Donors: ')
				donors.sort()
				for donor in donors:
					print(donor)
			elif response != 'list':
				response = response.capitalize()
				if response in donors:
					print('Donor found:', response)
				elif response not in donors:
					print('Added to list of Donors:', response)
					donors.append(response)
					donors_amts.append([response, 0, 0])
				new_response = input('Enter a Donation amount' +
					' (in USD): ')


def get_report():
    pass


# I/O
if __name__ == '__main__':
    while True:
        print('Main Menu:')
        response = input('Choose from the following: "1" - Send a "Thank You",'
            + ' "2" - Create a Report, or "q" to Quit: ')
        if response == '1':
            # call function
            send_ty()
            # print('You chose "1".')
        elif response == '2':
            pass
        elif response == 'q':
            print('Program execution completed.')
            break
        else:
            response = input('Choose "1", "2", or "q": ')
            if response == '1' or response == '2':
                continue
            elif response == 'q':
                print('Program execution completed.')
                break
            else:
                print('That is not an option. Closing program.')
                break	

else:
    print('This module is not intended to be imported.')

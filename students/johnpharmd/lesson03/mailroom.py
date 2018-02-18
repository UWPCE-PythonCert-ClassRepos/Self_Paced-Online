#!/usr/bin/env python3

# Data
donors_amts = [['Gates', 'Mr.', 150000, 3], ['Brin', 'Mr.', 150000, 3],
              ['Cerf', 'Mr.', 50000, 2], ['Musk', 'Mr.', 100000, 1],
              ['Berners-Lee', 'Mr.', 50000, 2],
              ['Wojcicki', 'Ms.', 125000, 1], ['Avey', 'Ms.', 200000, 2]]


# Processing
def send_ty():
	global donors_amts
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
				donors_amts.sort()
				for donor in donors_amts:
					print(donor[0])
			elif response != 'list':
				response = response.capitalize()
				for donor in donors_amts:
					if donor[0] == response:
						print('Donor found:', response)
					else:
						salutation = input('Salutation: "Ms." or "Mr."?: ')
						print('Added to list of Donors:', salutation,
							response)
						donors_amts.append([response, salutation,
							0, 0])
				new_response = int(input('Enter a Donation amount' +
					' (in USD): '))
				print('Added to', response, '\'s Donations:',
					new_response)
				for donor in donors_amts:
					if donor[0] == response:
						donor[2] += new_response
						donor[3] += 1
				print('Here is the full List:')
				donors_amts.sort()
				for donor in donors_amts:
					print(donor[0])
				form_st = 'Dear {} {}, Thank you for your generous donation in the amount of {} USD.'
				print(form_st.format('Donor'
					, response, new_response))


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

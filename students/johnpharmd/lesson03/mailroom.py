#!/usr/bin/env python3

# Data
donors_amts = [['Gates', 150000, 3], ['Brin', 150000, 3],
              ['Cerf', 50000, 2], ['Musk', 100000, 1],
              ['Berners-Lee', 50000, 2],
              ['Wojcicki', 125000, 1], ['Avey', 200000, 2]]


# Processing
def send_ty():
    global donors_amts
    while True:
	    print()
	    response = input('Enter full last name of Donor,'
	        + ' "list" for List of Donors'
	        + ', or "e" to Exit back to Main Menu: ')
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
	                if response == donor[0]:
	                    print('Donor found:', response)
	                else:
	                    continue    


def get_report():
    pass


# I/O
if __name__ == '__main__':
    while True:
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

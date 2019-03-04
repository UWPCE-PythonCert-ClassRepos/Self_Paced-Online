'''
    Name: Muhammad Khan
    Date: 02/28/2019
    Assignment03

'''

#Goal:
# Automate the mailroom job of an individual working at a local
# charity organization. The script will prompt the user for the varioius options
# and perform the desired tasks.

# Global donors List.

donors_list = [ ['Adam', 'Johnson', 6000.20, 2200, 1050,100],
              ['Matt', 'Marvin', 550,1000,250],
              ['Ashley', 'Wiggins', 55.66,270,1000],
              ['Kristina', 'Laughrey', 500, 500,200],
              ['Kimberley', 'Allen', 12000.99, 5000],
              ['Doug', 'Boolinger', 260.57, 930.90],
              ['Sherry', 'Henning', 6000, 2460.20, 900] ]

def prompt_user():
    print('Please choose one of the following options: \n')
    print("1: Send a Thank You")
    print("2: Create a report")
    print("3: Quit")
    return int(input("Option:  "))

def thank_you(donors_data = donors_list):
    name = name_prompt().split(' ')
    amount = donation_prompt(name)
    add_donation(name, amount, donors_data)
    email(name, amount)

def add_donation(name, amount, donors_data = donors_list):
    donorIndex = find_donor(name,donors_data)
    if donorIndex < len(donors_data):
        donors_data[donorIndex].append(amount)
    else:
        donors_data.append([name[0],name[1],amount])

def name_prompt():
    donor_name = input("Please enter the donor's full name OR \n"
                 +"type 'list' for the existing donors: ")
    if donor_name == 'list':
        display_list()
        donor_name = input("Please enter the donor's full name: ")
    return donor_name

def donation_prompt(name):
    donation_amount = input("Please enter the donation amount for {} {}: "
                            .format(*name))
    return float(donation_amount)

def display_list(donors_data=donors_list):
    print("\nOur generous donors: \n")
    for donor in donors_data:
        print(donor[0],donor[1])

def find_donor(donor_name, donors_data = donors_list):
    index = len(donors_data)
    for donor in donors_data:
        if (donor_name[0] == donor[0] and donor_name[1] == donor[1]):
            index = donors_data.index(donor)
    return index

def email(donor_name, amount):
    header = "\nDear {:} {:}".format(*donor_name)
    body = "\nThank you so much for your generous donation of $ {:.2f}."
    print(header, body.format(amount))

def print_report(donors_data = donors_list):
    title = "{:24} | {:12} | {:10} | {:16}"
    print(title.format('Donor Name','Total Given','Num Gifts','Average Gift'))
    strf_format = "{:12} {:12} $  {:10.2f} {:10d}   ${:10.2f}"
    print(67*('-'))
    report_list = calculate_total_gift(donors_data)
    report_list.sort(key = custom_sort, reverse = True)
    for donor in report_list:
        print(strf_format.format(*donor))

def calculate_total_gift(donors_data = donors_list):
    new_list = []
    for donor in donors_data:
        first,last = donor[0],donor[1]
        total_donation, num_of_gifts = sum(donor[2:]), len(donor)-2
        avg_gift = total_donation/num_of_gifts
        new_list.append([first,last,total_donation,num_of_gifts,avg_gift])
    return new_list

def custom_sort(a_list):
    return a_list[2]

if __name__ == "__main__":

    while (True):
        user_response = prompt_user()
        if ( user_response == 3):
            break
        elif ( user_response == 1):
            thank_you(donors_list)
        elif ( user_response == 2):
            print_report(donors_list)
        else:
            print("Invalid Response Please Try Again :)")

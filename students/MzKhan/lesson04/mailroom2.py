'''
    Name: Muhammad Khan
    Date: 03/08/2019
    Assignment04

'''
import sys
import os
import datetime
from operator import itemgetter as igetter

#Goal:
# Automate the mailroom job of an individual working at a local
# charity organization. The script will prompt the user for the varioius options
# and perform the desired tasks.

# Global donors List.
# This list is accessible everywhere in the script.

donors_list = [ ['Adam', 'Johnson', 6000.20, 2200, 1050,100],
              ['Matt', 'Marvin', 550,1000,250],
              ['Ashley', 'Wiggins', 55.66,270,1000],
              ['Kristina', 'Laughrey', 500, 500,200],
              ['Kimberley', 'Allen', 12000.99, 5000],
              ['Doug', 'Boolinger', 260.57, 930.90],
              ['Sherry', 'Henning', 6000, 2460.20, 900] ]

def prompt_user():
    """
    This method prompts the user for the valid input.
    input: string
    return: int
    """
    print('Please choose one of the following options: \n')
    print("1: Send a Thank You")
    print("2: Create a report")
    print("3: Send letters to everyone")
    print("4: Quit")
    return int(input("Option:  "))

def thank_you(donors_data):
    """
    This method asks for the donor's name and the donation amount
    from the user. Then, it adds the donation amount for the donor.
    It sends the thank you email to the donor for his/her donation.
    parm: list
    """
    name = name_prompt(donors_data).split(' ')
    amount = donation_prompt(name)
    add_donation(name, amount, donors_data)
    email(name, amount)

def add_donation(name, amount, data_list):
    """
    This method adds the donation amount for the given donor.
    If the donor is already present in the history, it appends the donation
    amount for that user.
    If the donor is a new donor, it appends the new donor to the donor's list
    parm: list
    parm: float
    parm: list
    """
    donor_index = find_donor(name,data_list)
    if donor_index < len(data_list):
        data_list[donor_index].append(amount)
    else:
        data_list.append([name[0],name[1],amount])

def name_prompt(donor_data):
    """
    This method prompts the user for the donor's name OR
    check the existing donors.
    parm: none
    return: string
    """
    donor_name = input("Please enter the donor's full name OR \n"
                 +"type 'list' for the existing donors: ")
    if donor_name == 'list':
        display_list(donor_data)
        donor_name = input("Please enter the donor's full name: ")
    return donor_name

def donation_prompt(name):
    """
    This method prompts the user for the donation amount for the given donor.
    parm: list
    return: float
    """
    donation_amount = input("Please enter the donation amount for {} {}: "
                            .format(*name))
    return float(donation_amount)

def display_list(data_list):
    """
    This method prints the donor's list to the user.
    parm: list
    """
    print("\nOur generous donors: \n")
    for donor in data_list:
        print(donor[0],donor[1])

def find_donor(donor_name, donors_data):
    """
    This method checks if the given donor exists in the donor's list.
    If the donor does exist, it returns its index
    If the donor doesn't exist, it returns the index to add the new donor.
    parm: list
    parm: list
    return: int
    """
    index = len(donors_data)
    for donor in donors_data:
        if (donor_name[0] == donor[0] and donor_name[1] == donor[1]):
            index = donors_data.index(donor)
            return index
    else:
        return index

def email(donor_name, amount):
    """
    This method generates the email for the given donor for his/her donation.
    parm: list
    parm: float
    """
    header = "\nDear {:} {:}".format(*donor_name)
    body = "\nThank you so much for your generous donation of $ {:.2f}."
    print(header, body.format(amount))

def print_report(donors_data):
    """
    This method prints the donors' report in the formatted tabular form.
    # parm: list
    """
    title = "{:24} | {:12} | {:10} | {:16}"
    print(title.format('Donor Name','Total Given','Num Gifts','Average Gift'))
    strf_format = "{:12} {:12} $  {:10.2f} {:10d}   ${:10.2f}"
    print(67*('-'))
    report_list = calculate_total_gift(donors_data)
    for donor in sorted(report_list, key = igetter(2), reverse = True):
        print(strf_format.format(*donor))

def calculate_total_gift(donors_data):
    """
    This method creates a new list from the global donors' list
    where each item of the list is a list of
    the donor's first name, last name, total donation, number of donations,
    and an average donation
    parm: list
    return: list
    """
    new_list = []
    for donor in donors_data:
        first,last = donor[0],donor[1]
        total_donation, num_of_gifts = sum(donor[2:]), len(donor)-2
        avg_gift = total_donation/num_of_gifts
        new_list.append([first,last,total_donation,num_of_gifts,avg_gift])
    return new_list

def quit():
    """
    This method exits out from the user interaction.
    """
    print("Thank you. Have a nice day:")
    sys.exit()

def send_letter_everyone(donors_data):
    ''' This method generates the thank you letters for each donor in the list
    parm: list
    '''
    date_format = '{:%m-%d-%Y}'.format(datetime.datetime.now())
    for donor in donors_data:
        _donor = []
        _donor.extend(donor[0:2])
        _donor.extend([donor[-1],sum(donor[2:]),len(donor)-2])
        letter=letter_format().format(*_donor)
        file_name = '_'.join(_donor[0:2])+"_"+date_format+'.txt'
        write_a_letter(file_name,letter)

def write_a_letter(filename, content):
    '''This method creates a new file in the Letters folder and writes to it.'''
    folder = "Letters"
    if not os.path.exists(folder):
        os.mkdir(folder)
    with open(os.path.join(folder,filename),'w+') as out:
        out.write(content)
        out.close()

def letter_format():
    """
    return: string
    """
    message = """Dear {} {},

    Thank you so much for your kind donation of ${:.2f}. With that you have
    generously donated a total amount of ${:.2f} in your {} donation(s).
    We must ensure you that your donations will be put to a very good use.

                                                        Sincerely,

                                                        -Team """
    return message


if __name__ == "__main__":

    #Main program flow control and the interaction with the user.
    options = {1:thank_you,2:print_report,3:send_letter_everyone,4:quit}
    while True:
        user_response = prompt_user()
        if user_response == 4:
            options[user_response]()
        elif user_response in options:
            options[user_response](donors_list)
        else:
            print("Invalid Response Please Try Again :)")

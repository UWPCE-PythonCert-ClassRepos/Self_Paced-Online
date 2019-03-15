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

# Global donors data.
# Accessible everywhere in the script.

donors_data = {"Adam Johnson":[6000.20, 2200, 1050,100],
               "Matt Marvin":[550,1000,250],
               "Ashley Wiggins":[55.66,270,1000],
               "Kristina Laughrey":[500, 500,200],
               "Kimberley Allen":[12000.99, 5000],
               "Doug Boolinger":[260.57, 930.90],
               "Sherry Henning":[6000, 2460.20, 900] }

def prompt_user():
    """
    prompt the user for the valid input.
    input: string
    return: int
    """
    print('Please choose one of the following options: \n')
    print("1: Send a Thank You")
    print("2: Create a report")
    print("3: Send letters to everyone")
    print("4: Quit")
    return int(input("Option:  "))

def thank_you():
    """send a thank you note to a donor for his/her donation."""
    name = name_prompt()
    amount = donation_prompt(name)
    add_donation(name, amount)
    email(name, amount)

def add_donation(name, amount):
    """
    parm: string
    parm: float
    """
    donors_data.setdefault(name,[]).append(amount)

def name_prompt():
    """return a name string"""
    donor_name = input("Please enter the donor's full name OR \n"
                 +"type 'list' for the existing donors: ")
    if donor_name == 'list':
        display_list()
        donor_name = input("Please enter the donor's full name: ")
    return donor_name.title()

def donation_prompt(name):
    """
    prompt the user for the donation amount for the given donor.
    parm: string
    return: float
    """
    donation_amount = input("Please enter the donation amount for {}: "
                            .format(name))
    return float(donation_amount)

def display_list():
    """print the donor's list to the user."""
    print("\nOur generous donors: \n")
    for donor in donors_data:
        print(donor)

def email(donor_name, amount):
    """
    generate the email for the given donor for his/her donation.
    parm: string
    parm: float
    """
    header = "\nDear {}".format(donor_name)
    body = "\nThank you so much for your generous donation of $ {:.2f}."
    print(header, body.format(amount))

def print_report():
    """Print the donors' report in the formatted tabular form."""
    title = "{:24} | {:12} | {:10} | {:20}"
    dashes=67*('-');print(dashes)
    print(title.format('Donor Name','Total Given','Num Gifts','Average Gift'))
    strf_format = "{:24} ${:12.2f}   {:^10d}  ${:12.2f}"
    print(dashes)
    report_list = calculate_total_gift()
    for donor in sorted(report_list, key = igetter(1), reverse = True):
        print(strf_format.format(*donor))
    print(dashes)
def calculate_total_gift():
    """
    create a list from the global donors' data.
    return: list
    """
    new_list = []
    for donor in donors_data:
        total_donation =sum(donors_data[donor][0:])
        num_of_gifts = len(donors_data[donor])
        avg_gift = total_donation / num_of_gifts
        new_list.append([donor, total_donation, num_of_gifts, avg_gift])
    return new_list

def quit():
    """exit out from the user interaction."""
    print("Thank you. Have a nice day:")
    sys.exit()

def send_letter_everyone():
    """generate the thank you letters for each donor in the list"""
    date_format = '{:%m-%d-%Y}'.format(datetime.datetime.now())
    for donor in donors_data:
        _donor = []
        donor_donations = donors_data.get(donor)
        _donor.extend([donor_donations[-1],sum(donor_donations[:]),
                                             len(donor_donations)])
        letter=letter_format().format(donor,*_donor)
        file_name = donor+"_"+date_format+'.txt'
        write_a_letter(file_name,letter)

def write_a_letter(filename, content):
    """create a new file in the Letters folder and write to it"""
    folder = "Letters"
    if not os.path.exists(folder):
        os.mkdir(folder)
    with open(os.path.join(folder,filename),'w+') as out:
        out.write(content)

def letter_format():
    """return the letter message"""
    message = """Dear {:},

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
        if user_response in options:
            options[user_response]()
        else:
            print("Invalid Response: Please try again :)")

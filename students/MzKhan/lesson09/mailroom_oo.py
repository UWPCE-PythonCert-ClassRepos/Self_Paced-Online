'''
Name: Muhammad Khan
Date: 04/07/2019
Assignment09
'''

import sys
import os
import re
import datetime
from operator import itemgetter as igetter

#Goal:
# Automate the mailroom job of an individual working at a local
# charity organization. The script will prompt the user for the varioius options
# and perform the desired tasks.

# Global donors data.
# Accessible everywhere in the script.
donors_name = ["Adam Johnson","Matt Marvin","Ashley Wiggins",
                "Kristina Laughrey","Kimberley Allen", "Doug Boolinger",
                "Sherry Henning"]
donations = [ [6000.20, 2200, 1050,100],
                [550,1000,250],
                [55.66,270,1000],
                [500, 500,200],
                [12000.99, 5000],
                [260.57, 930.90],
                [6000, 2460.20, 900] ]

# Create the dictionary using the dict comprehension.
donors_data_dict = dict(zip(donors_name,donations))



class Donors_Database:
    """Parent class that holds the Donors data"""
    # Class attribute.
    donors_data = donors_data_dict


    @classmethod
    def display_donors_list(cls):
        """Print the donor's list to the user."""
        print("\nOur generous donors: \n")
        for donor in cls.donors_data:
            print(donor)


class Thank_You(Donors_Database):
    """This class inherits from the parent class "Donors_Database"""

    def __init__(self , name, donation ):
        """instance attributes"""
        self.name = name
        self.donation = donation
        self.add_donation(self.name,self.donation)


    def add_donation(self,name, amount):
        """
        parm: string
        parm: float
        """
        Donors_Database.donors_data.setdefault(name,[]).append(amount)


    @property
    def email(self):
        """Generate the email for the given donor for his/her donation."""
        e_mail=Thank_You.email_message(self.name, self.donation)
        print(e_mail)


    @staticmethod
    def email_message(donor_name, amount):
        """Return a formatted string with donor_name and amount"""
        email_msg = """
        \rDear {:},

        \rThank you so much for your generous donation of $ {:.2f}.

        \rBest Regards,

        \r-Team"""
        return email_msg.format(donor_name,amount)


class Report(Donors_Database):
    """Class inherits from the Donors_Database"""

    @staticmethod
    def print_report():
        """Print the donors' report in the formatted tabular form."""
        title = "{:24} | {:12} | {:10} | {:20}"
        dashes=67*('-');print(dashes)
        print(title.format('Donor Name','Total Given','Num Gifts','Average Gift'))
        strf_format = "{:24} ${:12.2f}   {:^10d}  ${:12.2f}"
        print(dashes)
        for donor in Report.sorted_list_desc():
            print(strf_format.format(*donor))
        print(dashes)


    @staticmethod
    def sorted_list_desc():
        """Return a sorted list in the descending order based  on index 1"""
        new_list = Report.calculate_total_gift()
        sorted_list = sorted(new_list, key = igetter(1), reverse = True)
        return sorted_list


    @staticmethod
    def calculate_total_gift():
        """
        Create a list from the global donors' data.
        return: list
        """
        new_list = [ [donor, sum(donations[0:]),len(donations),
                   sum(donations[0:])/len(donations)]
                   for donor,donations in Donors_Database.donors_data.items() ]
        return new_list


class Send_Letter(Donors_Database):


    def send_letter_everyone(self):
        """Generate the thank you letters for each donor in the list"""
        date_format = '{:%m-%d-%Y}'.format(datetime.datetime.now())
        for donor, donations in self.donors_data.items():
            _donor = []
            _donor.extend([donations[-1],sum(donations[:]),len(donations)])
            letter=self.letter_format(donor,*_donor)
            file_name = donor+"_"+date_format+'.txt'
            self.write_a_letter(file_name,letter)


    def write_a_letter(self, filename, content):
        """Create a new file in the Letters folder and write to it"""
        folder = "Letters"
        if not os.path.exists(folder): os.mkdir(folder)
        with open(os.path.join(folder,filename),'w+') as out:
            out.write(content)


    def letter_format(self, *donor_info):
        """Return the letter message"""
        message = """Dear {:},

        Thank you so much for your kind donation of ${:.2f}. With that you have
        generously donated a total amount of ${:.2f} in your last {} donation(s).
        We must ensure you that your donations will be put to a very good use.

                                                            Sincerely,

                                                            -Team """
        return message.format(*donor_info)


def prompt_user():
    """Return user's selected option as an integer"""
    print()
    print('Please choose one of the following options:')
    print("1: Send a Thank You")
    print("2: Create a report")
    print("3: Send letters to everyone")
    print("4: Quit")
    try:
        return int(input("Option:  "))
    except ValueError as e:
        print("***INVALID Option Selected***")


def name_prompt():
    """Return a name string"""
    while True:
        donor_name = input("Please enter the donor's full name OR \n"
                 +"type 'list' for the existing donors: ")
        try:
            if not "".join(donor_name.split()).isalpha():
                raise Exception("The name should be all Alphabetic characters:")
            return donor_name.title()
        except Exception as e:
            print("INVALID Name: ",e)


def donation_prompt(name):
    """
    prompt the user for the donation amount for the given donor.
    parm: string
    return: float
    """
    input_msg = "Please enter the donation amount for {}: "
    donation_amount = input(input_msg.format(name))
    while True:
        try:
            return float(donation_amount)
        except ValueError:
            donation_amount=input("INVALID Amount: "+input_msg.format(name))


def quit():
    """Exit out from the user interaction."""
    print("Thank you. Have a nice day:")
    sys.exit()


if __name__=="__main__":
    """The flow control of the program. It separates the business logic from
    the data manipulation"""

    user_response = prompt_user()
    while True:

        if user_response == 1:
            name = name_prompt()
            if name.upper() == "LIST":
                Donors_Database.display_donors_list()
                user_response = 1
                continue
            thank = Thank_You(name, donation_prompt(name) )
            thank.email
        elif user_response == 2:
            Report.print_report()
        elif user_response == 3:
            letter = Send_Letter()
            letter.send_letter_everyone()
        elif user_response == 4:
            quit()
        else:
            print("***INVALID Option Selected***")
        user_response = prompt_user()




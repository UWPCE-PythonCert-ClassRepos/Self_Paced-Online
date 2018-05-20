#Natalie Rodriguez
#Lesson 09: Object Oriented Mailroom
# May 15, 2018

#Hints
'''
You’ll want a Donor class – this will hold all the information about the donor, and have attributes, properties,
and methods to provide access to the donor specific information that is needed.


You’ll then want a class that handles the collection of donors. This will hold all the donor objects,
but also methods to add a new donor, search for a given donor, etc. If you want a way to save and re-load your data,
this class would have that too.

Your class for the collection of donors will also hold the code that generates reports about multiple donors.

Remember that the user interaction code (anything with an input function) should be outside of these
“logic” or “model” classes.

In general, you will have a method for each of the functions in your non-OO version.
Which class they go it will depend on whether the method only needs the information from one donor,
or from the whole collection.

Rules of thumb for where to put methods:

Hopefully, once you made your code testable, all the user-interaction code (with input()) is self contained
in functions that don’t have any logic (data manipulation) in them. If not, then this is a good time to refactor.
If a function does something with a single donor – it should be a method in the Donor class.
If a function works with multiple donors – it should be in the class that handles a collection of donors.
If a function contains a call to input() – it belongs outside of the logic classes – either stand alone in
the module (like they are already) or perhaps all in a CLI class.'''

#!/usr/bin/env python3
import sys
from collections import defaultdict

class Donor:

    def __init__(self, name, donations=None):

        self.name = name
        if donations is None:
            self.donations = []
        else:
            self.donations = donations

    def add_donation(self, amount):
        try:
            self.donations.append(int(amount))
        except ValueError:
            print("Enter a donation amount.")

    def donation_amount(self):
        return len(self.donations)

    def total_donation(self):
        try:
            return sum(self.donations)
        except TypeError:
            return self.donations

    def donation_avg(self):
        try:
            return self.total_donation()/ self.donation_amount()
        except TypeError:
            return self.donations

class DonorHistory:

    def __init__(self, donors=None):
        self.donor_list = donors

    def thank_you(self):
        '''user inputs donor and amounts to dict.
        '''
        print('Type the full donor name (Enter "list" to show all donors or enter "dash" to return to the Donor Dashboard.')
        new_donor = input(':')

        if new_donor.lower() == 'list':
            donor_names = []
            for donor in self.donor_list:
                donor_names.append(donor.name)
            print(donor_names)

        elif new_donor.lower() == 'dash':
            return

        else:
            if new_donor in self.donor_list:
                try:
                    amount = float(input('Please enter the donation amount:'))
                    donor_list[Donor].add_donation(amount)

                except ValueError:
                    print("Please enter a valid amount.")
            else:
                amount = float(input('Please enter the donation amount:'))
                new_donor_object = Donor(new_donor, [amount])
                self.donor_list.append(new_donor_object)
                print('            Thank you {}, We greatly appreciate your generous donation of ${:.2f}.'.format(new_donor, amount))
                print('''            Your contribution to the purchase of land for conservation
            and habitat restoration will make a profound difference in allowing
            the environment to recover from the detrimental impact of human
            life. With noble individuals like yourself, we can make large strides
            to allow the North American continent to exist without the stressors of 
            agriculture and other human impacts. We appreciate and look forward to
            your continued support.
            
            Best,
            The Nature Conservancy''')

    def donor_report(self):
        '''Outputs a string table of donors and monetary amounts'''
        print('Donor History')
        report = []
        report.append('|{:<20}|{:<20}|{:<20}|{:<20}|'.format('    Donor Name', '   Total Donation', '  No. of Donations', '  Average Donation'))
        for donor in self.donor_list:
           report.append('|{:<20}|{:>20}|{:>20}|{:>20}|'.format(donor.name, donor.total_donation(), donor.donation_amount(), donor.donation_avg()))
        return '\n'.join(report)

    def print_donors(self):
        print(self.donor_report())

    def write_file(self):
        '''Creates a text file with a thank you message for each of the donors in the dictionary'''
        for donor_data in self.donor_list:
            filename = donor_data.name.replace(" ", "_") + ".txt"
            total_donation = donor_data.total_donation()
            letter = ('Thank you {} for you generous contributions in the amount of {:.2f}!'.format(donor_data.name, total_donation))
            with open(filename, 'w') as file:
                file.write(letter)
            print(f"{donor_data.name}'s thank you has been saved at: " + filename)


def donor_dashboard(prompt, dispatch_dict):
    '''Creates a menu that accepts user input and then selects a function based on that input'''
    while True:
        try:
            response = input(prompt)
            dispatch_dict[response]()
        except KeyError:
            print('Please enter a selection from the dashboard.')

def quit_dashboard():
    sys.exit("Exiting the Nature Conservancy Donor Dashboard. Goodbye!")

if __name__ == '__main__':

    Luke = Donor('Luke Rodriguez',[5512.75, 3250.50, 42.50])
    River = Donor('River Tails',[63.00, 1200.00, 300.00, 450.00, 4000.00])
    Virgil = Donor('Virgil Ferdinand',[350.00, 5000.00])
    Jokib = Donor('Joseph Kibson',[3498.00, 5.50])
    mailroom = DonorHistory([Luke, River, Virgil, Jokib])


    console_prompt = ("\nWelcome to the Nature Conservancy Donor Dashboard!\n"
                      "Please make a numerical selection.\n\n"
                      "1.) Send a thank you note. \n"
                      "2.) Create a Report. \n"
                      "3.) Send thank yous to all donors. \n"
                      "4.) Exit the donor dashboard.\n")

    console_dict = {'1': mailroom.thank_you,
                    '2': mailroom.print_donors,
                    '3': mailroom.write_file,
                    '4': quit_dashboard,
                    'q': quit_dashboard,
                    'Q': quit_dashboard}



    donor_dashboard(console_prompt, console_dict)

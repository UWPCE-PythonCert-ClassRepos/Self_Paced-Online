#!/usr/bin/env python3

import sys

#---------------------------------------------------------------------------
class Donor:

    def __init__(self, donor_name):
        self.donor_name = donor_name
        self.donation = []

    @property
    def donation_count(self):
        return len(self.donation)

    @property
    def donation_total(self):
        return sum(self.donation)

    @property
    def donation_avg(self):
        return round((self.donation_total / self.donation_count), 2)

    def add_donation(self, donation_amt):
        self.donation.append(donation_amt)



# -----------------------------------------------------------------------------
class DonorCollection:

    def __init__(self):
        self.donor_collection = []

    def find_donor(self, donor_name):
        for donor in self.donor_collection:
            if donor.donor_name == donor_name:
                return donor


    #------------------------------------------
    def add_donor_donation(self, donor_name, donation_amt):
        #print(donor_name, donation_amt)
        donor = self.find_donor(donor_name)
        if donor:   # existing donor
            donor.add_donation(donation_amt)    # append donation$ to the donor's list of donations
        else:   # new donor
            donor = Donor(donor_name)           # create new donor
            self.donor_collection.append(donor) # add new donor to collection
            donor.add_donation(donation_amt)    # append donation$ to the donor's list of donations


    #-----------------------------------------
    def list_donors(self):
        output = '\n'.join([donor.donor_name for donor in self.donor_collection])
        if len(output) == 0:
            output = "\nThere is no donor records."
        return output


    #----------------------------------------
    def create_report(self):
        donor_name = [donor.donor_name for donor in self.donor_collection]
        donation_total = [donor.donation_total for donor in self.donor_collection]
        donation_count = [donor.donation_count for donor in self.donor_collection]
        donation_avg = [donor.donation_avg for donor in self.donor_collection]
        sorted_donor_collection = sorted(zip(donor_name, donation_total, donation_count, donation_avg), key=lambda x: int(x[1]), reverse=True)

        print('\n{:20s}{:>22s}     {:10s}     {:15s}'.format('Donor Name', 'Total Donation Amt', 'Num of Donations', 'Avg Per Donation'))
        print('-' * 85)

        for donor in range(len(sorted_donor_collection)):
            print('{:<25}$ {:>15.2f}            {:<3}           $ {:>15.2f}'.format(*sorted_donor_collection[donor]))


    #----------------------------------------
    def compose_thank_you_letter(self, donor_name, donation_amt):

        thank_you_text = 'Dear {:s},\n\
        Thank you for your generosity to our Foundation in the total amount of ${:.2f}.\n\
        Sincerely,\n\
        Bill & Melinda Gates'
        return thank_you_text.format(donor_name, donation_amt)


    #-----------------------------------------------
    def write_thank_you_letter(self):
        for donor in self.donor_collection:
            filename = donor.donor_name + '.txt'
            thank_you_text = self.compose_thank_you_letter(donor.donor_name, donor.donation[-1] )
            with open(filename, 'w') as thks_letter:
                thks_letter.write(thank_you_text)

#------------------------------------------------------------------------------




def get_donor_name():
    donor_name = input('Please enter donor name. X exits / returns to main menu:  ').upper()
    if donor_name == 'X': # go back to MAIN MENU
        main()
    #elif donor_name == 'L':   # list current donors
        #print(donor_collection.list_donors())
        #main()
    else:
        return donor_name


def get_donation_amt():
    while True:
        donation_amt = input('Enter donation amount. X exits / returns to main menu:  ').upper()
        if donation_amt == 'X':
            main()
        else:
            return float(donation_amt)



#------------------------------------------------------------------------------
def quit_program():
    print('Bye!')
    sys.exit()



#-----------------------------------------------------------------------------
def invalid_menu():
    print('\nNot a valid option!\n\n')
    main()


#------------------------------------------------------------------------------
def add_donor_donation():
    donor_collection.add_donor_donation(get_donor_name(), get_donation_amt())


def main_menu_selection():
    response = input('\n\nMAIN MENU\nChoose from one of the options below:\n\
        A) Add donor - donation\n\
        R) Create a Report\n\
        T) Write thank-you files\n\
        Q) Quit the program\n\
        Please type A, R, T, or Q: ')
    return response.upper()

def main():
    # use of dictionary where 'key' is the menu choice and 'value' is function to call
    main_menu_options = {
        'A': add_donor_donation,
        'R': donor_collection.create_report,
        'T': donor_collection.write_thank_you_letter,
        'Q': quit_program
    }
    while True:
        main_menu_selected = main_menu_selection().upper()
        main_menu_options.get(main_menu_selected, invalid_menu)() #invalid_menu is to handle
                                                                # non-of-above choices


#------------------------------------------------------------------------------
if __name__ == "__main__":
    donor_collection = DonorCollection()
    main()
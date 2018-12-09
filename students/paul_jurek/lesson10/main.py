"""entry point to mailroom application"""

from pathlib import Path
from DonationController import DonationController, save_donation_controller, load_donation_controller
from Donor import Donor
from helpers import menu_selection

CONTROLLER = load_donation_controller('stw.p')

def main_menu():
    """calls main menu for program"""
    MAIN_MENU_OPTIONS = {'1': create_donation_menu,
                         '2': donor_report_menu,
                         '3': send_thank_you_letters,
                         '4': save_database}
    user_input = ('Options:\n'
                  '\t1: Create Donation\n'
                  '\t2: Create Donor Report\n'
                  '\t3: Send donors Thank Yous\n'
                  '\t4: Save Database\n'
                  '\t0: Quit\n'
                  'Please input number for option: ')

    menu_selection(user_input, MAIN_MENU_OPTIONS)


def create_donation_menu():
    """calls create donation menu
    
    this menu allows users to create donations for users"""

    while True:
        donor_selection = input('Please select donor id (enter "list" to see all donors): ')

        if donor_selection.lower().strip() == 'list':
            # displays existing donors
            CONTROLLER.display_donors()
            continue
        elif donor_selection.lower().strip() == 'quit':
            break
        else:
            try:
                donor_selection = int(donor_selection)
            except ValueError:
                print('please enter integer for donor')
                continue

            if CONTROLLER.find_donor(donor_selection) is None:
                print('Donor not found.  Enter donor''s name')
                firstname = input('Please enter donor''s first name: ')
                lastname = input('Please enter donor''s last name: ')
                CONTROLLER.create_donor(Donor(id=donor_selection, firstname=firstname, lastname=lastname))

            try:
                donation_amount = int(float(input("Select donation amount: "))*100)
            except ValueError:
                print('Donation Canceled. Please retry and input number for donation amount.')

            if CONTROLLER.find_donor(donor_selection) is None:
                print('Donor not found.  Enter donor''s name')
                firstname = input('Please enter donor''s first name: ')
                lastname = input('Please enter donor''s last name: ')
                CONTROLLER.create_donor(Donor(id=donor_selection, firstname=firstname, lastname=lastname))
            CONTROLLER.create_donation(donor=donor_selection, amount=donation_amount)
        #CONTROLLER.print_thank_you(fullname=thank_you_input, amount=donation_amount, donors=donors)
            break


def donor_report_menu():
    """creates donor report for user"""
    CONTROLLER.donor_report()


def send_thank_you_letters():
    """sends thank you letters to all our donors"""
    CONTROLLER.send_letters_to_everyone()


def save_database():
    """saves default database"""
    save_donation_controller(CONTROLLER, Path('stw.p'))


def create_sample_donor_database():
    """creates a sample donor database to fill in donations
    allows us to test scalability"""
if __name__ == '__main__':
    main_menu()

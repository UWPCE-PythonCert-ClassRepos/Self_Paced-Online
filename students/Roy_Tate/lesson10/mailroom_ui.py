#!/usr/bin/python3


# Author/Student:  Roy Tate (githubtater)


import mailroom_backend as mb
import time


class MailroomUI:

    def __init__(self, collection):
        if isinstance(collection, mb.DonorCollection):
            self.collection = collection
        else:
            raise TypeError('DonorCollection instance not found.')

    def menu_selection(self, arg_dict, response):
        """Dislay the user menu
        Args:
            arg_dict: dict of options
            response: option selected

        Returns:
            None. Based on the response, a function is executed"""
        try:
            arg_dict[response]['function']()
        except KeyError as e:
            print('\nInvalid response: ' + str(e) + '\nTry again.\n')
        except ValueError as e:
            print('\nInvalid entry: ' + str(e) + '\nTry again.\n')

    def main_menu(self):
        main_menu_args = {
            '1':{'option': '- Send a thank you', 'function': self.send_thank_you},
            '2':{'option': '- Print donor report', 'function': self.print_report},
            '3':{'option': '- Email all donors', 'function': self.email_all},
            '4':{'option': '- Challenge', 'function': self.challenge_menu},
            '5':{'option': '- Run Projections', 'function': self.run_projections},
            '6':{'option': '- Exit', 'function': self.die}
        }
        print('\n{:*^20}'.format(' MAIN MENU '))
        while True:
            for k, v in sorted(main_menu_args.items()):
                print(k, v['option'])
            response = input('\nEnter your selection: \n').strip()
            self.menu_selection(main_menu_args, response)

    def challenge_menu(self):
        """Menu presenting user with option to multiply all donations by a factor
            Args:
                None
            Returns:
                None
            Inputs:
                multiplier: the value to multiply all donations by"""
        multiplier = float(input('Enter the multiplier value: '))
        self.challenge_collection = self.collection.challenge(multiplier)
        print(self.challenge_collection.create_projection_report(f"(Challenge factor = {multiplier})"))
        print(self.collection.create_report())

    def run_projections(self):
        """Run the 'Under 50' and 'Over 100' projection reports"""
        launcher = ['Running projections', 'Finding values below $50', 'Finding values above $100', 'Finalizing Report']
        for i in launcher:
            print(i + '...')
            time.sleep(.25)
        self.projection_collection50, self.projection_collection100 = self.collection.run_projections()
        print(self.projection_collection50.create_projection_report(' Triple All Donations Under $50'))
        print(self.projection_collection100.create_projection_report(' Double All Donations Under $100'))
        print(self.collection.create_report())

    def die(self):
        """All good things must come to an end"""
        print('\nExiting.')
        exit(0)

    def send_thank_you(self):
        """Takes input and returns a thank you letter"""
        thank_you_args = {
            '1':{'option': '- Enter a new donation', 'function': self.get_donation_amount},
            '2':{'option': '- Back to the Main Menu', 'function': self.main_menu},
            'list':{'option': '- Print a list of all donors', 'function': self.print_list},
        }
        for k, v in sorted(thank_you_args.items()):
            print(k, v['option'])
        response = input('\nEnter your selection: \n').strip()
        self.menu_selection(thank_you_args, response)

    def print_report(self):
        """Print a report of all current donors and donations"""
        report = self.collection.create_report()
        print(report)

    def email_all(self):
        """Saves an 'email' in the current current directory for all users. The email thanks the user and outlines
        their total donation amount"""
        save_directory = input('\nEnter the directory to save to:  ')
        try:
            save_dir = self.collection.save_emails(save_directory)
            print(f'Files successfully saved in {save_dir}\n')
        except PermissionError:
            print(f'Invalid permissions on directory: {save_directory}\n'
                  f'Files not saved.')
        except OSError:
            print(f'Invalid path: {save_directory}\n'
                  f'Files not saved.\n')

    def get_donation_amount(self):
        """Receive input from the user to enter a new donation"""
        donor_name = input('\nEnter the donor name (First Last): \n')
        donation_amount = float(input('\nEnter the donation amount: \n'))
        self.collection.add(donor_name, donation_amount)
        for k, v in self.collection.donors.items():
            if k == donor_name.strip():
                print(v.letter)

    def print_list(self):
        """Print the names of the current donor list."""
        self.collection.print_all()


if __name__=="__main__":
    collection = mb.DonorCollection()
    donor_history = {'Fred Flintstone': [27.14, 89.14],
                     'Wilma Willbanks': [150.00],
                     'Barney Rubble': [250, 24, 57, 175],
                     }

    for name, amounts in donor_history.items():
        for amount in donor_history[name]:
            collection.add(name, amount)

    ui = MailroomUI(collection)
    ui.main_menu()



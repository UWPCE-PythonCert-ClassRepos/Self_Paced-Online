#!/usr/bin/python3


# Author/Student:  Roy Tate (githubtater)


import mailroom_backend as mb


class MailroomUI:

    def __init__(self, collection):
        if isinstance(collection, mb.DonorCollection):
            self.collection = collection
        else:
            raise TypeError('DonorCollection instance not found.')

    def menu_selection(self, arg_dict, response):
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
            '4':{'option': '- Exit', 'function': self.die}
        }
        print('\n{:*^20}'.format(' MAIN MENU '))
        while True:
            for k, v in sorted(main_menu_args.items()):
                print(k, v['option'])
            response = input('\nEnter your selection: \n').strip()
            self.menu_selection(main_menu_args, response)



    def die(self):
        print('\nExiting.')
        exit(0)

    def send_thank_you(self):
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
        report = self.collection.create_report()
        print(report)

    def email_all(self):
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
        donor_name = input('\nEnter the donor name (First Last): \n')
        donation_amount = float(input('\nEnter the donation amount: \n'))
        self.collection.add(donor_name, donation_amount)
        for k, v in self.collection.donors.items():
            if k == donor_name.strip():
                print(v.letter)



    def print_list(self):
        self.collection.print_all()


if __name__=="__main__":
    collection = mb.DonorCollection()

    # Populate the donor database
    collection.add('Bobby Jones', 232)
    collection.add('Bobby Jones', 1439)
    collection.add('Willie Wonka', 78979)
    collection.add('Fred Hammerman', 8477.232)
    collection.add('Fred Hammerman', 100343)
    collection.add('Fred Hammerman', 2563)
    ui = MailroomUI(collection)

    ui.main_menu()



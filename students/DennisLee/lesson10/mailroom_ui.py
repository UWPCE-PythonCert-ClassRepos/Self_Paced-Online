#!/usr/bin/env python3

import mailroom
import os

class DonorUI():

    def __init__(self, coll):
        self.feedback = self.get_resp
        if isinstance(coll, mailroom.DonorCollection):
            self.collection = coll
        else:
            raise TypeError("Must initialize with a DonorCollection object.")

    def manage_donors(self):
        """
        Display the menu of choices for donor management.

        :return:  None.
        """
        # create a dict of menu items/ menu text/ menu caller functions
        choices = {
        '1': {'option': 'Send a thank you', 'function': self.send_thank_you},
        '2': {'option': 'Create a report', 'function': self.collection.create_report},
        '3': {'option': 'Send all letters', 'function': self.send_all_letters},
        '4': {'option': 'Make projections', 'function': self.make_projections},
        '9': {'option': 'Quit', 'function': self.exit_screen}
        }
        
        while True:  # Print the menu list (with numbered choices)
            print("\nMENU:")
            for k, v in choices.items():
                print(k, v['option'])
            response = self.feedback("Type a menu selection number: ")
            self.call_menu_function(choices, response, 
                    self.respond_to_bad_main_menu_choice, bad_choice=response)
            if response == '9':  # Exit if "Quit" is chosen
                return

    def call_menu_function(
            self, choice_dict, choice, unfound_key_handler, **kwargs):
        """
        Call a menu function with a dict.

        :choice_dict:  Dict containing the `choice` string, with the dict
                    value being a another dict that contains a 'function'
                    key whose value is the function to call for `choice`.

        :choice:  A string that may or may not be a key in the choice_dict
                dictionary.

        :unfound_key_handler:  The function to call if the specified choice
                            is not a key in the dictionary.

        :kwargs:  Additional keyword arguments to pass to the unfound key
                handler.

        :return:  `True` if a menu function was successfully called;
                `False` otherwise (which also can be the desired result).
        """
        try:  # Get the selection number and call helper function
            choice_dict[choice]['function']()
        except KeyError:
            unfound_key_handler(**kwargs)
            return False
        else:
            return True

    def respond_to_bad_main_menu_choice(self, bad_choice):
        """
        Show error message if the user's main menu choice is invalid.
        
        :bad_choice:  The menu choice string as entered by the user.

        :return:  None.
        """
        print(f"\n'{bad_choice}' is an invalid response.")

    def exit_screen(self):
        """
        Simply print an exit message.

        :return:  None.
        """
        print("\nExiting.\n")
        return

    def send_thank_you(self):
        """
        Add new donations for new or existing donors, and send a thank-you
        letter.

        :return:  None.
        """
        alt_choices = {  # Dict of functions to show donor list or to quit
                '': {'function': self.exit_screen},
                'quit': {'function': self.exit_screen},
                'list': {'function': self.collection.print_donors}
        }
        print("\n")
        # Get the donor name, show all donors, or quit
        response = self.feedback("Type full donor name "
                "(or 'list' to show all donors, or 'quit'): ")

        self.call_menu_function(alt_choices, response, 
                self.get_donation_amount, donor=response)
        if response == 'list':
            self.send_thank_you()  # Still want to get a donor to thank

    def get_donation_amount(self, donor):
        """
        Ask user for a donation amount from the specified donor.

        :donor:  The name of the donor.

        :return:  None.
        """
        donation = self.feedback(
                f"Type amount to donate (or type 'quit'): ").lower()

        if donor in self.collection.donors:
            gifts = len(self.collection.donors[donor].donations)
        else:
            gifts = 0

        try:
            donation = float(donation)
        except ValueError:
            print(f"'{donation}' is not a valid donation amount.")
        else:
            self.collection.add(donor, donation)
            if donor in self.collection.donors:
                donor_obj = self.collection.donors[donor]
                if len(donor_obj.donations) == gifts + 1:
                    print("\n\n", donor_obj.form_letter, "\n\n")
                else:
                    print(f"\n\nDonation by '{donor}' of '{donation}' "
                            "was unsuccessful.\n\n")

    def send_all_letters(self):
        """
        Create all of the donor thank-you letters.

        :return:  None.
        """
        # Ask for the directory to save the letters to
        print('\nThe current directory is %s\n' % os.getcwd())
        new_dir = self.feedback('Type the directory to save the letters in'
                        ' (blank entry defaults to the current directory): ')
        try:
            full_dir_name = self.collection.save_letters(new_dir)
        except FileNotFoundError:
            print(f"Can't open or create folder '{new_dir}' - exiting "
                    "without creating the thank-you letters.")
        except PermissionError:
            print(f"Not allowed to write to '{new_dir}'.")
        except OSError:
            print(f"Specified folder '{new_dir}' is not valid.")
        else:
            print(f"\nLetters saved in folder '{full_dir_name}'.\n")

    def get_resp(self, prompt, **kwargs):
        return input(prompt).strip()

    def make_projections(self):
        proj_params = self.feedback(
                "\nProject your estimated donations by entering (1) your "
                "\nmatching factor (e.g., 1 means you double existing "
                "\ndonations, 2 means you triple existing donations, etc.), "
                "\n(2) the minimum existing donation amount, and (3) the "
                "\nmaximum existing donation amount, separated by whitespace:"
                "\n\n"
        )
        proj_vals = proj_params.split(None, 3)
        try:
            match_factor = float(proj_vals[0])
            min_gift = float(proj_vals[1])
            max_gift = float(proj_vals[2])
        except ValueError:
            print("\n\nOne of your entries is not a valid number.\n\n")
            self.exit_screen()
        except IndexError:
            print("\n\nYou did not enter three numbers.\n\n")
            self.exit_screen()
        else:
            cur_total = self.collection.projection_sum(
                    self.collection.projector(1.0, 0.0, 1e12))
            gifts_used_to_multiply = self.collection.projection_sum(
                    self.collection.projector(1.0, min_gift, max_gift))
            try:
                proj_gift = self.collection.projection_sum(
                        self.collection.projector(match_factor, min_gift, max_gift))
            except ValueError as ve:
                print(ve)
            else:
                print("\n\n",
                        f"Current donation total:  ${cur_total:>18,.2f}",
                        f"Matched donations:       ${gifts_used_to_multiply:>18,.2f}",
                        f"Your projected donation: ${proj_gift:>18,.2f}",
                        sep = "\n")


if __name__ == '__main__':
    # Initial donor list and the amounts they have donated
    donor_history = {
            'Red Herring': [65820.5, 31126.37, 15000, 2500],
            'Papa Smurf': [210.64, 1000, 57.86, 2804.83, 351.22, 48],
            'Pat Panda': [55324.4, 35570.53, 14920.50],
            'Karl-Heinz Berthold': [3545.2, 10579.31],
            'Mama Murphy': [156316.99, 8500.3, 12054.33, 600, 785.20],
            'Daphne Dastardly': [82]
    }

    coll = mailroom.DonorCollection()
    for name, amts in donor_history.items():
            coll.add(name, amts)

    print("\n\nViewing original database.\n\n")
    dui = DonorUI(coll)
    dui.manage_donors()

    print("\n\nMultiplying all donations by 3!\n\n")
    coll2 = coll.challenge(3)

    print("\n\nHere's collection 1:\n", coll)
    print("\nCollection 1 donors/donations:\n", coll.donors)
    print("\n\nHere's collection 2:\n", coll2)
    print("\nCollection 2 donors/donations:\n", coll2.donors)

    print("\n\nNow look at the new collection.\n\n")
    dui2 = DonorUI(coll2)
    dui2.manage_donors()

    print("\n\nNow filter out donations below 100 before multiplying.\n\n")
    coll3 = coll.challenge(3, 100)
    dui3 = DonorUI(coll3)
    dui3.manage_donors()

    print("\n\nNow filter out donations above 1000 before multiplying.\n\n")
    coll4 = coll.challenge(3, 0, 1000)
    dui4 = DonorUI(coll4)
    dui4.manage_donors()

    print("\n\nNow filter out donations below 100 and above 1000 before multiplying.\n\n")
    coll5 = coll.challenge(3, 100, 1000)
    dui5 = DonorUI(coll5)
    dui5.manage_donors()

    print("\n\nCheck whether the original donor collection is intact.\n\n")
    dui.manage_donors()

    del coll, coll2, coll3, coll4, coll5, dui, dui2, dui3, dui4, dui5, mailroom
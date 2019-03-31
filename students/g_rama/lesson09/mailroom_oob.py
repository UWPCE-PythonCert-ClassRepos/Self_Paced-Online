#!/usr/bin/env python3

from Donor import Donor
from DonorCollection import DonorCollection
from CLI import CLI

if __name__ == '__main__':


    donors = DonorCollection()
    cli = CLI()

    def thank_you():
        """Send a thank you letter"""
        fullname = CLI.fullname_input()
        if fullname.isalpha():
            if fullname == str("list"):
                donors.display_donors()
            elif fullname in donors.donors_collection_data.keys():
                amount = CLI.amount_input()
                donor = Donor(fullname, amount)
                donor.update_data_print_thanks()
            else:
                try:
                    amount = CLI.amount_input()
                    donor = Donor(fullname, amount)
                    donor.add_data_print_thanks()
                except ValueError:
                    print("Enter the correct amount in integer")
        else:
            print("Enter the donor name correctly")

    main_prompt = ("1 - Send a Thank You\n"
                   "2 - Create a Report\n"
                   "3 - Send letters to everyone\n"
                   "4 - Quit\n")
    main_dispatch = {"1": thank_you,
                     "2": donors.create_report,
                     "3": donors.send_letters,
                     "4": cli.exit_menu,
                     }
    cli.menu_selection(main_prompt, main_dispatch)

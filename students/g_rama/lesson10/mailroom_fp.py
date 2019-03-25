#!/usr/bin/env python3

from Donor import Donor
from DonorCollection import DonorCollection
from CLI import CLI

if __name__ == '__main__':

    donor = Donor()
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
                donor.update_data_print_thanks(amount, fullname)
            else:
                try:
                    amount = CLI.amount_input()
                    donor.add_data_print_thanks(amount, fullname)
                except ValueError:
                    print("Enter the correct amount in integer")
        else:
            print("Enter the donor name correctly")

    def challenge_factor():
        """A function to take the multiple """
        factor = CLI.mulfactor_input()
        min_donation = CLI.min_donation_input()
        max_donation = CLI.max_donation_input()
        donors.multiply_factor(factor, min_donation, max_donation, **donors.donors_collection_data)

    def projections():
        fullname = CLI.fullname_input()
        if fullname in donors.donors_collection_data.keys():
            projected_donor = {fullname: donors.donors_collection_data[fullname]}
            factor = CLI.mulfactor_input()
            min_donation = CLI.min_donation_input()
            max_donation = CLI.max_donation_input()
            donors.multiply_factor(factor, min_donation, max_donation, **projected_donor)


    main_prompt = ("1 - Send a Thank You\n"
                   "2 - Create a Report\n"
                   "3 - Send letters to everyone\n"
                   "4 - Challenge factor\n"
                   "5 - Projections with factors\n"
                   "6 - Quit\n")
    main_dispatch = {"1": thank_you,
                     "2": donor.create_report,
                     "3": donors.send_letters,
                     "4": challenge_factor,
                     "5": projections,
                     "6": cli.exit_menu,
                     }
    cli.menu_selection(main_prompt, main_dispatch)






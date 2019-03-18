#!/usr/bin/env python3

from Donor import Donor
from Donors import Donors
from CLI import CLI

if __name__ == '__main__':

    donor = Donor()
    donors = Donors()
    cli = CLI()
    main_prompt = ("1 - Send a Thank You\n"
                   "2 - Create a Report\n"
                   "3 - Send letters to everyone\n"
                   "4 - Quit\n")
    main_dispatch = {"1": donor.thank_you,
                     "2": donor.create_report,
                     "3": donor.send_letters,
                     "4": cli.exit_menu,
                     }
    cli.menu_selection(main_prompt, main_dispatch)

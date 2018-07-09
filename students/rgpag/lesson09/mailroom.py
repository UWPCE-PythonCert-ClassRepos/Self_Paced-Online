#!/usr/bin/env python3
import datetime
from mailroom_classes import (Donor, Donor_collect)

a = Donor("Jeff Bezos", [100])
b = Donor("Elon Musk", [500, 200])
c = Donor("Bill Gates", [50])
donor_list = [a, b, c]
D = Donor_collect(donor_list)

msg = """
\nDear {},\n\nThank you for your recent donation, did you \
realize you have now made {} lifetime donations? Wow, look at you all star! \
We are most grateful for your total donation amount of ${}.\n\nI will \
personally ensure these funds are put towards purchase of yummy \
donuts! Also, any additional contributions you make in the next 24 hours \
will be matched up to $1000. What a deal! Don't delay.\n\nHumbly yours,\n
Dime for Donuts\n
"""


def print_format_msg(msg_vars):
    print(msg.format(*msg_vars))


def don_in(don_amt=""):
    if don_amt == "":
        while True:
            try:
                don_amt = int(input('What was the donation amount?'))
            except ValueError:
                print('input must be an integer, try again')
            else:
                break
    return don_amt


def ind_thanks(name_in="", Donor_collect_obj=D):

    """ind_thanks(name_in="", D=D where 'D' is Donor_collect object)"""
    while name_in == "":
        name_in = input('Please provide full name (or try "list" or "menu") ')
    if name_in == 'menu':
        return False
    elif name_in == 'list':
        Donor_collect_obj.get_donors()
    elif name_in not in Donor_collect_obj.donor_dict:
        don_amt = don_in()
        Donor_collect_obj.new_donor(name_in, don_amt)
        print_format_msg(D.get_msg_vars(name_in))
        return
    else:
        don_amt = don_in()
        D.update_donor(name_in, don_amt)
        print_format_msg(D.get_msg_vars(name_in))
        return


def all_thanks(Donor_collect_obj=D):
    date = datetime.datetime.now()
    for donor in Donor_collect_obj.donor_dict:
        file_name = '{}_{}_{}_{}.txt'.format(donor, date.month, date.day,
                                             date.year)
        msg_vars = Donor_collect_obj.get_msg_vars(donor)
        with open(file_name, 'w') as new_file:
            new_file.write(msg.format(*msg_vars))


menu_switch_dict = {
    '1': ind_thanks,
    'send a thank you': ind_thanks,
    '2': D.print_rpt,
    'create a report': D.print_rpt,
    '3': all_thanks,
    'send letters to everyone': all_thanks
    }

if __name__ == "__main__":
    while True:
        sel = input("""\nWhat do you want to do?\
            \n\t(1) send a thank you\
            \n\t(2) create a report\
            \n\t(3) send letters to everyone\
            \n\t(4) quit\n""")
        if sel in ('4', 'quit'):
            break
        try:
            menu_switch_dict[sel]()
        except KeyError:
            print("invalid selection, please try again")
            continue

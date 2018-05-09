#!/usr/bin/env python3

'''
file: run_mailroom.py
elmar_m / 22e88@mailbox.org
Lesson09: executable for OOP mailroom program 
'''

from functions_mailroom import menu, list_donors, list_donations,\
    add, fakefunc, efunc, get_number_of_donations, get_average_donation


if __name__ == '__main__':

    prompt = '\
    \nPlease choose an option:\
    \n\t1: list donors\
    \n\t2: list donations of a donor\
    \n\t3: add donor and / or donation\
    \n\t4: send thankyou mail\
    \n\t5: show report\
    \n\t6: quit program\
    \n\t7: get number of donations of a donor\
    \n\t8: get average donation of a donor\n\n'

    dispatcher = {
        '1' : list_donors,
        '2' : list_donations,
        '3' : add,
        # '4' : thankyou,
        '4' : fakefunc,
        # '5' : report,
        '5' : fakefunc,
        '6' : efunc,
        '7' : get_number_of_donations,
        '8' : get_average_donation,
        }

    print('\n*** Welcome to OOP mailroom. ***')
    menu(prompt, dispatcher)
    print('\n***Thanks for using OOP mailroom. Goodbye.***\n')



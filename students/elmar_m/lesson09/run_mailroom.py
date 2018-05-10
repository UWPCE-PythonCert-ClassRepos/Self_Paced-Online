#!/usr/bin/env python3

'''
file: run_mailroom.py
elmar_m / 22e88@mailbox.org
Lesson09: executable for OOP mailroom program 
'''

from functions_mailroom import menu, list_donors, list_donations,\
    add, thankyou, fakefunc, report, efunc


if __name__ == '__main__':

    prompt = '\
    \nPlease choose an option:\
    \n\t1: list donors\
    \n\t2: list donations of a donor\
    \n\t3: add donor and / or donation\
    \n\t4: send thankyou mail\
    \n\t5: show report\
    \n\t6: quit program\n\n'

    dispatcher = {
        '1' : list_donors,
        '2' : list_donations,
        '3' : add,
        '4' : thankyou,
        # '4' : fakefunc,
        '5' : report,
        '6' : efunc,
        }

    print('\n*** Welcome to OOP mailroom. ***')
    menu(prompt, dispatcher)
    print('\n***Thanks for using OOP mailroom. Goodbye.***\n')



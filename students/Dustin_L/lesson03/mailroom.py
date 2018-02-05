#!/usr/bin/env python3
"""Mail Room Module

This module contains all of the functions for the Mail Room module.
"""

# Name, Gifts, Num Gifts, Total, Average
DONATION_DB = [['Toni Morrison',     [1000, 5000, 10000],           0, 0, 0],\
               ['Mike McHargue',     [12000, 50000, 27000],         0, 0, 0],\
               ["Flannery O'Connor", [38734, 6273, 67520],          0, 0, 0],\
               ['Angela Davis',      [74846, 38470, 7570, 50],      0, 0, 0],\
               ['Bell Hooks',        [634547, 47498, 474729, 4567], 0, 0, 0]]
THANK_YOU_OPT = 1
REPORT_OPT    = 2
QUIT_OPT      = 3

def get_usr_input():
    """Get input from user.

    Prompt user to select one of three choices. If the user selects one of these
    three, that value is returned. If not, the user is prompted again to select.

    Returns:
        int: Value corresponding to user choice
    """
    select_prompt = '\nPlease select from the following options:\n'\
                    '\t1. Send a Thank You\n'\
                    '\t2. Create a Report\n'\
                    '\t3. quit\n'\
                    ' --> '
    while True:
        usr_in = int(input(select_prompt).strip())

        if usr_in == THANK_YOU_OPT or usr_in == REPORT_OPT or usr_in == QUIT_OPT:
            break
        else:
            print('\nPlease enter either a "1", "2", or "3"\n')

    return usr_in


def main():
    """Main function"""
    choice = get_usr_input()


if __name__ == '__main__':
    main()

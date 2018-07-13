# ----------------------------------------------------------------------------------------------------------------------
# NAME: MICAH BRAUN
# PROJECT: mailroom_3.py - Lesson 05 Assignment
# PURPOSE: Working with exception handlers
# DATE: 06/23/2018
# EDITS MADE: 06/29/2018 -- Try, Except blocks added for exception handling, .get() removed from menu(),
# 'pair' var updated to handle error on quitting before assigning donation value to new name entry in thankyou()
#
# DESCRIPTION: Adding try/except blocks where appropriate to existing mailroom program to streamline code
#  and handle problems that could arise during runtime. ** NOTE: I had already built-in many if/else blocks
#  to handle 'bad' input from the user so I moved some out but where it would have caused a big disruption
#  to the architecture of the rest of the surrounding code, I left it as-is. **
#
# While I would like to add comprehensions to my program to simplify things or make it more succinct, I did
# not find any workable situations for me to apply the examples I had with the way I had structured things
# (short of re-writing the entire thing just to add comprehensions...)
# ----------------------------------------------------------------------------------------------------------------------

import time     # time to supply today's date for letters
import os       # for default working directory
import locale   # for currency formatting
import sys      # for error handling
#  --------------------------------------------------- DATA ------------------------------------------------------------

locale.setlocale(locale.LC_ALL, '')
today = time.strftime("%m/%d/%Y")

spacing = '- ' * 56  # formatting for DONOR header
donor_dict = {'Columns': ['NAMES', 'DONATION AMOUNT', 'NUMBER OF GIFTS', 'AVG. GIFTS'],
              'Rudolph Soares': ['Rudolph Soares', 1335, 3, 445],  # Donor info
              'Josef Mistretta': ['Josef Mistretta', 7500, 4, 1875],
              'Joye Agostini': ['Joye Agostini', 600, 2, 300],
              'Rachelle Levan': ['Rachelle Levan', 12100, 5, 2420],
              'Vena Ussery': ['Vena Ussery', 4000, 8, 500],
              'Efrain Lager': ['Efrain Lager', 795, 9, 88.34],
              'Mee Heine': ['Mee Heine', 4600, 4, 1150],
              'Tanya Essex': ['Tanya Essex', 75000, 2, 37500]}


#  ------------------------------------------------- PROCESSING --------------------------------------------------------

def menu():
    """Display menu of options to toggle between to perform separate actions"""
    header = "-" * 110  # formatting for header
    title = ' ' * 48 + "MAIL ROOM MENU"  # title display
    directions = "Select one of the three options:"  # directions to user for menu
    optA = "[A] Send a Thank you"  # option(s) for menu
    optB = "[B] Create a Report"
    optC = "[C] Create Letters for All Donors"
    optD = "[D] Quit"
    whole_menu_header = header + '\n' + title + '\n' + header  # header strung together as one uni

    while True:
        print(whole_menu_header)  # display header
        print(directions.center(110, ' '), '\n')  # center directions with header display
        print(optA + optB.center(37, ' ') + optC.center(36, ' ') + optD.center(25, ' ') + '\n')

        switch_function = {
            'A': thankyou,  # dictionary holding menu options
            'B': createreport,
            'C': writeletters,
            'D': quit_program,
        }
        try:
            usr_sel = (input("Menu Selection: ")).upper()  # user input for menu
            switch_function[usr_sel]()  # get user entry from dict

        except KeyError:
            print("Invalid Entry! Only enter A, B, C, or D.")  # display error on any other entry
        continue  # continue back to start of menu


def thankyou():
    """Function enables user to add to dictionary data (adding new donors and donation amounts as well as
    number of donations and average donations for new keys, and also updates existing keys."""
    print("Leaving menu...\n")
    while True:
        print("Enter the name of the person you are writing to (or enter 'list' to see a list of names or Q to quit) ")
        fname_prompt = input("First Name: ").strip().capitalize()  # first name variable (strip any spaces)
        if fname_prompt.upper() == "Q":  # if Q, then quit to menu()
            menu()
        elif fname_prompt.lower() == "list":
            displaylist()
        else:
            lname_prompt = input("Last Name: ").strip().capitalize()  # last name variable
            if lname_prompt.upper() == "Q":  # if Q, back to menu
                menu()
            elif lname_prompt.lower() == "list":  # if list, then list display
                displaylist()
            else:
                key = fname_prompt + " " + lname_prompt
                if key in donor_dict.keys():
                    existing_donor = input(
                        "That value is already in the list! Do you want to proceed with that selection? (Y/N): ")
                    if existing_donor.upper() == "Y":  # if user proceeds, print display
                        donation_amt_str = input("Enter in the donation amount from Donor {0}: $".format(key))
                        if donation_amt_str.lower() == 'q':
                            menu()
                        try:
                            donation_amt = int(donation_amt_str)
                        except ValueError:
                            print("Error: invalid entry.\n")
                        else:
                            print(
                                '{0} has donated ${1:,.2f}'.format(key, donation_amt))  # display name and donation amt
                            int(donation_amt)
                            get_index = 0  # index variable
                            for item in range(0, len(donor_dict)):  # set index var to current name
                                if list(donor_dict.values())[item][0] == key:
                                    get_index = item
                                    break
                            firstname = list(donor_dict.values())[get_index][0].split(' ', ).pop(
                                0)  # separate first name, create variable
                            current_donations = int(
                                list(donor_dict.values())[get_index][1])  # current amt/ var from dict{[val]}
                            sum_donations = current_donations + donation_amt  # sum of all donations (current + new)
                            list(donor_dict.values())[get_index][1] = float(sum_donations)  # update sum
                            num_donations = int(list(donor_dict.values())[get_index][2]) + 1  # num donations = self + 1
                            list(donor_dict.values())[get_index][2] = num_donations  # update num of donations
                            list(donor_dict.values())[get_index][3] = averagedonations(sum_donations,
                                                                                       num_donations)  # update avg
                            email_display = str(
                                input("Display Donor Email? (Y/N or Q): "))  # ask user if they want to to
                            if email_display.upper() == "Y":  # write email with name/amount
                                print(spacing)
                                print('Dear {0}, \n\nThank you for your continued support through your \
contribution of ${1:,.2f} towards our Foundation\'s fundraising goal.\n\nBest wishes,\n\
Foundation Board of Directors\n'.format(firstname, sum_donations))
                                print(spacing)
                            elif email_display.upper() == 'Q':
                                menu()
                            else:
                                continue
                else:
                    add_name = str(input("That name is not in the Donor list. Do you want to add it to the list? (Y/N) "))
                    if add_name.upper() == "Y":  # if input response == "Y", proceed
                        pair = {key: [key, 0, 0, 0]}
                        donor_dict.update(pair)
                        displaylist()
                        num_donations = 1  # add new item to new name index
                        donation_amt_str = input("Enter in the donation amount from Donor {0}: $".format(key))
                        if donation_amt_str.lower() == 'q':
                            menu()
                        try:
                            donation_amt = int(donation_amt_str)
                        except ValueError:
                            print("Error: Invalid entry.\n")
                        else:
                            print('{0} has donated ${1:,.2f}'.format(key, donation_amt))
                            get_index = 0  # counter, start at 0
                            for item in range(0, int(len(list(donor_dict.values())))):  # for items in donor_dict
                                if list(donor_dict.values())[item][0] == key:  # if item at[0] == full_name
                                    get_index = item  # set index to item
                                    break
                            # noinspection PyTypeChecker
                            list(donor_dict.values())[get_index].append(donation_amt)
                            # noinspection PyTypeChecker
                            list(donor_dict.values())[get_index].append(num_donations)  # append donation count to end
                            avg = averagedonations(donation_amt, num_donations)
                            list(donor_dict.values())[get_index].append(avg)  # append average to end of current index
                            firstname = list(donor_dict.values())[get_index][0].split(' ', ).pop(0)  # separate first name, create variable
                            email_display = str(input("Display Donor Email? (Y/N): "))  # ask user if they want to
                            if email_display.upper() == "Y":  # print email message
                                print(spacing)  # if Y, then print
                                print('Dear {0}, \n\nThank you for your continued support through your \
contribution of ${1:,.2f} towards our Foundation\'s fundraising goal.\n\nBest wishes,\n\
Foundation Board of Directors\n'.format(firstname, donation_amt))
                                print(spacing)
                            elif email_display.upper() == 'Q':
                                menu()
                            else:
                                continue


def createreport():
    """Function creates organized report of donor information based on current dictionary contents.
    Information is sorted in descending order based on total donation amounts."""
    print("Leaving menu...")
    while True:  # continual loop unless user terminates
        proceed = str(input("Generate Donor report? (Y/N): "))  # solicit user response to proceed
        if proceed.upper() == "Y":  # if user indicates yes
            input("Generating Donor report... [Press Enter]")  # on Enter press, proceed
            new_list = list(donor_dict.values())[1:]  # blank list to hold only values after headers
            new_list.sort(key=lambda sort_on: sort_on[1], reverse=True)  # sort list based on donation totals
            lst_heading = list(donor_dict.values())[0:1]  # container for only header
            final_lst = lst_heading + new_list  # join sorted list back with header
            print(spacing)
            print('{:>15s}'.format(str(final_lst[0][0])), end='')  # format header for display
            print('         |{:>20s}'.format(str(final_lst[0][1])), end='')
            print('   |{:>19s}'.format(str(final_lst[0][2])), end='')
            print('    |{:>15s}'.format(str(final_lst[0][3])))
            print(spacing)
            for i in range(1, int(len(final_lst))):  # format list contents
                print('{:>20s}'.format(str(final_lst[i][0])), end='')
                print('            ${:>10,.2f}{:>17}'.format(float(final_lst[i][1]), int(final_lst[i][2])), end='')
                print('                 ${:>10,.2f}'.format(float(final_lst[i][3])))
        else:
            back_to_menu = str(input("Do you want to quit back to the main menu? (Y/N): "))  # escape sequence
            if back_to_menu.upper() == "Y":
                input("Quitting... [Press Enter]")
                menu()
            else:
                continue  # if no esc, then continue loop


def writeletters():
    """Function writes donor letter to file in user-directed file path"""
    print("Leaving menu...")
    names_list = []  # empty list to hold list of donor_dict names w/o whitespace (for filenames)
    first_names = []  # first names separated out to be used for letters
    default = os.getcwd()  # get and assign current directory to variable
    default = default + "\\"  # format default so that it will be accepted (will work with Windows)
    while True:
        msg = input("Proceed to write letters to all donors in donor list? (Y/N) ")  # if user selects Y, proceed
        if msg.upper() == "Y":  # check input
            try:
                working_directory = str(input('\nEnter the file path where you want to write the letters - '
                                              'don\'t forget to use ''two \n\'\\\\\' as file separators to make sure'
                                              ' it is compatible if using Windows - (e.g. \'C:\\\\\': '))
            except Exception as e:              # exception handler - prints line of error, and type
                print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
            # working directory variable assignment by user - if blank, use default
            if working_directory == "":  # check for input on working_directory
                working_directory = default

            for x in range(int(len(donor_dict))):  # for items in the span of donor_dict
                firstname = list(donor_dict.values())[x][0]  # firstname = donor_dict at index[item], column[0]
                firstname = firstname.split(' ', ).pop(0)  # format var to split on whitespace (only first name)
                first_names.append(firstname)  # append this value to empty list first_names

            for i in range(int(len(list(donor_dict.values())))):  # for items in the span of donor_dict
                elem = list(donor_dict.values())[i][0]  # elem = donor_dict at index[i], column[0]
                elem = elem.replace(" ", "")  # format name w/o whitespace
                names_list.append(elem)  # append to name_list

            for names in range(1, int(len(names_list))):  # omit header (range 0), for each name in names_list[]
                try:
                    with open(working_directory + str(names_list[names]) + '.txt',
                              'a') as filename:  # create files/file-names
                        filename.write(today)  # write current date (mm/dd/yy)
                        filename.write('\n\nDear {0}, \n\nThank you for your continued support through your contribution '
                                       'of {1} towards our Foundation\'s fundraising goal.\n\nBest wishes,\n'
                                       'Foundation Board of Directors'
                                       '\n'.format(str(first_names[names]),
                                                   locale.currency(list(donor_dict.values())[names][1], grouping=True)))
                except Exception as e:              # exception handler - prints line of error, and type
                    print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
                # print letter message (first name and donation amount)
            print("Files being written to " + working_directory + "...")
            print("Done!")  # message to user advising where files are going, and when it is done

        elif msg.upper() == "N":  # if user selected "N" for msg = input()
            input("Exiting back to menu [Press ENTER]")  # message to user, leaving this function
            break  # break out of while-loop - back to menu()
        else:
            print("That's an unrecognized value! Only Y or N are accepted.")
            continue  # invalid input, warning message: back to beginning of function


def quit_program():
    """Function quits all processes"""
    input("Exiting Program...[Press ENTER]")    # I use PyCharm and exit() w/o import worked fine but
    from sys import exit                        # iPython was not running exit() without importing it from sys
    exit()                                      # so to avoid issues, I just kept this here


def displaylist():
    """Function returns current dictionary contents (names only)"""
    cut_off = int(len(list(donor_dict.values())) / 2)  # where list breaks for next line
    if int(len(list(donor_dict.values()))) - 1 % 2 != 0:  # even/odd check
        for i in range(0, int(len(list(donor_dict.values())) - int(len(list(donor_dict.values())) - 2) / 2)):
            if i == 0:  # header check
                print(spacing)
                print('{:>44s}'.format(str(list(donor_dict.values())[i][0])))  # print Donor Name header
                print(spacing)
            elif cut_off + i >= len(list(donor_dict.values())):  # if cut_off + i exceeds len(list)
                print('{:>30s}'.format(list(donor_dict.values())[i][0]))  # only print i (not cut_off + i)
                continue
            else:
                print('{:>30s}'.format(list(donor_dict.values())[i][0]),
                      '{:>35s}'.format(list(donor_dict.values())[cut_off + i][0]))
    else:
        for i in range(0, int(len(list(donor_dict.values())) / 2)):
            if i == 0:  # header check
                print(spacing)
                print('{:>44s}'.format(str(list(donor_dict.values())[i][0])))  # print Donor Name header
                print(spacing)
            else:
                print('{:>30s}'.format(list(donor_dict.values())[i][0]),
                      '{:>35s}'.format(list(donor_dict.values())[cut_off + i][0]))
    print()


def averagedonations(donations, num):
    """Returns average of donor's gifts"""
    sumgifts = donations
    numgifts = num

    average_donation = sumgifts / numgifts
    return average_donation


#  -------------------------------------------------- DISPLAY ----------------------------------------------------------

menu()  # Program starts here

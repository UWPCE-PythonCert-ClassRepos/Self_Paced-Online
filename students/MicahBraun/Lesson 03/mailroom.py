# ------------------------------------------------------------------------
# NAME: MICAH BRAUN
# PROJECT: mailroom.py
# PURPOSE: Working with arraysv(nested lists), manipulating data
# DATE: 05/24/2018
#
# DESCRIPTION: Program is menu-driven user interface for interacting
#              with a nested list of stored information. User is able
#              to add names to a list (not currently saved upon program
#              exit), append values to fields, check against current
#              fields, create mock "Thank You" e-mails based on user-
#              -input and associated fields, and generate tabular display
#              of data for viewing.
# ------------------------------------------------------------------------

# Data -------------------------------------------------------------------
spacing = '- ' * 55  # formatting for DONOR header
data_list = [['NAMES', 'DONATION AMOUNT', 'NUMBER OF GIFTS', 'AVG. GIFTS'],
             ['Rudolph Soares', 1500, 3, 1566],                                    # Donor info
             ['Josef Mistretta', 250, 5, 235],
             ['Joye Agostini', 5000, 2, 5750],
             ['Joni Mattix', 2750, 1, 2750],
             ['Rachelle Levan', 750, 3, 581],
             ['Vena Ussery', 1000, 7, 785],
             ['Efrain Lager', 10000, 1, 10000],
             ['Mee Heine', 15000, 2, 9750],
             ['Tanya Essex', 50000, 1, 50000],
             ['Garrett Hartsell', 800, 2, 1400]]

# Processing --------------------------------------------------------------

def menu():
    """Display menu of options to user"""
    header = "-" * 100  # formatting for header
    title = ' ' * 43 + "MAIL ROOM MENU"  # title display
    directions = "Select one of the three options:"  # directions to user for menu
    optA = "[A] Send a Thank you"  # option(s) for menu
    optB = "[B] Create a Report"
    optC = "[C] Quit"
    whole_menu_header = header + '\n' + title + '\n' + header  # header strung together as one uni


    while True:
        print(whole_menu_header)  # display header
        print(directions.center(100, ' '), '\n')  # center directions with header display
        print(optA + optB.center(60, ' ') + optC.center(31, ' ') + '\n')

        usr_sel = str(input("Menu Selection: ")).upper()

        if usr_sel == "A":
            print("Leaving menu...")
            thankyou()
        elif usr_sel == "B":
            print("Leaving menu...")
            createreport()
        elif usr_sel == "C":
            input("Exiting Program...[Press Enter]")
            exit()
        elif usr_sel != "A" or usr_sel != "B" or usr_sel != "C":
            print("\nOnly enter A, B, or C!")
            continue


def thankyou():
    """Method for sending 'Thank You' messages to Donors, using names *"""

    while True:
        search_names = [elem[0] for elem in data_list]                  # update search_names
        print("Enter the name of the person you are writing to (or enter 'list' to see a list of names or Q to quit) ")
        fname_prompt = input("First Name: ").strip().capitalize()       # first name variable (strip any spaces)
        if fname_prompt.upper() == "Q":                                 # if Q, then quit to menu()
            menu()
        elif fname_prompt.lower() == "list":                            # if firstname prompt == "list"
            if len(data_list) - 1 % 2 != 0:                             # check list to see if even/odd length
                for i in range(0, int(len(data_list) - 1 / 2)):         # list len(odd), i in size of list - 1/ 2
                    cut_off = int((len(data_list)) / 2)                 # starting, cut_off == len of initial data list / 2
                    if i == 0:                                          # check for header
                        print(spacing)
                        print('{:>44s}'.format(str(data_list[i][0])))   # print Donor Name header with decorations
                        print(spacing)
                    elif cut_off + i >= len(data_list):                 # if cut_off + i has exceeded len(data_list)
                        continue                                        # move on
                    else:
                        print('{:>30s}'.format(data_list[i][0]), '{:>35s}'.format(data_list[cut_off + i][0]))  # print out names
            else:
                if i == 0:                                                  # list(len(even)) -- for each item in list / 2
                    print(spacing)
                    print('{:>20s}'.format(str(data_list[i])))              # print Donor Name header
                    print(spacing)
                else:
                    print('{:>15s}'.format(data_list[i][0]), '{:>30s}'.format(data_list[cut_off + i][0]))
        else:
            lname_prompt = input("Last Name: ").strip().capitalize()        # last name variable
            if lname_prompt.upper() == "Q":                                 # if Q, back to menu
                menu()
            elif lname_prompt.lower() == "list":                            # if list, then list display
                if len(data_list) - 1 % 2 != 0:                             # check length of list, if odd print list -
                    for i in range(0, int(len(data_list) - 1 / 2)):         # -odd justified
                        cut_off = int((len(data_list)) / 2)
                        if i == 0:                                          # header check
                            print(spacing)
                            print('{:>44s}'.format(str(data_list[i][0])))   # print Donor Name header
                            print(spacing)
                        elif cut_off + i >= len(data_list):                 # if cut_off + i has exceeded len(data_list)
                            continue                                        # move on
                        else:
                            print('{:>30s}'.format(data_list[i][0]), '{:>35s}'.format(data_list[cut_off + i][0]))   # display names
                else:                                                       # if even list length - print names
                    if i == 0:
                        print(spacing)
                        print('{:>20s}'.format(str(data_list[i][0])))       # print Donor Name header
                        print(spacing)
                    else:
                        print('{:>15s}'.format(data_list[i][0]), '{:>30s}'.format(data_list[cut_off + i][0]))
            else:                                                           # if first+last name aren't list or empty
                full_name = fname_prompt + " " + lname_prompt               # full_name = vals of fname + lname
                if full_name in search_names:                               # search list of only names for full_name
                    existing_donor = input("That value is already in the list! Do you want to proceed with that selection? (Y/N): ")
                    if existing_donor.upper() == "Y":                       # if user proceeds, print display
                        donation_amt = int(input("Enter in the donation amount from Donor {0}: $".format(full_name)))
                        print('{0} has donated ${1}'.format(full_name, donation_amt))       # display name and donation amt
                        get_index = 0                                       # index variable

                        for item in range(0, len(data_list)):               # set index var to current name
                            if data_list[item][0] == full_name:
                                get_index = item
                                break
                        data_list[get_index][1] += donation_amt             # update donation amount
                        data_list[get_index][2] += 1                        # update num of donations
                        average = (data_list[get_index][1] * data_list[get_index][2]) / data_list[get_index][2]  # calculate avg
                        data_list[get_index][3] = average                   # update average

                        email_display = str(input("Display Donor Email? (Y/N): "))      # ask user if they want to to
                        if email_display.upper() == "Y":                                # write email with name/amount
                            print(spacing)
                            print('Dear {0}, \n\nThank you for your continued support through your \
contribution of ${1} towards our Foundation\'s fundraising goal.\n\nBest wishes,\n\
Foundation Board of Directors\n'.format(data_list[get_index][0], data_list[get_index][1]))
                            print(spacing)
                else:
                    name_found = False                                      # if name not found, set flag to False
                    if name_found is False:
                        add_name = input("That name is not in the Donor list. Do you want to add it to the list?  ").upper()
                        if add_name == "Y":                                 # if input response == "Y", proceed
                            data_list.append([full_name])                   # append new name to data_list
                            if len(data_list) - 1 % 2 != 0:                 # even/odd check
                                for i in range(0, int(len(data_list) - (len(data_list) - 2) / 2)):  # to be honest, I do not
                                    # actually know why this line works... I worked at different numbers for a long time
                                    # until I tried using this combination and it consistently displayed the names
                                    # in the right arrangement regardless of how many names were added. I do not
                                    # understand why it works, though.
                                    cut_off = int((len(data_list)) / 2)                 # where list breaks for next line
                                    if i == 0:                                          # header check
                                        print(spacing)
                                        print('{:>44s}'.format(str(data_list[i][0])))   # print Donor Name header
                                        print(spacing)
                                    elif cut_off + i >= len(data_list):                 # if cut_off + i exceeds len(list)
                                        print('{:>30s}'.format(data_list[i][0]))        # only print i (not cut_off + i)
                                        continue
                                    else:
                                        print('{:>30s}'.format(data_list[i][0]), '{:>35s}'.format(data_list[cut_off + i][0]))
                            else:
                                if i == 0:                                              # list length even
                                    print(spacing)
                                    print('{:>20s}'.format(str(data_list[i][0])))       # print Donor Name header
                                    print(spacing)
                                else:
                                    print('{:>15s}'.format(data_list[i][0]), '{:>30s}'.format(data_list[cut_off + i][0]))

                            add_donation_count = 1                                  # add new item to new name index
                            donation_amt = int(input("Enter in the donation amount from Donor {0}: $".format(full_name)))
                            print('{0} has donated ${1}'.format(full_name, donation_amt))
                            get_index = 0                                           # donation index (-1) end of list
                            for item in range(0, len(data_list)):                   # for items in data_list
                                if data_list[item][0] == full_name:                 # if item at[0] == full_name
                                    get_index = item                                # set index to item
                                    break
                            data_list[get_index].append(donation_amt)               # append donation amount to end of current lst [don_idx]
                            data_list[get_index].append(add_donation_count)         # append donation count to end
                            if data_list[get_index][2] == 1:                        # if donation count is 1 (it should be)
                                avg = data_list[get_index][1]                       # average variable assignment
                            data_list[get_index].append(avg)                        # append average to end of current index

                            email_display = str(input("Display Donor Email? (Y/N): "))      # ask user if they want to
                            if email_display.upper() == "Y":                                # print email message
                                print(spacing)                                              # if Y, then print
                                print('Dear {0}, \n\nThank you for your continued support through your \
contribution of ${1} towards our Foundation\'s fundraising goal.\n\nBest wishes,\n\
Foundation Board of Directors\n'.format(data_list[get_index][0], data_list[get_index][1]))
                                print(spacing)


def createreport():
    while True:                                                                 # continual loop unless user terminates
        proceed = str(input("Generate Donor report? (Y/N): "))                  # solicit user response to proceed
        if proceed.upper() == "Y":

            input("Generating Donor report... [Press Enter]")                   # on Enter press, proceed
            new_list = data_list[1:]                                            # blank list to hold only values after headers
            new_list.sort(key=lambda sort_on: sort_on[1], reverse=True)         # sort list based on donation totals
            lst_heading = data_list[0:1]                                        # container for only header
            final_lst = lst_heading + new_list                                  # join sorted list back with header
            print(spacing)
            print('{:>15s}'.format(str(final_lst[0][0])), end='')               # format header for display
            print('         |{:>20s}'.format(str(final_lst[0][1])), end='')
            print('   |{:>19s}'.format(str(final_lst[0][2])), end='')
            print('    |{:>15s}'.format(str(final_lst[0][3])))
            print(spacing)

            for i in range(1, int(len(final_lst))):                             # format list contents
                print('{:>20s}'.format(str(final_lst[i][0])), end='')
                print('            ${:>10,.2f}{:>17}'.format(float(final_lst[i][1]), int(final_lst[i][2])), end='')
                print('                 ${:>10,.2f}'.format(float(final_lst[i][3])))
        else:
            back_to_menu = str(input("Do you want to quit back to the main menu? (Y/N): "))     # escape sequence
            if back_to_menu.upper() == "Y":
                input("Quitting... [Press Enter]")
                menu()
            else:
                continue                                                          # if no esc, then continue loop


# Display -------------------------------------------------------------------

menu() # Program starts here

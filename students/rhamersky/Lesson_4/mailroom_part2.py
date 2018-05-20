#!/usr/bin/env python3
# Description: This program will allow a user to input a donor and a donation.
# The user will also be able to send out thank you notes to the donors.
# Developer: Ryan Hamersky
# Date: 05/13/2018
# Rev: A - 05/16/2018 updated code to reflect comments made by the instructor in mailroom_part.py.
#      Update variables to snake_case. Removed unnecessary 'continues' and 'returns'.
#      Changed 'bool' variable to 'bool_flag'. Updated misleading function names.
#      Reduced the amount of unnecessary print() statements.

# -----Data Section-----
import os
str_name = None     # --> User's name
int_option = int()  # --> User's option.
tup_donor_names = (["William Gates, III",1,10000.0],["Mark Zuckerberg",1,20000.0],
                   ["Jeff Bezos",1,1200.0],["Paul Allen",1,5000.0],
                   ["Mike Scott",1,25.0])  # --> Tuple that stores all donor's information
str_salutation = ""   # --> Email salutation
str_body = ""         # --> Email body
str_valediction = ""  # --> Email valediction

# -----Process Section-----
#  Methods defined in the menu class are related to general menu checks or options based on user inputs.

class menu(object):
    @staticmethod
    def menu_options():
        '''
        Try and except block used on User's option choice to check for integers.
        :return: Returns int data (1-4) which is used to determine what menu option will be executed.
        '''
        while True:
            try:
                int_choice = int(input(str_name + ", please select an option above. "))
            except ValueError:
                print(str_name + ", not a valid option. \n")
            # Verify that the user selected an option 1 through option 4.
            else:
                if 1 <= int_choice <= 4:
                    break
                else:
                    print("Integer selected is not a valid option. "
                          "Please, enter an integer and corresponds to the options given. \n")
        return int_choice
############## END OF MENU CLASS ######################

# Methods in the sub_menu class will execute code based off of the user's sub-menu choice.


class sub_menu(object):
    @staticmethod
    def send_thankyou():
        '''
        This method will create a list of donors, allow new donors to be added, store donations, and print a thank you
        statement to send to the donor by mail.
        :return:
        '''
        bool_flag = True  # --> Used as a flag.
        donor_name = input("Please, enter full name of donor. ").title()

        # Creates a donor list.
        while donor_name == "List":
            # --> Verifies that there is at least a donor is stored as a list row in the table tuple.
            if len(tup_donor_names) > 0:
                donor_list_creation()  # --> Creates a list of donors
                bool_flag = False  # --> Is used as a flag on the while loop below
            else:
                print("\n"+"There are no donors in list.")  # --> Let's the user know that a donor list does not exist.
                bool_flag = False  # --> Is used as a flag on the while loop below.
            break

        # Gathers donation information from the user and prints a thank-you message for the donor.
        while bool_flag:
            try:
                flo_donation_amount = float(input(str_name + ", please enter donation amount. "))

                # Updates donor tuple
                update_donor(donor_name, flo_donation_amount)

                # String formatting for a brief thank-you to donor.
                thankyou_message = "\n"+"{}, thank you for donating ${:,.2f}.".format(donor_name, flo_donation_amount)
                print(thankyou_message)

            except ValueError:  # --> Allows the program to continue if the user does not enter the right data type.
                print(str_name + ", not a valid amount. \n")
                continue

            else:
                break

    @staticmethod
    def create_report():
        '''
        This method takes the table tuple and creates a summary report for the user (name, number of gifts, total amount
        in gifts, and the average amount given. The code sorts the list rows into the largest amount amount give to the
        least amount given.
        :return:
        '''
        total = int()
        donation_count = int()
        lst_table = []
        # Creates a new list [name, number of gifts, average amount given, total amount in gifts] to be used to create
        # the summary chart.
        for row in tup_donor_names:
            for value in range(2, len(row)):
                total += row[value]
                donation_count += 1
            lst_table.append([row[0], row[1], total/donation_count, total])
            total = 0
            donation_count = 0
        # Reverses the list
        for row in lst_table:
            row.reverse()
        # Shorts the list form largest to smallest on the first element of each row.
        lst_table.sort(reverse=True)

        index = 0
        # Formatting the money elements and changing all int() & float() data to str() data
        # to use for creating the chart.
        for row in range(len(lst_table)):
            lst_table[row][index] = "${:,.2f}".format(lst_table[row][index])  # --> Total amount for gifts
            lst_table[row][index + 1] = "${:,.2f}".format(lst_table[row][index + 1])  # --> Avg. gift amount
            lst_table[row][index + 2] = str(lst_table[row][index + 2])  # --> Number of gifts
        # Reverses list
        for row in lst_table:
            row.reverse()

        lst_headers = ["Donor_Name", "Num_Gifts", "Average_Gift", "Total_Given"]  # --> List of headers for the chart.
        # Calculating the max length of all the elements.
        length1 = max(len(word) for word in lst_headers) + 10  # --> Max length for the header list
        length2 = max(len(word) for row in lst_table for word in row)  # --> Max length for the donor table
        # Calculates the max between the header list and the donor list
        max_length = max(length1, length2)
        # Creates the header for the chart
        for heading in lst_headers:
            print(("{0:{padding}}".format(heading, padding=max_length)), end=" ")
        print()
        # Creates the donor rows for the chart.
        for row in lst_table:
            print(("{0:{padding}}".format(row[0], padding=max_length)), end=" ")
            print(("{0:{padding}}".format(row[1], padding=max_length)), end=" ")
            print(("{0:{padding}}".format(row[2], padding=max_length)), end=" ")
            print(("{0:{padding}}".format(row[3], padding=max_length)), end=" ")
            print()
########### END OF SUB_MENU CLASS###############

# Methods defined in the files class are related to opening and renaming files.
# Modifications to the methods are needed if the files are not for a task priority list.


class files(object):
    @staticmethod
    def write_email(donors):
        '''
        Writes emails to the donors and saves them to text files.
        :param donors: Tuple table that stores all the donor's donation information.
        :return:
        '''
        for donor_name in donors:
            # Open text file and assign a mode to the file.
            newFile = open(donor_name[0] + ".txt", mode="w")
            newFile.write(thankyou_dispacth[int_option](donor_name[0],lifetime_donations(tup_donor_names)))
            newFile.close()
            print(donor_name[0] + "saved")

    @staticmethod
    def donor_email(donor, dictionary):
        '''
        Formats the email with donor's name and total lifetime donations.
        :param donor: Tuple table that stores all the donor's donation information.
        :param dictionary: A dictionary that stores the donor as the 'key' and the lifetime donation as the 'value'.
        :return: The concatenation how the three strings.
        '''
        str_salutation = "Dear {},".format(donor)
        str_body = "\n\n"+"Thank you for generosity! " \
                   "\n\n"+"This donation will be put to great use!" \
                   "\n\n"+"Your current lifetime donation is "+dictionary[donor]+"."
        str_valediction = "\n\n"+"Sincerely," \
                          "\n\n"+"The Team"
        thankyou_message = str_salutation+str_body+str_valediction
        return thankyou_message
############# END OF FILE CLASS #################


def update_donor(donor_name, donation_amount):
    '''
    Updates donor's donation history or creates a new donor.
    :param donor_name: The name of the donor.
    :param donation_amount: The amount of money the donor donated.
    :return:
    '''
    lst_donor_name = []
    global tup_donor_names
    # Creates a donor name list
    for row in range(len(tup_donor_names)):
        lst_donor_name.append(tup_donor_names[row][0])
    # Checks to see if donor has given before and updates history
    if donor_name in lst_donor_name:
        index = lst_donor_name.index(donor_name)  # --> Finds index of donor in  list
        tup_donor_names[index][1] = tup_donor_names[index][
                                          1] + 1  # --> Increase amount of times donor donated
        tup_donor_names[index].append(donation_amount)  # --> Adds donation to history
    # Adds new donor to the donor list
    else:
        tup_new_donor = ([donor_name, 1, donation_amount],)
        tup_donor_names += tup_new_donor

def donor_list_creation():
    '''
    Creates a donor list if the user types "list" the the program prompts the user to input a donor.
    :return: This function does not return anything. Return is just used to clearly show where this function ends.
    '''
    lst_donors = []
    # Creates a list just of donor names
    for row in tup_donor_names:
        lst_donors.append(row[0])
    lst_donors.sort()  # --> Sorts donors alphabetically by first name
    lst_headers = ["Donor_Name"]  # --> List for header
    length1 = max(len(word) for word in lst_headers) + 10  # --> Max length for header plus 10 (for buffer)
    length2 = max(len(word) for word in lst_donors)  # --> Max length for donor name
    max_length = max(length1, length2)  # --> Max length
    print()  # --> Formatting
    # Creating the header for the list
    for heading in lst_headers:
        print(("{0:{padding}}".format(heading, padding=max_length)), end=" ")
    print()  # --> Formatting
    # Creating the donor list
    for row in lst_donors:
        print(("{0:{padding}}".format(row, padding=max_length)), end=" ")
        print()

def choice1():
    '''
    Calls a method to add donors and/or donations to the master donor tuple table when the user inputs '1'.
    :return:
    '''
    # User selects option 1. Can display a list of the donors and where the user can add donors and donations.
    print()  # --> Formatting
    sub_menu.send_thankyou()

def choice2():
    '''
    Calls a method to create a summary report for the user when the user inputs '2'.
    :return:
    '''
    # User selects option 2. Creates a donation summary for the user.
    print()  # --> Formatting
    try:
        sub_menu.create_report()
    except ValueError:
        print("There are no donors on the list to create a report.")

def choice3():
    '''
    Calls a method to write and save emails to donors when the user inputs '3'.
    :return:
    '''
    print()  # --> Formatting
    files.write_email(tup_donor_names)

def choice4():
    '''
    Exits the program when the user inputs '4'.
    :return: Returns 'exit' which is the flag word to breakout of the program.
    '''
    print()  # --> Formatting
    return "exit"

def lifetime_donations(donors):
    '''
    Creates a dictionary that stores the donor's name as the 'key' and the lifetime donation as the 'value'.
    :param donors: Tuple table that stores all the donor's donation information.
    :return: Returns the newly created dictionary with the donor's name:lifetime donation
    '''
    # Local variables used for this function.
    lifetime_donations = int()
    dict_donor_donations = {}
    # Creates a dictionary (donor's name:lifetime donation)
    for donor in donors:
        for donation in range(2, len(donor)):
            lifetime_donations += donor[donation]
        lifetime_donations = "${:,.2f}".format(lifetime_donations)  # --> Formats the total amount for gifts
        dict_donor_donations[donor[0]] = lifetime_donations
        lifetime_donations = int()  # --> Resets lifetime donations.
    return dict_donor_donations

def main():
    '''
    This is the main function. This will run the full program.
    :return: This method does not return anything. Return is just used to clearly show where this method ends.
    '''
    while True:
        # User menu to update the priority list.
        print()  # --> Formatting
        print("\t\tMenu of Options\n\n"
              "\t\t1) Send a Thank You\n\n"
              "\t\t2) Create a Report\n\n"
              "\t\t3) Send letters to everyone\n\n"
              "\t\t4) Quit\n")
        # Error handles user's option choice.
        global int_option
        int_option = menu.menu_options()
        if menu_dispatch[int_option]() == "exit":
            break
        else:
            continue
    return

# -----Dispatch Dictionary Section-----
menu_dispatch = {1 : choice1,
                 2 : choice2,
                 3 : choice3,
                 4 : choice4
                 }

thankyou_dispacth = {3 : files.donor_email}

# -----Presentation Section-----
# The main block checks to see the program is not being imported then runs the program.
if __name__ == '__main__':
    # Asking the user for their name, strips spaces, and formats their name to be capitalized.
    str_name = input("Hello, for a more personal experience please enter your first name. ").strip(" ").capitalize()

    # Welcoming the user to the program. --> Create into a function.
    print("\nWelcome, " + str_name + ", to the donor mail program; here you can add donors and mail a thank-you message. "
                                 + "\n")
    main()

else:
    raise Exception("This file was not created to be imported")  # --> Gives an error if the program is being imported.

# Notifies the user that the program will be closing.
print("\n" + str_name + ", the program will be exiting now. Good bye!")

input("\n" + "Press enter to exit. ")
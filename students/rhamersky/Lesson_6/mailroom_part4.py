#!/usr/bin/env python3
# Description: This program will allow a user to input a donor and a donation.
# The user will also be able to send out thank you notes to the donors.
# Developer: Ryan Hamersky
# Date: 05/13/2018
# Rev: A - 05/16/2018 updated code to reflect comments made by the instructor in mailroom_part.py.
#      Update variables to snake_case. Removed unnecessary 'continues' and 'returns'.
#      Changed 'bool' variable to 'bool_flag'. Updated misleading function names.
#      Reduced the amount of unnecessary print() statements.
#
# Rev: B - 05/19/2018 updated code to reflect comments made by the instructor in mailroom_part3.py.
# Rev: C - 05/21/2018 updated code to reflect comments made on 05/20/2018.
#      Changed tuple data set to dictionary data set. Refactored program.

# -----Data Section-----
import os
str_name = str()    # --> User's name
int_user_input = int()  # --> User's option.
dic_donors = {"William Gates, III":[10000.0, 1], "Mark Zuckerberg":[20000.0, 1],
                   "Jeff Bezos":[1200.0,1],"Paul Allen":[5000.0,1],
                   "Mike Scott":[25.0,1]} # --> Dic that stores all donor's information
str_salutation = ""   # --> Email salutation
str_body = ""         # --> Email body
str_valediction = ""  # --> Email valediction


# -----Process Section-----
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

# Methods in the sub_menu class will execute code based off of the user's sub-menu choice.


class SubMenu():
    @staticmethod
    def send_thankyou():
        '''
        This method will  allow new donors to be added, store donations, and print a thank you
        statement to send to the donor by mail.
        :return:
        '''
        donor_name = input("Please, enter full name of donor. ").title()
        global dic_donors


        # Gathers donation information from the user and prints a thank-you message for the donor.
        while True:
            # Appends the donor list.
            if donor_name == "List":
                # --> Verifies that there is at least a donor is stored as a list row in the table tuple.
                if len(dic_donors) > 0:
                    print_donor_names()  # --> Prints a list of donors
                    break
                else:
                    print(
                        "\n" + "There are no donors in list.")  # --> Let's the user know that a donor list does not exist.
                    break

            try:
                flo_donation_amount = float(input(str_name + ", please enter donation amount. "))

                # Updates donor tuple
                dic_donors = update_donor(donor_name, flo_donation_amount)

                # String formatting for a brief thank-you to donor.
                thankyou_message = "\n"+"{}, thank you for donating ${:,.2f}.".format(donor_name, flo_donation_amount)
                print(thankyou_message)
                break

            except ValueError:  # --> Allows the program to continue if the user does not enter the right data type.
                print(str_name + ", not a valid amount. \n")
                continue

    @staticmethod
    def create_report():
        '''
        This method will create a report for the user with the following columns:
        donor's name, number of gifts, average gift amount, and lifetime donations.
        :return:
        '''
        longest_entry = float()
        # Finds the max amount of characters for all items stored in dic_donors.
        for name in dic_donors:
            entry_length = len(name)
            if longest_entry < entry_length:
                longest_entry = entry_length
            for index in range(0,1):
                entry_length = len(str(dic_donors[name][index]))
                if longest_entry < entry_length:
                    longest_entry = entry_length

        lst_headers = ["Donor_Name", "Num_Gifts", "Average_Gift", "Total_Given"]  # --> List of headers for the chart.

        # Creates the header for the chart
        for heading in lst_headers:
            print(("{0:{padding}}".format(heading, padding=longest_entry)), end=" ")
        print()

        # Creates the donor rows for the chart.
        sorted_dic = dic_sort()
        for name in sorted_dic:
            donation_avg = dic_donors[name][0] / dic_donors[name][1]
            print(("{0:{padding}}".format(name, padding=longest_entry)), end=" ")
            print(("{0:{padding}}".format("{}".format(dic_donors[name][1]), padding=longest_entry)), end=" ")
            print(("{0:{padding}}".format("${:,.2f}".format(donation_avg), padding=longest_entry)), end=" ")
            print(("{0:{padding}}".format("${:,.2f}".format(dic_donors[name][0]), padding=longest_entry)), end=" ")
            print()

########### END OF SUB_MENU CLASS###############

# Methods defined in the files class are related to opening and renaming files.
# Modifications to the methods are needed if the files are not for a task priority list.
class Files():
    @staticmethod
    def write_email(donors):
        '''
        Writes emails to the donors and saves them to text files.
        :param donors: Dictionary that stores all the donor's donation information.
        :return:
        '''
        for donor_name in donors:
            # Open text file and assign a mode to the file.
            new_file = open(donor_name + ".txt", mode="w")
            new_file.write(Files.donor_email(donor_name))
            new_file.close()
            print(donor_name + " saved to "+donor_name+".txt.")


    @staticmethod
    def donor_email(donor):
        '''
        Formats the email with donor's name and total lifetime donations.
        :param donor: Dictionary that stores all the donor's donation information.
        :param dictionary: A dictionary that stores the donor as the 'key' and the lifetime donation as the 'value'.
        :return: The concatenation how the three strings.
        '''
        str_salutation = "Dear {},".format(donor)
        str_body = "\n\n"+"Thank you for generosity! " \
                   "\n\n"+"This donation will be put to great use!" \
                   "\n\n"+"Your current lifetime donation is "+"${:,.02f}".format(dic_donors[donor][0]) + "."
        str_valediction = "\n\n"+"Sincerely," \
                          "\n\n"+"The Team"
        thankyou_message = str_salutation+str_body+str_valediction
        return thankyou_message
############# END OF FILE CLASS #################

def dic_sort():
    '''
    Takes a dictionary and creates a sorted tuple using the first element of the value list.
    It then puts the sorted data into a new dictionary.
    :return:
    '''
    sorted_tuple = sorted(dic_donors.items(), key=lambda x: x[1], reverse=True)
    new_dic = {}
    for items in sorted_tuple:
        new_dic[items[0]] = [items[1][0],items[1][1]]
    return new_dic

def update_donor(donor_name, donation_amount):
    '''
    Updates donor's donation history or creates a new donor.
    :param donor_name: The name of the donor.
    :param donation_amount: The amount of money the donor donated.
    :return:
    '''
    # Creates a donor name list
    #lst_donor_name = [dic_donors[row][0] for row in range(len(dic_donors))]  # --> Added list comprehension
    # Checks to see if donor has given before and updates history
    dic_new_donor_names = dic_donors
    if donor_name in dic_donors:
        dic_new_donor_names[donor_name][1] = dic_donors[donor_name][
                                          1] + 1  # --> Increase amount of times donor donated
        dic_new_donor_names[donor_name][0] = dic_donors[donor_name][0] + donation_amount  # --> Adds donation to history
    # Adds new donor to the donor list
    else:
        dic_new_donor_names[donor_name] = [donation_amount, 1]
    return dic_new_donor_names

def print_donor_names():
    '''
    Prints donors names if the user types "list" when the program prompts the user to input a donor.
    :return:
    '''
    # Creates a list just of donor names
    print("\n"+"Donor")
    for name in dic_donors:
        print(name)

def main():
    '''
    This is the main function. This will run the full program.
    :return:
    '''
    global dic_donors
    while True:
        # User menu to update the priority list.
        print()  # --> Formatting
        print("\t\tMenu of Options\n\n"
              "\t\t1) Send a Thank You\n\n"
              "\t\t2) Create a Report\n\n"
              "\t\t3) Send letters to everyone\n\n"
              "\t\t4) Quit\n")

        # Error handles user's option choice.
        int_user_input = menu_options()

        # User selects option 1. Can display a list of the donors and where the user can add donors and donations.
        if int_user_input == 1:
            print()  # --> Formatting
            SubMenu.send_thankyou()
            continue

        # User selects option 2. Creates a donation summary for the user.
        elif int_user_input == 2:
            print()  # --> Formatting
            SubMenu.create_report()

        # User selects option 3. Creates text files for thank-yous to donors.
        elif int_user_input == 3:
            Files.write_email(dic_donors)
            print()  # --> Formatting

        # User selects option 4. Allows the user to exit the program.
        elif int_user_input == 4:
            print()  # --> Formatting
            break


# -----Presentation Section-----
# The main block checks to see the program is not being imported then runs the program.
if __name__ == '__main__':
    # Asking the user for their name, strips spaces, and formats their name to be capitalized.
    str_name = input("Hello, for a more personal experience please enter your first name. ").strip(" ").capitalize()

    # Welcoming the user to the program. --> Create into a function.
    print("\nWelcome, " + str_name + ", to the donor mail program; here you can add donors and mail a thank-you message. "
                                 + "\n")
    main()

# Removed for unit test purposes. This line is causing the unit test not to run.
#else:
#    raise Exception("This file was not created to be imported")  # --> Gives an error if the program is being imported.

# Notifies the user that the program will be closing.
print("\n" + str_name + ", the program will be exiting now. Good bye!")

input("\n" + "Press enter to exit. ")
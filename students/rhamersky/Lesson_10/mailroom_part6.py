#!/usr/bin/env python3
# Description: This program will allow a user to input a donor and a donation.
# The user will also be able to send out thank you notes to the donors.
# Developer: Ryan Hamersky
# Date: 05/21/2018
# Rev: New

# -----Data Section-----
str_name = str()    # --> User's name
int_user_input = int()  # --> User's option.
dic_donors_sorted = {}  # --> Sorted dictionary of donors.
dic_donors = {"William Gates, III": [10000.0, 1], "Mark Zuckerberg": [20000.0, 1],
                   "Jeff Bezos": [7800.0,4, 2500, 2000, 3000, 300],"Paul Allen": [5000.0,1],
                   "Mike Scott": [25.0,1]} # --> Dic that stores all donor's information
str_salutation = ""   # --> Email salutation
str_body = ""         # --> Email body
str_valediction = ""  # --> Email valediction


# -----Process Section-----
# This class creates an donor object.
class Donor:
    initial_donation = 1  # --> Field is used as the initial donation is constant with all donor objects.

    def __init__(self, donor, donation):  # --> Constructs attributes donor and donation.
        self.donor = donor
        self.donation = donation

########### END OF DONOR OBJECT CLASS###############

# Methods in the Menu class will execute code based off of the user's menu choice.


class Menu:
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
                if 1 <= int_choice <= 5:
                    break
                else:
                    print("Integer selected is not a valid option. "
                          "Please, enter an integer and corresponds to the options given. \n")
        return int_choice

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
                    Data.print_donor_names()  # --> Prints a list of donors
                    break
                else:
                    print(
                        "\n" + "There are no donors in list.")  # --> Let's the user know that a donor list does not exist.
                    break

            try:
                flo_donation_amount = float(input(str_name + ", please enter donation amount. "))

                # Updates donor tuple
                new_donor = Donor(donor_name,flo_donation_amount)
                dic_donors = Data.update_donor(new_donor.donor, new_donor.donation, new_donor.initial_donation)

                # String formatting for a brief thank-you to donor.
                thankyou_message = "\n"+"{}, thank you for donating ${:,.2f}.".format(donor_name, flo_donation_amount)
                print(thankyou_message)
                break

            except ValueError:  # --> Allows the program to continue if the user does not enter the right data type.
                print(str_name + ", not a valid amount. \n")
                continue

    @staticmethod
    def user_donor_input():
        '''
        Try and except block used on User's option choice to check for integers.
        :return: Returns donor name to main function.
        '''
        while True:
            try:
                str_user_input = input(str_name + ", please enter a donor name to do a projection on. ").title()
            except ValueError:
                print(str_name + ", not a valid option. \n")
                # Verifies that the data type is part of the string class and that the donor name is in the donor dic.
            else:
                if str_user_input.__class__ == str().__class__ and str_user_input in dic_donors:
                    str_donations = "Yes"
                    break
                else:
                    print("Donor is not in donor list. \n")
        return str_user_input, str_donations

    @staticmethod
    def user_factor_input():
        '''
        Try and except block used on User's option choice to check for integers.
        :return: Returns factor input to the main function.
        '''
        while True:
            try:
                int_user_input = float(input(str_name + ", please enter a positive integer. "))
            except ValueError:
                print(str_name + ", not a valid option. \n")
                # Verifies that the data type is part of the int class and that the user input a value greater than 0.
            else:
                if int_user_input.__class__ == float().__class__ and int_user_input > 0:
                    break
                else:
                    print("Integer selected is not a valid option. "
                              "Please, enter an integer. \n")
        return int_user_input

    @staticmethod
    def user_filter_input():
        '''
        Try and except block used on User's option choice to check for integers.
        :return: Returns filter data to the main function.
        '''
        while True:
            try:
                str_user_input = input(str_name + ", please enter max to filter for amounts greater than or equal "
                                                  "to $2,500. \n or min to filter for "
                                                  "amounts less than $2,500. ").capitalize()
            except ValueError:
                print(str_name + ", not a valid option. \n")
            # Verifies that the data type is part of the string class and that the user put in the correct input.
            else:
                if str_user_input.__class__ == str().__class__ and (str_user_input == "Max"
                                                                    or str_user_input == "Min"):
                    break
                else:
                    print("Integer selected is not a valid option. "
                              "Please, enter max or min. \n")
        return str_user_input

########### END OF MENU CLASS###############

# Methods defined in the files class are related to opening and renaming files.
# Modifications to the methods are needed if the files are not for a task priority list.


class Files:
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

# The Data class is where the data get manipulated.


class Data:
    @staticmethod
    def update_donor(donor_name, donation_amount, initial_donation):
        '''
        Updates donor's donation history or creates a new donor.
        :param donor_name: The name of the donor.
        :param donation_amount: The amount of money the donor donated.
        :param initial_donation: The initial donation of the donor.
        :return:
        '''
        # Creates a donor name list
        # lst_donor_name = [dic_donors[row][0] for row in range(len(dic_donors))]  # --> Added list comprehension
        # Checks to see if donor has given before and updates history
        dic_new_donor_names = dic_donors
        if donor_name in dic_donors:
            dic_new_donor_names[donor_name][1] = dic_donors[donor_name][
                                                     1] + 1  # --> Increase amount of times donor donated
            dic_new_donor_names[donor_name][0] = dic_donors[donor_name][
                                                     0] + donation_amount  # --> Adds donation to history
            lst_donor_data = dic_new_donor_names[donor_name]  # --> Creates a list of the values in the dictionary.
            lst_donor_data.append(donation_amount)  # --> Appends donation amount to donor data list
            dic_new_donor_names[donor_name] = lst_donor_data  # --> Replaces the old value list with lst_donor_data.
        # Adds new donor to the donor list
        else:
            dic_new_donor_names[donor_name] = [donation_amount, initial_donation, donation_amount]
        return dic_new_donor_names

    @staticmethod
    def print_donor_names():
        '''
        Prints donors names if the user types "list" when the program prompts the user to input a donor.
        :return:
        '''
        # Creates a list just of donor names
        print("\n" + "Donor")
        for name in dic_donors:
            print(name)

    @staticmethod
    def dic_sort(dic_donors):
        '''
        Takes a dictionary and creates a sorted tuple using the first element of the value list.
        It then puts the sorted data into a new dictionary.
        :param dic_donors: The dictionary of donors.
        :return:
        '''
        dic_donors_total_donation = {}
        # Removes all past donations from the value list.
        for key in dic_donors:
            lst_total_donation = dic_donors[key]
            dic_donors_total_donation[key] = lst_total_donation
        sorted_tuple = sorted(dic_donors_total_donation.items(), key=lambda x: x[1], reverse=True)
        sorted_dic = {}
        for items in sorted_tuple:
            sorted_dic[items[0]] = [items[1][0], items[1][1]]
        return sorted_dic

    @staticmethod
    def create_report(dic_donors):
        '''
        This method will create a report for the user with the following columns:
        donor's name, number of gifts, average gift amount, and lifetime donations.
        :param dic_donors: The dictionary of donors.
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
        sorted_dic = Data.dic_sort(dic_donors)
        for name in sorted_dic:
            donation_avg = dic_donors[name][0] / dic_donors[name][1]
            print(("{0:{padding}}".format(name, padding=longest_entry)), end=" ")
            print(("{0:{padding}}".format("{}".format(dic_donors[name][1]), padding=longest_entry)), end=" ")
            print(("{0:{padding}}".format("${:,.2f}".format(donation_avg), padding=longest_entry)), end=" ")
            print(("{0:{padding}}".format("${:,.2f}".format(dic_donors[name][0]), padding=longest_entry)), end=" ")
            print()

    @staticmethod
    def challenge(str_past_donations, name_of_donor, str_filter,  factor):
        '''
        This function will increase all the donations by a factor.
        :param factor: The number to multiply the donations by.
        :return: Returns the total factored amount.
        '''
        lst_values = []
        new_factored_donation = int()
        # Checks to see if there are past donations from the donor.
        if str_past_donations == "No":
            lst_values.append(dic_donors[name_of_donor][0])
        else:
            for index in range(2, len(dic_donors[name_of_donor])):
                lst_values.append(dic_donors[name_of_donor][index])

        # Filters donations
        if str_filter == "Max":
            lst_values = filter(lambda filter_value: filter_value >= 2500, lst_values)
        else:
            lst_values = filter(lambda filter_value: filter_value < 2500, lst_values)

        # Adds a factor to the filtered donations.
        factored_donations = map(lambda donation: donation * factor, lst_values)

        # Sums factored donations
        for past_donation in list(factored_donations):
            new_factored_donation += past_donation

        return print(name_of_donor + ", could have donated ${:,.2f}.".format(new_factored_donation))

def main():
    '''
    This is the main function. This will run the full program.
    :return:
    '''

    while True:
        # User menu to update the priority list.
        print()  # --> Formatting
        print("\t\tMenu of Options\n\n"
              "\t\t1) Send a Thank You\n\n"
              "\t\t2) Create a Report\n\n"
              "\t\t3) Send letters to everyone\n\n"
              "\t\t4) Projection\n\n"
              "\t\t5) Quit\n")

        # Error handles user's option choice.
        int_user_input = Menu.menu_options()

        # User selects option 1. Can display a list of the donors and where the user can add donors and donations.
        if int_user_input == 1:
            print()  # --> Formatting
            Menu.send_thankyou()
            continue

        # User selects option 2. Creates a donation summary for the user.
        elif int_user_input == 2:
            print()  # --> Formatting
            Data.create_report(dic_donors)

        # User selects option 3. Creates text files for thank-yous to donors.
        elif int_user_input == 3:
            Files.write_email(dic_donors)
            print()  # --> Formatting

        # User selects option 4. Allows the donor to see how much they could have donated.
        elif int_user_input == 4:
            str_name_of_donor, str_past_donations = Menu.user_donor_input()
            if str_name_of_donor != None:
                int_factor = Menu.user_factor_input()
                str_min_max = Menu.user_filter_input()
                Data.challenge(str_past_donations, str_name_of_donor, str_min_max, int_factor)
            else:
                continue

        # User selects option 5. Allows the user to exit the program.
        elif int_user_input == 5:
            print()  # --> Formatting
            break

# -----Presentation Section-----
# The main block checks to see the program is not being imported then runs the program.
if __name__ == '__main__':
    # Asking the user for their name, strips spaces, and formats their name to be capitalized.
    str_name = input("Hello, for a more personal experience please enter your first name. ").strip(" ").capitalize()

    # Welcoming the user to the program. --> Create into a function.
    print(
        "\nWelcome, " + str_name + ", to the donor mail program; here you can add donors and mail a thank-you message. "
        + "\n")
    main()

else:
    raise Exception("This file was not created to be imported")  # --> Gives an error if the program is being imported.

# Notifies the user that the program will be closing.
print("\n" + str_name + ", the program will be exiting now. Good bye!")

input("\n" + "Press enter to exit. ")
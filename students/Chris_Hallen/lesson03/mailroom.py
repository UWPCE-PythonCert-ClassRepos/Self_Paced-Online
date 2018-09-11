#!/usr/bin/env python3


response = ''
donor_list = ['Zach Galifianakis', 23757, 3, "Conan O'Brien", 45000, 3, 'Kristen Wiig', 111222, 2, 'Sarah Silverman', 100, 1, 'Bill Burr', 12, 1, 'Will Ferrell', 100000, 2, ]

while response != 'quit':  # This program will constantly run until a user enters 'quit' - regardless of whether 'quit'is upper or lower case or a combination thereof
    def send_a_thank_you(donor_list):
        """This function asks whether a user wants to show a list of existing donors, a single existing donor, or
           to create a new donor.  This function prints a list of existing donors if the user enters 'list' -
           regardless if 'list' is upper or lower case or a combination thereof.  This function adds a new donor
           name to the end of the existing donor_list if a donor name entered is not in the donor_list.  If a new donor is entered,
           this function will then ask how much the new donor wants to contribute.  The new donor's contribution will be added to the
           end of the existing list along with the amount of times the new donor contributed (i.e. 1).  If
           an existing donor on the donor_list is selected, the function will ask the user how much the new donor
           wants to contribute.  The new amount will be added to the grand total the existing donor has already
           contributed and the number of times the existing donor contributed will be increased by 1."""
        donor_response = ''
        donor_response = input("Please enter a full name of a donor.  Enter 'list' to show a full listing of all donors. \n> ")
        while donor_response == 'list':
            print(donor_list[::3])
            donor_response = input("Please enter a full name of a donor. Enter 'list' to show a full listing of all donors.\n> ")
        member_index = donor_list.index(donor_response) if donor_response in donor_list else -1
        if member_index >= 0 and member_index < len(donor_list):
            donation_amount = 0
            donation_amount = input("Please enter an amount that was donated: ")
            donation_amount = float(donation_amount)
            donor_list[member_index + 2] += 1
            donor_list[member_index + 1] += donation_amount
            print("\nThank you {} for donation number {} of ${:.2f}!".format(donor_list[member_index], donor_list[member_index + 1], donor_list[member_index + 2]))
        else:
            donation_amount = 0
            donation_amount = input("Please enter an amount that was donated: ")
            donation_amount = float(donation_amount)
            donor_list.append(donor_response)
            donor_list.append(donation_amount)
            donor_list.append(1)
            print("\nThank you {} for donation number {} of ${:.2f}!".format(donor_list[-3], donor_list[-1], donor_list[-2]))

    def create_a_report(donor_list):
        """This function prints a donor report with a formatted header and muliple lines thereafter for each donor"""
        num_of_donors = len(donor_list) / 3
        num_of_donors = int(num_of_donors)
        print("Donor Name" + (' ' * 15) + " | " + "Total Given" " | " "Num Gifts" + " | " + "Average Gift\n" + ('- ' * 30))
        donor_line = "{:25} ${:>11.2f} {:^13} ${:>11.2f}\n"
        multiple_donor_lines = donor_line * num_of_donors

        def add_average_donation(donor_list):
            """This function within the create_a_report function returns a new list after taking the existing donor_list,
               takes the first 3 entries of each donor - name, total donations, number of donations - and adds the
               average amount each donor contributes to the end of each donor's profile.  This makes the donor_list 1/3 bigger
               than the original list."""
            new_length = (len(donor_list) / 3) * 4
            longer_list = []
            beg = 0
            end = 3
            while len(longer_list) < new_length:
                longer_list.extend(donor_list[beg:end])
                longer_list.append(longer_list[-2] / longer_list[-1])
                beg += 3
                end += 3
            return longer_list
        longer_list = add_average_donation(donor_list)
        print(multiple_donor_lines.format(*longer_list))
    response = input("Would you like to 'Send a Thank You', 'Create a Report' or 'quit'? \n > ")
    response = response.lower()
    while response != 'send a thank you' and response != 'create a report' and response != 'quit':
        response = input("\nThat response doesn't seem to be one of the three options. \nPlease enter your response again.\nWould you like to 'Send a Thank You', 'Create a Report' or 'quit'? \n > ")
    if response == 'send a thank you':
        send_a_thank_you(donor_list)
    elif response == 'create a report':
        create_a_report(donor_list)

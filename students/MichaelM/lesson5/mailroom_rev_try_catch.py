import os
import pathlib

pth = pathlib.Path('./')
tmp_directory = "{}/tmp/".format(os.getcwd())

esteemed_donors_headers = ["Donor Name", "Total Donation", "Number of Donations", "Ave Donation"]
esteemed_donors = [["John Jacob Astor", 10.0],
                   ["John Jacob Astor", 100.0],
                   ["John Jacob Astor", 1000.0],
                   ["John Jacob Astor", 10000.0],
                   ["Alan Rufus, 1st Lord of Richmond", 10.0],
                   ["Henry Ford", 10.0],
                   ["Henry Ford", 100.0],
                   ["Henry Ford", 1000.0],
                   ["Cornelius Vanderbilt", 10.0],
                   ["Jakob Fugger", 10.0],
                   ["Jakob Fugger", 100.0]]


def spam_donors():
    """
        adds a year end thank you letter for each donor to a subdirectory

        {Extended description}

        Parameters:
        {none}

        Returns:
        {none}
    """

    os.makedirs(tmp_directory, exist_ok=True)
    for row in list_donors():
        sum_amt = 0.0
        # converted to list comprehension
        tmp_amt_list = [row2[1] for row2 in esteemed_donors if row2[0] == row]
        sum_amt = float(sum(tmp_amt_list))
        tmp_dest_file = f"{tmp_directory}/{row}_Thank_You_Letter.txt"
        with open(tmp_dest_file, 'w') as wf:
            wf.write(spam("all_donors", row, 0.0, "", sum_amt))


def spam(letter_type, donor="", donation_amt=0.0, spam_type="", total_amt_donated=0.0):
    """
    creates an email thank you text prints the text to the screen. The template text contains parameters within the body

    {Extended description}

    Parameters:
    letter_type (string): integer to be padded
    donor (string): integer to be padded
    donation_amt (string): integer to be padded
    spam_type (string): integer to be padded
    total_amt_donated (float): integer to be padded

    Returns:
    result (string): the email text

    """
    donation = "${0:,.2f}".format(int(donation_amt))
    total_donation = "${0:,.2f}".format(int(total_amt_donated))
    results = ""
    if letter_type == "all_donors":
        results = f"{donor}, warm seasons greetings,\n" \
                  f"Once again our society looks back upon this year's generousity from our many donors.\n" \
                  f"Our records show to date your generosity of {total_donation} has been among the most generous." \
                  f"We hope to continue our relationship into the next year and beyond.\n" \
                  f"\n" \
                  f"Kind regards,\n" \
                  f"The Minimalist Society"
    elif letter_type == "new" and spam_type == "ty":
        results = f"[Subject]: Thank you for your generous donation\n" \
                  f"\n" \
                  f"[Body]: {donor},\n" \
                  f"Thank you for your generous donation. We are always grateful to greet new members of " \
                  f"our ever expanding family.\n" \
                  f"Your current and future beneficent contributions will go towards " \
                  f"administering our clients with our services.\n" \
                  f"Your initial contribution of {donation} illustrates an exceedingly benevolent nature.\n" \
                  f"\n" \
                  f"Kind regards,\n" \
                  f"The Minimalist Society\n" \
                  f"[End]"
    elif letter_type == "existing_donor" and spam_type == "ty":
        results = f"[Subject]: Once again, thank you for your generous donation\n" \
                  f"\n" \
                  f"[Body]: {donor},\n" \
                  f"Thank you for your generous donation. Your beneficent contribution of {donation} will go " \
                  f"towards administering our clients with our services.\n" \
                  f"Our records show to date your generosity " \
                  f"of {total_donation} illustrates an exceedingly benevolent nature.\n" \
                  f"\n" \
                  f"Kind regards,\n" \
                  f"The Minimalist Society\n" \
                  f"[End]"
    return results


def create_ty_letter():
    """
        takes user input and incorporates this input into a list of donors and returns text to the screen

        Extended description:
        If a donor (user_response) exists the function will take the input, add their current donation and print
        to screen an email template containing the new data. If the donor does not exists the donor will be added
        to the list and the user will be prompted for a donation amount after which the new data will be incorporated
        into email and printed to screen.

        12/1/14/2018 function modified to add try/except blocks and list comprehensions


        Parameters:
        my_int (int): integer to be padded

        Returns:
        result (string): a padded number

        """
    found_donor_count = 0
    response_donor_name = ""
    response_donation_amt = 0.0
    sum_amt = 0.0
    tmp_donor_list = list(list_donors())
    user_response = input(
        "-type 'list' to view a list of donors\n-type 'new' to  "
        "add a donor to the list\n- type in an existing donor to add a new donation >")
    if user_response.lower() == "list":
        print()
        # converted to list comprehension
        [print(''.join([str(elem) for elem in row])) for row in list_donors()]
    print()

    if user_response.lower() == "new":
        response_donor_name = input("What is the donor's name? >")
        response_donation_amt = 0.0
        while True:
            try:
                response_donation_amt = float(input("How much is {}'s donation? >".format(response_donor_name.title())))
            except ValueError:
                print("Please enter the donation in dollars")
                continue
            else:
                break
        add_donor(response_donor_name.title(), response_donation_amt)
        print("{0:,.2f} added to {1}'s total.".format(response_donation_amt, response_donor_name.title()))
        print("\nThank you email:\n{}".format(spam("new", response_donor_name, response_donation_amt, "ty")))
        print()
        print()

    elif tmp_donor_list.count(user_response.title()) > 0:
        response_donation_amt = 0.0
        print("{} found.".format(user_response.title()))
        while True:
            try:
                response_donation_amt = float(input("How much is the donation? >".format(user_response.title())))
            except ValueError:
                print("Please enter the donation in dollars")
                continue
            else:
                break
        add_donor(user_response.title(), response_donation_amt)
        # converted to list comprehension
        tmp_amt_list = [row[1] for row in esteemed_donors if row[0] == user_response.title()]
        sum_amt = float(sum(tmp_amt_list))
        print("{0:,.2f} added to {1}'s total. "
              "{1}'s total contribution is {2:,.2f}".format(response_donation_amt,
                                                            user_response.title(),
                                                            sum_amt))
        print("\nThank you email:\n{}".format(spam("existing_donor", user_response.title(), response_donation_amt, "ty", sum_amt)))
        print()


def create_report():
    """
    creates a report summarizing donors and donations and prints the report to the screen.

    {Extended description}

    Parameters:
    {none}

    Returns:
    {none}

    """
    tmp_donor_list = []
    for row in list_donors():
        donor_sum = sum([t[1] for t in esteemed_donors if t[0] == row])
        donation_cnt = len([t[1] for t in esteemed_donors if t[0] == row])
        donor_ave = donor_sum / donation_cnt
        tmp_donor_list.append([row, donor_sum, donation_cnt, donor_ave])
    print("{name:<40}{total_donation:<20}{donation_cnt:<30}{ave_donation:}".format(
        name=esteemed_donors_headers[0],
        total_donation=esteemed_donors_headers[1],
        donation_cnt=esteemed_donors_headers[2],
        ave_donation=esteemed_donors_headers[3]))
    tmp_donor_list = sorted(tmp_donor_list, key=lambda x: x[1], reverse=True)
    # converted to list comprehension
    [print("{name:<40}{total_donation:<20}{donation_cnt:<30}{ave_donation:}".format(name=row[0],
                                                                                    total_donation=row[1],
                                                                                    donation_cnt=row[2],
                                                                                    ave_donation=row[3])
           ) for row in tmp_donor_list]
    print()


def list_donors():
    """
    Returns a set of distinct donors.

    {Extended description}

    Parameters:
    {none}

    Returns:
    distinct_donors (list): distinct donor list

    """
    # converted to list comprehension
    donors = [i[0] for i in esteemed_donors]
    distinct_donors = set(donors)
    return distinct_donors


def add_donor(donor, amt):
    """
        adds a new donor to the list

        {Extended description}

        Parameters:
        donor (string): new donor
        amt (int): donation amount

        Returns:
        {none}

        """
    esteemed_donors.append([donor, amt])


def quit():
    """
            quit program handler

            {Extended description}

            Parameters:
            {none}

            Returns:
            {none}

            """
    print("that's lunch!")

esteemed_donors_headers = ["Donor Name", "Total Donation", "Number of Donations", "Ave Donation"]
esteemed_donors = [["John Jacob Astor", 10],
                   ["John Jacob Astor", 100],
                   ["John Jacob Astor", 1000],
                   ["John Jacob Astor", 10000],
                   ["Alan Rufus, 1st Lord of Richmond", 10],
                   ["Henry Ford", 10],
                   ["Henry Ford", 100],
                   ["Henry Ford", 1000],
                   ["Cornelius Vanderbilt", 10],
                   ["Jakob Fugger", 10],
                   ["Jakob Fugger", 100]]


def create_ty_letter(user_response):
    """
        takes user input and incorporates this input into a list of donors and returns text to the screen

        Extended description:
        If a donor (user_response) exists the function will take the input, add their current donation and print
        to screen an email template containing the new data. If the donor does not exists the donor will be added
        to the list and the user will be prompted for a donation amount after which the new data will be incorporated
        into email and printed to screen.


        Parameters:
        my_int (int): integer to be padded

        Returns:
        result (string): a padded number

        """
    found_donor_count = 0
    if user_response.lower() == "list":
        for row in list_donors():
            print(''.join([str(elem) for elem in row]))
    print()
    if user_response.lower() != "list":
        for donor in esteemed_donors:
            if user_response.title() == donor[0]:
                found_donor_count += 1
    print()
    # new donor
    if found_donor_count == 0 and user_response.lower() != "list":
        response_1 = ""
        response_2 = 0.0
        sum_amt = 0.0
        response_1 = user_response.title()
        response_2 = input("How much is {}'s donation? >".format(user_response.title()))

        response_2 = float(response_2)
        add_donor(user_response.title(), response_2)
        for donor in esteemed_donors:
            if donor[0] == response_1:
                sum_amt = sum_amt + donor[1]

        print("{0:,.2f} added to {1}'s total. "
              "{1}'s total contribution is {2:,.2f}".format(response_2,
                                                            user_response.title(),
                                                            sum_amt))
        print("\nThank you email:\n{}".format(spam("new", response_1, response_2, "ty")))
        print()
    # existing donor
    if found_donor_count != 0 and user_response.lower() != "list":
        response_2 = 0.0
        sum_amt = 0.0
        response_1 = user_response.title()
        response_2 = input("{} found. How much is the donation? >".format(user_response.title()))
        response_2 = float(response_2)
        add_donor(user_response.title(), response_2)
        for donor in esteemed_donors:
            if donor[0] == response_1:
                sum_amt = sum_amt + donor[1]
        print("{0:,.2f} added to {1}'s total. "
              "{1}'s total contribution is {2:,.2f}".format(response_2,
                                                            user_response.title(),
                                                            sum_amt))
    print("\nThank you email:\n{}".format(spam("existing_donor", response_1, response_2, "ty", sum_amt)))
    print()


def spam(donor_type, donor, donation_amt, spam_type, total_amt_donated=0):
    """
    creates an email thank you text prints the text to the screen. The template text contains parameters within the body

    {Extended description}

    Parameters:
    donor_type (string): integer to be padded
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
    if donor_type == "new" and spam_type == "ty":
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
    elif donor_type == "existing_donor" and spam_type == "ty":
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
    for row in tmp_donor_list:
        print("{name:<40}{total_donation:<20}{donation_cnt:<30}{ave_donation:}".format(name=row[0],
                                                                                       total_donation=row[1],
                                                                                       donation_cnt=row[2],
                                                                                       ave_donation=row[3]))
    print()


def list_donors():
    """
    Returns a list of distinct donors

    {Extended description}

    Parameters:
    {none}

    Returns:
    distinct_donors (list): distinct donor list

    """
    donors = []
    for donor in esteemed_donors:
        donors.append(donor[0])
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

import os
import pathlib

pth = pathlib.Path('./')

esteemed_donors_headers = ["Donor Name", "Total Donation", "Number of Donations", "Ave Donation"]
# per Natasha modified to dictionary 1/5/2018
esteemed_donors_dict = {"John Jacob Astor": [10.0, 100.0, 1000.0, 10000.0],
                        "Alan Rufus, 1st Lord of Richmond": [10.0],
                        "Henry Ford": [10.0, 100.0, 1000.0],
                        "Cornelius Vanderbilt": [10.0],
                        "Jakob Fugger": [10.0, 100.0]}

summed_donor_list = []
tmp_directory = "{}/tmp/".format(os.getcwd())

#1/6/2019 module function calls seperated into function for assertion testing
def function_calls(func, action="", new_donor_name="", directory="", response_donation_amt=0.0):
    if func == "ty" and action == "list":
        create_ty_letter("list")
    elif func == "ty" and action == "new":
        create_ty_letter("new", new_donor_name, response_donation_amt)
    elif func == "ty" and action == "add_to_donor":
        create_ty_letter("add_to_donor", new_donor_name, response_donation_amt)
    elif func == "cr":
        create_report()
    elif func == "s":
        spam_donors(directory)


def spam_donors(tmp_dir):
    """
        adds a year end thank you letter for each donor to a subdirectory
        converted to dictionary comprehension 1/4/2019

        {Extended description}

        Parameters:
        {none}

        Returns:
        {none}
    """

    esteemed_donors_dict_summed = {k: sum(v) for (k, v) in esteemed_donors_dict.items()}
    os.makedirs(tmp_dir, exist_ok=True)
    for k, v in esteemed_donors_dict_summed.items():
        sum_amt = float(v)
        tmp_dest_file = f"{tmp_dir}/{k}_Thank_You_Letter.txt"
        with open(tmp_dest_file, 'w') as wf:
            wf.write(spam("all_donors", k, 0.0, "", sum_amt))


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


def create_ty_letter(action="", new_donor_name="", donation_amt=0.0):
    """
        takes user input and incorporates this input into a list of donors and returns text to the screen

        12/14/2018 function modified to add try/except blocks and list comprehensions
        12/28/2018 modified params to push out input prompts
        1/5/2019 modified for dictionaries

        Parameters:
        action: string the action the function is to perform
        new_donor_name: string  default="" if the function is adding a new donor, the donor to be added
        Returns:
        {}
        """
    distinct_donor_list = []
    if action.lower() == "list":
        distinct_donor_list = list(esteemed_donors_dict.keys())
        print()
        # fixed 1/6/2019 per natasha, "this is considered an anti-pattern (print() function + comprehension, print function
        # returns None), use comprehensions when you are capturing the result"
        for item in distinct_donor_list:
            print(item)
        print()
    elif action.lower() == "new":
        print("")
        tmp_amt = [donation_amt]
        esteemed_donors_dict[new_donor_name.title()] = tmp_amt
        print("{0:,.2f} added to {1}'s total.".format(donation_amt, new_donor_name.title()))
        print("\nThank you email:\n{}".format(spam("new", new_donor_name, donation_amt, "ty")))
        print()
        print()
    elif action.lower() == "add_to_donor":
        print("{} found.".format(new_donor_name.title()))
        esteemed_donors_dict.setdefault(new_donor_name.title(), []).append(donation_amt)
        # converted to dict comprehension
        esteemed_donors_dict_summed = {k: sum(v) for (k, v) in esteemed_donors_dict.items()}
        sum_amt = float(esteemed_donors_dict_summed[new_donor_name.title()])
        print("{0:,.2f} added to {1}'s total. "
              "{1}'s total contribution is {2:,.2f}".format(donation_amt,
                                                            new_donor_name.title(),
                                                            sum_amt))
        print("\nThank you email:\n{}".format(
            spam("existing_donor", new_donor_name.title(), donation_amt, "ty", sum_amt)))
        print()

#1/06/2019 pulled printing out into a new def for assertions
#1/06/2019 moved the summed list to a class object for assertions
def create_report():
    """
    creates a list summarizing donors and donations for printing to the screen.

    {Extended description}

    Parameters:
    {none}

    Returns:
    {none}

    """
    esteemed_donors_dict_summed = {k: sum(v) for (k, v) in esteemed_donors_dict.items()}
    esteemed_donors_dict_donation_cnt = {k: len(v) for (k, v) in esteemed_donors_dict.items()}
    for k, v in list(esteemed_donors_dict.items()):
        donor_sum = float(esteemed_donors_dict_summed[k])
        donation_cnt = esteemed_donors_dict_donation_cnt[k]
        donor_ave = donor_sum / donation_cnt
        summed_donor_list.append([k, donor_sum, donation_cnt, donor_ave])
    print_report(summed_donor_list)


def print_report(donor_list):
    """
        prints a report summarizing donors and donations and prints the report to the screen.

        {Extended description}

        Parameters:
        donor_list: list

        Returns:
        {none}

        """
    print("{name:<40}{total_donation:<20}{donation_cnt:<30}{ave_donation:}".format(
        name=esteemed_donors_headers[0],
        total_donation=esteemed_donors_headers[1],
        donation_cnt=esteemed_donors_headers[2],
        ave_donation=esteemed_donors_headers[3]))
    tmp_donor_list = sorted(donor_list, key=lambda x: x[1], reverse=True)
    # converted to list comprehension
    [print("{name:<40}{total_donation:<20}{donation_cnt:<30}{ave_donation:}".format(name=row[0],
                                                                                    total_donation=row[1],
                                                                                    donation_cnt=row[2],
                                                                                    ave_donation=row[3])
           ) for row in tmp_donor_list]
    print()

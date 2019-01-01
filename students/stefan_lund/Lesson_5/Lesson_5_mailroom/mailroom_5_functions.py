#!/usr/bin/env python3


import os
import datetime
import sys
import mailroom_5_read_write_data


# "start" menu functions


def send_a_thank_you():
    """
    sole function is to switch to the "thank you" menue
    """
    return "thank_you"


def create_a_report():
    """
        function prints out a report of current names in the data dictionary,
            displaying "Donor Name", "Total Given", "Num Gifts", "Average Gift"
    """
    data = mailroom_5_read_write_data.data

    name_len = 0
    amount_len = 0

    for name, donations in data.items():
        if len(name) > (name_len - 3):
            name_len = len(name) + 3
        for date in donations:
            amount = str(donations[date])
            if len(amount) > (amount_len - 3):
                amount_len = len(amount) + 3

    temp_str = "Donor Name", "Total Given", "Num Gifts", "Average Gift"
    temp_form = "\n{:<{nl}}|{:>{al}}|{:>{al}}|{:>{al}}"
    header = temp_form.format(*temp_str, nl=name_len, al=amount_len)
    print(header)

    # separation line used to make presentation look nice
    p = "+"
    s = "-"
    lne = s * (name_len)
    e = p + (s * (amount_len))
    lne += 3 * e
    print(lne)

    for name, donations in data.items():
        number_of = 0
        donation = 0
        for date in donations:
            donation += donations[date]
            number_of += 1

            total = float(donation)
            number_of = int(number_of)
            average = total / number_of

        temp_form = "{:<{nl}} ${:>{al}.2f}  {:>{al}} ${:>{al}.2f}"
        line = temp_form.format(name,
                                total,
                                number_of,
                                average,
                                nl=name_len,
                                al=amount_len - 1)
        print(line)

    return "start"


def send_letters_to_everyone():
    """
        sends one type of letter chosen from a template of letters to
            all names in the data dictionary
        each letter is stored as a txt file in cwd folder "letter_to_everyone"
    """
    data = mailroom_5_read_write_data.data
    letter_template = letter_templates("2")  # needs date, name, and total amount
    today = todays_date()
    year, month, day = today[0], today[1], today[2]

    letters = []
    # create letters
    for name, donations in sorted(data.items()):
        donation = 0
        for date in donations:
            donation += donations[date]

        total = float(donation)

        letter = letter_template.format(name=name,
                                        amount=total,
                                        date=month+"/"+day+"/"+year)
        donor = "_".join(name.split())
        letter_file = donor + "__" + year + "_" + month + "_" + day
        letters.append((letter, letter_file))


    # print letter to screen and store letter

    # create the directory to store the letters if it doesn't exist
    pth = os.path.join(os.getcwd(), "letter_to_everyone")
    if not os.path.exists(pth):
        os.makedirs(pth)

    for letter, letterfile in letters:
        print("\n", letter)
        destination = os.path.join(pth, letterfile)

        try:
            with open(destination, 'w') as outfile:
                for line in letter:
                    outfile.write(line)
        except FileNotFoundError:
            print("Could not find the file")

    print("stored letters in ", pth)

    return "start"


# "thank you" menu functions

def main_menu():
    """
    sole function is to switch to the "start" menue
    """
    return "start"

def list_of_names():
    """
        prints out a list of names currently in the "data" dictionary
    """
    data = mailroom_5_read_write_data.data

    # determine width of fields to print in
    name_list = data.keys()
    name_length = []
    # list comprehension
    [name_length.append(len(name)) for name in name_list]
    name_len = max(name_length) + 3

    # print table header
    temp_str = "Donor Name"
    temp_form = "\n| {:<{nl}}|"
    header = temp_form.format(temp_str, nl=name_len)
    frame = "\n+" + "-" * (name_len + 1) + "+"
    print(frame, header, frame)

    # print each name in alphabetical order
    for name in sorted(name_list):
        temp_form = "| {:<{nl}}|"
        line = temp_form.format(name, nl=name_len)
        print(line)

    return "thank_you"


def enter_name():
    """
    updates data dictionary with the donation from a new or a present donor
    and prints out a thank you letter
    and stores the letter in cwd folder "thank_you_letter"
    """
    data = mailroom_5_read_write_data.data
    today = todays_date()
    year, month, day = today[0], today[1], today[2]  #  str type

    # user enter name, check if input is letters or space
    name_of_letters = False
    while not name_of_letters:
        name = input("\nEnter name, 'First Last': ")
        name_of_letters = is_letters_or_space(name)

    # user enter new_amount, check if new_amount is a number, 2 decimals or less
    digits_in_amount = False
    while not digits_in_amount:
        new_amount = input("\nEnter amount donated: ")
        digits_in_amount = is_digit_or_period(new_amount)

    # entered name is not case sensitive
    name = name.lower().title()
    amount = float(new_amount)
    date = year + "/" + month + "/" + day

    # update data, pylint is throwing an Error here,
    #   value mailroom_5_read_write_data.data
    # is unsubscriptable if data is set to None. Canged it to {}.
    # for more than one entry per day tobe counted the updating has to be changed
    if date in mailroom_5_read_write_data.data[name]:
        mailroom_5_read_write_data.data[name][date] += amount
    else:
        mailroom_5_read_write_data.data[name][date] = amount

    # send one of the existing letter from letter_templates
    letter_template = letter_templates("1")

    letter = letter_template.format(name=name,
                                    amount=amount,
                                    date=date)
    print("\n", letter)

    # store letter to file
    donor = "_".join(name.lower().split())
    letter_file = donor + "__" + today[0] + "_" + today[1] + "_" + today[2] + "_a"
    pth = os.path.join(os.getcwd(), "thank_you_letter")
    if not os.path.exists(pth):
        os.makedirs(pth)
    destination = os.path.join(pth, letter_file)

    try:
        with open(destination, 'w') as outfile:
            for line in letter:
                outfile.write(line)
    except FileNotFoundError:
        print("Could not find the file")

    print("\nstored letter here:\n", pth)

    return "thank_you"

# "quit" function is available to both "start" and "thank you" menus
def quit():
    """
        the only function changing the variable 'finished' to True
    """
    # store data
    mailroom_5_read_write_data.store_data()

    print("\nleaving mailroom_part2")
    sys.exit()


# -----------------------------------------------------------------------------
#  functions managing or helping the mailroom script but not called by the user



def is_digit_or_period(string):
    """
        checks if all chars in "string" are digits 0 to 9 or a decimal period
        returns True of False
    """
    chars = set('0123456789.')
    digits_and_one_dot = all((c in chars) for c in string) and string.count(".") < 2

    if digits_and_one_dot and "." in string:
        decimals = string.split(".")[1]
        too_many_decimals = decimals[2:]
        zeros = all((c == '0') for c in too_many_decimals) is True
        if not zeros:
            return False

    return digits_and_one_dot


def is_letters_or_space(string):
    """
    checks if all chars in "string" are letters or a space
    returns True or False
    """
    return all(c.isalpha() or c.isspace() for c in string)


def todays_date():
    """
    returns a list containing year, month, day in str format of todays date
    """
    today = datetime.date.today()
    year, month, day = str(today.year), str(today.month), str(today.day)
    return [year, month, day]


def letter_templates(version):
    """
    holds letter templates that can be changed or added new ones to
    could also be read from a file
    """

    # abbreviations for new line, tab and space bar:
    n = "\n"
    t = "\t"
    st = " " + "\t"

    header = "Seattle, WA {date}"
    dear_donor = n * 3 + t + "Dear {name}," + n * 2
    regards_from = st * 5 + "Sincerely," + n * 2 + st * 6 + "-The Team"


    # for letter 1, date: todays date, name, amount: amount of donation
    # registered today
    thank_you_for_amount = (st + "Thank you for your very "
                            "kind donation of ${amount:.2f}." + n * 2)
    money_will_be_used_for = st + "It will be put to very good use." + n * 2


    # for letter 2, date: todays date, name, amount: total amount donated
    yearly_amount_thank_you = st +"Your very generous donation of ${amount:.2f} \
    this year is very much appreciated." + n * 2
    money_is_used_for = (st + "It is put to very good use helping this "
                         "and that." + n * 2)

    # thank you letter sent out after a donation has been made
    donation_thank_you = header +\
                         dear_donor +\
                         thank_you_for_amount +\
                         money_will_be_used_for +\
                         regards_from

    # letter sent to everybody who has donated
    total_donation_thanks = header +\
                            dear_donor +\
                            yearly_amount_thank_you +\
                            money_is_used_for +\
                            regards_from

    version_dict = {"1": donation_thank_you, "2": total_donation_thanks,
                    "3": "under construction"}

    return version_dict[version]

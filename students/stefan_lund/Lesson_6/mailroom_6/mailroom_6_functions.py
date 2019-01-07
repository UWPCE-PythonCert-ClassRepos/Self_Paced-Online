#!/usr/bin/env python3

""" mailroom module evolution
"""
import string
import datetime
import os

# 4 functions on the menu
def create_a_report(data):
    """
        function prints out a report of current names in the data dictionary,
            displaying "Donor Name", "Total Given", "Num Gifts", "Average Gift"
    """

    rprt_dict = report_header(data)

    print_header(rprt_dict)

    for name, donations in sorted(data.items()):
        detail_dict = detail_from(donations)
        rprt_dict["name"] = name
        rprt_dict.update(detail_dict)

        line = rprt_dict["temp_form"].format(**rprt_dict)
        print(line)


def list_of_names(data):
    """
        prints out a list of names currently in the "data" dictionary
    """
    name_list = data.keys()
    list_dict = list_header(data)

    print_header(list_dict)

    for name in sorted(name_list):
        list_dict["name"] = name
        line = list_dict["temp_form"].format(**list_dict)
        print(line)


def send_letters_to_everyone(data):
    """
        sends one type of letter chosen from a template of letters to
            all names in the data dictionary
        each letter is stored as a txt file in cwd folder "letter_to_everyone"
    """

    type_letter = "2"

    for name, donations in sorted(data.items()):
        total_amount = sum(donations["total"])  #  donations is a list of floats
        letter = print_letter(type_letter, name, total_amount)
        save_letter(type_letter, name, letter)


def enter_name(data):
    """
    updates data dictionary with the donation from a new or a present donor
    and prints out a thank you letter
    and stores the letter in cwd folder "thank_you_letter"
    """

    name = name_input()
    # amount is float
    amount = amount_input()

    # entered name is not case sensitive
    name = name.lower().title()

    if name in data:
        data[name]["total"].append(amount)
    else:
        data[name] = {"total": []}
        data[name]["total"] = [amount]

    type_letter = "1"
    letter = print_letter(type_letter, name, amount)
    save_letter(type_letter, name, letter)


# run the module using function "ask_questions"
def ask_questions(data):

    """
    displays the "start" or the "thank you" menu according to current option
    default when script starts is "start" menu
    when "Quit" is chosen, script terminates at the quit function
    """

    menu = {"a": {"create a report": create_a_report},
            "b": {"list of names": list_of_names},
            "c": {"send letters to everyone": send_letters_to_everyone},
            "d": {"enter name": enter_name},
            "e": {"quit": "finished"}}

    stop = False
    while not stop:
        good = False
        while not good:
            # while loop continues until user enters a value from the switch menu
            print("\nYour options are:\n")

            for letter_key, act in menu.items():
                action = list(act.keys())[0]
                option_line = f"{letter_key}.)  {action}"
                print(option_line)

            answer = input("\nEnter letter according to your choice: ")

            # check to see if the "answer" letter is one of the keys in the
            # menu dictionary.
            if answer in menu.keys():
                action = list(menu[answer].keys())[0]
                if answer == "e":
                    print("\nleaving mailroom_part2")
                    # mailroom_6.store_data()
                    stop = True
                    break
                else:
                    menu[answer][action](data)
            else:
                print("Choice is one of these: ", " ,".join(list(menu.keys())))


# helper functions
def print_letter(type_letter, name, total_amount):

    """ type_letter : str    "1" == > "thank_you_letter"
                             "2" == > "letter_to_everyone"
        name        : str    name
        total_amount: str    amount, type str
    """

    letter_template = letter_templates(type_letter)  # needs date, name, and total amount
    date = todays_date()

    letter_info = {"name"   : name,
                   "amount" : total_amount,
                   "date"   : date}

    letter = letter_template.format(**letter_info)
    print("\n", letter)

    return letter


def save_letter(type_letter, name, letter):
    """
    save letter: saves the letter to a file in cwd
    """
    donor = name.split()
    date = todays_date()
    donor.extend(date.split("/"))

    letter_file = "_".join(donor)
    letter_type = {"1": "thank_you_letter", "2": "letter_to_everyone"}

    # create the directory to store the letters if it doesn't exist
    pth = os.path.join(os.getcwd(), letter_type[type_letter])
    if not os.path.exists(pth):
        os.makedirs(pth)

    destination = os.path.join(pth, letter_file)

    try:
        with open(destination, 'w') as outfile:
            for line in letter:
                outfile.write(line)
    except FileNotFoundError:
        print("Could not find the file")

    print("stored letters in:\n", pth)


def print_header(header_dict):
    """ prints the header for the two tables
        formats are proided for in the header_dict, a dictionary
    """
    assert (isinstance(header_dict, dict)), "header_dict is not a dict!"
    header_lne = "\n{frame}\n{line}\n{frame}"
    print(header_lne.format(**header_dict))


def name_lengths(data):
    """
    data: {"Name1": [list of donations], ....}
    Name1 etc are the dict keys, type str
    name_length: integer
    """

    # name_len = max([len(name) for name in data]) + 4
    name_lenths = [len(name) for name in data]

    return name_lenths


def max_length(lst_of_int, longest_header_word):
    """
    lst_of_int : list of integers
    longest_header_word : string, title in header with most letters
    returns the the largest number in lst_of_int unless len("Average Gift")
        is a longer str, adds 3 to this number which is always 15 or more
    """
    assert (isinstance(lst_of_int, list)), "lst_of_int is not a list!"
    assert (isinstance(longest_header_word, str)), "longest_header_word is not a string!"
    # making sure there's enough room for the longest title "Average Gift".
    amount_length = max(max(lst_of_int), len(longest_header_word))
    return amount_length


def amount_lengths(data):
    """
    data: dictionary, {"Name1": [vars in list donations of type float], ....}
    amount_len: add all vars in list and make this value a type str with
                two decimals , name for name each str total is appended to
                len_list
    return len_lst: list of integer(s)
    """
    assert (isinstance(data, dict)), "var data is not a dict!"
    # _ = None
    # len_lst = []
    # _ = [len_lst.append(len("%.2f" % (sum(val["total"])))) for val in data.values()]

    len_lst = [len("%.2f" % (sum(data[name]["total"]))) for name in data]

    return len_lst


def detail_from(donations):
    """ donations: list, contains float numbers, possibly empty list
        total: str type number of int type number
        number_of _donations: str type number with two decimals
        average: str type number with two decimals
        return: tuple, total, number_of _donations, average
    """
    assert (isinstance(donations, dict)), "var donations is not a dict!"
    assert (isinstance(donations["total"], list)), 'var donations["total"] is not a list!'
    number_of_donations = len(donations["total"])
    total = sum(donations["total"])
    average = 0
    if number_of_donations > 0:
        average = total / number_of_donations

    temp_dict = {"total"     : "%.2f" % (total),
                 "num"       : str(int(number_of_donations)),
                 "average"   : "%.2f" % (average)}

    return temp_dict


def make_frame(field_length_dict):
    """ returns a frame built of '+' and '-' to correspond to the appropriate
        width for each field where 'nl' key is for the name field and
        'al' is for the amount fields.
    """

    [(key, length)] = field_length_dict.items()
    assert (key in ["al", "nl"]), "Strange key in field_length_dict!"

    if key == "nl":
        return "+" + "-" * (length)
    return 3 * (("-" * (length)) + "+")


def list_header(data):
    """constructs the header and gets size information to print the header
    """
    name_lens = name_lengths(data)
    name_len = max_length(name_lens, "Donor Name") + 4

    donor_dict = {"name"    : "Donor Name",
                  "nl"      : name_len}

    donor_form = "|{name:<{nl}}|"
    donor_lne = make_frame({"nl": name_len})

    donor_header = {"frame"      : donor_lne + "+",
                    "line"       : donor_form.format(**donor_dict),
                    "temp_form"  : donor_form,
                    "nl"         : name_len}

    return donor_header


def report_header(data):
    """constructs the header and gets size information to print the header
    """
    amount_lengs = amount_lengths(data)
    amount_len = max_length(amount_lengs, "Average Gift") + 3
    lst_dict = list_header(data)

    report_form = "{total:>{al}}|{num:>{al}}|{average:>{al}}|"
    report_lne = make_frame({"al": amount_len})

    report_dict = {"name"       : "Donor Name",
                   "total"      : "Total Given",
                   "num"        : "Num Gifts",
                   "average"    : "Average Gift",
                   "al"         : amount_len,
                   "nl"         : lst_dict["nl"],
                   "frame"      : report_lne,
                   "temp_form"  : report_form}



    reprt_dict = {"frame"      : lst_dict["frame"] + report_dict["frame"],
                  "line"       : (lst_dict["temp_form"] + report_dict["temp_form"]).
                                 format(**report_dict),
                  "temp_form"  : lst_dict["temp_form"] + report_dict["temp_form"],
                  "al"         : report_dict["al"],
                  "nl"         : lst_dict["nl"]}

    return reprt_dict


def decimal_count(float_number):
    """
        float_number : user input converted to float
        checks if more than two decimals and if so, raise ValueError they are
            greater than 0.
        returns input value if no ValueErrror raised
    """
    if "." in str(float_number):
        decimals = str(float_number).split(".")[1]
        too_many_decimals = decimals[2:]
        zeroes = all((c == '0') for c in too_many_decimals) is True
        if not zeroes:
            raise ValueError

    return float_number


def amount_input():
    """ user entered amount,
            raise ValueError if input cannot be a float or if input has more
            than 2 decimals and they are greater than 0.
        returns accepted user entered amount
    """

    while True:
        try:
            new_amount = float(input("\nEnter amount donated: "))
            amount = decimal_count(new_amount)
        except ValueError:
            print("invalid amount value, try again")
        else:
            break
    return amount


def is_letters_space_or_hyphen(strng):
    """
    checks if all chars in "string" are letters, a space or a hyphen
    good_chars is a string of all chars that are accepted
    returns True or False
    """
    # all upper and lover case letters, "space bar" for "first last" name and
    # "-" hyphen for "Anne-Marie"
    good_char = string.ascii_lowercase + ' ' + '-'
    str_set = set(strng.lower())
    return all(char in good_char for char in str_set)


def name_input():
    """ user entered name,
            check if input is letters or space
        returns name input
    """

    good_name = False
    while not good_name:
        name = input("\nEnter name, 'First Last': ")
        good_name = is_letters_space_or_hyphen(name)

        if not good_name:
            print("doesn't look like a name, try again")

    return name


def todays_date():
    """
    returns a string "year/month/day" of todays date
    """
    today = datetime.date.today()
    # year, month, day = str(today.year), str(today.month), str(today.day)
    date = str(today.year), str(today.month), str(today.day)
    return "/".join(date)


def letter_templates(version):
    """
    holds letter templates that can be changed or added new ones to
    could also be read from a file
    """

    # abbreviations for new line, tab and space bar:
    # n = "\n"
    # t = "\t"
    # st = " " + "\t"

    header = "Seattle, WA {date}"
    # dear_donor = n * 3 + t + "Dear {name}," + n * 2
    # regards_from = st * 5 + "Sincerely," + n * 2 + st * 6 + "-The Team"

    dear_donor = "\n" * 3 + "\t" + "Dear {name}," + "\n" * 2
    regards_from = " \t" * 5 + "Sincerely," + "\n" * 2 + " \t" * 6 + "-The Team"

    thank_you_for_amount = (" \t" + "Thank you for your very "
                            "kind donation of ${amount:.2f}." + "\n" * 2)
    money_will_be_used_for = " \t" + "It will be put to very good use." + "\n" * 2


    # for letter 2, date: todays date, name, amount: total amount donated
    yearly_amount_thank_you = " \t" +"Your very generous donation of\
    ${amount:.2f} this year is very much appreciated." + "\n" * 2
    money_is_used_for = (" \t" + "It is put to very good use helping this "
                         "and that." + "\n" * 2)

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


if __name__ == '__main__':

    names = {
        "William Gates, III"  : {"total": [300000.00, 353784.49]},
        "Mark Zuckerberg"     : {"total": [5000.00, 5000.00, 6396.10]},
        "Jeff Bezos"          : {"total": [877.33]},
        "Paul Allen"          : {"total": [200, 200, 308.42]}
        }

    ask_questions(names)

# python3

# The Mailroom Automation
# mailroom.py

import os
import pickle
import datetime
import sys

# functions available to the user, only from the "menu"
# "start" menu functions


def send_a_thank_you():
    """
    sole function is to switch to the "thank you" menue
    """
    option = "thank you"
    return option


def create_a_report():
    """
        function prints out a report of current names in the data dictionary,
            displaying "Donor Name", "Total Given", "Num Gifts", "Average Gift"
    """
    global data

    name_len = 0
    amount_len = 0

    for name, numbers in data.items():
        if len(name) > (name_len - 3):
            name_len = len(name) + 3
        if len(numbers[0]) > (amount_len - 3):
            amount_len = len(numbers[0]) + 3

    temp_str = "Donor Name", "Total Given", "Num Gifts", "Average Gift"
    temp_form = "\n{:<{nl}}|{:>{al}}|{:>{al}}|{:>{al}}"
    header = temp_form.format(*temp_str, nl=name_len, al=amount_len)
    print(header)
    p = "+"
    s = "-"
    lne = s * (name_len)
    e = p + (s * (amount_len))
    lne += 3 * e
    print(lne)

    for name in sorted(data.keys()):
        donations = data[name]
        total, number_of = donations
        # if name is entered but no donation has been made, avoid division by 0
        if number_of == "0":
            average = 0
        else:
            total = float(total)
            number_of = int(number_of)
            average = total / number_of

        temp_form = "{:<{nl}} ${:>{al}.2f}  {:>{al}} ${:>{al}.2f}"
        line = temp_form.format(name, total, number_of, average, nl=name_len, al=amount_len - 1)
        print(line)

    option = "start"
    return option


def send_letters_to_everyone():
    """
        sends one type of letter chosen from a template of letters to
            all names in the data dictionary
        each letter is stored as a txt file in cwd folder "letter_to_everyone"
    """
    global data

    letter_template = letter_templates("2")
    today = todays_date()

    temp_date = today[1] + "/" + today[2] + "/" + today[0]
    for name in sorted(data.keys()):
        donations = data[name]
        total, _ = donations
        letter = letter_template.format(name=name,
                                        amount=total,
                                        date=temp_date)
        print("\n", letter)

        # store letter
        donor = "_".join(name.split())
        letter_file = donor + "__" + today[0] + "_" + today[1] + "_" + today[2] + "_b"
        pth = os.path.join(os.getcwd(), "letter_to_everyone")
        if not os.path.exists(pth):
            os.makedirs(pth)
        destination = os.path.join(pth, letter_file)

        try:
            with open(destination, 'w') as outfile:
                for line in letter:
                    outfile.write(line)
        except:
            print("something went wrong, read")

        print("stored letters in ", pth)

    option = "start"
    return option


# "thank you" menu functions

def main_menu():
    """
    displays the "start" or the "thank you" menu according to current option
    default when script starts is "start" menu
    when "Quit" is chosen, script terminates at the quit function
    """
    global menu
    option = "start"
    while True:
        sub_menu = menu[option]
        option = ask_questions(sub_menu)


def list_of_names():
    """
        prints out a list of names currently in the "data" dictionary
    """
    global data

    name_list = data.keys()
    name_length = []
    [name_length.append(len(name)) for name in name_list]
    name_len = max(name_length) + 3

    temp_str = "Donor Name"
    temp_form = "\n| {:<{nl}}|"
    header = temp_form.format(temp_str, nl=name_len)
    frame = "\n+" + "-" * (name_len + 1) + "+"
    # print("\n+" + "-" * (name_len + 1) + "+")
    print(frame, header, frame)
    # print("+" + "-" * (name_len + 1) + "+")

    for name in sorted(name_list):
        temp_form = "| {:<{nl}}|"
        line = temp_form.format(name, nl=name_len)
        print(line)

    option = "thank you"
    return option


def enter_name():
    """
    updates data dictionary with the donation from a new or a present donor
    and prints out a thank you letter
    and stores the letter in cwd folder "thank_you_letter"
    """
    global data

    # user enter name, check if input is alpha or space
    name_of_letters = False
    while not name_of_letters:
        name = input("\nEnter name, 'First Last': ")
        name_of_letters = is_alpha_or_space(name)

    # user enter new_amount, check if new_amount is a number
    digits_in_amount = False
    while not digits_in_amount:
        new_amount = input("\nEnter amount donated: ")
        digits_in_amount = is_digit_or_period(new_amount)

    # entered name is not case sensitive
    name_list_lower = []
    for nme in data.keys():
        name_list_lower.append(nme.lower())

    print(name, name in name_list_lower)

    # see if name is an existing name or a new and unknown name
    if name.lower() in name_list_lower:
        name = name.title()
        # add new donation to previous total
        amount = '%.2f' % (float(data[name][0]) + float(new_amount))
        # update times donating
        times = str(int(data[name][1]) + 1)
    else:
        name = name.title()
        amount = '%.2f' % float(new_amount)
        times = str(1)

    # update data
    data[name] = (str(amount), times)

    # send one of the existing letter from letter_templates
    letter_template = letter_templates("1")
    today = todays_date()

    temp_date = today[1] + "/" + today[2] + "/" + today[0]
    new_amount = '%.2f' % float(new_amount)
    letter = letter_template.format(name=name,
                                    amount=new_amount,
                                    date=temp_date)
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
    except:
        print("something went wrong, enter_name")

    print("stored letter in ", pth)

    option = "thank you"
    return option


# "quit" function is available to both "start" and "thank you" menus
def quit():
    """
        the only function changing the variable 'finished' to True
    """
    store_data()
    print("leaving mailroom_part2")
    sys.exit()


# -----------------------------------------------------------------------------
#  functions managing or helping the mailroom script but not called by the user


def ask_questions(sub_menu):
    """
        called by "main_menu" function with with either "start" or "thank you"
            menu
        only the letters displyed in front of each option is an acceptable
            answer
        converts the choice to a function
        returns the answer from the call to the function to main_menu
    """
    good_answer = False
    while not good_answer:
        print("\nYour options are:\n")

        for key, value in sub_menu.items():
            # print the options looking pretty
            value = value.__name__
            option_list = value.split("_")
            option_string = " ".join(option_list)
            option_string = option_string.title()
            s = f"{key}.)  {option_string}"
            print(s)

        answer = input("\nEnter letter according to your choice: ")

        # check to see if the "answer" letter is one of the keys in the sub_menu dictionary
        good_answer = sub_menu.get(answer, False)

    return sub_menu[answer]()


def is_digit_or_period(string):
    """
        checks if all chars in "string" are digits 0 to 9 or a decimal period
        returns True of False
    """
    chars = set('0123456789.')
    return all((c in chars) for c in string)


def is_alpha_or_space(string):
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
    n = "\n"
    t = "\t"
    s = " "

    # letter 1, date: todays date, name, amount: amount of donation registered today
    l1 = "Seattle, WA {date}" + n * 3 + t + "Dear {name}," + n * 2
    l2 = ((t + s) * 1 + "Thank you for your very "
          "kind donation of ${amount}." + n * 2)
    l3 = (t + s) * 1 + "It will be put to very good use." + n * 2
    l4 = (t + s) * 5 + "Sincerely," + n * 2
    l5 = (t + s) * 6 + "-The Team"
    letter1 = l1 + l2 + l3 + l4 + l5

    # letter 2, date: todays date, name, amount: total amount donated
    day = (t + s) * 8 + "{date}" + n * 6
    l1 = "Dear {name}," + n * 2
    l2 = (t + s) * 1 + "Your very generous donation of ${amount} \
    this year is very much appreciated." + n * 2
    l3 = (t + s) * 1 + "It will be put to very good use." + n * 2
    l4 = (t + s) * 5 + "Sincerely," + n * 2
    l5 = (t + s) * 6 + "-The Team"
    letter2 = day + l1 + l2 + l3 + l4 + l5

    version_dict = {"1": letter1, "2": letter2, "3": "under construction"}

    return version_dict[version]


def get_data_from(file_name):
    """
    uses the pickle module to retrieve data from file as a dictionary
    file_name: file name where the data of the donors etc. can be found.
    must be in the cwd,
    data_dict = {name:(amount, times donating), etc}
    """

    global data, data_file
    # data_dict = {}
    source = os.path.join(os.getcwd(), file_name)
    try:
        with open(source, 'rb') as infile:
            # data_dict = pickle.load(infile)
            data = pickle.load(infile)

            # set the global variable data_file
            data_file = source
    except:
        print("something went wrong, read")


def store_data():
    """
    writes data to data_file
    file_path:  abspath including file-name
    data:       dictionary
    stores pickled data in binary format
    """
    global data, data_file

    try:
        with open(data_file, 'wb') as outfile:
            pickle.dump(data, outfile, protocol=pickle.HIGHEST_PROTOCOL)
            print("\nstored data in: ", data_file)
    except:
        print("\nsomething went wrong, store_data")


# data and data_file is set by the 'get_data_from' function
# data and data_file are global variables
data_file = None
data = None


if __name__ == '__main__':

    menu = {"start":     {"a": send_a_thank_you,
                          "b": create_a_report,
                          "c": send_letters_to_everyone,
                          "d": quit},

            "thank you": {"a": main_menu,
                          "b": list_of_names,
                          "c": enter_name,
                          "d": quit}}

    file = "dictionary.pickle"

    # read from file and make the dictionary available to the module
    #   as the variable data
    get_data_from(file)

    # start the run_mailroom_part2
    main_menu()

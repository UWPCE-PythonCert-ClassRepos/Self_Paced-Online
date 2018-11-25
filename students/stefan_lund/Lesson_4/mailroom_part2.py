# python3

# The Mailroom Automation
# mailroom.py

import os
import pickle
import datetime

# functions available to the user, only from the "menu"
# "start" menu functions

def send_a_thank_you():
    """
    sole function is to switch to the "thank you" menue
    """
    option = "thank you"
    finished = False

    return finished, option

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
    for name, numbers in data.items():
        d0 = name
        d1 = float(numbers[0])
        d2 = int(numbers[1])
        if d2 == 0:
            d3 = 0
        else:
            d3 = d1 / d2

        temp_form = "{:<{nl}} ${:>{al}.2f}  {:>{al}} ${:>{al}.2f}"
        line = temp_form.format(d0, d1, d2, d3, nl=name_len, al=amount_len - 1)
        print(line)

    option = "start"
    finished = False
    return finished, option

def send_letters_to_everyone():
    """
        sends one type of letter chosen from a template of letters to
            all names in the data dictionary
        each letter is stored as a txt file in cwd
    """
    global data

    letter_template = letter_templates("2")
    today = todays_date()

    temp_date = today[1] + "/" + today[2] + "/" + today[0]
    for key in data.keys():
        letter = letter_template.format(name=key,
                                        amount=data[key][0],
                                        date=temp_date)
        print("\n", letter)

        # store letter
        donor = "_".join(key.split())
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

    option = "start"
    finished = False
    return finished, option


# "thank you" menu functions

def main_menu():
    """
    displays the "start" or the "thank you" menu according to current option
    default when script starts is "start" menu
    variable "finished" is False for all choices except "Quit" which returns
    "finished" as True
    """
    global menu
    option = "start"
    finished = False
    while not finished:
        sub_menu = menu[option]
        print("1.  main_menu, ", finished, option)
        finished, option = ask_questions(sub_menu)

        # when "Quit returns "finished as True the while loop ends but script
        # crashes, the solution with if and break was added
        if finished:
            print("2.  main_menu, ", finished, option)
            store_data()
            break

def list_of_names():
    """
        prints out a list of names currently in the "data" dictionary
    """
    global data
    name_list = data.keys()

    name_len = 0
    for name in name_list:
        if len(name) > (name_len - 3):
            name_len = len(name) + 3

    temp_str = "Donor Name"
    temp_form = "\n| {:<{nl}}|"
    header = temp_form.format(temp_str, nl=name_len)
    frame = "\n+" + "-" * (name_len + 1) + "+"
    # print("\n+" + "-" * (name_len + 1) + "+")
    print(frame, header, frame)
    # print("+" + "-" * (name_len + 1) + "+")

    for name in name_list:
        temp_form = "| {:<{nl}}|"
        line = temp_form.format(name, nl=name_len)
        print(line)

    option = "thank you"
    finished = False
    return finished, option

def enter_name():
    """
    updates data dictionary with the donation from a new or a present donor
    and prints out a thank you letter
    and stores the letter in cwd with a file name
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
    for name in data.keys():
        name_list_lower.append(name.lower())

    # name_list = data.keys()
    # [name_list_lower.append(name.lower()) for name in name_list]

    # see if name is an existing name or a new and unknown name
    if name.lower() in name_list_lower:
        name = name.title()
        amount = '%.2f' % (float(data[name][0]) + float(new_amount))
        # amount = str(float(data[name][0]) + float(new_amount))
        times = str(int(data[name][1]) + 1)
        # data[name][0] = str(float(data[name][0]) + float(new_amount))
        # data[name][1] = str(int(data[name][1]) + 1)
    else:
        name = name.title()
        amount = '%.2f' % float(new_amount)
        times = str(1)

    data[name] = (amount, times)
    print("enter_name  ", data)

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

    option = "thank you"
    finished = False
    return finished, option


# "quit" function is available to both "start" and "thank you" menus
def quit():
    """
        the only function changing the variable 'finished' to True
    """
    option = "start"
    finished = True
    return finished, option

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
            # s = f"{key}.)  {value.__name__}"
            s = f"{key}.)  {value}"
            print(s)

        answer = input("\nEnter letter according to your choice: ")
        good_answer = sub_menu.get(answer, False)

    func_answer = good_answer.lower().split()
    func = "_".join(func_answer)
    # print("ask_questions,   func: ", func)                                  #

    method = eval(func)
    return method()

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

    version_dict = {"1":letter1, "2":letter2, "3":"under construction"}

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

menu = {"start":     {"a": 'Send a Thank You',
                      "b": 'Create a Report',
                      "c": 'Send Letters to Everyone',
                      "d": 'Quit'},

        "thank you": {"a": 'Main Menu',
                      "b": 'List of Names',
                      "c": 'Enter Name',
                      "d": 'Quit'}}

# data = ["William Gates, III", 653784.49, 2, "Mark Zuckerberg",
        # 16396.10, 3, "Jeff Bezos", 877.33, 1, "Paul Allen", 708.42, 3]

if __name__ == '__main__':
    # bin_text: file in cwd containing name, total amount, number of times donating
    #   file is binary and "/" delimited, (no "\n").
    file = "dictionary.pickle"

    # read from file and make the dictionary available to the module
    #   as the variable data
    get_data_from(file)

    # start the run_mailroom_part2
    main_menu()

# python3

# The Mailroom Automation
# mailroom.py
import os
import datetime

def send_a_thank_you(menu, data):

    option = "thank you"
    finished = False
    while not finished:
        finished = ask_questions(menu, option, data)

    return finished

def enter_name(menu, file_name):
    """
        updates file_name file with the donation from a new or a present donor
    """
    name_list = get_names_from(file_name)
    name = input("\nEnter name, 'First Last': ")
    amount = input("\nEnter amount donated: ")

    # entered name is not case sensitive
    name_list_lower = []
    [name_list_lower.append(name.lower()) for name in name_list]
    if name.lower() in name_list_lower:
        data = get_data_from(file_name)
        name = name.title()
        amount = '%.2f' % (float(data[name][0]) + float(amount))
        # amount = str(float(data[name][0]) + float(amount))
        times = str(int(data[name][1]) + 1)
        data[name] = (amount, times)
        # data[name][0] = str(float(data[name][0]) + float(amount))
        # data[name][1] = str(int(data[name][1]) + 1)
        store_data_to(file_name, data)
    else:
        name = name.title()
        amount = '%.2f' % float(amount)
        times = str(1)
        data = {name:(amount, times)}
        store_data_to(file_name, data, add=True)

    # send a letter
    letter_template = letter_templates("1")
    today = todays_date()

    temp_date = today[1] + "/" + today[2] + "/" + today[0]
    letter = letter_template.format(name=name,
                                    amount=amount,
                                    date=temp_date)
    print("\n", letter)

    donor = "_".join(name.lower().split())
    letter_file = donor + "__" + today[0] + "_" + today[1] + "_" + today[2] + "_a"

    # store letter to file
    store_data_to(letter_file, letter)

    return False

def send_letters_to_everyone(menu, file_name):
    """
        data: {'name': ['total amount donated',
                           'number of times donating']}

    """
    data = get_data_from(file_name)
    letter_template = letter_templates("2")
    today = todays_date()

    temp_date = today[1] + "/" + today[2] + "/" + today[0]
    for key in data.keys():
        letter = letter_template.format(name=key,
                                        amount=data[key][0],
                                        date=temp_date)
        print("\n", letter)

        donor = "_".join(key.split())
        letter_file = donor + "__" + today[0] + "_" + today[1] + "_" + today[2]

        store_data_to(letter_file, letter)

    return False

def letter_templates(version):



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

    version_dict = {"1":letter1, "2":letter1, "3":"under construction"}

    return version_dict[version]

def todays_date():
    """
        returns a list containing year, month, day in str format
    """
    today = datetime.date.today()
    year, month, day = str(today.year), str(today.month), str(today.day)
    return [year, month, day]

def get_names_from(in_file):
    """
        in_file: file name for file in cwd where data is stored
        returns: list of recorded names
    """
    data = get_data_from(in_file)
    name_list = []
    for name in data:
        name_list.append(name)

    return name_list

def list_of_names(menu, file_name):
    """
        file_name: file name for file in cwd where data is stored
    """
    name_list = get_names_from(file_name)

    name_len = 0
    for name in name_list:
        if len(name) > (name_len - 3):
            name_len = len(name) + 3

    temp_str = "Donor Name"
    temp_form = "\n{:<{nl}}|"
    header = temp_form.format(temp_str, nl=name_len)
    print(header)
    print("-" * name_len + "+")

    for name in name_list:
        temp_form = "{:<{nl}}|"
        line = temp_form.format(name, nl=name_len)
        print(line)

    return False

def quit(menu, file_name):
    return True

def read_in_pieces(file_object, piece_size=32):
    """
        Function (generator) to read a file piece by piece.
        Default piece_size: 32 bytes to read a small file in several pieces
    """
    while True:
        data = file_object.read(piece_size)
        if not data:
            break
        # print("data: ", data, "size: ", sys.getsizeof(data))
        yield data

def is_alpha_or_space(string):
    return all(c.isalpha() or c.isspace() for c in string)

def is_digit_or_period(string):
    chars = set('0123456789.')
    return all((c in chars) for c in string)

def get_data_from(file_name):
    """

    file_name: file name where the data of the donors etc. can be found.
        must be in the cwd,
        info is '/' delimited, bytes
            info containing name, total amount, number of donations
    data_dict = {name:(amount, times donating), etc}
    """

    data_dict = {}
    source = os.path.join(os.getcwd(), file_name)
    try:
        with open(source, 'rb') as infile:
            str_data = []
            previous_str_data = tuple()
            for bin_data_piece in read_in_pieces(infile):
                new_str_data = bin_data_piece.decode('utf-8').split('/')

                #  remove trailing white space when delimiter present in the last position
                if new_str_data[-1:][0] == "":
                    new_str_data = new_str_data[:-1]

                if len(previous_str_data) > 0 and len(new_str_data) > 0:

                    a = is_alpha_or_space(previous_str_data[-1]) and is_alpha_or_space(new_str_data[0])
                    b = is_digit_or_period(previous_str_data[-1]) and is_digit_or_period(new_str_data[0])

                    if a or b:
                        previous_temp = list(previous_str_data)
                        if "." in previous_temp[-1] and len(previous_temp[-1].split(".")[1]) == 2:
                            patch = previous_temp[-1]
                            previous_new = previous_temp[:-1]
                            previous_new.append(patch)
                            previous_new.extend(new_str_data[:])
                        else:
                            patch = previous_temp[-1] + new_str_data[0]
                            previous_new = previous_temp[:-1]
                            previous_new.append(patch)
                            previous_new.extend(new_str_data[1:])
                    else:
                        previous_new = list(previous_str_data).extend(new_str_data)

                    new_str_data = previous_new

                add_info = new_str_data[:3 * (len(new_str_data) // 3)]

                previous_str_data = tuple(new_str_data[3 * (len(new_str_data) // 3):])
                str_data.extend(add_info)
                # print(str_data)
        data_dict = {key:values for key, values in
        zip(str_data[::3], zip(str_data[1::3], str_data[2::3]))}
        # print("data_dict: ", data_dict)
        return data_dict
    except:
        print("something went wrong, read")

def write_to(file_path, data, mode='wb'):
    """
        writes data to file_path
        file_path:  abspath + file-name
        data:       string
        stores data in binary format
    """
    try:
        with open(file_path, mode) as otf:
            bin_data = data.encode("utf-8")
            otf.write(bin_data)
        print("\nstored data in: ", file_path)
    except:
        print("\nsomething went wrong, write")

def store_data_to(file_name, data, add=False):
    """
        file_name: file name of file where the data will be stored.
            path to file is the cwd,
            info is '/' delimited, bytes
                info containing name, total amount, number of donations
        data: dictionary, {name:(amount, times donating), etc}
    """
    destination = os.path.join(os.getcwd(), file_name)
    str_data = data

    if isinstance(data, dict):
        str_data = ""
        for key, value in data.items():
            str_data += key + "/" + value[0] + "/" + value[1] + "/"

    mode = 'wb'
    if add:
        str_data = "/" + str_data
        mode = 'ab'

    write_to(destination, str_data, mode)

def create_a_report(menu, file_name):
    data = get_data_from(file_name)
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

    return False

def ask_questions(menu, option, file_name):
    """

    """
    good_answer = False
    while not good_answer:
        print("\nYour options are:\n")

        for key, value in menu[option].items():
            # s = f"{key}.)  {value.__name__}"
            s = f"{key}.)  {value}"
            print(s)
        answer = input("\nEnter letter according to your choice: ")
        good_answer = menu[option].get(answer, False)

    func_answer = good_answer.lower().split()
    func = "_".join(func_answer)
    print(func)                                                                #

    method = eval(func)
    return method(menu, file_name)

def main_menu(menu, file):
    option = "start"
    finished = False
    while not finished:
        finished = ask_questions(menu, option, file)

    print("\nLeaving the Mailroom 1.", "finished: ", finished)
    return finished

def run_mailroom(file):
    """
    data: list with name, total of donations - dddd.cc, number of gift occations
    """

    menu = {"start":     {"a": 'Send a Thank You',
                          "b": 'Create a Report',
                          "c": 'Send Letters to Everyone',
                          "d": 'Quit'},

            "thank you": {"a": 'Main Menu',
                          "b": 'List of Names',
                          "c": 'Enter Name',
                          "d": 'Quit'}}

    main_menu(menu, file)
    # not sure how well this ends, does it gets stuck here holding a
        # boolean return value or does the script really terminate?

data = ["William Gates, III", 653784.49, 2, "Mark Zuckerberg",
        16396.10, 3, "Jeff Bezos", 877.33, 1, "Paul Allen", 708.42, 3]

if __name__ == '__main__':
    # bin_text: file in cwd containing name, total amount, number of times donating
        # file is binary and "/" delimited, (no "\n").
    file = "bin_text.bin"
    run_mailroom(file)

#!/usr/bin/env python3


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

    return "start"


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

    return "thank_you"


def print_header(header_dict):
    header_lne = "\n{frame}\n{line}\n{frame}"
    print(header_lne.format(**header_dict))


def name_length(data):
    """
    data: {"Name1": [list of donations], ....}
    Name1 etc are the dict keys, type str
    name_length: integer
    """

    # width of name field to print
    name_list = data.keys()
    name_len = []
    # list comprehension
    [name_len.append(len(name)) for name in name_list]
    name_lenth = max(name_len) + 4

    return name_lenth

def amount_length_max(lst_of_int):
    """
    lst_of_int : list of integers
    returns the the largest number in lst_of_int unless len("Average Gift")
        is a longer str, adds 3 to this number
    """
    amount_length = max(max(lst_of_int), len("Average Gift")) + 3
    return amount_length


def amount_lengths(data):
    """
    data: {"Name1": [list of donations], ....}
    amount_len: add all vars in list and make this value a type str with
                two decimals , name for name each str total is appended to
                len_list
    return len_lst: list of integer(s)
    """

    len_lst = []
    [len_lst.append(len("%.2f" % (sum(val["total"])))) for val in data.values()]
    return len_lst


def detail_from(donations):
    """ donations: list, contains float numbers, possibly empty list
        total: str type number of int type number
        number_of _donations: str type number with two decimals
        average: str type number with two decimals
        return: tuple, total, number_of _donations, average
    """

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

    name_len = name_length(data)
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

    amount_lengs = amount_lengths(data)
    amount_len = amount_length_max(amount_lengs)
    lst_dict = list_header(data)

    report_dict = {"name"    : "Donor Name",
                   "total"   : "Total Given",
                   "num"     : "Num Gifts",
                   "average" : "Average Gift",
                   "al"      : amount_len,
                   "nl"      : lst_dict["nl"]}

    report_form = "{total:>{al}}|{num:>{al}}|{average:>{al}}|"

    report_lne = make_frame({"al": amount_len})
    reprt_dict = {"frame"      : lst_dict["frame"] + report_lne,
                  "line"       : (lst_dict["temp_form"] + report_form).format(**report_dict),
                  "temp_form"  : lst_dict["temp_form"] + report_form,
                  "al"         : amount_len,
                  "nl"         : lst_dict["nl"]}

    return reprt_dict

names = {
    "William Gates, III"  : {"total": [300000.00, 353784.49]},
    "Mark Zuckerberg"     : {"total": [5000.00, 5000.00, 6396.10]},
    "Jeff Bezos"          : {"total": [877.33]},
    "Paul Allen"          : {"total": [200, 200, 308.42]}
    }

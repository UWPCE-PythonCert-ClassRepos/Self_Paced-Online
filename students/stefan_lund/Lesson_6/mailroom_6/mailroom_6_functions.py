#!/usr/bin/env python3


def create_a_report(data):
    """
        function prints out a report of current names in the data dictionary,
            displaying "Donor Name", "Total Given", "Num Gifts", "Average Gift"
    """

    rprt_header = report_header(data)

    for line in rprt_header[:3]:
        print(line)

    temp_form = rprt_header[3]
    amount_len = rprt_header[4]
    name_len = rprt_header[5]

    for name, donations in data.items():
        total, number_of_donations, average = detail_from(donations)

        line = temp_form.format(name,
                                total,
                                number_of_donations,
                                average,
                                nl=name_len,
                                al=amount_len)
        print(line)

    return "start"


def list_of_names(data):
    """
        prints out a list of names currently in the "data" dictionary
    """
    name_list = data.keys()

    lst_header = list_header(data)
    # print header
    for line in lst_header[:3]:
        print(line)

    temp_form = lst_header[3]
    name_len = lst_header[4]
    # print each name in alphabetical order
    for name in sorted(name_list):
        # temp_form = "| {:<{nl}}|"
        line = temp_form.format(name, nl=name_len)
        print(line)

    return "thank_you"


def name_length(data):
    """
    data: {"Name1": [list of donations], ....}
    Name1 etc are the dict keys
    name_length: integer
    """

    # determine width of name field to print
    name_list = data.keys()
    name_len = []
    # list comprehension
    [name_len.append(len(name)) for name in name_list]
    name_lenth = max(name_len) + 4

    return name_lenth


def amount_length(data):
    """
    data: {"Name1": [list of donations], ....}
    amount_len: len of str value for the sum of each list of donations
        associated with each name, list content is float numbers
    amount_length: integer
    """

    len_lst = []
    [len_lst.append(len("%.2f" % (sum(val["total"])))) for val in data.values()]

    amount_lenth = max(max(len_lst), len("Average Gift")) + 3

    return amount_lenth


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

    return ("%.2f" % (total),
            str(int(number_of_donations)),
            "%.2f" % (average))


def list_header(data):

    name_len = name_length(data)
    donor_str = ["Donor Name"]
    donor_form = "|{:<{nl}}|"

    p = "+"
    s = "-"
    donor_lne = p + s * (name_len)

    donor_header = [donor_lne + p,
                    donor_form.format(*donor_str, nl=name_len),
                    donor_lne + p,
                    donor_form,
                    name_len]

    return donor_header


def report_header(data):

    amount_len = amount_length(data)

    report_str = ["Donor Name", "Total Given", "Num Gifts", "Average Gift"]

    report_form = "{:>{al}}|{:>{al}}|{:>{al}}|"

    p = "+"
    s = "-"
    report_lne = 3 * ((s * (amount_len)) + p)

    donor_lne, _, _, donor_form, name_len = list_header(data)

    reprt_header = [donor_lne + report_lne,
                    (donor_form + report_form).format(*report_str,
                                                      nl=name_len,
                                                      al=amount_len),
                    donor_lne + report_lne,
                    donor_form + report_form,
                    amount_len,
                    name_len]

    return reprt_header


names = {
    "William Gates, III"  : {"total": [300000.00, 353784.49]},
    "Mark Zuckerberg"     : {"total": [5000.00, 5000.00, 6396.10]},
    "Jeff Bezos"          : {"total": [877.33]},
    "Paul Allen"          : {"total": [200, 200, 308.42]}
    }

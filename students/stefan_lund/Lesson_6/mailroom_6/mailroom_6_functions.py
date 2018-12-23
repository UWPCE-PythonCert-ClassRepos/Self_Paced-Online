#!/usr/bin/env python3



def create_a_report():
    """
        function prints out a report of current names in the data dictionary,
            displaying "Donor Name", "Total Given", "Num Gifts", "Average Gift"
    """
    data = mailroom_5_read_write_data.data

    # name_len = 0
    # amount_len = 0
    #
    # for name, donations in data.items():
    #     if len(name) > (name_len - 3):
    #         name_len = len(name) + 3
    #     for date in donations:
    #         amount = str(donations[date])
    #         if len(amount) > (amount_len - 3):
    #             amount_len = len(amount) + 3
    #
    # temp_str = "Donor Name", "Total Given", "Num Gifts", "Average Gift"
    # temp_form = "\n{:<{nl}}|{:>{al}}|{:>{al}}|{:>{al}}"
    # header = temp_form.format(*temp_str, nl=name_len, al=amount_len)
    # print(header)
    #
    # # separation line used to make presentation look nice
    # p = "+"
    # s = "-"
    # lne = s * (name_len)
    # e = p + (s * (amount_len))
    # lne += 3 * e
    # print(lne)

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



def list_of_names():
    """
        prints out a list of names currently in the "data" dictionary
    """
    data = mailroom_5_read_write_data.data

    # # determine width of fields to print in
    # name_length = []
    # name_list = data.keys()
    # # list comprehension
    # [name_length.append(len(name)) for name in name_list]
    # name_len = max(name_length) + 3
    #
    # # print table header
    # temp_str = "Donor Name"
    # temp_form = "\n| {:<{nl}}|"
    # header = temp_form.format(temp_str, nl=name_len)
    # frame = "\n+" + "-" * (name_len + 1) + "+"
    print(frame, header, frame)

    # print each name in alphabetical order
    for name in sorted(name_list):
        temp_form = "| {:<{nl}}|"
        line = temp_form.format(name, nl=name_len)
        print(line)

    return "thank_you"

def table_size(data):
    """
    data: {"Name1": [list of donations], ....}
    returns headers for list_of_names, create_a_report and the width of the
        name field and the amount field which is used for all the other fields
        return = [[header1], field_widht1], [[header2], field_widht2]
    """

    len_lst = []
    [len_lst.append((len(name),
                     len("%.2f" % (sum(val["total"]))))) for name, val in names.items()]

    name_len = max([sublist[0] for sublist in len_lst]) + 4
    amount_len = max(max([sublist[1] for sublist in len_lst]),
                     len("Average Gift")) + 3

    return name_len, amount_len


def table_header(data):

    name_len, amount_len = table_size(names)

    donor_str = ["Donor Name"]
    report_str = ["Donor Name", "Total Given", "Num Gifts", "Average Gift"]


    donor_form = "|{:<{nl}}|"
    report_form = "{:>{al}}|{:>{al}}|{:>{al}}|"

    p = "+"
    s = "-"
    donor_lne = p + s * (name_len)
    report_lne = 3 * (p + (s * (amount_len))) + p
    lne = donor_lne, report_lne

    donor_header = [[donor_lne + p,
                     donor_form.format(*donor_str, nl=name_len),
                     donor_lne + p],
                    name_len]

    report_header = [[donor_lne + report_lne,
                      (donor_form + report_form).format(*report_str, nl=name_len, al=amount_len),
                      donor_lne + report_lne],
                     amount_len]

    return donor_header, report_header



names = {
    "William Gates, III"  : {"total": [300000.00, 353784.49]},
    "Mark Zuckerberg"     : {"total": [5000.00, 5000.00, 6396.10]},
    "Jeff Bezos"          : {"total": [877.33]},
    "Paul Allen"          : {"total": [200, 200, 308.42]}
    }

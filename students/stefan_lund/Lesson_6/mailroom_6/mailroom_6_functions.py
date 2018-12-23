#!/usr/bin/env python3



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

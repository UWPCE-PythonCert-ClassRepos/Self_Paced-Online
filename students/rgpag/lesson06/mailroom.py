#!/usr/bin/env python3
import datetime

donors = {
    'Jeff Bezos': [250, 750, 1000, 1000],
    'Mark Zuckerberg': [10, 10],
    'Bill Gates': [10000, 20000, 10607],
    'Paul Allen': [10, 10, 10, 10, 10, 15],
}

msg = """
\nDear {},\n\nThank you for your recent donation, did you \
realize you have now made {} lifetime donations? Wow, look at you all star! \
We are most grateful for your total donation amount of ${}.\n\nI will \
personally ensure these funds are put towards purchase of yummy \
donuts! Also, any additional contributions you make in the next 24 hours \
will be matched up to $1000. What a deal! Don't delay.\n\nHumbly yours,\n
Dime for Donuts\n
"""


def print_format_msg(msg_vars):
    print(msg.format(*msg_vars))


def don_in(don_amt=""):
    if don_amt == "":
        while True:
            try:
                don_amt = int(input('What was the donation amount?'))
            except ValueError:
                print('input must be an integer, try again')
            else:
                break
    return don_amt


def new_donor(new_name, don_amt=""):
    if don_amt == "":
        don_amt = don_in()
    donors[new_name] = [don_amt]
    return new_name, 1, don_amt


def update_don(ret_don, don_amt=""):
    if don_amt == "":
        don_amt = don_in()
    donors[ret_don].append(don_amt)
    count = len(donors[ret_don])
    total_amt = sum(donors[ret_don])
    return ret_don, count, total_amt


def menu_sel_1(name_in="", don_amt=""):
    while name_in == "":
        name_in = input('Please provide full name (or try "list" or "menu") ')
    if name_in == 'menu':
        return False
    elif name_in == 'list':
        for donor in donors:
            print(donor)
    elif name_in not in donors:
        msg_vars = new_donor(name_in, don_amt)
        print_format_msg(msg_vars)
        return msg_vars
    else:
        msg_vars = update_don(name_in, don_amt)
        print_format_msg(msg_vars)
        return msg_vars


def get_key(item):
    return item[1]


def menu_sel_2():
    db = []
    print('{:<20}| {:^15}| {:^10}| {:>12}'.format('Donor Name',
          'Total Given', 'Num Gifts', 'Avg Gift'))
    print('-'*63)
    s = '{:<20} ${:>15}  {:^10} ${:>12.2f}'
    for donor in (donors):
        amt = sum(donors[donor])
        count = len(donors[donor])
        avg = amt/count
        db.append([donor, amt, count, avg])
    db_sort = sorted(db, key=get_key, reverse=True)
    # prints donor's name, amount, count, average sorted by amount
    for i in range(len(db_sort)):
        print(s.format(db_sort[i][0], db_sort[i][1], db_sort[i][2],
                       db_sort[i][3]))


def menu_sel_3():
    date = datetime.datetime.now()
    for donor in donors:
        file_name = '{}_{}_{}_{}.txt'.format(donor, date.month, date.day,
                                             date.year)
        msg_vars = (donor, len(donors[donor]), sum(donors[donor]))
        with open(file_name, 'w') as new_file:
            new_file.write(msg.format(*msg_vars))


menu_switch_dict = {
    '1': menu_sel_1,
    'send a thank you': menu_sel_1,
    '2': menu_sel_2,
    'create a report': menu_sel_2,
    '3': menu_sel_3,
    'send letters to everyone': menu_sel_3
    }


if __name__ == "__main__":
    while True:
        sel = input("""\nWhat do you want to do? (select from below options)\
            \n\t(1) send a thank you\
            \n\t(2) create a report\
            \n\t(3) send letters to everyone\
            \n\t(4) quit\n""")
        if sel in ('4', 'quit'):
            break
        try:
            menu_switch_dict[sel]()
        except KeyError:
            print("invalid selection, please try again")
            continue

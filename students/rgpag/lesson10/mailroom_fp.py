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


def challenge(factor, min_donation=0, max_donation=None, donor_dict=donors):
    challenge_donors = {}
    for donor in donor_dict:
        if max_donation is None:
            filt_list = list(filter(lambda x: x >= min_donation, donor_dict[donor]))
        else:
            filt_list = list(filter(lambda x: x >= min_donation and x <= max_donation,
                             donor_dict[donor]))
        challenge_donors[donor] = list(map(lambda x: x*factor, filt_list))
    return challenge_donors


def donors_sum(donor_dict=donors):
    total = 0
    for donor in donors:
        total += sum(donor_dict[donor])
    return total


def challenge_demo():
    factor_in = int(input('What is the challenge factor?'))
    min_in = int(input('What is the min_donation?'))
    max_in = input('What is the max_donation?')
    if max_in == 'None':
        max_in = None
    else:
        max_in = int(max_in)
    demo = challenge(factor_in, min_in, max_in)
    print('\n', 'Matching contribution amount: ', donors_sum(demo))


def thank_you(name_in="", don_amt=""):
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


def report():
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
    db_sort = sorted(db, key=lambda x: x[1], reverse=True)
    # prints donor's name, amount, count, average sorted by amount
    for i in range(len(db_sort)):
        print(s.format(db_sort[i][0], db_sort[i][1], db_sort[i][2],
                       db_sort[i][3]))


def send_letters():
    date = datetime.datetime.now()
    for donor in donors:
        file_name = '{}_{}_{}_{}.txt'.format(donor, date.month, date.day,
                                             date.year)
        msg_vars = (donor, len(donors[donor]), sum(donors[donor]))
        with open(file_name, 'w') as new_file:
            new_file.write(msg.format(*msg_vars))


menu_switch_dict = {
    '1': thank_you,
    'send a thank you': thank_you,
    '2': report,
    'create a report': report,
    '3': send_letters,
    'send letters to everyone': send_letters,
    '4': challenge_demo,
    'challenge demo': challenge_demo
    }


if __name__ == "__main__":
    while True:
        sel = input("""\nWhat do you want to do? (select from below options)\
            \n\t(1) send a thank you\
            \n\t(2) create a report\
            \n\t(3) send letters to everyone\
            \n\t(4) challenge demo\
            \n\t(5) quit\n""")
        if sel in ('5', 'quit'):
            break
        try:
            menu_switch_dict[sel]()
        except KeyError:
            print("invalid selection, please try again")
            continue

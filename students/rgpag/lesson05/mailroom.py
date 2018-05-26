#!/usr/bin/env python3
import datetime

# initialize donor dictionary
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


def new_donor(new_name):
    don_amt = int(input('What was the donation amount?'))
    donors[new_name] = [don_amt]
    return new_name, 1, don_amt


def update_don(ret_don):
    don_amt = int(input('What was the donation amount?'))
    donors[ret_don].append(don_amt)
    count = len(donors[ret_don])
    total_amt = sum(donors[ret_don])
    return ret_don, count, total_amt


def get_key(item):
    return item[1]


def menu_sel_1():
    name = input('Please provide full name ')
    if name == 'quit':
        q = 1
        return q
    elif name == 'list':
        for z in donors:
            print(z)
    elif name not in donors:
        msg_vars = new_donor(name)
        print(msg.format(*msg_vars))
    else:
        msg_vars = update_don(name)
        print(msg.format(*msg_vars))


def menu_sel_2():
    db = []
    print('{:<20}| {:^15}| {:^10}| {:>12}'.format('Donor Name',
          'Total Given', 'Num Gifts', 'Avg Gift'))
    print('-'*63)
    s = '{:<20} ${:>15}  {:^10} ${:>12.2f}'
    for x in (donors):
        amt = sum(donors[x])
        count = len(donors[x])
        avg = amt/count
        db.append([x, amt, count, avg])
    db_sort = sorted(db, key=get_key, reverse=True)
    for i in range(len(db_sort)):
        print(s.format(db_sort[i][0], db_sort[i][1], db_sort[i][2],
                       db_sort[i][3]))


def menu_sel_3():
    y = datetime.datetime.now()
    for i in donors:
        file_name = '{}_{}_{}_{}.txt'.format(i, y.month, y.day, y.year)
        new_file = open(file_name, 'w')
        msg_vars = (i, len(donors[i]), sum(donors[i]))
        new_file.write(msg.format(*msg_vars))
        new_file.close()


menu_switch_dict = {
    '1': menu_sel_1,
    'send a thank you': menu_sel_1,
    '2': menu_sel_2,
    'create a report': menu_sel_2,
    '3': menu_sel_3,
    'send letters to everyone': menu_sel_3}


if __name__ == "__main__":
    q = 0
    while q == 0:
        sel = input('\nWhat do you want to do?\n\t(1) send a thank you\n\t\
(2) create a report\n\t(3) send letters to everyone\n\t(4) quit\n')
        if sel in ('4', 'quit'):
            break
        menu_switch_dict[sel]()

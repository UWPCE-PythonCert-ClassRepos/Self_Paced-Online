#!/usr/bin/env python3
# initialize lists
import datetime

donors = ['Jeff Bezos', 'Mark Zuckerberg', 'Bill Gates', 'Paul Allen']
i_amount = [3000, 20, 40607, 65]
i_count = [4, 2, 3, 6]
quit = 0

# initialize amt_dict
amt_dict = {}
cnt_dict = {}
avg_dict = {}
i = 0
for i in range(len(donors)):
    amt_dict[donors[i]] = i_amount[i]
    cnt_dict[donors[i]] = i_count[i]
    avg_dict[donors[i]] = i_amount[i]/i_count[i]


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
    donors.append(new_name)
    don_amt = int(input('What was the donation amount?'))
    amt_dict[new_name] = don_amt
    cnt_dict[new_name] = 1
    avg_dict[new_name] = don_amt/1
    return new_name, 1, don_amt


def update_don(ret_don):
    don_amt = int(input('What was the donation amount?'))
    if don_amt == 0:
        return ret_don, cnt_dict[ret_don], amt_dict[ret_don]
    cnt_dict[ret_don] += 1
    amt_dict[ret_don] += don_amt
    avg_dict[ret_don] = amt_dict[ret_don]/cnt_dict[ret_don]
    return ret_don, cnt_dict[ret_don], amt_dict[ret_don]


def getKey(item):
    return item[1]


def menu_sel_1():
    name = input('Please provide full name ')
    if name == 'quit':
        quit = 1
        return quit
    elif name == 'list':
        for z in donors:
            print(z)
    elif name not in (donors):
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
        db.append([x, amt_dict[x], cnt_dict[x], avg_dict[x]])
    db_sort = sorted(db, key=getKey, reverse=True)
    for i in range(len(db_sort)):
        print(s.format(db_sort[i][0], db_sort[i][1], db_sort[i][2],
                       db_sort[i][3]))


def menu_sel_3():
    y = datetime.datetime.now()
    for i in range(len(donors)):
        don_name = donors[i]
        file_name = '{}_{}_{}_{}.txt'.format(don_name, y.month, y.day, y.year)
        new_file = open(file_name, 'w')
        msg_vars = (don_name, cnt_dict[don_name], amt_dict[don_name])
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
    while quit == 0:
        sel = input('\nWhat do you want to do?\n\t(1) send a thank you\n\t\
(2) create a report\n\t(3) send letters to everyone\n\t(4) quit\n')
        if sel in ('4', 'quit'):
            break
        menu_switch_dict[sel]()

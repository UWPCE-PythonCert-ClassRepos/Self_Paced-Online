# init lists
donors = ['Mike', 'Joe', 'Kyle', 'Nick', 'Sid']
i_amount = [3000, 20, 40607, 65, 400]
i_count = [4, 2, 3, 6, 7]
msg = """
\nDearest {},\n\nThank you for your most recent donation, did you \
realize you have now made {} lifetime donations? Wow, look at you all star! \
We are most grateful for your total donation amount of ${}.\n\nI will \
personally ensure these gifts are put soley towards purchase of yummy \
donuts! Also, any additional contributions you make in the next 24 hours \
will be matched up to $1000. What a deal! Don't delay.\n\nHumbly yours,\n
Dime for Donuts\n
"""


def new_donor(new_name):
    donors.append(new_name)
    don_amt = int(input('What was the donation amount?'))
    i_amount.append(don_amt)
    i_count.append(1)
    return donors[-1], i_count[-1], i_amount[-1]


def update_don(ret_don):
    i = donors.index(ret_don)
    don_amt = int(input('What was the donation amount?'))
    if don_amt == 0:
        return donors[i], i_count[i], i_amount[i]
    i_amount[i] += don_amt
    i_count[i] += 1
    return donors[i], i_count[i], i_amount[i]


def getKey(item):
    return item[1]


if __name__ == "__main__":
    def mailRoom():
        while 1 == 1:
            sel = input('What do you want to do: (1)"send a thank you",'
                        + '(2)"create a report", (3)"quit"? ')
            # (1)send thank you
            if sel in ('1', 'send a thank you'):
                name = input('Please provide full name ')
                if name == 'quit':
                    break
                elif name == 'list':
                    print(donors)
                    continue
                elif name not in (donors):
                    msg_vars = new_donor(name)
                else:
                    msg_vars = update_don(name)

                print(msg.format(*msg_vars))
                continue

            # (2) create a report
            elif sel in('2', 'create a report'):
                db = []
                print('{:<20}| {:^15}| {:^10}| {:>12}'.format('Donor Name',
                      'Total Given', 'Num Gifts', 'Avg Gift'))
                print('-'*63)
                s = '{:<20} ${:>15}  {:^10} ${:>12.2f}'
                for i in range(len(donors)):
                    avg_don = i_amount[i]/i_count[i]
                    db.append([donors[i], i_amount[i], i_count[i], avg_don])
                db_sort = sorted(db, key=getKey, reverse=True)
                for i in range(len(db_sort)):
                    print(s.format(db_sort[i][0], db_sort[i][1], db_sort[i][2],
                                   db_sort[i][3]))

            # (3) quit
            elif sel in ('3', 'quit'):
                break

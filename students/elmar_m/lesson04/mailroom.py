#!/usr/bin/env python3

'''
file: mailroom.py
elmar_m / 22e88@mailbox.org
Lesson04: Mailroom Exercise Part 2
'''

donors = {
    'bill' : [2000, 7.5, 950000],
    'steve' : [5.5, 234000, 928],
    'donald' : [657, 234, 28.57, 90456],
    'angie' : [2, 99, 297765, 47, 28346],
    'kim' : [38982, 66.23, 9856, 0.1],
    }
 

opts = '> Options: q == quit | t == thankyou | r == report'


def mail(n, m):
    '''
    Create mail text.
    '''
    print('Dear {}, thank you very much for your donation of {} dollars.\n'.format(n, m))


def thankyou():
    '''
    Show list of known donors, add new donor to list, 
    add new donation to donor and print letter of thanks.
    '''
    name = None
    while name != 'x':
        print('>> give me a donor name, or type "l" to see a list. Type "x" to exit.')
        name = input('>> ')
        if name == 'l':
            print(' '.join(donors.keys()))
        elif name == 'x':
            break
        elif name in donors.keys():
            print('>>', name, 'already in list')
            donation = input('>> please add current donation:\n>> ')
            donors[name].append(int(donation))
            print('>>', donation, 'added to donation list of', name, 'thank you.\n')
            mail(name, donation)
        elif not name in donors.keys():
            print('>>', name, 'not in list, adding it ')
            donors[name] = [] 
            donation = input('>> please add current donation:\n>> ')
            donors[name].append(int(donation))
            print('>>', donation, 'added to donation list of', name, 'thank you.\n')
            mail(name, donation)
    print(opts)


def report():
    '''
    Show an overview of current donors and donations
    '''
    # get the highest number of digits to create formatstring accordingly:
    sumlist = []
    for i in donors.keys():
        sumlist.append(sum(donors[i]))
    maxn = len(str(max(sumlist)))
    maxn += 2

    fstring = '{:<20} ' + '|' + '{:>' + str(maxn) + '} ' + '|' + '{:>9}' + '|' + '{:>20}' 
    print(fstring.format('Donor Name', 'Total', 'Num Gifts', 'Average Gift'))  
    print('-' * (maxn + 54)) 
    for i in donors.keys():
        print(fstring.format(i, sum(donors[i]), len(donors[i]),  sum(donors[i])//len(donors[i]) )) 
    print(opts)


def main():
    answer = None
    print(opts)
    while answer != 'q':
        answer = input('> ')
        if answer == 't':
            thankyou()
        elif answer == 'r':
            report()
        

if __name__ == '__main__':
    main()

#!/usr/bin/env python3

'''
file: mailroom.py
elmar_m / 22e88@mailbox.org
Lesson03: Mailroom Exercise Part 1
'''

donors = {
    'bill' : [2000, 7.5, 950000],
    'steve' : [5.5, 234000, 928],
    'donald' : [657, 234, 28.57, 90456],
    'angie' : [2, 99, 297765, 47, 28346],
    'kim' : [38982, 66.23, 9856, 0.1],
    }
 
def mail(n, m):
    # return('Dear', n, 'thank you very much for your donation of', m, 'dollars')
    print('Dear {}, thank you very much for your donation of {} dollars.'.format(n, m))

def thankyou():
    name = None
    while name != 'x':
        print('>> give me a donor name, or type "l" to see a list. Type "x" to exit.')
        name = input('>> ')
        if name == 'l':
            print(' '.join(donors.keys()))
        elif name == 'x':
            break
        elif name in donors.keys():
            # print('>>', name, 'donated:', donors[name])
            print('>>', name, 'already in list')
            # donors[name].append('10')
            donation = input('>> please add current donation:\n>> ')
            donors[name].append(int(donation))
            print('>>', donation, 'added to donation list of', name, 'thank you.\n')
            mail(name, donation)
        elif not name in donors.keys():
            print('>>', name, 'not in list, adding it ')
            donors[name] = [] 
            

def report():
    print('>> generating report...')
    print('>> donors so far:', ' '.join(donors.keys()))

    print('Donor Name   | Total Given   | Num Gifts | Average Gift')

    # get the highest number:
    sumlist = []
    for i in donors.keys():
        sumlist.append(sum(donors[i]))
    maxn = len(str(max(sumlist)))
    maxn += 2
    print('maxwert', maxn)

    # fstring = '{:<20} {:=$20} {:>' + str(dcount) + '.2f}'
    # fstring = '{:<20} $ {:=20} {:>20} {:=20}'
    # fstring = '{} ' + '{:>' + str(maxn) + '} ' + '{:>5} {:>20}' #  not OK
    # fstring = '{:<20} ' + '{:>' + str(maxn) + '} ' + '{:>9} {:>20}' # OK
    # fstring = '{:<20} ' + '|' + '{:>' + str(maxn) + '} ' + '|' + '{:>9}' + '|' + '{:>20}' # OK
    fstring = '{:<14} ' + '|' + '{:>' + str(maxn) + '} ' + '|' + '{:>9}' + '|' + '{:>' + str(maxn) + '}'
    print(fstring)
    
    # print header line:
    # print(fstring.format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift'))  # ~OK
    print(fstring.format('Donor Name', 'Total', 'Num Gifts', 'Average Gift'))  
    # print('-' * (maxn + 54)) # ~OK
    print('-' * (2 * maxn + 26))

    for i in donors.keys():
        # print('>>', i, 'donated:', donors[i])
        # print('{} $ {} {} $ {}'.format(i, sum(donors[i]), len(donors[i]),  sum(donors[i])//len(donors[i]) ))
        # print('{:<20} {:=$20} {:>20} {:=20}'.format(i, sum(donors[i]), len(donors[i]),  sum(donors[i])//len(donors[i]) ))     # fail
        # print('{:<20} $ {:=20} {:>20} {:=20}'.format(i, sum(donors[i]), len(donors[i]),  sum(donors[i])//len(donors[i]) )) # OK
        print(fstring.format(i, sum(donors[i]), len(donors[i]),  sum(donors[i])//len(donors[i]) )) 


def main():
    answer = None
    print(
        'options: 1 == quit | 2 == thankyou | 3 == report'
        )
        
    while answer != 'quit' and answer != '1':
        answer = input('> ')

        if answer == 'thankyou' or answer == '2':
            thankyou()
        elif answer == 'report' or answer == '3':
            report()
        
        


if __name__ == '__main__':
    main()

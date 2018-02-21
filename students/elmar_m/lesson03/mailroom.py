#!/usr/bin/env python3

'''
file: mailroom.py
elmar_m / 22e88@mailbox.org
Lesson03: Mailroom Exercise Part 1
'''

donors = {
    'bill' : ['2000', '7.5', '950000'],
    'steve' : ['5.5', '234000', '928'],
    'donald' : ['657', '234', '28.57', '90456'],
    'angie' : ['2', '99', '297765', '47', '28346'],
    'kim' : ['38982', '66.23', '9856', '0.1'],
    }



def thankyou():
    name = None
    while name != 'x':
        print('>> give me a donor name, or type "l" to see a list. Type "x" to exit.')
        name = input('>> ')
        if name == 'l':
            print(' '.join(donors.keys()))
        elif name in donors.keys():
            # print('>>', name, 'donated:', donors[name])
            print('>>', name, 'already in list, please add current donation: ')
        elif not name in donors.keys():
            print('>>', name, 'not in list, adding it ')
            


def report():
    print('>> generating report...')
    print('>> donors so far:', ' '.join(donors.keys()))
    for i in donors.keys():
        print('>>', i, 'donated:', donors[i])


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

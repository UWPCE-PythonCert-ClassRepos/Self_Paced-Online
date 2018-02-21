#!/usr/bin/env python3

'''
file: mailroom.py
elmar_m / 22e88@mailbox.org
Lesson03: Mailroom Exercise Part 1
'''

def thankyou():
    print('thanks...')
    pass

def report():
    print('generating report...')
    pass


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

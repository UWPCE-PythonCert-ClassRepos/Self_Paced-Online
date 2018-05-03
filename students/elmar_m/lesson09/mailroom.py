#!/usr/bin/env python3

'''
file: mailroom.py
elmar_m / 22e88@mailbox.org
Lesson09: OOP mailroom program 
'''

class donor:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        self.uid = '{}_{}'.format(fname, lname) 


class donation:
    def __init__(self, asset, currency=None ):
        if currency is not None:
            self.amount = int(asset)
            self.currency = currency
        else:
            self.real_value = str(asset)
            





def main():
    print('This is executing main...\n')


if __name__ == '__main__':
    main()

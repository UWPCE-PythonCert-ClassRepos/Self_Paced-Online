#!/usr/bin/env python3

'''
file: mailroom.py
elmar_m / 22e88@mailbox.org
Lesson09: OOP mailroom program 
'''

import io

class Donor:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        self.uid = '{}_{}'.format(fname, lname) 


#class donation:
#    def __init__(self, asset, currency=None ):
#        self.amount = asset 
#        if currency is None:
#            self.currency = 'dollar'
    
            

class Collection:


    def __init__(self):
        self.db = open('./database', 'a+')

    def add(self, donor, amount):
        #with open(self.db, 'a+') as f:
        #    # f.write(str(donor + amount))
        #    f.write(donor + amount)
        #    return donor, amount
        self.db.write(donor + amount)
        return donor, amount
        

    def get(donor):
        pass

        

def main():
    print('This is executing main...\n')


if __name__ == '__main__':
    main()

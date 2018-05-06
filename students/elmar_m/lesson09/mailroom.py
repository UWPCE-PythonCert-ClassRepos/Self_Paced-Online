#!/usr/bin/env python3

'''
file: mailroom.py
elmar_m / 22e88@mailbox.org
Lesson09: OOP mailroom program 
'''

import sqlite3


class Donor:

    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        self.uid = '{}_{}'.format(fname, lname) 


class Collection:

    def __init__(self):
        self.db= sqlite3.connect('BLABLA.db')
        self.cursor = self.db.cursor()

    def _create_table(self):
        ''' Other columns like e.g. date of donation could be 
            inserted anytime without breaking the class interface
        '''
        self.cursor.execute("create table mailroom (donation_ID INTEGER PRIMARY KEY AUTOINCREMENT, donor TEXT, donation INT DEFAULT 0)")
        # self.db.close()
        return True

    def add_donor(self, donor):
        self.cursor.execute("insert into mailroom (donor) values(?)", (donor,)) 
        self.db.commit()
        # self.db.close()

    def add_donation(self, donor, amount):
        self.cursor.execute("insert into mailroom (donor, donation) values(?, ?)", (donor, amount)) 
    #    self.db.commit()
    #    self.db.close()


    def get_donations(self, donor):
        # self.cursor.execute("select * from mailroom where donor = ?", (donor,))
        self.cursor.execute("select donation from mailroom where donor = ?", (donor,))
        # self.db.close()
        return self.cursor.fetchall()

    
    def get_donors(self):
        self.cursor.execute("select donor from mailroom")
        donors = set(self.cursor.fetchall())
        # return self.cursor.fetchall()
        return donors
        


def efunc():
    return 'exiting'


def fakefunc():
    pass

def listdonors():
    db = Collection()
    for i in db.get_donors():
        print('\t{} {}'.format('Nice person:', i)) 


#sub_d= {
#    #Dispatcher dictionary submenu
#    'l' : list_donors,
#    'a' : add,
#    'x' : efunc,
#    'm' : mail,
#    }

def menu(prompt, dispatcher):
    try:
        while True:
            response = input(prompt)
            if dispatcher[response]() == 'exiting':
                break
    except KeyError:
        print('\n\tSorry, unknown option:', response, '\n')
        menu(prompt, dispatcher)


if __name__ == '__main__':

    prompt = '\
    \nPlease choose an option:\
    \n\t1: list donors\
    \n\t2: list donations of a donor\
    \n\t3: add donor and / or donation\
    \n\t4: send thankyou mail\
    \n\t5: show report\
    \n\t6: quit program\n\n'

    dispatcher = {
        '1' : listdonors,
        # '2' : listdonations,
        '2' : fakefunc,
        # '3' : add,
        '3' : fakefunc,
        # '4' : thankyou,
        '4' : fakefunc,
        # '5' : report,
        '5' : fakefunc,
        '6' : efunc,
        }

    print('\n*** Welcome to OOP mailroom. ***')
    menu(prompt, dispatcher)
    print('\n***Thanks for using OOP mailroom. Goodbye.***\n')



#!/usr/bin/env python3

'''
file: mailroom.py
elmar_m / 22e88@mailbox.org
Lesson09: OOP mailroom program 
'''

# import io

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
        self.cursor.execute("create table mailroom (donor TEXT PRIMARY KEY, donation INT)")
        # self.db.close()
        return True


    def get_donor(self, donor):
        self.cursor.execute("select * from mailroom where donor = ?", (donor,))
        # self.db.close()
        return self.cursor.fetchall()

    def add_donation(self, donor, amount):
        self.cursor.execute("insert into mailroom values(?, ?)", (donor, amount) ) 
        self.db.commit()
        self.db.close()






    #def db_lookup(x):
    #    sender_found = None     # Hilfsvariable setzen
    #    # Datenbankabfrage durchfuehren:
    #    connection = sqlite3.connect(dbname)
    #    cursor = connection.cursor()
    #    cursor.execute("select * from addresses where sender = ?", (x,))
    #    # Wenn cursor einen Inhalt hat, die Variable sender_found mit diesem Inhalt belegen:
    #    for i in cursor:
    #        sender_found = i[0]
    #    # Den Inhalt der Hilfsvariablen zurueckgeben:
    #    return sender_found
    #    connection.close()








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

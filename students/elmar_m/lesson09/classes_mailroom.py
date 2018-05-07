'''
file: classes_mailroom.py
elmar_m / 22e88@mailbox.org
Lesson09: classes for OOP mailroom program 
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
        self.db.commit()
    #    self.db.close()


    def get_donations(self, donor):
        # self.cursor.execute("select * from mailroom where donor = ?", (donor,))
        self.cursor.execute("select donation from mailroom where donor = ?", (donor,))
        # self.db.close()
        return self.cursor.fetchall()


    def get_average_donation(self, donor):
        pass


    def get_number_of_donations(self, donor):
        pass

    
    def sum_up_donations(self, donor):
        pass
    

    #def report(self):      # ?? das hier oder oben die Einzelfunktionen?
    #    pass               # ?? oder dies hier nutzt die Einzelfunktionen,
                            # welche dann nur 'intern' sind?

    #def send_mails(self):  # hier oder draussen?
    #    pass


    def get_all_donors(self):
        self.cursor.execute("select donor from mailroom")
        donors = set(self.cursor.fetchall())
        return donors
        

    def check_existence(self, donor):
        self.cursor.execute("select * from mailroom where donor = ?", (donor,))
        if self.cursor.fetchall():
            return True
        else:
            return None


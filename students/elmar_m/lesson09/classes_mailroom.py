'''
file: classes_mailroom.py
elmar_m / 22e88@mailbox.org
Lesson09: classes for OOP mailroom program 
'''

import sqlite3, time

class Donor:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        self.uid = '{}_{}'.format(fname, lname) 


class Collection:
    def __init__(self):
        self.db= sqlite3.connect('BLABLA.db')
        self.cursor = self.db.cursor()
        self.cursor.execute('''create table if not exists mailroom
                     (donation_ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                    date TEXT, donor TEXT, donation INT DEFAULT 0)''')


    #def add_donor(self, donor):
    #    #if self.cursor.execute('insert into mailroom (donor) values(?)', (donor,)):
    #    #    self.db.commit()
    #    #    return True
    #    #else:
    #    #    return None
    #    # self.db.close()
    #    self.cursor.execute('insert into mailroom (donor) values(?)', (donor,))
    #    self.db.commit()


    def add_donation(self, donor, amount):
        ts = time.strftime('%Y%m%d-%H%M%S')
        try: 
            self.cursor.execute('insert into mailroom (date, donor, donation) values(?, ?, ?)', (ts, donor, amount)) 
            self.db.commit()
            return True
        except sqlite3.Error as e:
            print('Exception raised: {}'.format(e))
        finally:
            self.db.close()


    def get_donations(self, donor):
        self.cursor.execute('select date, donation from mailroom where donor = ?', (donor,))
        # self.db.close()
        return self.cursor.fetchall()


    def get_average_donation(self, donor):
        self.cursor.execute('select donation from mailroom where donor = ?', (donor,))
        num = self.get_number_of_donations(donor)
        res = self.cursor.fetchall()
        dlist = [x[0] for x in res]
        total = sum(dlist) 
        avg = total / num
        return avg
        

    def get_number_of_donations(self, donor):
        self.cursor.execute('select * from mailroom where donor = ?', (donor,))
        num = self.cursor.fetchall()
        return len(num)

    
    def sum_donations(self, donor):
        pass
    

    #def report(self):      # ?? das hier oder oben die Einzelfunktionen?
    #    pass               # ?? oder dies hier nutzt die Einzelfunktionen,
                            # welche dann nur 'intern' sind?

    #def send_mails(self):  # hier oder draussen?
    #    pass


    def get_all_donors(self):
        self.cursor.execute('select donor from mailroom')
        donors = set(self.cursor.fetchall())
        return donors
        


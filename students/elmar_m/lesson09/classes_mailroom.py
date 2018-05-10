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


# class Collection:
class Mailroom:
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


    def _get_average_donation(self, donor):
        total = self._get_donations_total(donor)
        num = self._get_number_of_donations(donor)
        avg = total / num
        # return avg
        return format(avg, '.2f')
        

    def _get_number_of_donations(self, donor):
        self.cursor.execute('select * from mailroom where donor = ?', (donor,))
        num = self.cursor.fetchall()
        return len(num)

    
    def _get_donations_total(self, donor):
        self.cursor.execute('select donation from mailroom where donor = ?', (donor,))
        res = self.cursor.fetchall()
        dlist = [x[0] for x in res]
        total = sum(dlist) 
        return total
    

    def get_all_donors(self):
        ''' fetchall liefert eine Liste von 1-Element tuples
            fetchone liefert einzelne 1-Element tuples
        '''
        self.cursor.execute('select donor from mailroom')
        raw = set(self.cursor.fetchall())    # unifying result by putting it into a set
        # donors = self._beautify(raw) 
        # return donors
        return raw


    # Currently not needed here, as it's done in the functions_mailroom.py
    #def _beautify(self, listoftuples):
    #    ''' cursor.fetchall() returns a list of tuples (in our case one-element tuples).
    #        This method changes that into a list of single items (INT, STRING, whatever). 
    #    '''
    #    resultlist = [x[0] for x in listoftuples]       
    #    return resultlist
        

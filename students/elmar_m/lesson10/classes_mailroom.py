'''
file: classes_mailroom.py
elmar_m / 22e88@mailbox.org
Lesson09: classes for OOP mailroom program 
'''

import sqlite3, time
from collections import defaultdict 

class Donor:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        self.uid = '{}_{}'.format(fname, lname) 
        self.db= sqlite3.connect('BLABLA.db')
        self.dcursor = self.db.cursor()
        self.dcursor.execute('''create table if not exists donors
                     (uid TEXT PRIMARY KEY, 
                    fname TEXT, lname TEXT, last_donation INT DEFAULT 0)''')


    def check_existence(self, uid):
        self.dcursor.execute('select * from donors where uid = ?', (uid,))
        result = self.dcursor.fetchall()
        if len(result) == 0:
            # print('====Donor / UID not found: {}'.format(uid))
            return None
        else:
            # print('====HOORAY, Donor / UID FOUND: {}'.format(uid))
            return True
        
    
    def create(self, uid, fname, lname, last_donation=None):
        # print('++++ HOORAY, in create...')
        try:
            self.dcursor.execute('''insert into donors 
                    (uid, fname, lname, last_donation)
                     values (?, ?, ?, ?)''', (uid, fname, lname, last_donation))
            self.db.commit()
            return True
        except sqlite3.Error as e:
            print('Exception raised: {}'.format(e))
            return False


    def get_last_donation(self, donor):
        try:
            self.dcursor.execute('select from donors (last_donation) where uid = ?', (donor))
            # return self._beutify(self.dcursor.fetchall())
            return self.dcursor.fetchall()
        except sqlite3.Error as e:
            print('Exception raised: {}'.format(e))
            return None
                    

class Mailroom:
    def __init__(self):
        self.db= sqlite3.connect('BLABLA.db')
        self.cursor = self.db.cursor()
        self.cursor.execute('''create table if not exists mailroom
                     (donation_ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                    date TEXT, donor TEXT, donation INT DEFAULT 0)''')


    def add_donation(self, donor, amount):
        ts = time.strftime('%Y%m%d-%H%M%S')
        try: 
            self.cursor.execute('insert into mailroom (date, donor, donation) values(?, ?, ?)', (ts, donor, amount)) 
            self.cursor.execute('update donors set last_donation = ? where uid = ?', (amount, donor)) 
            self.db.commit()
            return True
        except sqlite3.Error as e:
            print('Exception raised: {}'.format(e))


    def get_donations(self, donor):
        self.cursor.execute('select date, donation from mailroom where donor = ?', (donor,))
        return self.cursor.fetchall()


    def _get_average_donation(self, donor):
        total = self._get_donations_total(donor)
        num = self._get_number_of_donations(donor)
        avg = total / num
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
        self.cursor.execute('select donor from mailroom')
        raw = set(self.cursor.fetchall())    # unifying result by putting it into a set
        # donors = self._beautify(raw) 
        # return donors
        return raw
    

    def _preview(self, show):
        self.cursor.execute(show)
        rows = self._beautify(self.cursor.fetchall())
        print('\n\tThis operation will affect {} already existing donations'.format(rows[0]))

    
    def _preview_total(self, total): 
        self.cursor.execute(total)
        value = self._beautify(self.cursor.fetchall())
        print('\tYou have to give an additional donation of {} to pass the CHALLENGE !'.format(value[0]))


    def multiply(self, factor, above=None, below=None):
        if above is None and below is None:
            sql_show = 'select count(*) from mailroom where donation'
            sql_total = 'select sum(donation) from mailroom where donation'
            sql = 'update mailroom set donation = donation * ?'
            werte = (factor,)
        elif below:
            sql_show = 'select count(*) from mailroom where donation < ' + below
            sql_total = 'select sum(donation) from mailroom where donation < ' + below
            sql = 'update mailroom set donation = donation * ? where donation < ?'
            werte = (factor, below)
        elif above:
            sql_show = 'select count(*) from mailroom where donation > ' + above
            sql_total = 'select sum(donation) from mailroom where donation > ' + above
            sql = 'update mailroom set donation = donation * ? where donation > ?'
            werte = (factor, above)

        try:
            self._preview(sql_show)
            self._preview_total(sql_total)
            self.cursor.execute(sql, werte)
            self.db.commit()
            return True
        except sqlite3.Error as e:
            print('Exception raised 3: {}'.format(e))


    # ToDo: make more consistent usage of this function throughout the program... or omit it at all.
    def _beautify(self, listoftuples):
        ''' cursor.fetchall() returns a list of tuples (in our case mostly one-element tuples).
            This method changes that into a list of single items (INT, STRING, whatever). 
        '''
        resultlist = [x[0] for x in listoftuples]       
        return resultlist
        

    def report(self):
        donordict = defaultdict(list)
        maxn = 0
        for i in self.get_all_donors():
            person = i[0]
            total = self._get_donations_total(person)
            slen = len(str(total))
            if slen > maxn:
                maxn = slen
            num = self._get_number_of_donations(person)
            avg = self._get_average_donation(person)
            donordict[person].append(total)
            donordict[person].append(num)
            donordict[person].append(avg)
        
        maxn += 3
        fstring = '\t{:<20} ' + '|' + '{:>' + str(maxn) + '} ' + '|' + '{:>9}' + '|' + '{:>20}' 
        print(fstring.format('Donor Name', 'Total', 'Num Gifts', 'Average Gift'))  
        print('\t' + '-' * (maxn + 54)) 

        for i in donordict:
            print(fstring.format(i, donordict[i][0], donordict[i][1], donordict[i][2])) 
        
    
    def mail(self):
        with open('./MAIL_TEMPLATE', 'r') as fr:
            lines = fr.readlines()

            for name in self._beautify(self.get_all_donors()):
                ts = time.strftime('%Y%m%d-%H%M%S')
                filename = name + '_' + ts + '.txt'
    
                # donation = '500'
                self.cursor.execute('select * from donors where uid = ?', (name,))
                result = self.cursor.fetchall()
                if len(result) == 0:
                    print('====Last_donation not found: {}'.format(name))
                else:
                    # print('====Last_donation FOUND: {} {}'.format(name, result))
                    last_donation = result[0][3]
                    donation = str(last_donation)
                    # print(donation)
                    # return

                with open(filename, 'w') as fw:
                    for i in lines:
                        if 'NAME' in i:
                            new = i.replace('NAME', name)
                            fw.write(new)
                        elif 'DONATION' in i:
                            new = i.replace('DONATION', donation)
                            fw.write(new)
                        else:
                            fw.write(i)
                    print('\tMailtext for {} successfully written to {}'.format(name, filename))
                    
               


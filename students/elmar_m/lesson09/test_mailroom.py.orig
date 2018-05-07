#!/usr/bin/env python3

'''
file: test_mailroom.py
elmar_m / 22e88@mailbox.org
Lesson09: unittests for mailroom.py class
'''


import unittest 
import mailroom 

class Mailroom_Tests(unittest.TestCase):
    
    def test_Donor(self):   
        obj = mailroom.Donor('John', 'Doe')
        self.assertIs(obj.firstname, 'John')
        self.assertIs(obj.lastname, 'Doe')
        self.assertEqual(obj.uid, 'John_Doe')

    
    def test_Collection(self):

        db = mailroom.Collection()
        # db._create_table()

        db.add_donor('brathahn')
        db.add_donor('b')
        db.add_donor('kalleinz')

        db.add_donation('b', 500) 
        db.add_donation('b', 1500) 
        db.add_donation('kalleinz', 500) 
        db.add_donation('kalleinz', 1500) 
        print(db.get_donations('b'))
        print('kalleinz:', db.get_donations('kalleinz'))
        print('brathahn:', db.get_donations('brathahn'))
        # print('all donors:', db.get_donors())
        for i in db.get_all_donors():
            print('{} {}'.format('nice person:', i))
        db.check_existence('kalleinz')
        db.check_existence('gibsnich')
        




if __name__ == '__main__':
    unittest.main()


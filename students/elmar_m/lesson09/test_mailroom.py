#!/usr/bin/env python3

'''
file: test_mailroom.py
elmar_m / 22e88@mailbox.org
Lesson09: unittests for mailroom.py class
'''


import unittest 
from classes_mailroom import Collection, Donor

class Mailroom_Tests(unittest.TestCase):
    
    def test_Donor(self):   
        # obj = mailroom.Donor('John', 'Doe')
        obj = Donor('John', 'Doe')
        self.assertIs(obj.firstname, 'John')
        self.assertIs(obj.lastname, 'Doe')
        self.assertEqual(obj.uid, 'John_Doe')

    
    def test_Collection(self):
        nice_person = Donor('John', 'Doe')

        db = Collection()
        db._create_table()

        db.add_donor(nice_person.uid)
        self.assertTrue(db.check_existence('John_Doe'))
        self.assertFalse(db.check_existence('NonExisting_FakeUser'))

        self.assertTrue(db.add_donation(nice_person.uid, 8999))
        #db.add_donation('b', 500) 
        #db.add_donation('b', 1500) 
        #db.add_donation('kalleinz', 500) 
        #db.add_donation('kalleinz', 1500) 
        #print(db.get_donations('b'))
        #print('kalleinz:', db.get_donations('kalleinz'))
        #print('brathahn:', db.get_donations('brathahn'))
        ## print('all donors:', db.get_donors())
        #for i in db.get_all_donors():
        #    print('{} {}'.format('nice person:', i))
        #db.check_existence('kalleinz')
        #db.check_existence('gibsnich')
        




if __name__ == '__main__':
    unittest.main()


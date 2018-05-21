import os
import sys
import unittest
import mailroom04 as mailroom


class Mailroom04Test(unittest.TestCase):

    # Tests that donor_db looks like it should.
    def test_donor_db(self):
        donor_db = {'John Smith': [18774.48, 8264.47, 7558.71], 'Jane Doe': [281918.99, 8242.13],
                        'Alan Smithee': [181.97, 955.16], 'Tom D.A. Harry': [67.1, 500.98], 'Joe Shmoe': [200.01]}
        self.assertEqual(mailroom.donor_db, donor_db)

    # Tests that list_donors() is creating list of donor names correctly.
    def test_donor_list(self):
        donor_list = ['John Smith', 'Jane Doe', 'Alan Smithee', 'Tom D.A. Harry', 'Joe Shmoe']
        self.assertEqual(mailroom.list_donors(), donor_list)


if __name__ == '__main__':
    unittest.main()

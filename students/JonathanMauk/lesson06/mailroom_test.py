import os
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

    # Tests that donor letters are being generated with intended formatting.
    def test_letter_formatting(self):
        letter_text = '''
        Dear John Smith,
    
            Thank you for your very kind donation of $5.0, and for your continuing support.
    
            Your generous contribution will be put to very good use.
    
                           Sincerely,
                              -The Team
                              '''
        self.assertEqual(mailroom.create_letter(0, 'John Smith', 5.0), letter_text)

    # Tests that letter text files are actually created in script directory.
    def test_file_creation(self):
        mailroom.create_txt_files()
        assert os.path.isfile('John Smith.txt')

    # Tests that report is generating with expected values.
    def test_report(self):
        report = '''John Smith                | $  34597.66 |     3     | $   11532.55
Jane Doe                  | $ 290161.12 |     2     | $  145080.56
Alan Smithee              | $   1137.13 |     2     | $     568.56
Tom D.A. Harry            | $    568.08 |     2     | $     284.04
Joe Shmoe                 | $    200.01 |     1     | $     200.01\n'''
        self.assertEqual(mailroom.report_generation(), report)


if __name__ == '__main__':
    unittest.main()

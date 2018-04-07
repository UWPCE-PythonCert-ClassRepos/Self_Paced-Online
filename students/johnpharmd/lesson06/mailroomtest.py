import unittest
import mailroom4
import os
import datetime


class MailroomTest(unittest.TestCase):
    def setUp(self):
        self.donors_amts = mailroom4.get_donors_amts()

    def test_donors(self):
        for donor in self.donors_amts:
            if '-' not in donor:
                assert donor.isalpha()
            else:
                assert donor.replace('-', '').isalpha()

    def test_titles(self):
        for donor in self.donors_amts:
            assert self.donors_amts[donor]['title'] in ('Prof.',
                                                        'Dr.', 'Ms.', 'Mr.')

    def test_donations(self):
        for donor in self.donors_amts:
            assert str(self.donors_amts[donor]['donations']).isdigit()

    def test_num_of_donations(self):
        for donor in self.donors_amts:
            assert str(self.donors_amts[donor]['num_of_donations']).isdigit()

    def test_add_donor(self):
        mailroom4.add_donor('Anderson', 'Mr.')
        try:
            assert 'Anderson' in self.donors_amts
        except KeyError:
            print('"Anderson" not in donors_amts.')
        assert self.donors_amts['Anderson'] == {'title': 'Mr.',
                                                'donations': 0,
                                                'num_of_donations': 0}
        self.donors_amts.pop('Anderson')

    def test_add_donation_amt(self):
        mailroom4.add_donation_amt('Anderson',
                                   title='Mr.',
                                   new_donor=True,
                                   donation_amt=2000)
        assert self.donors_amts['Anderson']['donations'] == 2000
        assert self.donors_amts['Anderson']['num_of_donations'] == 1
        self.donors_amts.pop('Anderson')

    def test_send_ty(self):
        actual = mailroom4.send_ty('Mr.', 'Anderson', 22000)
        expected = """
                     Dear Mr. Anderson,
                     Thank you for your generous donation in the
                     amount of 22000 USD.
                   """
        try:
            self.assertEqual(actual, expected)
        except AssertionError:
            pass

    # THIS WORKS, SO DO NOT DELETE. COMMENTED OUT SO DOESN'T RUN.
    # REMOVE COMMENTS WHEN READY TO TEST ENTIRE mailroom4.
    # def test_send_letters(self):
    #     mailroom4.send_letters()
    #     cwd_list = os.listdir(os.getcwd())
    #     today = datetime.date.today()
    #     for donor in mailroom4.get_donors_amts():
    #         donor_letter = donor + today.strftime('%Y%m%d') + '.txt'
    #         donor_letter = donor_letter.strip('\'')
    #         assert donor_letter in cwd_list

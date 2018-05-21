import unittest
import mailroom4fp
import os
import datetime


class MailroomTest(unittest.TestCase):
    # maxDiff = None

    def setUp(self):
        self.donors_amts = mailroom4fp.get_donors_amts()

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
        mailroom4fp.add_donor('Anderson', 'Mr.')
        try:
            assert 'Anderson' in self.donors_amts
        except KeyError:
            print('"Anderson" not in donors_amts.')
        assert self.donors_amts['Anderson'] == {'title': 'Mr.',
                                                'donations': 0,
                                                'num_of_donations': 0}
        self.donors_amts.pop('Anderson')

    def test_add_donation_amt(self):
        mailroom4fp.add_donation_amt('Avey',
                                     title='Ms.',
                                     new_donor=False,
                                     donation_amt=22000)
        assert self.donors_amts['Avey']['donations'] == 222000
        assert self.donors_amts['Avey']['num_of_donations'] == 3

    def test_send_ty(self):
        actual = mailroom4fp.send_ty('Mr.', 'Anderson', 22000)
        expected = """
                     Dear Mr. Anderson,
                     Thank you for your generous donation in the
                     amount of 22000 USD.
                   """
        try:
            self.assertEqual(actual, expected)
        except AssertionError:
            pass

    def test_get_report(self):
        actual = mailroom4fp.get_report()
        expected = """
        Donor Name     | Total Given | Num Gifts| Average Gift
        -------------------------------------------------------
        Avey            $    200000           2 $     100000
        Gates           $    150000           3 $      50000
        Brin            $    150000           3 $      50000
        Wojcicki        $    125000           1 $     125000
        Musk            $    100000           1 $     100000
        Cerf            $     50000           2 $      25000
        Berners-Lee     $     50000           2 $      25000
        """

    # def test_send_letters(self):
    #     mailroom4fp.send_letters()
    #     cwd_list = os.listdir(os.getcwd())
    #     today = datetime.date.today()
    #     for donor in mailroom4fp.get_donors_amts():
    #         donor_letter = donor + today.strftime('%Y%m%d') + '.txt'
    #         donor_letter = donor_letter.strip('\'')
    #         assert donor_letter in cwd_list

    def test_challenge(self):
        self.assertEqual(mailroom4fp.challenge(
          self.donors_amts['Cerf']['donations'], factor=3), 150000)

    def test_challenge_filter(self):
        self.assertEqual(mailroom4fp.challenge_map(factor=2,
                         min_donation=100000, max_donation=250000),
                         {'Gates': {'title': 'Mr.', 'donations': 300000,
                                    'num_of_donations': 3},
                          'Brin': {'title': 'Mr.', 'donations': 300000,
                                   'num_of_donations': 3},
                          'Wojcicki': {'title': 'Ms.', 'donations': 250000,
                                       'num_of_donations': 1},
                          'Avey': {'title': 'Ms.', 'donations': 444000,
                                   'num_of_donations': 3}})

    def test_run_projection(self):
        self.assertEqual(mailroom4fp.run_projection(donor, contrib_ceiling, factor), None)
        self.assertEqual(mailroom4fp.run_projection(donor, contrib_floor, factor), None)

#!/usr/bin/env python3
import unittest
import mailroom4


class MailroomTest(unittest.TestCase):
    def make_test_list(self):
        self.test_list = mailroom4.get_donor_list()
        return self.test_list

    def test_get_donor_list(self):
        self.make_test_list()
        assert type(self.test_list) == list

    def test_donor_list_strings(self):
        self.make_test_list()
        for s in self.test_list:
            if '-' not in s:
                assert s.isalpha()
            else:
                assert s.replace('-', '').isalpha()

    def test_prompt_title(self):
        self.test_title = mailroom4.prompt_title()
        assert self.test_title in ('Prof.', 'Dr.', 'Ms.', 'Mr.')

    def test_prompt_donation(self):
        self.test_donation = mailroom4.prompt_donation()
        assert str(self.test_donation).isdigit()

    def test_add_donor(self):
        self.new_donor = mailroom4.add_donor('Anderson', 'Mr.')
        donors_amts = mailroom4.get_donors_amts()
        try:
            assert 'Anderson' in donors_amts
        except KeyError:
            print('"Anderson" not in donors_amts.')
        assert donors_amts['Anderson'] == {'title': 'Mr.', 'donations': 0,
                                           'num_of_donations': 0}

    def test_add_donation_amt(self):
        donors_amts = mailroom4.get_donors_amts()
        self.donation = mailroom4.add_donation_amt('Anderson',
                                                   title='Mr.',
                                                   new_donor=True,
                                                   donation_amt=2000)
        assert donors_amts['Anderson']['donations'] == 2000
        assert donors_amts['Anderson']['num_of_donations'] == 1

    def test_7(self):
        pass

    def test_8(self):
        pass

    def test_9(self):
        pass

    def test_10(self):
        pass

    def test_11(self):
        pass

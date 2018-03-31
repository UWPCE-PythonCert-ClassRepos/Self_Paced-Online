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

    def test_5(self):
        pass

    def test_6(self):
        pass

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

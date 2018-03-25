#!/usr/bin/env python3
import unittest
import mailroom4


class MailroomTest(unittest.TestCase):
    def test_get_donor_list(self, test_list):
        for s in test_list:
            assert type(s) == str

    def test_2(self):
        pass

    def test_3(self):
        pass

    def test_4(self):
        pass

    def test_5(self):
        pass


a_test = MailroomTest()
a_test.test_get_donor_list(mailroom4.get_donor_list())

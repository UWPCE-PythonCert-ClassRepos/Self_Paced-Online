import unittest
import os
import mailroom5_OO as ml5


class MyFuncTestCase(unittest.TestCase):

    def test_1_donor_settergetter(self):
        d1 = ml5.Donor("James Bond")
        expected = tuple("James Bond".split())
        actual = d1.name
        self.assertEqual(expected, actual)
        d2 = ml5.Donor()
        d2.name = "Alex Rolex"
        print(d2.name)
        expected = tuple("Alex Rolex".split())
        actual = d2.name
        self.assertEqual(expected, actual)

    def test_2_donations_settergetter(self):
        d1 = ml5.Donor("Chris Ping")
        d1.donations = 10
        d1.donations = 20
        d1.donations = 300
        expected = [10, 20, 300]
        actual = d1.donations
        self.assertEqual(expected, actual)

    def test_3_avg_total_num(self):
        d1 = ml5.Donor("Timmy Tommy")
        for i in range(10):
            d1.donations = (10 * i) + 10
        lst = [(10 * i) + 10 for i in range(10)]
        expected = sum(lst)
        actual = d1.total
        self.assertEqual(expected, actual)
        expected = sum(lst) / len(lst)
        actual = d1.average
        self.assertEqual(expected, actual)
        expected = len(lst)
        actual = d1.number
        self.assertEqual(expected, actual)

    def test_4_greetings(self):
        d1 = ml5.Donor("Stephan LeClerc")
        d1.donations = 100
        actual = d1.greetings
        expected = """
    Ex Programmers Charity
    1999 Heartbeat Avenue
    11111 Fresh Spring, Alaska

    Dear Stephan LeClerc,

    Thank you so much for your generous donation of $100

    It will be put to very good use.

                       Sincerely,
                          -The Team

    """
        self.assertEqual(expected, actual)

    def test_5_add_donor(self):
        d1 = ml5.Donor("Stephan LeClerc")
        d2 = ml5.Donor("Chris Ping")
        d3 = ml5.Donor("James Bond")
        for i in range(4):
            d1.donations, d2.donations, d3.donations = \
                                                       (10 * i) + 10, \
                                                       (10 * i+2) + 10, \
                                                       (10 * i+3) + 10
        dd = ml5.DonorsCollection()
        dd.donors = d1
        dd.donors = d2
        dd.donors = d3
        actual = [dd.donors[tuple("Stephan LeClerc".split())],
                  dd.donors[tuple("Chris Ping".split())],
                  dd.donors[tuple("James Bond".split())]]
        expected = [d1, d2, d3]
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()

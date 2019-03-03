"""Ian Sahlberg
Python210
2/13/2019
Unit Testing"""


import unittest as u
import Mailroom3 as m
from Mailroom3 import amount_append
from Mailroom3 import donate
from Mailroom3 import print_report
from Mailroom3 import quit


class tests(u.TestCase):

    """
    def test_donate(self): #Requires test input = amount below (100)
        test_dict = {'bugs mouse': [32, 5], 'mickey bunny': {678}}
        amount_donated = 100
        expected = 100
        actual = donate()
        self.assertEqual(expected,actual)
    """

    def test_amount_append(self):
        dict = {'Roberto' : []}
        name = 'Roberto'
        amount = 23.00
        expected = {name : [amount]}
        m.amount_append(name, dict, amount)
        self.assertDictEqual(expected, dict)


    def test_print_list(self):
        dict = {'Bob': 1, 'Mary': 2}
        expected = ['Bob', 'Mary']
        actual = m.print_list(dict)
        self.assertEqual(expected, actual)

    def test_email(self):
        name = 'Bibs'
        amount = 666.00
        expected = 'Thank you {} for the generous donation of $ {:.2f}. We appreciate your generosity.\n\nSincerely, \n\nThe Helping R Us Team\n\n'.format(name.title(), amount)
        actual = m.email(name, amount)
        self.assertEqual(expected, actual)

    def test_quit(self):
        actual = quit(self)
        expected = 'Until next time!'
        self.assertEqual(expected, actual)


    def test_sort_stats(self):
        dict = {'bob johnson': [150.00],
         'susan skoosan': [2000.00, 550.00]}
        expected = [('susan skoosan', [2550.00, 2, 1275.00]), ('bob johnson', [150.00, 1, 150.00])]
        actual = m.sort_and_stats_dict(dict)
        self.assertListEqual(expected, actual)

    def test_print_report(self):
        dict = {'bob johnson': [150,1,150],
             'susan skoosan': [2550,2,1275],
             'tim tam':[10.50,1,10],
             'roxanne raffle':[211,3,70],
             'jon jacob':[5005,2,2502]}
        dict_2 = sorted(list(dict.items()), key=lambda x: x[1], reverse=True)
        actual = print_report(dict_2)
        expected = """Donor Name       |      Donor Total    |  Count of Donations    |  Average of Donations
,----------------------------------------------------------------------------------------
jon jacob           $    5005.00                2                  $        2502
susan skoosan       $    2550.00                2                  $        1275
roxanne raffle      $    211.00                 3                  $          70
bob johnson         $    150.00                 1                  $         150
tim tam             $    10.50                  1                  $          10"""

        self.assertEqual(expected,str(actual).rstrip())


    def test_email_file(self):
        import datetime as dt
        dict = ({'Haggus': [4.00]})
        expected = 'Thank you Haggus for the generous donation of $ 4.00. We appreciate your generosity.Sincerely, The Helping R Us Team'
        a = m.email_file(dict)
        with open ('Haggus_{}.txt'.format(dt.date.today()), 'r') as file:
            x = file.read()
            actual = "".join(x.splitlines())
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    u.main()

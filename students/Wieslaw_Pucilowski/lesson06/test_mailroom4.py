import unittest
import os
import mailroom4 as mlr



class MyFuncTestCase(unittest.TestCase):
    def test_1_select_user(self):
        test_user = ('Haruto', 'Asai')
        expected = {'first_name': test_user[0], 'last_name': test_user[1],
                    'donations': len(mlr.dict_all[test_user]),
                    'total': sum(mlr.dict_all[test_user])}
        actual = mlr.select_user('Haruto', 'Asai')
        self.assertEqual(expected, actual)

    def test_2_all_users(self):
        for test_user in mlr.dict_all:
            expected = {'first_name': test_user[0], 'last_name': test_user[1],
                        'donations': len(mlr.dict_all[test_user]),
                        'total': sum(mlr.dict_all[test_user])}
            actual = mlr.select_user(* test_user)
            self.assertEqual(expected, actual)

    def test_3_write_letter(self):
        for test_user in mlr.dict_all:
            mlr.write_letter(test_user[0], test_user[1])
            assert os.path.isfile(test_user[0]+'_'+test_user[1]+'.txt')

    def test_4_donor_greeting(self):
        for first, last in mlr.dict_all:
            expected = """
    Ex Programmers Charity
    1999 Heartbeat Avenue
    11111 Fresh Spring, Alaska

    Dear {first_name} {last_name},

    Thank you so much for your generous donation of ${total}

    It will be put to very good use.

                       Sincerely,
                          -The Team

    """.format(**mlr.select_user(first, last))
            actual = mlr.donor_greeting(first, last)
            self.assertEqual(expected, actual)

    def test_5_create_report(self):
        expected = """Donor Name                    | Total Given       | Num Gifts| Average Gift      
--------------------------------------------------------------------------------
Alvaro Speedy                  $           1280.50          3 $           426.83
Andreas Bolen                  $           1220.00          2 $           610.00
Ivan Smirnoff                  $           1200.00          1 $          1200.00
Haruto Asai                    $           1042.50          2 $           521.25
Ilunga Mulungma                $            900.00          2 $           450.00
Karl Marx                      $            485.40          2 $           242.70
Richard Lionheart              $            366.80          3 $           122.27
Denis Donuts                   $             68.00          1 $            68.00
Great Gatsby                   $              0.50          1 $             0.50
"""
        actual = mlr.create_report()
        self.assertEqual(expected, actual)

    def test_6_add_donor_dict(self):
        mlr.add_donor_dict('Johny', 'Holiday', 10)
        mlr.add_donor_dict('Johny', 'Holiday', 30.55)
        expected = [10, 30.55]
        actual = mlr.dict_all[('Johny', 'Holiday')]
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()

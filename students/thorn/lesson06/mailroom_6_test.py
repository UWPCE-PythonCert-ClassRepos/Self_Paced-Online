import unittest
import mailroom_6

# TODO: mocks

class mailroom_6_unit_test(unittest.TestCase):
    ''' Sets up test information. '''
    donors = {
    'Tom Horn': [599.23, 1000.00],
    'Theo Hartwell': [0.01, 0.01, 0.1],
    'Bailey Kimmitt': [8723.22, 27167.22, 91817.66],
    'Paul Hubbell': [90012.32, 2312.24],
    'David Beckham': [1817266.11, 123123.66, 111335.112]
    }   
    
    sorted_donors = [   
    #   Unrounded -> rounding occurs in string formatting
        ['David Beckham', 2051724.882, 3, 683908.294], 
        ['Bailey Kimmitt', 127708.1, 3, 42569.36666666667], 
        ['Paul Hubbell', 92324.56000000001, 2, 46162.280000000006], 
        ['Tom Horn', 1599.23, 2, 799.615],
        ['Theo Hartwell', 0.12000000000000001, 3, 0.04]
    ]

#     formatted_report = (
# """
# Donor:                    | $    Total     |   Donations   | $   Average   |
# ----------------------------------------------------------------------------
# David Beckham             | $  2,051,724.88|              3| $   683,908.29
# Bailey Kimmitt            | $    127,708.10|              3| $    42,569.37
# Paul Hubbell              | $     92,324.56|              2| $    46,162.28
# Tom Horn                  | $      1,599.23|              2| $       799.62
# Theo Hartwell             | $          0.12|              3| $         0.04""")

    def test_get_donor_names(self):
        ''' Gets the list of donor names. Original list should be the same as the unmodified main program. '''
        self.assertEqual(mailroom_6.get_donor_names(), self.donors.keys())

    def test_get_donor_totals(self):
        ''' Assert the totals are working as intended. '''
        self.assertEqual(mailroom_6.get_donor_totals('Tom Horn'), 1599.23)

    def test_create_report_lines(self):
        ''' Returns sorted list of the original donors dictionary that matches above.  Not a great test -> doesn't account for rounding in the final product. '''
        self.assertEqual(mailroom_6.create_report_lines(), self.sorted_donors)

    def test_create_report(self):
        ''' Compares a line in the report to make sure they're formatted correctly. '''
        becks_line = 'David Beckham             | $  2,051,724.88|              3| $   683,908.29'
        report = mailroom_6.create_report().split('\n')
        self.assertEqual(report[2], becks_line)


if __name__ == '__main__':
    unittest.main()
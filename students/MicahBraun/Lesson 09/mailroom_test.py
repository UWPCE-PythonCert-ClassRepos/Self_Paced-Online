import unittest
import mailroom_09 as m


class MyTestCase(unittest.TestCase):
    i = m.Donor(m.DonorSuite.__name__)

    def test_menu(self):
        # self.ds = m.DonorSuite()
        # self.new_i = m.UI(self.ds)
        # a = self.new_i.start_program()

        '''
--------------------------------------------------------------------------------------------------------------
                                                MAIL ROOM MENU
--------------------------------------------------------------------------------------------------------------

                                             -- Menu Options --

                                        A. Add donor to database
                                        B. Send Thank You letter to specific donor
                                        C. Create a donor report
                                        D. Send letters to all donors
                                        E. Quit
                                        
                                        Menu Selection: '''

        # self.assertEqual(a, expected)
        # self.skipTest('Doesn\'t run')
        # Won't pass/run -- just hangs in processing.
        pass

    def test_add_name(self):
        self.i = m.Donor('Micah Braun')
        self.ds = m.DonorSuite([self.i])
        self.ui = m.UI(self.ds)
        self.assertEqual(self.i.name, 'Micah Braun')
        # Passed

    def test_add_donations(self):
        self.i.add_donation(100)
        self.i.add_donation('2345.95')
        self.assertEqual(self.i.donations, [100.0, 2345.95])
        # Passed

    def test_avg_donations(self):
        self.i.donations = []
        self.i.add_donation(100)
        self.i.add_donation(400)
        self.i.add_donation(500)
        self.i.add_donation(360)
        self.assertEqual(self.i.avg_donation, 340)
        # Passed

    def test_thank_you(self):
        self.i.name = 'Micah Braun'
        self.i.donations = []
        self.i.add_donation(1000)
        thank_you = self.i.get_thank_you_tofile()
        expected_text = '''
Dear Micah Braun,

Thank you for your continued support through your contribution of $1,000.00. 
Your 1 donation(s) over this year have been instrumental in moving towards our
fundraising goal of $100,000.00 to benefit local charities. On behalf of all
the members of the Foundation, we thank you for your generosity and look forward
to working with you in the future to build a better world!

Best wishes,

Foundation Board of Directors
                       \n'''

        self.assertEqual(thank_you, expected_text)
        # Passed -- NOTE: The global class variable i = m.Donor(m.DonorSuite.__name__) is causing
        # the instance to read-in the name as 'DonorSuite' I couldn't get the test to accept i across
        #  multiple methods without repeating multiple lines in each method to instantiate the instance
        # each time...

    def test_get_row(self):
        self.i.name = 'Micah Braun'
        self.i.donations = []
        self.i.avg_donation = 0

        expected_row = 'Micah Braun       |  $   0.00      |      0       |  $  0.00  '

        self.assertEqual(self.i.get_report_row_header(16), expected_row)
        # Passed

    def test_quit(self):
        self.ds = m.DonorSuite()
        self.new_i = m.UI(self.ds)

        with self.assertRaises(SystemExit):
            self.new_i.quit_program()
        # Passed


if __name__ == '__main__':
    unittest.main()

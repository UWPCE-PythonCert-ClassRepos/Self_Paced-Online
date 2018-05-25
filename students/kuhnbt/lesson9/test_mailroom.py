import unittest
import ui_classes as mr

class mailroomTest(unittest.TestCase):

    def setUp(self):
        self.d = mr.Donor('Dave Kusuda')
        self.collection = mr.DonorCollection([self.d])
        self.ui = mr.UserInteraction(self.collection)

    def test_donor(self):
        self.assertEqual(self.d.name, 'Dave Kusuda')

    def test_add_donation(self):
        self.d.add_donation(20)
        self.d.add_donation('40')
        self.assertEqual(self.d.donations, [20.0, 40.0])
        self.d.add_donation([30, 60])
        self.assertEqual(self.d.donations, [20.0, 40.0, 30.0, 60.0])

    def test_average_donation(self):
        self.d.donations = []
        self.d.add_donation(15)
        self.d.add_donation(60)
        self.assertEqual(self.d.average_donation, 37.5)

    def test_donorcollection(self):
        self.assertEqual(self.collection.donors[0].name, self.d.name)

    def test_collection_types(self):
        with self.assertRaises(TypeError):
            self.collection.add_donor('Jeff Reynolds')

    def test_get_thank_you(self):
        self.d.donations = []
        self.d.add_donation(100)
        thank_you = self.d.get_thank_you()

        expected_text = 'Dear Dave Kusuda:\nThank you for your'\
            ' generous donation of $100.00.\nI really appreciate your '\
            '1\ndonation to our organization.\nI assure you that your'\
            ' contributions will be put to\ngood use!\n\nRegards,\nBen'
        self.assertEqual(thank_you, expected_text)

    def test_get_thank_you_multiple(self):
        self.d.donations = []
        self.d.add_donation([100, 200])
        thank_you = self.d.get_thank_you()

        expected_text = 'Dear Dave Kusuda:\nThank you for your'\
            ' generous donation of $200.00.\nI really appreciate your '\
            '2\ndonations to our organization.\nI assure you that your'\
            ' contributions will be put to\ngood use!\n\nRegards,\nBen'
        self.assertEqual(thank_you, expected_text)

    def test_report_header(self):
        expected_header = 'Donor Name      |Total Given |Num Gifts '\
                          '|Average Gift'
        self.assertEqual(self.ui.get_report_header(16),
                         expected_header)

    def test_report_row(self):
        expected_row = 'Dave Kusuda     |$   0.00    |    0     '\
                       '|$  0.00  '
        self.assertEqual(self.d.get_report_row(16), expected_row)

    def test_exit(self):
        with self.assertRaises(SystemExit):
            self.ui.quit_program()

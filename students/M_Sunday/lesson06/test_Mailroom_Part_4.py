#!usr/bin/python
import Mailroom_Part_4
import unittest
from mock import patch
import io
from operator import itemgetter
import os


class TestMailroom(unittest.TestCase):

    donor_data = {'John Marks': [5000.34, 2500, 1267],
                  'Matt Smith': [750],
                  'Kelsey Rodgers': [55.76],
                  'John Williams': [500, 1898],
                  'Morgan Stanley': [12000.98, 8670],
                  'Roger Johnson': [264, 942.23],
                  'Sherry Wilson': [4000, 2324.1, 1352],
                  'Alex Grant': [8739, 4312]}

    def test_get_menu_option(self):
        with patch('builtins.input', return_value='1'):
            self.assertEqual(Mailroom_Part_4.get_menu_option(), "1")
        with patch('builtins.input', return_value='olikujyh'):
            self.assertEqual(Mailroom_Part_4.get_menu_option(), "olikujyh")

    def test_menu_display(self):
        with patch('builtins.input', return_value='1'):
            self.assertEqual(Mailroom_Part_4.menu_display(), "1")
        with patch('builtins.input', return_value='2'):
            self.assertEqual(Mailroom_Part_4.menu_display(), "2")
        with patch('builtins.input', return_value='3'):
            self.assertEqual(Mailroom_Part_4.menu_display(), "3")
        with patch('builtins.input', return_value='4'):
            self.assertEqual(Mailroom_Part_4.menu_display(), "4")
        with patch('builtins.input', return_value='sadwertdfhgfd'):
            self.assertEqual(Mailroom_Part_4.menu_display(), "sadwertdfhgfd")

    def test_list_display(self):
        self.assertEqual(Mailroom_Part_4.list_display(), None)
        #expect = "---- List of all Donors ----" \
        #         "- John Marks" \
        #         "- Matt Smith" \
        #         "- Kelsey Rodgers" \
        #         "- John Williams" \
        #         "- Morgan Stanley" \
        #         "- Roger Johnson" \
        #         "- Sherry Wilson" \
        #         "- Alex Grant" \
        #         "----------------------------"
        #Mailroom_Part_4.list_display()
        #self.text_ = io.StringIO()
        #self.assertEqual(self.text_, expect)

    def test_list_details(self):
        self.assertEqual(Mailroom_Part_4.list_details([]), None)

        self.data2 = [["UW Student1", 1, 1000, 1000], ["UW Student2", 2, 2500, 1250]]
        header = "\n{:<18}| {:<12}| {:<10}| {:<12}".format("Donor Name", "Total "
                                                                         "Given", "Num Gifts",
                                                           "Average Gift")
        buffer = "------------------------------------------------------------------"
        print(header, buffer)
        for item in sorted(self.data2, key=itemgetter(-2), reverse=True):
            print("{:<18} $  {:>9.2f}  {:>10}  $   {:>9.2f}".format(item[0], item[2], item[1], item[3]))
        self.expected = io.StringIO()
        Mailroom_Part_4.list_details(self.data2)
        self.actual = io.StringIO()
        self.assertEqual(self.actual.getvalue(), self.expected.getvalue())

    def test_compose_email(self):
        greeting_email = "\nDear Joan Rodgers,"
        body_email = "\nThank you very much for your generous donation of 1342"
        print(greeting_email, body_email)
        self.expected_val = io.StringIO()
        Mailroom_Part_4.compose_email("Joan Rodgers", "1342")
        self.actual_val = io.StringIO()
        self.assertEqual(self.actual_val.getvalue(), self.expected_val.getvalue())

    def test_get_donation_amount(self):
        with patch('builtins.input', return_value='2134'):
            self.assertEqual(Mailroom_Part_4.get_donation_amount("John"), "2134")
        with patch('builtins.input', return_value='$34.432234'):
            self.assertEqual(Mailroom_Part_4.get_donation_amount("John"), "$34.432234")

    def test_add_donation(self):
        with patch('builtins.input', return_value='5555'):
            greeting_email = "\nDear Matt Smith,"
            body_email = "\nThank you very much for your generous donation of 5555"
            print(greeting_email, body_email)
            self.expected_val_ = io.StringIO()
            Mailroom_Part_4.add_donation("Matt Smith")
            self.actual_val_ = io.StringIO()
            self.assertEqual(self.actual_val_.getvalue(), self.expected_val_.getvalue())

    def test_thank_you(self):
        print("---- List of all Donors ----"
              "- John Marks"
              "- Matt Smith"
              "- Kelsey Rodgers"
              "- John Williams"
              "- Morgan Stanley"
              "- Roger Johnson"
              "- Sherry Wilson"
              "- Alex Grant"
              "----------------------------")
        self.expected = io.StringIO()
        Mailroom_Part_4.thank_you('list')
        self.actual = io.StringIO()
        self.assertEqual(self.actual.getvalue(), self.expected.getvalue())

        with patch('builtins.input', return_value="one thousand"):
            self.assertRaises(ValueError, Mailroom_Part_4.thank_you("Joan Rodgers"))

        with patch('builtins.input', return_value="234"):
            greeting_email = "\nDear John Marks,"
            body_email = "\nThank you very much for your generous donation of 234"
            print(greeting_email, body_email)
            self.expected_val = io.StringIO()
            Mailroom_Part_4.thank_you("John Marks")
            self.actual_val = io.StringIO()
            self.assertEqual(self.actual_val.getvalue(), self.expected_val.getvalue())

    def test_get_donors_name(self):
        with patch('builtins.input', return_value='list'):
            self.assertEqual(Mailroom_Part_4.get_donors_name(), "list")
        with patch('builtins.input', return_value='?><:'):
            self.assertEqual(Mailroom_Part_4.get_donors_name(), "?><:")

    def test_thank_you_input(self):
        with patch('builtins.input', return_value='Morgan Stanley'):
            with patch('builtins.input', return_value='555'):
                greeting_email = "\nDear Morgan Stanley,"
                body_email = "\nThank you very much for your generous donation of 555"
                print(greeting_email, body_email)
                self.expected_val = io.StringIO()
                Mailroom_Part_4.thank_you_input()
                self.actual_val = io.StringIO()
                self.assertEqual(self.actual_val.getvalue(), self.expected_val.getvalue())

    def test_calc_data(self):
        summary_data = Mailroom_Part_4.calc_data()
        self.assertEqual(summary_data[0][1], 3)

    def test_report(self):
        print("Donor Name        | Total Given | Num Gifts | Average Gift"
              "------------------------------------------------------------------"
              "Morgan Stanley     $   20670.98           2  $    10335.49"
              "Alex Grant         $   13051.00           2  $     6525.50"
              "John Marks         $    8767.34           3  $     2922.45"
              "Sherry Wilson      $    7676.10           3  $     2558.70"
              "John Williams      $    2398.00           2  $     1199.00"
              "Roger Johnson      $    1206.23           2  $      603.12"
              "Matt Smith         $     750.00           1  $      750.00"
              "Kelsey Rodgers     $      55.76           1  $       55.76")
        self.expected = io.StringIO()
        Mailroom_Part_4.report()
        self.actual = io.StringIO()
        self.assertEqual(self.actual.getvalue(), self.expected.getvalue())

    def test_send_all_letters(self):
        Mailroom_Part_4.send_all_letters()
        for name in self.donor_data.keys():
            first = name.split()[0]
            last = name.split()[1]
            name_ = [first, last]
            filename = "./{}_{}.txt".format(*name_)
            print(filename)
            self.assertEqual(os.path.isfile(filename), True)



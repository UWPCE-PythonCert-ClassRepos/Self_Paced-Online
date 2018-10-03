# ------------------------------------------------- #
# Title: Lesson 9, mail room 5.2 testing
# Dev:   Craig Morton
# Date:  10/1/2018
# Change Log: CraigM, 10/1/2018, mail room 5.2 testing
# ------------------------------------------------- #


import unittest
import mailroom_behavior
import mailroom_data


class DataTest(unittest.TestCase):

    def create_default_db(self):
        db = mailroom_data.DonorCapture()
        d1 = mailroom_data.Donor("Bill", "Gates")
        d1.add_donation(50)
        d2 = mailroom_data.Donor("Paul", "Allen")
        d2.add_donation(30)
        d2.add_donation(40)
        d3 = mailroom_data.Donor("Jeff", "Bezos")
        d3.add_donation(80)
        d3.add_donation(90)
        d3.add_donation(100)
        db.add_donor(d1)
        db.add_donor(d2)
        db.add_donor(d3)
        return db

    def test_donor(self):
        name_tuple = ("Test", "This")
        donor = mailroom_data.Donor(name_tuple[0], name_tuple[1])
        self.assertEqual("Test This", donor.get_name())
        self.assertEqual(name_tuple, donor.get_key())
        donor.add_donation(50)
        self.assertEqual([50], donor.get_donations())
        donor.add_donation(25)
        self.assertEqual([50, 25], donor.get_donations())

    def test_donor_collection(self):
        donors = mailroom_data.DonorCapture()
        d1 = mailroom_data.Donor("Test", "This")
        d1.add_donation(50)
        d1.add_donation(25)
        d2 = mailroom_data.Donor("This", "Test")
        d2.add_donation(150)
        d2.add_donation(125)
        donors.add_donor(d1)
        donors.add_donor(d2)
        d_names = [d.get_name() for d in donors.get_donors()]
        self.assertIn(d1.get_name(), d_names)
        self.assertIn(d2.get_name(), d_names)
        for d in donors.get_donors():
            if d.get_name() == d1.get_name():
                self.assertEqual(d1.get_donations(), d.get_donations())
            elif d.get_name() == d2.get_name():
                self.assertEqual(d2.get_donations(), d.get_donations())
            else:
                self.fail("Could not find donor: {name}".format(d.get_name()))
        donors.add_donation("Test", "This", 10)
        for d in donors.get_donors():
            if d.get_name() == d1.get_name():
                self.assertEqual([50, 25, 10], d.get_donations())

    def test_thank_you(self):
        db = self.create_default_db()
        expected = "Thank you Test This for your generous donation of $55.00"
        letter = mailroom_behavior.send_thank_you(db, "Test", "This", 55)
        self.assertEqual(letter, expected)
        expected = "Thank you Test This for your generous donation of $10.00"
        letter = mailroom_behavior.send_thank_you(db, "Test", "This", 10)
        self.assertEqual(letter, expected)

    def test_create_report(self):
        db = self.create_default_db()
        expected_list = list()
        expected_list.append("Donor Name    | Total Given   | Num Gifts | Average Gift")
        expected_list.append("--------------------------------------------------------")
        expected_list.append(
            "{name:<14}  ${total:>13.2f}   {num:>9d}  ${avg:>12.2f}".format(
                name="Jeff Bezos", total=270, num=3, avg=90))
        expected_list.append(
            "{name:<14}  ${total:>13.2f}   {num:>9d}  ${avg:>12.2f}".format(
                name="Paul Allen", total=70, num=2, avg=35))
        expected_list.append(
            "{name:<14}  ${total:>13.2f}   {num:>9d}  ${avg:>12.2f}".format(
                name="Bill Gates", total=50, num=1, avg=50))
        expected = '\n'.join(expected_list)
        result = mailroom_behavior.create_report(db)
        self.assertEqual(expected, result)

    def test_send_letters(self):
        db = self.create_default_db()
        template = "{name} {amount} {total}"
        expected_list = list()
        expected_list.append(("Jeff Bezos", "Jeff Bezos 100.00 270.00"))
        expected_list.append(("Paul Allen", "Paul Allen 40.00 70.00"))
        expected_list.append(("Bill Gates", "Bill Gates 50.00 50.00"))
        result_list = mailroom_behavior.send_letters(db, template)
        self.assertIn(expected_list[0], result_list)
        self.assertIn(expected_list[1], result_list)
        self.assertIn(expected_list[2], result_list)


if __name__ == "__main__":
    unittest.main()

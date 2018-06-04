import unittest

import mailroom_actions
import mailroom_db

class DBTest(unittest.TestCase):

    def create_default_db(self):
        db = mailroom_db.DonorCollection()
        # Some default data
        d1 = mailroom_db.Donor("Jimmy", "Stewart")
        d1.add_donation(50)
        d2 = mailroom_db.Donor("Cary", "Grant")
        d2.add_donation(30)
        d2.add_donation(40)
        d3 = mailroom_db.Donor("Audrey", "Hepburn")
        d3.add_donation(80)
        d3.add_donation(90)
        d3.add_donation(100)
        db.add_donor(d1)
        db.add_donor(d2)
        db.add_donor(d3)
        return db


    def test_donor(self):
        name_tuple = ("Hello", "World")
        # Test creating the donor, getting name, getting key
        donor = mailroom_db.Donor(name_tuple[0], name_tuple[1])
        self.assertEqual("Hello World", donor.get_name())
        self.assertEqual(name_tuple, donor.get_key())
        # Test adding/getting donations
        donor.add_donation(50)
        self.assertEqual([50], donor.get_donations())
        donor.add_donation(25)
        self.assertEqual([50, 25], donor.get_donations())


    def test_donor_collection(self):
        donors = mailroom_db.DonorCollection()
        # Test adding donors
        d1 = mailroom_db.Donor("Hello", "World")
        d1.add_donation(50)
        d1.add_donation(25)
        d2 = mailroom_db.Donor("World", "Hello")
        d2.add_donation(150)
        d2.add_donation(125)
        donors.add_donor(d1)
        donors.add_donor(d2)
        d_names = [d.get_name() for d in donors.get_donors()]
        # Verify donors got added, and donor info is correct
        self.assertIn(d1.get_name(), d_names)
        self.assertIn(d2.get_name(), d_names)
        for d in donors.get_donors():
            if d.get_name() == d1.get_name():
                self.assertEqual(d1.get_donations(), d.get_donations())
            elif d.get_name() == d2.get_name():
                self.assertEqual(d2.get_donations(), d.get_donations())
            else:
                self.fail("Could not find donor: {name}".format(d.get_name()))

        # Verify adding a donor
        donors.add_donation("Hello", "World", 10)
        for d in donors.get_donors():
            if d.get_name() == d1.get_name():
                self.assertEqual([50, 25, 10], d.get_donations())


    def test_thank_you(self):
        db = self.create_default_db()
        expected = "Thank you Hello World for your generous donation of $55.00"
        letter = mailroom_actions.send_thank_you(db, "Hello", "World", 55)
        self.assertEqual(letter, expected)

        expected = "Thank you Hello World for your generous donation of $10.00"
        letter = mailroom_actions.send_thank_you(db, "Hello", "World", 10)
        self.assertEqual(letter, expected)


    def test_create_report(self):
        db = self.create_default_db()
        expected_list = list()
        expected_list.append("Donor Name    | Total Given   | Num Gifts | Average Gift")
        expected_list.append("--------------------------------------------------------")
        expected_list.append(
            "{name:<14}  ${total:>13.2f}   {num:>9d}  ${avg:>12.2f}".format(
                name="Audrey Hepburn", total=270, num=3, avg=90))
        expected_list.append(
            "{name:<14}  ${total:>13.2f}   {num:>9d}  ${avg:>12.2f}".format(
                name="Cary Grant", total=70, num=2, avg=35))
        expected_list.append(
            "{name:<14}  ${total:>13.2f}   {num:>9d}  ${avg:>12.2f}".format(
                name="Jimmy Stewart", total=50, num=1, avg=50))
        expected = '\n'.join(expected_list)

        result = mailroom_actions.create_report(db)

        self.assertEqual(expected, result)


    def test_send_letters(self):
        db = self.create_default_db()
        template = "{name} {amount} {total}"
        expected_list = list()
        expected_list.append(("Audrey Hepburn", "Audrey Hepburn 100.00 270.00"))
        expected_list.append(("Cary Grant", "Cary Grant 40.00 70.00"))
        expected_list.append(("Jimmy Stewart", "Jimmy Stewart 50.00 50.00"))

        result_list = mailroom_actions.send_letters(db, template)

        self.assertIn(expected_list[0], result_list)
        self.assertIn(expected_list[1], result_list)
        self.assertIn(expected_list[2], result_list)


if __name__ == "__main__":
    unittest.main()

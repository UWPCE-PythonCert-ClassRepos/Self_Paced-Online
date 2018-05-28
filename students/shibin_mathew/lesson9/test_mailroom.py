import unittest
from mailroom import Donor, Collection

class MailroomTests(unittest.TestCase):
    #  Unit Tests for Donor and Collection classes
    def test_Donor_constructor(self):
        t = Donor("Shibin", 35.45)
        self.assertEqual(t.names, "Shibin")
        self.assertEqual(t.amount, 35.45)

    def test_set_names(self):
        t = Donor("Shibin", 25.67)
        self.assertEqual(t.names, "Shibin")
        t.names = "John"
        self.assertEqual(t.names, "John")

    def test_set_amount(self):
        t = Donor("Shibin", 35.69)
        self.assertEqual(t.amount, 35.69)
        t.amount = 54.29
        self.assertEqual(t.amount, 54.29)

    def test_Collection_constructor(self):
        c = Collection(("Shibin", 25.45))
        self.assertEqual(c.donors2, ("Shibin", 25.45))

    def test_set_donors(self):
        c = Collection(("Shibin", 45.58))
        self.assertEqual(c.donors2, ("Shibin", 45.58))
        c.donors2 = ("Kimberly", 57)
        self.assertEqual(c.donors2, ("Kimberly", 57))

    def test_print_donor_names(self):
        c = Collection(("Shibin", "Jordy"))
        self.assertEqual(c.print_donor_names(), ["Shibin", "Jordy"])


if __name__ == '__main__':
    unittest.main()

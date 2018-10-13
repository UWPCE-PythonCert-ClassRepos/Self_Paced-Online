import unittest
import mailroom_oo as mailroom

class TestMailRoom(unittest.TestCase):

    def test_donor(self):
        test_donor = mailroom.Donor("Tony", "Lee", [100.0])
        self.assertEqual(test_donor.donations, [100.0])
        self.assertEqual(test_donor.full_name, "Tony Lee" )

        test_donor.add_donation(200.0)
        self.assertEqual(test_donor.donations, [100.0, 200.0] )

    def test_donor_history(self):
        d1 = mailroom.Donor("Tony", "Lee", [100.0])
        d2 = mailroom.Donor("Andy", "Arko", [200.0])
        test_dh = mailroom.DonorHistory([d1, d2])
        self.assertEqual(test_dh.get_all_donor_names(), ["Tony Lee", "Andy Arko"])
        d3 = mailroom.Donor("Michelle", "Cao", [300.0])
        test_dh.add_donor(d3)
        self.assertEqual(test_dh.get_all_donor_names(), ["Tony Lee", "Andy Arko", "Michelle Cao"])
        self.assertEqual(test_dh.donors[0].donations, [100])
        self.assertEqual(test_dh.donors[1].first, 'Andy')
        self.assertEqual(test_dh.donors[1].last, 'Arko')
        self.assertEqual(test_dh.donors[0].full_name, 'Tony Lee')

if __name__ == '__main__':
    unittest.main()

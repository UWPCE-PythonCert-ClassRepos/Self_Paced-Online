import unittest
import mailroom as mr

class TestDonor(unittest.TestCase):

    def test_donor(self):
        donor1 = mr.donor("Bob", [100, 200])
        self.assertEqual(donor1.name, "Bob")
        self.assertEqual(donor1.donation, [100, 200])
        
        self.assertEqual(donor1.total, 300)
        
        donor1.add_donation(300)
        self.assertEqual(donor1.donation, [100, 200, 300])
    
class TestDonorDatabase(unittest.TestCase):
    def test_Database(self):
        donor1 = mr.donor("Jake", [100, 200])
        donor2 = mr.donor("Amy", [100])
        donor3 = mr.donor("Rosa", [200])
        database = mr.DonorDatabase([donor1, donor2, donor3])
        self.assertEqual(database.donors[0].name, donor1.name)
        self.assertEqual(database.donors[2].name, donor3.name)
        
        donor4 = mr.donor("Charles", [20])
        database.add_donor(donor4)
        self.assertEqual(database.donors[3].name, donor4.name)
        self.assertEqual(database.donors[3].donation, donor4.donation)
        
if __name__ == "__main__":
    unittest.main()

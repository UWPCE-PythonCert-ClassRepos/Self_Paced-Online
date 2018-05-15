import unittest
from mailroom_part4 import donor_history

   
    
class TestMailRoom(unittest.TestCase):
    def test_get_all_donor_names(self):
        self.assertEqual(['Andrew Kim', 'Jamie Park', 'Tim Duncan', 'Billy Yan'], list(donor_history))

if __name__ == '__main__':
    unittest.main()
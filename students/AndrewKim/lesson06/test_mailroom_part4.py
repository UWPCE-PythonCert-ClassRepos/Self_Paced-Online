import unittest
import os
import mailroom_part4
from mailroom_part4 import donor_history, send_all, thank_you_msg

   
    
class TestMailRoom(unittest.TestCase):
    def test_get_all_donor_names(self):
        self.assertEqual(['Andrew Kim', 'Jamie Park', 'Tim Duncan', 'Billy Yan'], list(donor_history))
	
    def test_send_all(self):
        mailroom_part4.send_all()
        assert os.path.isfile('Andrew Kim.txt')
        assert os.path.isfile('Jamie Park.txt')
        assert os.path.isfile('Tim Duncan.txt')
        assert os.path.isfile('Billy Yan.txt')

    def test_thank_you_msg(self):
        msg = thank_you_msg('Jamie Park')
        assert msg == 'thank you Jamie Park for your generous donation of 4.0'
	
if __name__ == '__main__':
    unittest.main()
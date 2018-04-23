import mailroom 
import unittest
import sys, os 

class TestDonorCollection(unittest.TestCase):

    def test_validate_user_selection(self):

        action_dict = { 1: 'test', 2: 'test', 3: 'test', 4: 'test' }

        valid_selection = mailroom.validate_user_selection(0, action_dict)
        assert not valid_selection

        valid_selection = mailroom.validate_user_selection('a', action_dict)
        assert not valid_selection

        valid_selection = mailroom.validate_user_selection(1, action_dict)
        assert valid_selection

        valid_selection = mailroom.validate_user_selection(4, action_dict)
        assert valid_selection


if __name__ == '__main__':
    unittest.main()
 

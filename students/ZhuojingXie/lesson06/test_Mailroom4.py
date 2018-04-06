
import os
import unittest
from Mailroom4 import list_name, send_letters_to_everyone

class TestMailRoom(unittest.TestCase):
      def test_list_name (self):
          self.assertEqual(list_name(), ('Andy','Bryce','Charile','David','Elaine'))

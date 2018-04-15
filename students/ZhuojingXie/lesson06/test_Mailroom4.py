import unittest
from unittest import mock
import mailroom4
import copy

class TestMailRoom4(unittest.TestCase):


    def test_list_name(self):

        data = [{'name':'Andy','donation':[960,256,123.5,40]},{'name':'Bryce','donation':[30,45,27]}]



        self.assertEqual(data[0], {'name':'Andy','donation':[960,256,123.5,40]})




    def send_letters_to_everyone(self):
        data = [{'name':'Andy','donation':[960,256,123.5,40]},{'name':'Bryce','donation':[30,45,27]}]
        mailroom4.letters_to_everyone()
        assert os.path.isfile('Andy.txt')








if __name__ == '__main__':
    unittest.main()

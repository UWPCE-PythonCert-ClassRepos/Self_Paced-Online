'''
Shin Tran
Python 210
Assignment 6
'''

# Writing test cases for the Args_kwargs_lab

import unittest
from Args_kwargs_lab import funct

class Test_args_kwargs_lab(unittest.TestCase):

    deft1_list = ['yellow', 'red', 'blue', 'purple']
    test2_list = ['green','white','blue','purple']
    test3_list = ['green','white','black','orange']
    test4_list = ['yellow', 'blue', 'red', 'purple']
    test5_list = ['black', 'blue', 'red', 'purple']
    test6_list = ['blue', 'green', 'red', 'yellow']
    test7_list = ['black', 'white', 'blue', 'purple']
    test8_dict = {'fore_color':'cyan', 'back_color':'magenta', 'link_color':'gray', 'visited_color':'chartreuse'}
    test9_dict = {'link_color':'gray', 'visited_color':'chartreuse'}

    # No parameters are passed in
    def test1(self):
        self.assertEqual(funct(), self.deft1_list)

    # The first two parameters are passed in
    def test2(self):
        self.assertEqual(funct('green','white'), self.test2_list)

    # Four parameters are passed in
    def test3(self):
        self.assertEqual(funct('green','white','black','orange'), self.test3_list)

    # Two specified parameters are passed in
    def test4(self):
        self.assertEqual(funct(link_color='red', back_color='blue'), self.test4_list)

    # The first parameter is passed in, two specified parameters are passed in
    def test5(self):
        self.assertEqual(funct('black', link_color='red', back_color='blue'), self.test5_list)

    # A list of four elements is passed in
    def test6(self):
        self.assertEqual(funct(*self.test6_list), self.test6_list)

    # A list of two elements is passed in as the first two parameters
    def test7(self):
        self.assertEqual(funct(*self.test7_list[:2]), self.test7_list)

    # A dictionary of four elements is passed in
    def test8(self):
        test8_list = [v for k, v in self.test8_dict.items()]
        self.assertEqual(funct(**self.test8_dict), test8_list)

    # A dictionary of two specified elements is passed in
    def test9(self):
        test9_list = ['yellow','red','gray','chartreuse']
        self.assertEqual(funct(**self.test9_dict), test9_list)

    # A list of two elements and a dictionary of two specified elements are passed in
    def test10(self):
        test10_list = ['magenta','cyan','gray','chartreuse']
        test10_list2 = test10_list[:2]
        self.assertEqual(funct(*test10_list2, **self.test9_dict), test10_list)

    # The first parameter, list of two elements,
    # and a dictionary of one element are passed in
    def test11(self):
        test11_list = ['purple', 'green']
        test11_dict = {'visited_color':'white'}
        test11_answer = ['blue','purple', 'green','white']
        self.assertEqual(funct('blue', *test11_list, **test11_dict), test11_answer)

    # The first parameter, list of one element, dictionary of one element are passed in
    def test12(self):
        test12_list = ['blue']
        test12_dict = {'link_color':'yellow'}
        test12_answer = ['red','blue', 'yellow','purple']
        self.assertEqual(funct('red', *test12_list, **test12_dict), test12_answer)

# Main method to call the program
if __name__ == '__main__':
    unittest.main()
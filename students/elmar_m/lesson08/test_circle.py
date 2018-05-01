#!/usr/bin/env python3

'''
file: test_circle.py
elmar_m / 22e88@mailbox.org
Lesson08: unittests for circle class
'''

'''
This tests include some print statements which can be uncommented
if one wants to see the results in a more human-readable form.
'''

import unittest as ut
import circle as ci 
import random as ra

class mytests(ut.TestCase):

    def test_Circle(self):
        ''' make sure objects with required attributes will be created: '''
        for i in range(1,100):
            name = 'a' + str(i)
            name = ci.Circle(i)
            self.assertTrue(name)
            self.assertTrue(hasattr(name, 'radius'))
            self.assertTrue(hasattr(name, 'diameter'))
            self.assertTrue(hasattr(name, 'area'))
            self.assertTrue(hasattr(name, 'from_diameter'))
            self.assertEqual(name.radius, name.diameter / 2)
        
            ''' make sure radius changes if diameter is changed and vice versa: '''
            r_before = name.radius
            # print('radius before change: {}'.format(r_before))
            d_before = name.diameter
            # print('diameter before change: {}'.format(d_before))
            # print('doing change by diameter ...')
            name = name.from_diameter(name.diameter * 5)
            self.assertEqual(name.diameter, r_before * 10)
            # print('radius after change: {}'.format(name.radius))
            # print('diameter after change: {}'.format(name.diameter))

            '''
             make sure it's possible to get the area of the circle object, 
            that it's greater than zero and it's impossible to change it:
            '''
            x = name.area 
            self.assertGreater(x, 0)
            bigger = x + 1
            with self.assertRaises(AttributeError):
                name.area = bigger
            
            ''' make sure it's possible to add one circle object to another: '''
            second_c = ci.Circle(i + 1)
            self.assertTrue(name + second_c)  
                        
            '''
            make sure the radius of the resulting circle equals the sum of 
            the two given circle's radiusses:
            '''
            r1 = name.radius
            # print('r1: {}'.format(r1))
            r2 = second_c.radius
            # print('r2: {}'.format(r2))
            r_expected = r1 + r2
            # print('r_expected: {}'.format(r_expected))

            third_c = name + second_c
            self.assertEqual(third_c.radius, r_expected)
    
            '''
            make sure it's possible to multiply a circle object 
            with an integer, and that the result is another circle object
            with the correct radius:
            '''
            for r in range(34, 99):
                new_c = name * r 
                self.assertIsInstance(new_c, ci.Circle)
                self.assertEqual(new_c.radius, name.radius * r)
    
    '''
    Test if circles are sortable. Create a list of circles with random radiusses and 
    sort that list by radius size. 
    '''
    def test_Circle_sort(self):
        c_list = []
        # for i in range(1, 1000000):      # uncomment print statements before activating this line ;))
        for i in range(1, 100):
            circle = ci.Circle(ra.randint(5, 3000000))
            c_list.append(circle)
        # for c in c_list:
        #     print('item in c_list: {}'.format(c))

        s_list = sorted(c_list)

        for i,j in enumerate(s_list[:-1]):
            # print('index in s_list: {}, content object: {}'.format(i, j)) 
            # print('next index in s_list: {}, next content object: {}'.format(i+1, s_list[i+1])) 
            c1 = j
            c2 = s_list[i + 1]
            # self.assertLess(c1.radius, c2.radius)    
            self.assertLessEqual(c1.radius, c2.radius)  # this has to be LessEqual instead of Less,
                                                        # because it's possible that a random number
                                                        # for circle radius is picked twice
        


if __name__ == '__main__':
    ut.main()


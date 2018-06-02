#!/usr/bin/env python3

# chmod +x test_html_render.py needs to be performed before executable

'''
    File Name: test_html_render.py
    Author: Matt Hudgins
    Date created: 5/28/18
    Date last modified: 5/28/18
    Python Version 3.6.4
'''

from io import StringIO
import html_render as hr
import unittest

class test_html_rendering(unittest.TestCase):

    def element_test(self):
        element = hr.Element()
        self.assertEqual(element.content, [])

    def test_render(self):
        element = hr.Element('Testing.')
        f = StringIO()
        element.render(f)
        self.assertEqual(f.getvalue(), "<>\n" + element.indent + "Testing.\n</>\n")



if __name__ == '__main__':
    unittest.main()

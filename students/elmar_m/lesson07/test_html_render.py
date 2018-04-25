#!/usr/bin/env python3

# file: test_html_render.py

import unittest as ut
import html_render as hr

class mytests(ut.TestCase):

    '''
        Test if html_render provides a class named 'Element'    
        with certain attributes
    '''
    def test_element(self):
        self.assertTrue(issubclass(hr.Element, object))
        obj = hr.Element()
        self.assertIsInstance(obj, hr.Element)
        self.assertTrue(hasattr(obj, 'tag'))
        self.assertTrue(hasattr(obj, 'i_level'))
        self.assertTrue(hasattr(obj, 'content'))
        self.assertTrue(hasattr(obj, 'append'))
        self.assertTrue(hasattr(obj, 'render'))

    
    def test_Html(self):
        self.assertTrue(issubclass(hr.Html, hr.Element))
        obj = hr.Html()
        self.assertIsInstance(obj, hr.Html)
        self.assertIsInstance(obj, hr.Element)

    
    def test_Body(self):
        self.assertTrue(issubclass(hr.Body, hr.Element))
        obj = hr.Body()
        self.assertIsInstance(obj, hr.Body)
        self.assertIsInstance(obj, hr.Element)


    def test_P(self):
        self.assertTrue(issubclass(hr.P, hr.Element))
        obj = hr.P()
        self.assertIsInstance(obj, hr.P)
        self.assertIsInstance(obj, hr.Element)

if __name__ == '__main__':
    ut.main()



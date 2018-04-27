#!/usr/bin/env python3

'''
file: test_html_render.py
elmar_m / 22e88@mailbox.org
Lesson07: unittests for HTML renderer
'''

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
        self.assertTrue(obj.tag == 'element')
        self.assertTrue(hasattr(obj, 'content'))
        self.assertTrue(hasattr(obj, 'append'))
        self.assertTrue(hasattr(obj, 'render'))
        self.assertTrue(hasattr(obj, 'props'))
        self.assertTrue(type(obj.props) == list)
        self.assertTrue(len(obj.props) == 0)
        self.assertTrue(hasattr(obj, 'propstring'))
        self.assertTrue(type(obj.propstring) == str)
        self.assertTrue(len(obj.propstring) == 0)

    
    def test_Html(self):
        self.assertTrue(issubclass(hr.Html, hr.Element))
        obj = hr.Html()
        self.assertIsInstance(obj, hr.Html)
        self.assertIsInstance(obj, hr.Element)
        self.assertTrue(obj.tag == 'html')

    
    def test_Body(self):
        self.assertTrue(issubclass(hr.Body, hr.Element))
        obj = hr.Body()
        self.assertIsInstance(obj, hr.Body)
        self.assertIsInstance(obj, hr.Element)
        self.assertTrue(obj.tag == 'body')


    def test_P(self):
        self.assertTrue(issubclass(hr.P, hr.Element))
        obj = hr.P()
        self.assertIsInstance(obj, hr.P)
        self.assertIsInstance(obj, hr.Element)
        self.assertTrue(obj.tag == 'p')
        self.assertTrue(hasattr(obj, 'props'))
        self.assertTrue(type(obj.props) == list)
        self.assertTrue(len(obj.props) == 0)
        self.assertTrue(hasattr(obj, 'propstring'))
        self.assertTrue(type(obj.propstring) == str)
        self.assertTrue(len(obj.propstring) == 0)


    def test_Head(self):
        self.assertTrue(issubclass(hr.Head, hr.Element))
        obj = hr.Head()
        self.assertIsInstance(obj, hr.Head)
        self.assertIsInstance(obj, hr.Element)
        self.assertTrue(obj.tag == 'head')

    def test_Title(self):
        self.assertTrue(issubclass(hr.Title, hr.Element))
        obj = hr.Title('this is a test')
        self.assertIsInstance(obj, hr.Title)
        self.assertIsInstance(obj, hr.Element)
        self.assertTrue(obj.tag == 'title')
        self.assertTrue(hasattr(obj, 'render'))


    def test_SelfClosingTag(self):
        self.assertTrue(issubclass(hr.SelfClosingTag, hr.Element))
        obj = hr.SelfClosingTag()
        self.assertIsInstance(obj, hr.SelfClosingTag)
        self.assertIsInstance(obj, hr.Element)
        self.assertTrue(hasattr(obj, 'render'))
    

    def test_Meta(self):
        self.assertTrue(issubclass(hr.Meta, hr.SelfClosingTag))
        obj = hr.Meta()
        self.assertIsInstance(obj, hr.Meta)
        self.assertIsInstance(obj, hr.SelfClosingTag)
        self.assertIsInstance(obj, hr.Element)
        self.assertTrue(obj.tag == 'meta')
        self.assertTrue(hasattr(obj, 'props'))
        self.assertTrue(type(obj.props) == list)
        self.assertTrue(len(obj.props) == 0)
        self.assertTrue(hasattr(obj, 'propstring'))
        self.assertTrue(type(obj.propstring) == str)
        self.assertTrue(len(obj.propstring) == 0)


    def test_Hr(self):
        self.assertTrue(issubclass(hr.Hr, hr.SelfClosingTag))
        obj = hr.Hr()
        self.assertIsInstance(obj, hr.Hr)
        self.assertIsInstance(obj, hr.SelfClosingTag)
        self.assertIsInstance(obj, hr.Element)
        self.assertTrue(obj.tag == 'hr')


    def test_A(self):
        self.assertTrue(issubclass(hr.A, hr.Element))
        obj = hr.A('https://www.uw.edu', 'university')
        self.assertIsInstance(obj, hr.A)
        self.assertIsInstance(obj, hr.Element)
        self.assertTrue(obj.tag == 'a')
        self.assertTrue(hasattr(obj, 'render'))


    def test_H(self):
        self.assertTrue(issubclass(hr.H, hr.Element))
        obj = hr.H(2, 'headertext')
        self.assertIsInstance(obj, hr.H)
        self.assertIsInstance(obj, hr.Element)
        self.assertTrue(obj.tag == 'h')
        self.assertTrue(type(obj.size) == int)
        self.assertTrue(type(obj.text) == str)
        self.assertTrue(hasattr(obj, 'render'))


    def test_Ul(self):
        self.assertTrue(issubclass(hr.Ul, hr.Element))
        obj = hr.Ul()
        self.assertIsInstance(obj, hr.Ul)
        self.assertIsInstance(obj, hr.Element)
        self.assertTrue(obj.tag == 'ul')
        self.assertTrue(hasattr(obj, 'props'))
        self.assertTrue(type(obj.props) == list)
        self.assertTrue(len(obj.props) == 0)
        self.assertTrue(hasattr(obj, 'propstring'))
        self.assertTrue(type(obj.propstring) == str)
        self.assertTrue(len(obj.propstring) == 0)


    def test_Li(self):
        self.assertTrue(issubclass(hr.Li, hr.Ul))
        obj = hr.Li()
        self.assertIsInstance(obj, hr.Li)
        self.assertIsInstance(obj, hr.Ul)
        self.assertIsInstance(obj, hr.Element)
        self.assertTrue(obj.tag == 'li')
        self.assertTrue(hasattr(obj, 'props'))
        self.assertTrue(type(obj.props) == list)
        self.assertTrue(len(obj.props) == 0)
        self.assertTrue(hasattr(obj, 'propstring'))
        self.assertTrue(type(obj.propstring) == str)
        self.assertTrue(len(obj.propstring) == 0)


if __name__ == '__main__':
    ut.main()



#!/usr/bin/env python3

import unittest
import os
from io import StringIO
from html_render import Element, Body,A, Title,Hr,SelfClosingTag,H, Meta

class ElementTestCase(unittest.TestCase):
    """Test class Element"""
    def test_append(self):
        """test append"""
        # create Element instance
        p = Element()
        expected = "This is a test"
        p.append(expected)
        actual = p.a_list[0]
        self.assertEqual(expected, actual)

    def test_render(self):
        """test render()"""
        p = Element()
        test_str = "this is a render test"
        # add content
        p.append(test_str)
        f = StringIO()
        # indent  4 spaces
        p.render(f, "    ")
        expected = ["    <html>", p.indent*' ' + "    this is a render test", "    </html>"]
        expected_page = "\n".join(expected) + "\n"
        self.assertEqual(expected_page, f.getvalue())

class BodyTestCase(unittest.TestCase):
    """Test class Body"""
    def test_render(self):
        p =  Body()
        test_str = "this is a Body render test"
        p.append(test_str)
        f = StringIO()
        p.render(f)
        expected = ["<body>", p.indent*' ' + "this is a Body render test", "</body>"]
        expected_page = "\n".join(expected) + "\n"
        self.assertEqual(expected_page, f.getvalue())

class ATestCase(unittest.TestCase):
    """ Test class A"""
    def test_render(self):
        p = A("OneLineTag", "test render")
        f = StringIO()
        p.render(f)
        #print(f.getvalue())
        expected = "<a href=" + '"' + "OneLineTag" + '"' +">test render</a>\n"
        self.assertEqual(expected, f.getvalue())

class TitleTestCase(unittest.TestCase):
    """Test class Title"""
    def test_render(self):
        p = Title("Python Intro = Lesson 7")
        f = StringIO()
        p.render(f)
        expected = "<title>Python Intro = Lesson 7</title>\n"
        self.assertEqual(expected, f.getvalue())

class HrTestCase(unittest.TestCase):
    """Test class Hr"""
    def test_render1(self):
        p = Hr()
        f = StringIO()
        p.render(f)
        expected = "<hr/> \n"
        self.assertEqual(expected, f.getvalue())

    def test_render2(self):
        """Test TypeError Exception"""
        p = Hr()
        self.assertRaises(TypeError, p.append,"Test exception")

class HTestCase(unittest.TestCase):
    """Test number level"""
    def test_init(self):
        p = H(4, "Lesson7 - HTML")
        f = StringIO()
        p.render(f)
        expected = "<h4>Lesson7 - HTML</h4>\n"
        self.assertEqual(expected, f.getvalue())

class MetaTestCase(unittest.TestCase):
    def test_render(self):
        p = Meta()
        f = StringIO()
        p.render(f)
        expected = "<meta charset=" + '"' + "UTF-8" +'"' + " /> \n"
        self.assertEqual(expected, f.getvalue())

if __name__ == '__main__':
    unittest.main()
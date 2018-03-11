#!/usr/bin/env python3
"""Unit tests for HTML Render"""
import unittest
import html_render as hr


class TestElement(unittest.TestCase):
    """Test class containing all unit tests for the Element class"""
    def setUp(self):
        self.element = hr.Element()

    def tearDown(self):
        pass

    def test_append(self):
        self.element.append('Testing the append method...')
        self.assertTrue(self.element.content == [
                        'Testing the append method...'],
                        msg=self.element.content)


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/env python3
"""Unit tests for HTML Render"""
import os
import unittest
import html_render as hr


class TestElement(unittest.TestCase):
    """Test class containing all unit tests for the Element class"""
    def setUp(self):
        self.element = hr.Element()

    def tearDown(self):
        # Remove any unit test generated files
        files = os.listdir()
        for f in files:
            if "unit_test_" in f:
                os.remove(os.path.join(os.getcwd(), f))

    def test_append(self):
        """Test the append method"""
        self.element.append('Testing the append method...')
        self.assertTrue(self.element.content == [
                        'Testing the append method...'],
                        msg=self.element.content)

    def test_render_def_indent(self):
        """Test the render method with def indentation"""
        self.element.tag = 'html'
        self.element.append('Testing the render method...')
        result = ('<html>\n'
                  '    Testing the render method...\n'
                  '<\\html>\n')

        with open('unit_test_render.txt', 'w+') as f:
            self.element.render(f)
            f.seek(0)
            self.assertTrue(f.read(50) == result)

    def test_render_custom_indent(self):
        """Test the render method with custom indentation"""
        self.element.tag = 'html'
        self.element.append('Testing the render method...')
        result = ('    <html>\n'
                  '        Testing the render method...\n'
                  '    <\\html>\n')

        with open('unit_test_render.txt', 'w+') as f:
            self.element.render(f, '    ')
            f.seek(0)
            self.assertTrue(f.read(60) == result)


if __name__ == '__main__':
    unittest.main()

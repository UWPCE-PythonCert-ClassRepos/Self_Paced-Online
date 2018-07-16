#!/usr/bin/env python3

import unittest
import html_render as hr
import os
from io import StringIO


class TestRender(unittest.TestCase):

    def test_render_html(self):
        element = hr.Element("Test")
        element.tag = 'html'
        f = StringIO()
        element.render(f)
        self.assertEqual(
                         f.getvalue(), "<html>\n"
                         + element.indent + "Test\n</html>\n")
        element.tag = 'body'
        f = StringIO()
        element.render(f)
        self.assertEqual(
                         f.getvalue(), "<body>\n"
                         + element.indent + "Test\n</body>\n")
        element.tag = 'p'
        f = StringIO()
        element.render(f)
        self.assertEqual(
                         f.getvalue(), "<p>\n"
                         + element.indent + "Test\n</p>\n")

    def test_append_elem(self):
        test = hr.Element('some stuff in here')
        test.append('some more stuff in here')
        self.assertEqual(
                         test.content,
                         ['some stuff in here', 'some more stuff in here'])

    def test_element_html(self):
        test_element = hr.Element('some stuff')
        self.assertEqual(test_element.content, ["some stuff"])


if __name__ == '__main__':
    unittest.main()

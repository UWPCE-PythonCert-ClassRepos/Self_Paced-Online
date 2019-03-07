#!/usr/bin/env python3

import unittest
import html_render as hr
from io import StringIO


class HtmlRenderTest(unittest.TestCase):

    def test_element(self):
        test = hr.Element("test")
        self.assertEqual(test.content, ["test"])


    def test_append(self):
        test = hr.Element("test")
        test.append("test2")
        self.assertEqual(test.content, ["test", "test2"])


    def test_style(self):
        test = hr.Element("test", style='font-color:blue;')
        self.assertEqual(test.kwargs, {'style': 'font-color:blue;'})


    def test_render(self):
        test = hr.Element("test")
        test.tag = "tag"
        f = StringIO()
        test.render(f)
        self.assertEqual(f.getvalue(), "<tag>\n" + test.indent + "test\n</tag>\n")


    def test_selfclosingtag(self):
        test = hr.SelfClosingTag()
        test.tag = "tag"
        f = StringIO()
        test.render(f)
        self.assertEqual(f.getvalue(), "<tag />\n")


    def test_onelinetag(self):
        test = hr.OneLineTag("Testing a test")
        test.tag = "tag"
        f = StringIO()
        test.render(f)
        self.assertEqual(f.getvalue(), "<tag>Testing a test</tag>\n")


    def test_atag(self):
        test = hr.A("http://google.com", "Link")
        f = StringIO()
        test.render(f)
        self.assertEqual(f.getvalue(), "<a href = \"http://google.com\">\n" + test.indent + "Link\n</a>\n")


    def test_htag(self):
        test = hr.H(1, "Big Test")
        f = StringIO()
        test.render(f)
        self.assertEqual(f.getvalue(), "<h1>Big Test</h1>\n")

if __name__ == '__main__':
    unittest.main()
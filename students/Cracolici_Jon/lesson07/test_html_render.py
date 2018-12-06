# Jon Cracolici
# UW-Python Cert
# Lesson 07 - html render test suite


import pytest
import unittest
import html_render as hr
from io import StringIO
import os

class TestElement(unittest.TestCase):
    """This is my unit testing suite for the Element class"""

    #This section tests the Element Class
    def test_element(self):
        trial_elem = hr.Element(content='sample content')
        self.assertEqual(trial_elem.content, ['sample content'])

    def test_element_append(self):
        trial_elem = hr.Element(content='sample content')
        trial_elem.append('more sample content')
        self.assertEqual(trial_elem.content, ['sample content', 'more sample content'])

    def test_element_render(self):
        trial_elem = hr.Element(content='sample content')
        f = StringIO()
        trial_elem.render(f, cur_ind=1)
        standard = '    <html>\n        sample content\n    </html>\n'
        self.assertEqual(standard, f.getvalue())


class TestHTML(unittest.TestCase):
    """This is my unit testing suite for the html tag of the Element class"""

    def test_element_render(self):
        trial_elem = hr.Html(content='sample content')
        f = StringIO()
        trial_elem.render(f, cur_ind=1)
        standard = '<!DOCtype html>\n    <html>\n    </html>\n'
        self.assertEqual(standard, f.getvalue())


class TestBody(unittest.TestCase):
    """This is my unit testing suite for the body tag of the Element class"""

    def test_element_render(self):
        trial_elem = hr.Body(content='sample content')
        f = StringIO()
        trial_elem.render(f, cur_ind=1)
        standard = '    <body>\n        sample content\n    </body>\n'
        self.assertEqual(standard, f.getvalue())


class TestP(unittest.TestCase):
    """This is my unit testing suite for the p tag of the Element class"""

    def test_element_render(self):
        trial_elem = hr.P(content='sample content')
        f = StringIO()
        trial_elem.render(f, cur_ind=1)
        standard = '    <p>\n        sample content\n    </p>\n'
        self.assertEqual(standard, f.getvalue())


class TestHead(unittest.TestCase):
    """This is my unit testing suite for the head tag of the Element class"""

    def test_head_render(self):
        trial_elem = hr.Head(content='sample content')
        f = StringIO()
        trial_elem.render(f, cur_ind=1)
        standard = '    <head>\n        sample content\n    </head>\n'
        self.assertEqual(standard, f.getvalue())


class TestOneLineTag(unittest.TestCase):
    """This is my unit testing suite for the onelinetest subclass of the Element class"""

    def test_onelinetag_render(self):
        trial_elem = hr.OneLineTag(content='sample content')
        f = StringIO()
        trial_elem.render(f, cur_ind=1)
        standard = '    <html>sample content</html>\n'
        self.assertEqual(standard, f.getvalue())


class TestTitle(unittest.TestCase):
    """This is my unit testing suite for the title tag of the onelinetag class"""

    def test_title_render(self):
        trial_elem = hr.Title(content='sample content')
        f = StringIO()
        trial_elem.render(f, cur_ind=1)
        standard = '    <title>sample content</title>\n'
        self.assertEqual(standard, f.getvalue())


class TestSelfClosingTag(unittest.TestCase):
    """This is my unit testing suite for the self-closing subclass of the Element class"""

    def test_sct_render(self):
        trial_elem = hr.SelfClosingTag()
        f = StringIO()
        trial_elem.render(f, cur_ind=1)
        standard = '    < />\n'
        self.assertEqual(trial_elem.tag, '')
        self.assertEqual(standard, f.getvalue())


class TestHr(unittest.TestCase):
    """This is my unit testing suite for the hr tag of the self-closing class"""

    def test_hr_render(self):
        trial_elem = hr.Hr()
        f = StringIO()
        trial_elem.render(f, cur_ind=1)
        standard = '    <hr />\n'
        self.assertEqual(standard, f.getvalue())


class TestBr(unittest.TestCase):
    """This is my unit testing suite for the br tag of the self-closing class"""

    def test_br_render(self):
        trial_elem = hr.Br()
        f = StringIO()
        trial_elem.render(f, cur_ind=1)
        standard = '    <br />\n'
        self.assertEqual(standard, f.getvalue())


class TestA(unittest.TestCase):
    """This is my unit testing suite for the a(link) subclass of the Element class"""

    def test_a_render(self):
        trial_elem = hr.A("http:google.com", content='link')
        f = StringIO()
        trial_elem.render(f, cur_ind=1)
        standard = '    <a href = "http:google.com">link</a>\n'
        self.assertEqual(standard, f.getvalue())


class TestUl(unittest.TestCase):
    """This is my unit testing suite for the ul tag of the Element class"""

    def test_ul_render(self):
        trial_elem = hr.Ul(content='sample content')
        f = StringIO()
        trial_elem.render(f, cur_ind=1)
        standard = '    <ul>\n        sample content\n    </ul>\n'
        self.assertEqual(standard, f.getvalue())


class TestLi(unittest.TestCase):
    """This is my unit testing suite for the li tag of the Element class"""

    def test_li_render(self):
        trial_elem = hr.Li(content='sample content')
        f = StringIO()
        trial_elem.render(f, cur_ind=1)
        standard = '    <li>\n        sample content\n    </li>\n'
        self.assertEqual(standard, f.getvalue())


class TestH(unittest.TestCase):
    """This is my unit testing suite for the h tag of the onelinetag class"""

    def test_H_render(self):
        trial_elem = hr.H(3, content='sample content')
        f = StringIO()
        trial_elem.render(f, cur_ind=1)
        standard = '    <h3>sample content</h3>\n'
        self.assertEqual(standard, f.getvalue())


class TestMeta(unittest.TestCase):
    """This is my unit testing suite for the meta tag of the self-closing  class"""

    def test_meta_render(self):
        trial_elem = hr.Meta(charset="UTF-8")
        f = StringIO()
        trial_elem.render(f, cur_ind=1)
        standard = '    <meta charset = "UTF-8" />\n'
        self.assertEqual(standard, f.getvalue())


if __name__ == '__main__':
    unittest.main()
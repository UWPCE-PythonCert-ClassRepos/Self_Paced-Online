import unittest
import html_render as hr
import os.path
import io
import sys
from io import StringIO


class TestHTMLRender(unittest.TestCase):

    def test_Element_render(self):
        f = StringIO()
        testelement = hr.Element()
        testelement.render(f)
        self.assertEqual(f.getvalue(), "<tag>\n<\\tag>\n")

    def test_Element_append(self):
        f = StringIO()
        testelement = hr.Element()
        testelement.append('test1')
        testelement.append('test2')
        testelement.render(f)
        self.assertEqual(f.getvalue(), "<tag>\n    test1test2\n<\\tag>\n")

    def test_Html_render(self):
        f = StringIO()
        testelement = hr.Html()
        testelement.render(f)
        self.assertEqual(f.getvalue(), "<html>\n<\html>\n")

    def test_Html_append(self):
        f = StringIO()
        testelement = hr.Html()
        testelement.append('test1')
        testelement.append('test2')
        testelement.render(f)
        self.assertEqual(f.getvalue(), "<html>\n    test1test2\n<\html>\n")

    def test_Body_render(self):
        f = StringIO()
        testelement = hr.Body()
        testelement.render(f)
        self.assertEqual(f.getvalue(), "<body>\n<\\body>\n")

    def test_Body_append(self):
        f = StringIO()
        testelement = hr.Body()
        testelement.append('test1')
        testelement.append('test2')
        testelement.render(f)
        self.assertEqual(f.getvalue(), "<body>\n    test1test2\n<\\body>\n")

    def test_P_render(self):
        f = StringIO()
        testelement = hr.P()
        testelement.render(f)
        self.assertEqual(f.getvalue(), "<p>\n<\p>\n")

    def test_P_append(self):
        f = StringIO()
        testelement = hr.P()
        testelement.append('test1')
        testelement.append('test2')
        testelement.render(f)
        self.assertEqual(f.getvalue(), "<p>\n    test1test2\n<\p>\n")

    def test_append_body_html(self):
        f = StringIO()
        testelement = hr.Html()
        body = hr.Body()
        testelement.append(body)
        testelement.render(f)




if __name__ == '__main__':
    unittest.main()

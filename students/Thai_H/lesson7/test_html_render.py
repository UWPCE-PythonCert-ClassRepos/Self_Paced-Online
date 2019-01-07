

import unittest
import html_render as hr
from io import StringIO


class Test_ElementClass(unittest.TestCase):

    def test_Element(self):
        element = hr.Element()
        self.assertEqual(element.content, [])

    def test_Br(self):
        test = hr.Br()
        file = StringIO()
        test.render(file)
        self.assertEqual(file.getvalue(), "<br>\n</br>\n")


    def test_HTml_render(self):
        test = hr.Html()
        file = StringIO()
        test.render(file)
        self.assertEqual(file.getvalue(), '<!DOCTYPE html>\n<html>\n</html>\n')

    def test_H(self):
        test = hr.H(2, "header")
        file = StringIO()
        test.render(file)
        self.assertEqual(file.getvalue(), '<h2>' + 'header ' + '</h2>\n')

    def test_A(self):
        test_anchor_tag = hr.A('http://www.boeing.com', 'link')
        file = StringIO()
        test_anchor_tag.render(file)
        self.assertEqual(file.getvalue(), '<a href="http://www.boeing.com">\n' + '    link\n' + '</a>\n')



if __name__ == '__main__':
    unittest.main()
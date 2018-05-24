#!/usr/bin/env python

import html_render as hr
from io import StringIO
import unittest


class Test_Html_Render(unittest.TestCase):

    def setUp(self):
        self.html = hr.Html()
        self.head = hr.Head(hr.Title('The Title is Title'))
        self.body = hr.Body()
        self.paragraph = hr.P('This is my paragraph', style="color:blue;")
        self.horizontal_rule = hr.Hr()
        self.anchor = hr.A('http://chicktech.org', 'link')
        self.unorderedlist = hr.Ul(id="UL_List", style="line-height:100%")
        self.headertwo = hr.H(3, 'This is a Header 3 ')
        self.meta = hr.Meta(charset="UTF-8")

    def test_append(self):
        """Test the append method"""
        self.html.append(
            'This is a test of the append method...')
        self.assertTrue(self.html.content == ['This is a test of the append method...'],
                        msg=self.html.content)

    def test_element_content(self):
        """testing append method through element reference"""
        test_element = hr.Element("this is some content")
        self.assertEqual(test_element.content, ["this is some content"])
        test_element.append("Adding additional content")
        self.assertEqual(test_element.content, [
                         "this is some content", "Adding additional content"])

    def test_element_tag(self):
        """Testing override tag properties"""
        self.assertEqual(self.body.tag, 'body')
        self.assertEqual(self.head.tag, 'head')
        self.assertEqual(self.paragraph.tag, 'p')
        self.assertEqual(self.horizontal_rule.tag, 'hr')
        self.assertEqual(self.anchor.tag, 'a')

    def test_add_attribute(self):
        """Add style to element"""
        test_element = hr.Element("content to add", style='Bold')
        self.assertTrue(test_element.attributes == {
                        'style': "Bold"}, msg=test_element.attributes)
        self.assertTrue(self.paragraph.attributes == {
                        'style': 'color:blue;'}, msg=self.paragraph.attributes)

    def test_one_line_tag(self):
        """Testing one line tag - title tag"""
        test_element = hr.OneLineElement("Testing One Line Element - Title")
        test_element.tag = 'title'
        f = StringIO()
        test_element.render(f)
        self.assertEqual(f.getvalue(), "<title> Testing One Line Element - Title </title>\n")

    def test_self_closing_tag(self):
        f=StringIO()
        self.meta.render(f)
        self.assertTrue(f.getvalue(), "<meta charset=\"UTF-8\" />\n")

    def test_render(self):
        """Test the render full page """
        self.body.append(hr.P('This is my paragraph'))
        self.html.append(self.head)
        self.html.append(self.body)

        html_output = ('<!DOCTYPE html>\n'
                       '<html>\n'
                       '    <head>\n'
                       '        <title> The Title is Title </title>\n'
                       '    </head>\n'
                       '    <body>\n'
                       '        <p>\n'
                       '            This is my paragraph\n'
                       '        </p>\n'
                       '    </body>\n'
                       '</html>\n')

        with open('unit_tests.txt', 'w+') as file:
            self.html.render(file)
            file.seek(0)
            result = file.read(len(html_output))
            self.assertTrue(result == html_output, msg=result)


if __name__ == '__main__':
    unittest.main()

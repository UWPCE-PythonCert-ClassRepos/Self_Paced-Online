
#!/usr/bin/python3 pytest

# Author: Roy Tate (githubtater)

import unittest
import html_render as hr
from io import StringIO

class TestHTMLRender(unittest.TestCase):
    item_one = 'This is item number 1'
    item_two = 'This is item number 2'

    def test_verify_element_class_attributes(self):
        '''Verify that the basic class attributes can be accessed'''
        element_attr = hr.Element()
        self.assertEqual(element_attr.tag, '')
        self.assertEqual(element_attr.indent, '    ')

    def test_element_class_renders_content(self):
        '''Verify items can be appended to an element'''
        item_one = 'This is item number 1'
        element = hr.Element()
        element.append(self.item_one)
        self.assertEqual(element.content[-1], self.item_one)


    def test_onelinetag_class_renders_content(self):
        test_tag = hr.OneLineTag('Test Title Test')
        test_tag.tag = 'title'
        test_tag.indent = ''
        output = StringIO()
        test_tag.render(output)
        self.assertEqual(output.getvalue(), '<title>\nTest Title Test\n</title>\n')

    def test_html_class(self):
        '''Verify the Html.render function overrides Element.render'''
        new_html = hr.Html()
        self.assertEqual(new_html.tag, 'html')
        output = StringIO()
        new_html.render(output)
        self.assertEqual(output.getvalue(), '<!DOCTYPE html>\n<html>\n</html>\n')

    def test_unordered_list_generates_correctly(self):
        ul_test = hr.Ul(self.item_one)
        output = StringIO()
        ul_test.render(output)
        self.assertEqual(output.getvalue(), '<ul>\n    This is item number 1\n</ul>\n')

    def test_href_link_generates_correctly(self):
        href_link = hr.A('www.python.org', 'link to python.org')
        href_link.indent = ''
        output = StringIO()
        href_link.render(output)
        self.assertEqual(output.getvalue(), '<a href="www.python.org">\nlink to python.org\n</a>\n')

    def test_h_tag_returns_correct_size(self):
        header = hr.H(1, 'Head1')
        header.indent = ''
        output = StringIO()
        header.render(output)
        self.assertEqual(output.getvalue(), '<h1>\nHead1\n</h1>\n')

    def test_self_closing_tag(self):
        '''Verify SelfClosingTag.render overrides Element.render'''
        sc_tag = hr.SelfClosingTag()
        sc_tag.tag = 'br'
        output = StringIO()
        sc_tag.render(output)
        self.assertEqual(output.getvalue(), '<br />\n')

        sc_tag_attr = hr.SelfClosingTag(charset='UTF-8')
        sc_tag_attr.tag = 'meta'
        output = StringIO()
        sc_tag_attr.render(output)
        self.assertEqual(output.getvalue(), '<meta charset="UTF-8" />\n')

if __name__ == "__main__":
    unittest.main()
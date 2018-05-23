#!/usr/bin/env python

import html_render as hr
import io
import unittest


class Test_Html_Render(unittest.TestCase):

    def setUp(self):
        self.html = hr.Html()
        self.head = hr.Head(hr.Title('The Title is Title'))
        self.body = hr.Body()
        self.paragraph = hr.P('This is my paragraph', style="Bold")
        self.horizontal_rule = hr.Hr()
        self.anchor = hr.A('http://chicktech.org', 'link')
        self.unorderedlist = hr.Ul(id="UL_List", style="line-height:100%")
        self.headertwo = hr.H(2, 'This is a Header 2 ')
        self.meta = hr.Meta(charset="UTF-8")

    def test_append(self):
        """Test the append method"""
        self.html.append(
            'This is a test of the append method...')
        self.assertTrue(self.html.content == ['This is a test of the append method...'],
                        msg=self.html.content)

    def test_render(self):
        """Test the render method"""
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

    def test_self_closing(self):
        """Test the self closing"""
        self.body.append(self.paragraph)
        self.body.append(self.horizontal_rule)
        self.html.append(self.head)
        self.html.append(self.body)

        html_output = ('<!DOCTYPE html>\n'
                       '<html>\n'
                       '    <head>\n'
                       '        <title> The Title is Title </title>\n'
                       '    </head>\n'
                       '    <body>\n'
                       '        <p style="Bold">\n'
                       '           This is my paragraph\n'
                       '        </p>\n'
                       '        <hr />\n'
                       '    </body>\n'
                       '</html>\n')

        with open('unit_tests2.txt', 'w+') as file:
            self.html.render(file)
            file.seek(0)
            result = file.read(len(html_output))
            self.assertTrue(result == html_output, msg=result)

    def test_lists(self):
        """Testing lists"""
        self.unorderedlist.append(hr.Li("Apples"))
        self.unorderedlist.append(hr.Li("Oranges"))
        self.body.append(self.paragraph)
        self.body.append(self.horizontal_rule)
        self.body.append(self.unorderedlist)
        self.html.append(self.head)
        self.html.append(self.body)

        html_output = ('<!DOCTYPE html>\n'
                       '<html>\n'
                       '    <head>\n'
                       '        <title> This is a title </title>\n'
                       '    </head>\n'
                       '    <body>\n'
                       '        <p style="Bold" cls="Intro">\n'
                       '            500\n'
                       '        </p>\n'
                       '        <hr />\n'
                       '        <ul id="UL_List" style="line-height:100%">\n'
                       '            <li>\n'
                       '                Apples\n'
                       '            </li>\n'
                       '            <li>\n'
                       '                Oranges\n'
                       '            </li>\n'
                       '        </ul>\n'
                       '    </body>\n'
                       '</html>\n')

        with open('unit_tests.txt', 'w+') as file:
            self.html.render(file)
            file.seek(0)
            result = file.read(len(html_output))
            self.assertTrue(result == html_output, msg=result)



if __name__ == '__main__':
    unittest.main()

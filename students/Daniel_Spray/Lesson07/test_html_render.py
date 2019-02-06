import unittest
import html_render as hr
import run_html_render
import os
from html_render import *
from run_html_render import *
from io import StringIO

class TestHtmlRender(unittest.TestCase):
    '''Write a class with a full suite of tests for html_render.py'''

#Step 1 tests:

    def test_files_rendered(self):
        '''Run a test to ensure output html files were written'''
        run_html_render
        for step in range(1,8):
            self.assertTrue(os.path.exists('test_html_output'+str(step)+'.html'))

    def test_initialization(self):
        '''Run a test to check initialization variables'''
        hr.Element.__init__(self)
        expected_content = []
        expected_kwargs = {}
        self.assertEqual(expected_content,self.content)
        self.assertEqual(expected_kwargs,self.kwargs)

    def test_append(self):
        '''Run a test to ensure you can add content'''
        actual = hr.Element("test string")
        actual.append("more text")
        expected = ["test string","more text"]
        self.assertEqual(expected,actual.content)

    def test_render(self):
        '''Run a test to check that your content gets rendered properly'''
        test_content = hr.Element("test string")
        test_content.tag = "a"
        f = StringIO()
        test_content.render(f)
        expected = "<a>\n    test string\n</a>\n"
        actual = f.getvalue()
        self.assertEqual(expected,actual)

#Step 2 and 8 test

    def test_basic_tags(self):
        '''Run a test for html, body, and p tags'''
        test_content = hr.Html(hr.Body(hr.P("test string")))
        f = StringIO()
        test_content.render(f)
        expected = "<!DOCTYPE html>\n<html>\n    <body>\n        <p>\n            test string\n        </p>\n    </body>\n</html>\n"
        actual = f.getvalue()
        self.assertEqual(expected,actual)

#Step 3 test

    def test_one_line_tag(self):
        '''Run a test for single line tags'''
        test_content = hr.OneLineTag("test string")
        test_content.tag = "title"
        f = StringIO()
        test_content.render(f)
        expected = "<title>test string</title>\n"
        actual = f.getvalue()
        self.assertEqual(expected,actual)

#Step 4 test

    def test_styles(self):
        '''Run a test for adding styles to a tag'''
        test_content = hr.P("test string",style="text-align: center; font-style: oblique;")
        f = StringIO()
        test_content.render(f)
        expected = '<p style="text-align: center; font-style: oblique;">\n    test string\n</p>\n'
        actual = f.getvalue()
        self.assertEqual(expected,actual)

#Step 5 test

    def test_self_closing_tag(self):
        '''Run a test for self closing tags'''
        test_content = hr.SelfClosingTag("test string")
        test_content.tag = "br"
        f = StringIO()
        test_content.render(f)
        expected = "<br />\n"
        actual = f.getvalue()
        self.assertEqual(expected,actual)

#Step 6 test

    def test_anchor_tag(self):
        '''Run a test for tags with links'''
        test_content = hr.A("http://google.com","test link")
        f = StringIO()
        test_content.render(f)
        expected = '<a href="http://google.com">test link</a>\n'
        actual = f.getvalue()
        self.assertEqual(expected,actual)

#Step 7 test

    def test_list_tags(self):
        '''Run a test for list tags'''
        test_list = hr.Ul("Test List")
        test_list.append(hr.Li("Thing one"))
        test_list.append(hr.Li("Thing two"))
        f = StringIO()
        test_list.render(f)
        expected = '<ul>\n    Test List\n    <li>\n        Thing one\n    </li>\n    <li>\n        Thing two\n    </li>\n</ul>\n'
        actual = f.getvalue()
        self.assertEqual(expected,actual)

#Step 8 meta test

    def test_meta(self):
        '''Run a test for html, body, and p tags'''
        test_content = hr.Meta("test string",charset="UTF-8")
        f = StringIO()
        test_content.render(f)
        expected = '<meta charset="UTF-8" />\n'
        actual = f.getvalue()
        self.assertEqual(expected,actual)

#Final output test

    def test_final_output(self):
        try:
            with open('test_html_output8.html','r') as f:
                actual = f.read()
        except FileNotFoundError:
                print("The file wasn't created")
                actual = ''
        expected="""<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8" />
        <title>PythonClass = Revision 1087:</title>
    </head>
    <body>
        <h2>PythonClass - Example</h2>
        <p style="text-align: center; font-style: oblique;">
            Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text
        </p>
        <hr />
        <ul id="TheList" style="line-height:200%">
            <li>
                The first item in a list
            </li>
            <li style="color: red">
                This is the second item
            </li>
            <li>
                And this is a 
                <a href="http://google.com">link</a>
                to google
            </li>
        </ul>
    </body>
</html>
"""
        self.assertEqual(expected,actual)

if __name__ == '__main__':
     unittest.main()
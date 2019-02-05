import unittest
import html_render
import run_html_render
import os
from html_render import *
from run_html_render import *

class TestHtmlRender(unittest.TestCase):
    '''Write a class with a full suite of tests for html_render.py'''
    run_html_render
    def test_step_one(self):
        self.assertTrue(os.path.exists('test_html_output1.html'))
        try:
            with open('test_html_output1.html','r') as f:
                actual = f.read()
        except FileNotFoundError:
                print("The file wasn't created")
                actual = ''
        expected="""<html>
    Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text
    And here is another piece of text -- you should be able to add any number
</html>
"""
        self.assertEqual(expected,actual)

    def test_step_two(self):
        self.assertTrue(os.path.exists('test_html_output2.html'))
        try:
            with open('test_html_output2.html','r') as f:
                actual = f.read()
        except FileNotFoundError:
                print("The file wasn't created")
                actual = ''
        expected="""<!DOCTYPE html>
<html>
    <body>
        <p>
            Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text
        </p>
        <p>
            And here is another piece of text -- you should be able to add any number
        </p>
    </body>
</html>
"""
        self.assertEqual(expected,actual)
    def test_step_three(self):
        self.assertTrue(os.path.exists('test_html_output3.html'))
        try:
            with open('test_html_output3.html','r') as f:
                actual = f.read()
        except FileNotFoundError:
                print("The file wasn't created")
                actual = ''
        expected="""<!DOCTYPE html>
<html>
    <head>
        <title>PythonClass = Revision 1087:</title>
    </head>
    <body>
        <p>
            Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text
        </p>
        <p>
            And here is another piece of text -- you should be able to add any number
        </p>
    </body>
</html>
"""
        self.assertEqual(expected,actual)
    def test_step_four(self):
        self.assertTrue(os.path.exists('test_html_output4.html'))
        try:
            with open('test_html_output4.html','r') as f:
                actual = f.read()
        except FileNotFoundError:
                print("The file wasn't created")
                actual = ''
        expected="""<!DOCTYPE html>
<html>
    <head>
        <title>PythonClass = Revision 1087:</title>
    </head>
    <body>
        <p style="text-align: center; font-style: oblique;">
            Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text
        </p>
    </body>
</html>
"""
        self.assertEqual(expected,actual)
    def test_step_five(self):
        self.assertTrue(os.path.exists('test_html_output5.html'))
        try:
            with open('test_html_output5.html','r') as f:
                actual = f.read()
        except FileNotFoundError:
                print("The file wasn't created")
                actual = ''
        expected="""<!DOCTYPE html>
<html>
    <head>
        <title>PythonClass = Revision 1087:</title>
    </head>
    <body>
        <p style="text-align: center; font-style: oblique;">
            Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text
        </p>
        <hr />
    </body>
</html>
"""
        self.assertEqual(expected,actual)
    def test_step_six(self):
        self.assertTrue(os.path.exists('test_html_output6.html'))
        try:
            with open('test_html_output6.html','r') as f:
                actual = f.read()
        except FileNotFoundError:
                print("The file wasn't created")
                actual = ''
        expected="""<!DOCTYPE html>
<html>
    <head>
        <title>PythonClass = Revision 1087:</title>
    </head>
    <body>
        <p style="text-align: center; font-style: oblique;">
            Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text
        </p>
        <hr />
        And this is a 
        <a href="http://google.com">link</a>
        to google
    </body>
</html>
"""
        self.assertEqual(expected,actual)
    def test_step_seven(self):
        self.assertTrue(os.path.exists('test_html_output7.html'))
        try:
            with open('test_html_output7.html','r') as f:
                actual = f.read()
        except FileNotFoundError:
                print("The file wasn't created")
                actual = ''
        expected="""<!DOCTYPE html>
<html>
    <head>
        <title>PythonClass = Revision 1087:</title>
    </head>
    <body>
        <h2>PythonClass - Class 6 example</h2>
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
    def test_step_eight(self):
        self.assertTrue(os.path.exists('test_html_output8.html'))
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

if __name__ == '__main__':
     unittest.main()
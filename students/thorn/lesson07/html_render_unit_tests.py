'''
Thomas Horn
4.13.2018
Lesson 7 - HTML Render and Subclassing
'''

import unittest
import html_render as hr
from io import StringIO

# class TagTests(unittest.TestCase):
#     def test_html(self):
#         ''' Test that it starts with <html> and ends with </html> '''
#         e = hr.Element()
#         test = hr.Html()
#         e.render(hello)
#         f = StringIO()
#         test.render(f)
#         lines = f.getvalue()
#         lines.strip()
#         print(lines)


class Step3Tests(unittest.TestCase):
    def test_head(self):
        ''' Test for proper head tag and that I remember how to make these. '''
        correct_tag = "head"
        self.assertEqual(hr.Head.tag, correct_tag)

    def test_OneLineTag(self):
        ''' Test to make sure <title> tags are printed on the same line as their content as their super class OneLineTag dictates. '''
        test = hr.OneLineTag("One Line Test")
        test.tag = "title"
        f = StringIO()
        test.render(f)
        # Check for start and end with title
        self.assertEqual(f.getvalue()[:7], "<title>")        
        self.assertEqual(f.getvalue()[-9:], "</title>\n")


class Step4Tests(unittest.TestCase):
    def test_element_accepts_kwargs(self):
        ''' Test to just make sure element accepts different # kwargs. '''
        test = hr.Element("some text content", id="TheList", style="line-height:200%")
        # print(type(test.attributes))
        # print(test.attributes)

class SelfClosingTests(unittest.TestCase):
    def test_self_closing_tag(self):
        ''' Tests if a Br self closing tag is properly formatted. '''
        test = hr.Br()
        test.tag_name = 'br'
        test_correct = '<br />\n' # need the newline
        f = StringIO()
        test.render(f)
        self.assertEqual(f.getvalue(), test_correct)

# class LinkTest(unittest.TestCase):
#     def test_link(self):
#         ''' Test to make sure a test link equals <a href="http://google.com">link</a> '''
#         test = hr.A('http://google.com', 'link')
#         test_correct = '<a href="http://gooogle.com">link</a>'
#         f = StringIO()
#         test.render(f)
#         self.assertEqual(f.getvalue(), test_correct)
        
class HTest(unittest.TestCase):
    def test_H(self):
        ''' Tests for a proper H1level '''
        test = hr.H(1, "Test")
        test_correct = "<h1>Test</h1>\n"
        f = StringIO()
        test.render(f)
        print(f.getvalue())
        self.assertEqual(f.getvalue(), test_correct)


class MetaTest(unittest.TestCase):
    def test_Meta(self):
        ''' Tests for a <meta charset="UTF-8" /> '''
        test = hr.Meta(charset="UTF-8")
        test_correct = '<meta charset="UTF-8" />\n'
        f = StringIO()
        test.render(f)
        print(f.getvalue())
        self.assertEqual(f.getvalue(), test_correct)



if __name__ == "__main__":
    unittest.main()
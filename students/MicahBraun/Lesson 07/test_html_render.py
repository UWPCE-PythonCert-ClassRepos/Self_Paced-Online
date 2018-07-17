# ----------------------------------------------------------------------------------------------------------------------
# NAME: MICAH BRAUN
# PROJECT: Assignment 07 - test_html_render.py
# PURPOSE: Testing html-creating doc with unittest
# DATE: 07/16/2018
#
# DESCRIPTION: Runs tests against html_render.py to check for integrity of module(s) and expected behaviour.
# ----------------------------------------------------------------------------------------------------------------------
import unittest
from io import StringIO
import html_render as h


class TestElementClass(unittest.TestCase):
    """
    Tests content of element (should be empty)
    """
    def test_Element(self):
        """
        Test Part I
        """
        elem = h.Element()
        self.assertEqual(elem.content, [])

    def test_Append(self):
        """
        Test append method
        :return: Test should return equals
        """

        assert_test_val1 = h.Element()
        assert_test_val1.append('Append Test...')                           # test append 1 value
        self.assertEqual(assert_test_val1.content, ['Append Test...'])

        assert_test_val2 = h.Element('Append Test...')                      # test appending another value to existing
        assert_test_val2.append('12345')
        self.assertEqual(assert_test_val2.content, ['Append Test...', '12345'])

    def test_Render1(self):
        test = h.Element('Test out')      # assign var to import class Element w/ content val as string
        f = StringIO()                        # assign var to import StringIO class (read/write str to buffer)
        test.render(f)                    # write Element(test_val) using render() method to buffer (to file)
        self.assertEqual(f.getvalue(), '<>\n' + test.indent + 'Test out\n</>\n')   # test equality w/ buffer val

    def test_HTml_render(self):
        test = h.Html()
        f = StringIO()
        test.render(f)
        self.assertEqual(f.getvalue(), '<!DOCTYPE html>\n<html>\n</html>\n')

    def test_Br(self):
        test = h.Br()
        f = StringIO()
        test.render(f)
        self.assertEqual(f.getvalue(), "<br>\n</br>\n")

    def test_A(self):
        test_anchor = h.A('http://www.google.com', 'link')
        f = StringIO()
        test_anchor.render(f)
        self.assertEqual(f.getvalue(), '<a href="http://www.google.com">\n' + '    link\n' + '</a>\n')

    def test_H(self):
        test = h.H(2, "header")
        f = StringIO()
        test.render(f)
        self.assertEqual(f.getvalue(), '<h2>' + 'header ' + '</h2>\n')

    def test_Img(self):
        test = h.Img(source="test", alternate="test", ht="1", wd="2", hspace="3")
        f = StringIO()
        test.render(f)
        self.assertEqual(f.getvalue(), '<img src="test" alt="test" height="1" width="2" hspace="3">\n</img>\n')

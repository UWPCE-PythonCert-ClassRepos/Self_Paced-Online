# ------------------------------------------- #
# Student:   Tri Nguyen
# Instructor: Natasha Aleksandrova
# Date:  23-Mar-2018
# ------------------------------------------- #

import unittest
import html_render as hr
from io import StringIO


class TestHtmlRender(unittest.TestCase):

    def test_Element_class(self):

        test = hr.Element('some string', style='color: blue;')
        self.assertIsInstance(test.content, list)
        self.assertIsInstance(test.kwargs, dict)


    def test_append(self):
        ''' test append method '''
        test_list = ['one', 'two', 'three']
        test = hr.Element()
        test.append('one')
        test.append('two')
        test.append('three')
        self.assertEqual(test.content, test_list)


    def test_render(self):
        ''' test render method '''
        test = hr.Element('Here is a sentence.')
        test.tag_name = 'p'
        test_temp = f'<p>\n{test.indent}Here is a sentence.\n</p>\n'
        f = StringIO()
        test.render(f)
        self.assertEqual(f.getvalue(), test_temp)


    def test_set_attr(self):
        ''' test set_attr method '''
        test_temp = ' style="text-align: center;"'
        test = hr.Element('some string', style='text-align: center;')
        self.assertEqual(test.set_attr(), test_temp)


    def test_OneLineTag(self):
        test = hr.OneLineTag('PythonClass = Revision 1087:')
        test.tag_name = 'title'
        test_temp = '<title>PythonClass = Revision 1087:</title>\n'
        f = StringIO()
        test.render(f)
        self.assertEqual(f.getvalue(), test_temp)


    def test_SelfClosingTag(self):
        test = hr.SelfClosingTag()
        test.tag_name = 'hr'
        test_temp = '<hr/>\n'
        f = StringIO()
        test.render(f)
        self.assertEqual(f.getvalue(), test_temp)


if __name__ == '__main__':
    unittest.main()
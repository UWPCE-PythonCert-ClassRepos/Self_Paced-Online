#!/usr/bin/env python3

# file: test_html_render.py

import unittest as ut
import html_render as hr

class mytests(ut.TestCase):

    ''' Test if html_render provides a class named 'Element': '''   
    def test_element(self):
        # obj = hr.Element('html', 0)
        obj = hr.Element()
        # pass
        self.assertIsInstance(obj, hr.Element)

    ''' Test if class 'element' provides an attribute named 'tagname': '''
    def test_tagname(self):
        pass

    ''' Test if class 'element' provides an attribute named 'indentation': '''
    def test_indent(self):
        pass
    
    ''' Test if class 'element' provides a method named 'append': '''
    def test_append(self):
        pass

    ''' Test if class 'element' provides a method named 'render': '''
    def test_render(self):
        pass
    


if __name__ == '__main__':
    ut.main()



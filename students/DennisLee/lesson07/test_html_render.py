#!/usr/bin/env python3

import unittest
import html_render as hr

class ElementTestCase(unittest.TestCase):
    def setUp(self):
        self.e = hr.Element()
        self.strs_before = (
                "  \n Why  am   \n\tI here?     \t",
                "\n\t  \n  Here's   that rainy   day...   \t  \n",
                "I told  you   about...\n"
        )
        self.strs_after = (
                "Why am I here?", 
                "Here's that rainy day...",
                "I told you about..."
        )
    def tearDown(self):
        self.e = None
    def test_init(self):
        x = hr.Element(self.strs_before[0])
        self.assertEqual(x.contents, [self.strs_after[0]])
        x = hr.Element(self.strs_before)
        self.assertEqual(x.contents, list(self.strs_after))
        del x
    def test_append(self):
        self.assertEqual(len(self.strs_before), len(self.strs_after))

        self.assertRaises(AttributeError, self.e.append, 50)
        for i in range(len(self.strs_before)):
            self.e.append(self.strs_before[i])
            self.assertEqual(self.e.contents, list(self.strs_after[:i+1]))
    def test_render_1(self):
        self.assertFalse(self.e.render('', 5))
    def test_render_2(self):
        self.assertFalse(self.e.render('Bogus2\\Bogus3\\Bogosity.txt', 5))
    def test_render_3(self):
        self.assertFalse(self.e.render('R:\\Bogus2\\Bogus3\\Bogosity.txt', 5))
    def test_render_4(self):
        self.assertFalse(self.e.render(100, 5))
    def test_render_100(self):
        self.assertTrue(self.render_helper('test_html_file.html', -11))
    def test_render_101(self):
        self.assertTrue(self.render_helper('test_html_file.html', 0))
    def test_render_102(self):
        self.assertTrue(self.render_helper('test_html_file.html', 10))
    def test_render_103(self):
        self.assertTrue(self.render_helper('test_html_file.html', 'dfafd'))
    def test_render_104(self):
        self.assertTrue(self.render_helper('test_html_file.html', '   -9 \n '))
    def test_render_105(self):
        self.assertTrue(self.render_helper('test_html_file.html', '  0 \t   '))
    def test_render_106(self):
        self.assertTrue(self.render_helper('test_html_file.html', ' \n  6 '))
    def render_helper(self, filename, ind):
        for str in self.strs_before:
            self.e.append(str)
        result = self.e.render(filename, ind)
        if result:
            if not isinstance(ind, int):
                ind = 2
            else:
                ind = int(ind)
                if ind <= 0:
                    ind = 2
            with open(filename, 'r') as f:
                self.strs_out = f.readlines()
            self.assertEqual(len(self.strs_out), 3)
            self.assertEqual(self.strs_out[0], "<html>\n")
            self.assertEqual(self.strs_out[2], "</html>\n")
            self.assertEqual(self.strs_out[1], 
                            ' '*ind + ' '.join(self.strs_after) + ' \n')
        return result
        

if __name__ == '__main__':
    unittest.main()
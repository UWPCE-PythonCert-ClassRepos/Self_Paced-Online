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
    def test_append(self):
        self.assertRaises(AttributeError, self.e.append, 50)
        self.e.append(self.strs_before[0])
        self.assertEqual(self.e.contents, [self.strs_after[0]])
        self.e.append(self.strs_before[1])
        self.assertEqual(self.e.contents, list(self.strs_after[0:2]))
        self.e.append(self.strs_before[2])
        self.assertEqual(self.e.contents, list(self.strs_after))
    def test_render(self):
        ind = 11
        filename = 'test_html_file.html'
        for str in self.strs_before:
            self.e.append(str)
        self.e.render(filename, ind)
        with open(filename, 'r') as f:
            self.strs_out = f.readline()
        self.assertEqual(len(self.strs_out), 3)
        self.assertEqual(self.strs_out[0], "<html>")
        self.assertEqual(self.strs_out[2], "</html>")
        self.assertEqual(self.strs_out[1], ' '*ind + ' '.join(self.strs_after))

if __name__ == '__main__':
    unittest.main()
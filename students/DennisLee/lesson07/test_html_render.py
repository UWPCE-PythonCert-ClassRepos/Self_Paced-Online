#!/usr/bin/env python3

import unittest
import html_render as hr

class ElementTestCase(unittest.TestCase):
    def __init__(self):
        pass
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
        self.e.append(self.strs_before[0])
        self.assertEqual(self.e.contents, [self.strs_after[0]])
        self.e.append(self.strs_before[1])
        self.assertEqual(self.e.contents, list(self.strs_after[0:1]))
        self.e.append(self.strs_before[2])
        self.assertEqual(self.e.contents, list(self.strs_after))
    def test_render(self):
        filename = 'test_html_file.html'
        for self.str in self.strs_before:
            self.e.append(self.str)
        self.e.render(filename, 11)
        with open(filename, 'r') as f:
            self.strs_out = f.readline()
        self.assertEqual(len(self.strs_out), 3)
        self.assertEqual(self.strs_out[0], "<html>")
        self.assertEqual(self.strs_out[2], "</html>")
        self.assertEqual(self.strs_out[1], 
                ' '*self.e.indent + ' '.join(self.strs_after))

if __name__ == '__main__':
    unittest.main()
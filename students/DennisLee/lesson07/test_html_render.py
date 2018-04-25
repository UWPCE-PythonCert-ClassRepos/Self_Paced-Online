#!/usr/bin/env python3

import unittest, os
import html_render as hr

class ElementTestCase(unittest.TestCase):
    def setUp(self):
        self.strs_before = (
                "  \n Why  am   \n\tI here?     \t",
                "\n\t  \n  Here's   that rainy   day...   \t  \n",
                "I told  you   about...\n",
                "    \n \t  \n  There's  a   somebody I'm longing  to   see\n",
                "   \n \t \t Someone  who'll \twatch\nover\nme   \t   ",
                "\tI\tdid\nit\t\tmy      \n\n\t\tway\t\t\n\t"
        )
        self.strs_after = (
                "Why am I here?", 
                "Here's that rainy day...",
                "I told you about...",
                "There's a somebody I'm longing to see",
                "Someone who'll watch over me",
                "I did it my way"
        )
    def tearDown(self):
        del self.strs_before
        del self.strs_after

    def test_init_1(self):
        x = hr.Element(self.strs_before[0])
        self.assertEqual(x.contents, [self.strs_after[0]])
        del x
    def test_init_2(self):
        with self.assertRaises(TypeError):
            x = hr.Element(70.0)
            del x
    def test_init_3(self):
        x = hr.Element('')
        self.assertEqual(x.contents, [])
        del x
    def test_init_4(self):
        x = hr.Element('\t\n    ')
        self.assertEqual(x.contents, [])
        del x
    def test_init_5(self):
        x = hr.Element(self.strs_before[0])
        x.append(self.strs_before[1])
        self.assertEqual(x.contents, list(self.strs_after[:2]))
        del x
    def test_init_6(self):
        x = hr.Element()
        self.assertEqual(x.contents, [])
        del x
    def test_init_7(self):
        x = hr.Element(None)
        self.assertEqual(x.contents, [])
        del x

    def test_append_internal(self):
        self.assertEqual(len(self.strs_before), len(self.strs_after))
    def test_append_1(self):
        self.e = hr.Element()
        with self.assertRaises(TypeError):
            self.e.append(50)
        del self.e
    def test_append_2(self):
        self.e = hr.Element(self.strs_before[0])
        with self.assertRaises(TypeError):
            self.e.append(50)
        del self.e
    def test_append_3(self):
        self.e = hr.Element()
        for i in range(len(self.strs_before)):
            self.e.append(self.strs_before[i])
            self.e.append("  ")
            self.assertEqual(self.e.contents, list(self.strs_after[:i+1]))
        del self.e
    def test_append_4(self):
        self.e = hr.Element(self.strs_before[0])
        for i in range(1, len(self.strs_before)):
            self.e.append(self.strs_before[i])
            self.e.append("  ")
            self.assertEqual(self.e.contents, list(self.strs_after[:i+1]))
        del self.e


    def test_render_1(self):
        self.e = hr.Element()
        with self.assertRaises(ValueError):
            self.e.render('', '  ')
        del self.e
    def test_render_100(self):
        self.assertTrue(self.render_helper('', 'html'))
    def test_render_101(self):
        self.assertTrue(self.render_helper('  ', 'html'))
    def test_render_102(self):
        self.assertTrue(self.render_helper('    ', 'html'))
    def test_render_103(self):
        with self.assertRaises(TypeError):
            self.render_helper(2, 'html')
    def test_render_104(self):
        with self.assertRaises(ValueError):
            self.render_helper('dfafd', 'html')
    def test_render_105(self):
        with self.assertRaises(ValueError):
            self.render_helper('\t', 'html')
    def render_helper(self, ind, element_tag=''):
        result, filename = False, 'test_html_file_dennislee.html'
        self.e = hr.Element()
        if element_tag:
            self.e.tag = element_tag
        for str in self.strs_before:
            self.e.append(str)
        fobj = open(filename, 'w')
        result = self.e.render(fobj, ind)
        fobj.close()
        if result:
            with open(filename, 'r') as f:
                self.strs_out = f.readlines()
            self.assertEqual(self.strs_out[0], f"<{element_tag}>\n")
            self.assertEqual(self.strs_out[1], 
                    ind + ' '.join(self.strs_after) + ' \n')
            self.assertEqual(self.strs_out[-1], f"</{element_tag}>\n")
        os.remove(filename)
        del self.e
        return result

# class Step2ElementTestCase(ElementTestCase):
#     def setUp(self):
#         self.html_element = hr.Html()
#         self.body_element = hr.Body()
#         self.p1_element = hr.P("hello")
#         self.p2_element = hr.P()
#         self.strs_before = (
#                 "  \n Why  am   \n\tI here?     \t",
#                 "\n\t  \n  Here's   that rainy   day...   \t  \n",
#                 "I told  you   about...\n",
#                 "    \n \t  \n  There's  a   somebody I'm longing  to   see\n",
#                 "   \n \t \t Someone  who'll \twatch\nover\nme   \t   ",
#                 "\tI\tdid\nit\t\tmy      \n\n\t\tway\t\t\n\t"
#         )
#         self.strs_after = (
#                 "Why am I here?", 
#                 "Here's that rainy day...",
#                 "I told you about..."
#                 "There's a somebody I'm longing to see",
#                 "Someone who'll watch over me",
#                 "I did it my way"
#         )
#     def tearDown(self):
#         del self.html_element
#         del self.p1_element
#         del self.p2_element
#         del self.body_element
#         del self.strs_before
#         del self.strs_after

#     def test_render_P(self):
#         para = hr.P(self.strs_before[0])
#         for string in self.strs_before[1:]:
#             para.append(string)
#         self.assertEqual(para.contents, list(self.strs_after))
#     def test_Body_element_1(self):
#         bod = hr.Body(self.strs_before[0])
#         for string in self.strs_before[1:]:
#             bod.append(string)
#         self.assertEqual(bod.contents, list(self.strs_after))
#     def test_Html_element_1(self):
#         pg = hr.Html(self.strs_before[0])
#         for string in self.strs_before[1:]:
#             pg.append(string)
#         self.assertEqual(pg.contents, list(self.strs_after))
#     def test_hierarchical_1(self):
#         para1 = hr.P(self.strs_before[0])
#         para1.append(self.strs_before[1])
#         para2 = hr.P(self.strs_before[2])
#         para2.append(self.strs_before[3])
#         para3 = hr.P(self.strs_before[4])
#         para3.append(self.strs_before[5])

#         bod = hr.Body()
#         bod.append(para1)
#         bod.append(para2)
#         bod.append(para3)
        
#         pg = hr.Html(bod)


if __name__ == '__main__':
    unittest.main()
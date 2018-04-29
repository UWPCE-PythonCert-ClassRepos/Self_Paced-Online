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
        self.attrs_fail = {
            'id': 60,
            'alt': '  \t  \n \tFancy      \t\t   Pants   \n\n\t\n '
        }
        self.attrs_pass = {
            'id': 'Marker',
            'alt': '  \t  \n \tFancy      \t\t   Pants   \n\n\t\n '
        }
        self.alt_normalized = "Fancy Pants"
        self.random_tag = "SomeTagName"
        self.test_filename = "test_html_file_dennislee.html"
    def tearDown(self):
        del self.strs_before, self.strs_after, self.attrs_fail, self.attrs_pass
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

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
    
    def test_init_100(self):
        with self.assertRaises(TypeError):
            x = hr.Element(self.strs_before[0], **self.attrs_fail)
            del x
    def test_init_101(self):
        with self.assertRaises(TypeError):
            x = hr.Element(self.strs_before[0],
                    id=self.attrs_fail['id'],
                    alt=self.attrs_fail['alt'])
            del x
    def test_init_105(self):
        x = hr.Element(self.strs_before[0], **self.attrs_pass)
        x.tag = self.random_tag
        with open(self.test_filename, 'w') as fobj:
            self.assertTrue(x.render(fobj, '    '))
        with open(self.test_filename, 'r') as f:
            str = f.read()
        self.assertEqual(str, '<SomeTagName id="Marker" alt="Fancy Pants">\n'
                f'    {self.strs_after[0]}\n'
                '</SomeTagName>\n')
        del x, fobj, f
    def test_init_106(self):
        x = hr.Element(**self.attrs_pass)
        x.append(self.strs_before[0])
        x.append(self.strs_before[1])
        x.tag = self.random_tag
        with open(self.test_filename, 'w') as fobj:
            self.assertTrue(x.render(fobj, '    '))
        with open(self.test_filename, 'r') as f:
            str = f.read()
        self.assertEqual(str, '<SomeTagName id="Marker" alt="Fancy Pants">\n'
                f'    {self.strs_after[0]} {self.strs_after[1]}\n'
                '</SomeTagName>\n')
        del x, fobj, f
    def test_init_107(self):
        x = hr.Element(self.strs_before[0], **self.attrs_pass)
        y = hr.P(self.strs_before[1])
        x.append(y)
        x.append(self.strs_before[2])
        x.tag = self.random_tag
        with open(self.test_filename, 'w') as fobj:
            self.assertTrue(x.render(fobj, '    '))
        with open(self.test_filename, 'r') as f:
            str = f.read()
            self.assertEqual(str, '<SomeTagName id="Marker" alt="Fancy Pants">\n'
                    f'    {self.strs_after[0]}\n'
                    '    <p>\n'
                    f'        {self.strs_after[1]}\n'
                    '    </p>\n'
                    f'    {self.strs_after[2]}\n'
                    '</SomeTagName>\n')
        del x, y, fobj, f


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
        result = False
        self.e = hr.Element()
        if element_tag:
            self.e.tag = element_tag
        for str in self.strs_before:
            self.e.append(str)
        with open(self.test_filename, 'w') as fobj:
            self.assertTrue(self.e.render(fobj, ind))
        with open(self.test_filename, 'r') as f:
            self.strs_out = f.readlines()
            self.assertEqual(len(self.strs_out), 3)
            self.assertEqual(self.strs_out[0], f"<{element_tag}>\n")
            self.assertEqual(self.strs_out[1], 
                    ind + ' '.join(self.strs_after) + '\n')
            self.assertEqual(self.strs_out[-1], f"</{element_tag}>\n")
            del self.strs_out
            result = True
        del self.e, fobj, f
        return result

    def test_P_element_1(self):
        para = hr.P()
        for string in self.strs_before:
            para.append(string)
        self.assertEqual(para.contents, list(self.strs_after))
        del para
    def test_P_element_2(self):
        para = hr.P(self.strs_before[0])
        for string in self.strs_before[1:]:
            para.append(string)
        self.assertEqual(para.contents, list(self.strs_after))
        del para
    def test_Body_element_1(self):
        bod = hr.Body()
        for string in self.strs_before:
            bod.append(string)
        self.assertEqual(bod.contents, list(self.strs_after))
        del bod
    def test_Body_element_2(self):
        bod = hr.Body(self.strs_before[0])
        for string in self.strs_before[1:]:
            bod.append(string)
        self.assertEqual(bod.contents, list(self.strs_after))
        del bod
    def test_Html_element_1(self):
        pg = hr.Html()
        for string in self.strs_before:
            pg.append(string)
        self.assertEqual(pg.contents, list(self.strs_after))
        del pg
    def test_Html_element_2(self):
        pg = hr.Html(self.strs_before[0])
        for string in self.strs_before[1:]:
            pg.append(string)
        self.assertEqual(pg.contents, list(self.strs_after))
        del pg
    def test_Head_element_1(self):
        title = hr.Title('    \tSome \t marquee \t  text    \n')
        head = hr.Head(title)
        with open(self.test_filename, 'w') as fobj:
            self.assertTrue(head.render(fobj, '    '))
        with open(self.test_filename, 'r') as f:
            self.strs_out = f.readlines()
            self.assertEqual(len(self.strs_out), 3)
            self.assertEqual(self.strs_out[0], "<head>\n")
            self.assertEqual(self.strs_out[1], 
                    "    <title>Some marquee text</title>\n")
            self.assertEqual(self.strs_out[2], "</head>\n")
            del self.strs_out
        del head, title, fobj, f

    def test_hierarchical_1(self):
        para1 = hr.P(self.strs_before[0])
        para1.append(self.strs_before[1])
        para2 = hr.P(self.strs_before[2])
        para2.append(self.strs_before[3])
        para3 = hr.P(self.strs_before[4])
        para3.append(self.strs_before[5])

        bod = hr.Body()
        bod.append(para1)
        bod.append(para2)
        bod.append(para3)
        
        pg = hr.Html(bod)

        self.test_filename = 'test_hierarchical.html'
        with open(self.test_filename, 'w') as fobj:
            self.assertTrue(pg.render(fobj, '    '))
        with open(self.test_filename, 'r') as f:
            self.strs_out = f.readlines()
            self.assertEqual(len(self.strs_out), 13)
            self.assertEqual(self.strs_out[0], "<html>\n")
            self.assertEqual(self.strs_out[1], "    <body>\n")
            self.assertEqual(self.strs_out[2], "        <p>\n")
            self.assertEqual(self.strs_out[3], "            " +
                    self.strs_after[0] + " " +
                    self.strs_after[1] + "\n")
            self.assertEqual(self.strs_out[4], "        </p>\n")
            self.assertEqual(self.strs_out[5], "        <p>\n")
            self.assertEqual(self.strs_out[6], "            " +
                    self.strs_after[2] + " " +
                    self.strs_after[3] + "\n")
            self.assertEqual(self.strs_out[7], "        </p>\n")
            self.assertEqual(self.strs_out[8], "        <p>\n")
            self.assertEqual(self.strs_out[9], "            " +
                    self.strs_after[4] + " " +
                    self.strs_after[5] + "\n")
            self.assertEqual(self.strs_out[-3], "        </p>\n")
            self.assertEqual(self.strs_out[-2], "    </body>\n")
            self.assertEqual(self.strs_out[-1], "</html>\n")
            del self.strs_out
        del pg, bod, para1, para2, para3, fobj, f

    def test_OneLineTag_1(self):
        para = hr.P(self.strs_before[0])
        bod = hr.Body(para)
        elem = hr.OneLineTag(bod)
        elem.tag = self.random_tag
        with open(self.test_filename, 'w') as fobj:
            with self.assertRaises(TypeError):
                elem.render(fobj, '    ')
        del elem, bod, para, fobj
    def test_OneLineTag_2(self):
        para = hr.P(self.strs_before[0])
        elem = hr.OneLineTag()
        elem.tag = self.random_tag
        for str in self.strs_before:
            elem.append(str)
        elem.append(para)
        with open(self.test_filename, 'w') as fobj:
            with self.assertRaises(TypeError):
                elem.render(fobj, '    ')
        del elem, para, fobj
    def test_OneLineTag_3(self):
        elem = hr.OneLineTag(self.strs_before[0])
        elem.tag = self.random_tag
        with open(self.test_filename, 'w') as fobj:
            self.assertTrue(elem.render(fobj, '    '))
        with open(self.test_filename, 'r') as f:
            str_out = f.read()
        self.assertEqual(str_out, 
                "    <{0}>{1}</{0}>\n".format(elem.tag, self.strs_after[0]))
        del fobj, f, elem
    def test_OneLineTag_4(self):
        elem = hr.OneLineTag()
        elem.tag = self.random_tag
        for str in self.strs_before:
            elem.append(str)
        with open(self.test_filename, 'w') as fobj:
            self.assertTrue(elem.render(fobj, '    '))
        with open(self.test_filename, 'r') as f:
            str_out = f.read()
        self.assertEqual(str_out, 
                "    <{0}>{1}</{0}>\n".format(
                elem.tag, ' '.join(self.strs_after)))
        del fobj, f, elem
    def test_Title_1(self):
        elem = hr.Title()
        for str in self.strs_before:
            elem.append(str)
        with open(self.test_filename, 'w') as fobj:
            self.assertTrue(elem.render(fobj, '    '))
        with open(self.test_filename, 'r') as f:
            str_out = f.read()
        self.assertEqual(str_out, "    <{0}>{1}</{0}>\n".format(
                "title", ' '.join(self.strs_after)))
        del fobj, f, elem

        




if __name__ == '__main__':
    unittest.main()
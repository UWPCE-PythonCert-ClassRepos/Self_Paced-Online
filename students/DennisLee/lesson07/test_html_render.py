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
    def test_init_8(self):
        x = hr.Element(self.strs_before)
        self.assertEqual(x.contents, list(self.strs_after))
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
    def test_append_5(self):
        self.e = hr.Element(self.strs_before[:2])
        self.e.append(self.strs_before[2:4])
        self.assertEqual(self.e.contents, list(self.strs_after[:4]))
        del self.e


    def test_render_1(self):
        self.e = hr.Element()
        with self.assertRaises(ValueError):
            self.e.render('', '  ')
        del self.e
    def test_render_2(self):
        self.e = hr.Element()
        with self.assertRaises(AttributeError):
            self.e.render(self.e, '  ')
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
        result, self.strs_out, self.e = False, None, hr.Element()
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
            result = True
        del self.e, fobj, f, self.strs_out
        return result

    def test_P_element_1(self):
        para = hr.P()
        para.append(self.strs_before)
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
        self.strs_out, head = None, hr.Head(title)
        with open(self.test_filename, 'w') as fobj:
            self.assertTrue(head.render(fobj, '    '))
        with open(self.test_filename, 'r') as f:
            self.strs_out = f.readlines()
            self.assertEqual(len(self.strs_out), 3)
            self.assertEqual(self.strs_out[0], "<head>\n")
            self.assertEqual(self.strs_out[1], 
                    "    <title>Some marquee text</title>\n")
            self.assertEqual(self.strs_out[2], "</head>\n")
        del head, title, fobj, f, self.strs_out

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
            self.assertEqual(str_out, "<{0}>{1}</{0}>\n".format(
                    elem.tag, self.strs_after[0]))
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
                    "<{0}>{1}</{0}>\n".format(
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
            self.assertEqual(str_out, "<{0}>{1}</{0}>\n".format(
                    "title", ' '.join(self.strs_after)))
        del fobj, f, elem

    def test_SelfClosingTag_10(self):
        elem = hr.SelfClosingTag()
        elem.tag = self.random_tag
        with open(self.test_filename, 'w') as fobj:
            self.assertTrue(elem.render(fobj, '    '))
        with open(self.test_filename, 'r') as f:
            str_out = f.read()
            self.assertEqual(str_out, f"<SomeTagName />\n")
        del fobj, f, elem
    def test_SelfClosingTag_20(self):
        elem = hr.SelfClosingTag(**self.attrs_pass)
        elem.tag = self.random_tag
        with open(self.test_filename, 'w') as fobj:
            self.assertTrue(elem.render(fobj, '    '))
        with open(self.test_filename, 'r') as f:
            str_out = f.read()
            self.assertEqual(
                    str_out, '<SomeTagName id="Marker" alt="Fancy Pants" />\n')
        del fobj, f, elem
    def test_SelfClosingTag_25(self):
        horizontal_rule = hr.Hr(**self.attrs_pass)
        line_break = hr.Br(id='My'+self.attrs_pass['id'],
                alt=self.attrs_pass['alt']+' and Shirts')
        para = hr.P(self.strs_before[0])
        para.append(line_break)
        para.append(self.strs_before[1])
        body = hr.Body()
        body.append(horizontal_rule)
        body.append(para)
        with open(self.test_filename, 'w') as fobj:
            self.assertTrue(body.render(fobj, '    '))
        with open(self.test_filename, 'r') as f:
            strs_out = f.readlines()
            self.assertEqual(len(strs_out), 8)
            self.assertEqual(strs_out[0],  '<body>\n')
            self.assertEqual(strs_out[1],  '    <hr id="Marker" alt="Fancy Pants" />\n')
            self.assertEqual(strs_out[2],  '    <p>\n')
            self.assertEqual(strs_out[3], f'        {self.strs_after[0]}\n')
            self.assertEqual(strs_out[4],  '        <br id="MyMarker" alt="Fancy Pants and Shirts" />\n')
            self.assertEqual(strs_out[5], f'        {self.strs_after[1]}\n')
            self.assertEqual(strs_out[6],  '    </p>\n')
            self.assertEqual(strs_out[7],  '</body>\n')
        del fobj, f, horizontal_rule, line_break, para, body, strs_out

    def test_Br_1(self):
        with self.assertRaises(TypeError):
            elem = hr.Br(self.strs_before[0])
            del elem
    def test_Br_2(self):
        with self.assertRaises(TypeError):
            elem = hr.Br(self.strs_before[0], **self.attrs_pass)
            del elem
    def test_Br_3(self):
        elem, t = hr.Br(), hr.Title()
        with self.assertRaises(TypeError):
            elem.append(t)
        del elem, t
    def test_Br_10(self):
        line_break = hr.Br()
        with open(self.test_filename, 'w') as fobj:
            self.assertTrue(line_break.render(fobj, '    '))
        with open(self.test_filename, 'r') as f:
            str_out = f.read()
            self.assertEqual(str_out, '<br />\n')
        del line_break, f, fobj
    def test_Br_20(self):
        line_break = hr.Br(**self.attrs_pass)
        with open(self.test_filename, 'w') as fobj:
            self.assertTrue(line_break.render(fobj, '    '))
        with open(self.test_filename, 'r') as f:
            str_out = f.read()
            self.assertEqual(str_out, '<br id="Marker" alt="Fancy Pants" />\n')
        del line_break, f, fobj

    def test_Hr_1(self):
        elem, t = None, hr.Title()
        with self.assertRaises(TypeError):
            elem = hr.Hr(t)
        del elem, t
    def test_Hr_2(self):
        elem, t = None, hr.Title()
        with self.assertRaises(TypeError):
            elem = hr.Hr(t, **self.attrs_pass)
        del elem, t
    def test_Hr_3(self):
        elem = hr.Hr()
        with self.assertRaises(TypeError):
            elem.append(self.strs_before[0])
        del elem
    def test_Hr_10(self):
        horizontal_rule = hr.Hr()
        with open(self.test_filename, 'w') as fobj:
            self.assertTrue(horizontal_rule.render(fobj, '    '))
        with open(self.test_filename, 'r') as f:
            str_out = f.read()
            self.assertEqual(str_out, '<hr />\n')
        del horizontal_rule, f, fobj
    def test_Hr_20(self):
        horizontal_rule = hr.Hr(**self.attrs_pass)
        with open(self.test_filename, 'w') as fobj:
            self.assertTrue(horizontal_rule.render(fobj, '    '))
        with open(self.test_filename, 'r') as f:
            str_out = f.read()
            self.assertEqual(str_out, '<hr id="Marker" alt="Fancy Pants" />\n')
        del horizontal_rule, f, fobj

    def test_A_201(self):
        with self.assertRaises(TypeError):
            link = hr.A("   https://www.wikipedia.org/  ", 50)
            del link
    def test_A_202(self):
        with self.assertRaises(TypeError):
            link = hr.A(self.attrs_pass, 
                    '\t   \t  \n  Grand \t \tWiki   \t\n   \t')
            del link
    def test_A_203(self):
        link = hr.A("   https://www.wikipedia.org/  ", 
                '\t   \t  \n  Grand \t \tWiki   \t\n   \t')
        with open(self.test_filename, 'w') as fobj:
            self.assertTrue(link.render(fobj, '    '))
        with open(self.test_filename, 'r') as f:
            str_out = f.read()
            self.assertEqual(str_out, 
                    '<a href="https://www.wikipedia.org/">Grand Wiki</a>\n')
        del link, f, fobj
    def test_A_204(self):
        strs_out = None
        para = hr.P(
                "  \t  Here's \t Britannica's  \nworst\t  nightmare: \n\n\t  ")
        link = hr.A("   https://www.wikipedia.org/  ", 
                '\t   \t  \n  Grand \t \tWiki   \t\n   \t')
        para.append(link)
        para.append(" \t . \n    ")
        body = hr.Body(para)
        with open(self.test_filename, 'w') as fobj:
            self.assertTrue(body.render(fobj, '   '))
        with open(self.test_filename, 'r') as f:
            strs_out = f.readlines()
            self.assertEqual(len(strs_out), 7)
            self.assertEqual(strs_out[0], '<body>\n')
            self.assertEqual(strs_out[1], '   <p>\n')
            self.assertEqual(strs_out[2], 
                    "      Here's Britannica's worst nightmare:\n")
            self.assertEqual(strs_out[3], '      '
                    '<a href="https://www.wikipedia.org/">Grand Wiki</a>\n')
            self.assertEqual(strs_out[4], '      .\n')
            self.assertEqual(strs_out[5], '   </p>\n')
            self.assertEqual(strs_out[6], '</body>\n')
        del strs_out, para, link, body, f, fobj
        

    def test_Ul_100(self):
        strs_out, br = None, hr.Br()
        line_items = [hr.Li(self.strs_before[i]) for i in range(3)]
        line_items.append(hr.Li(
                id=" \n \t First \n \n \t ", alt="  Hi \t\t there!  \n"))
        line_items[3].append([self.strs_before[3], br, self.strs_before[4]])
        line_items.append(hr.Li(self.strs_before[-1]))
        ul = hr.Ul(**self.attrs_pass)
        ul.append(line_items)
        with open(self.test_filename, 'w') as fobj:
            self.assertTrue(ul.render(fobj, '  '))
        with open(self.test_filename, 'r') as f:
            strs_out = f.readlines()
            self.assertEqual(len(strs_out), 19)
            self.assertEqual(strs_out[0],   '<ul id="Marker" alt="Fancy Pants">\n')
            self.assertEqual(strs_out[1],   '  <li>\n')
            self.assertEqual(strs_out[2],  f'    {self.strs_after[0]}\n')
            self.assertEqual(strs_out[3],   '  </li>\n')
            self.assertEqual(strs_out[4],   '  <li>\n')
            self.assertEqual(strs_out[5],  f'    {self.strs_after[1]}\n')
            self.assertEqual(strs_out[6],   '  </li>\n')
            self.assertEqual(strs_out[7],   '  <li>\n')
            self.assertEqual(strs_out[8],  f'    {self.strs_after[2]}\n')
            self.assertEqual(strs_out[9],   '  </li>\n')
            self.assertEqual(strs_out[10],  '  <li id="First" alt="Hi there!">\n')
            self.assertEqual(strs_out[11], f'    {self.strs_after[3]}\n')
            self.assertEqual(strs_out[12],  '    <br />\n')
            self.assertEqual(strs_out[13], f'    {self.strs_after[4]}\n')
            self.assertEqual(strs_out[14],  '  </li>\n')
            self.assertEqual(strs_out[15],  '  <li>\n')
            self.assertEqual(strs_out[16], f'    {self.strs_after[5]}\n')
            self.assertEqual(strs_out[17],  '  </li>\n')
            self.assertEqual(strs_out[18],  '</ul>\n')
        del strs_out, line_items, ul, f, fobj
        
    def test_H_050(self):
        with self.assertRaises(ValueError):
            header = hr.H(7, "Some header")
            del header
    def test_H_051(self):
        with self.assertRaises(ValueError):
            header = hr.H(0, "Some header")
            del header
    def test_H_052(self):
        with self.assertRaises(ValueError):
            header = hr.H(-3, "Some header")
            del header
    def test_H_053(self):
        with self.assertRaises(ValueError):
            header = hr.H(10, "Some header")
            del header
    def test_H_060(self):
        with self.assertRaises(TypeError):
            header = hr.H(2.0, "Some header")
            del header
    def test_H_070(self):
        with self.assertRaises(TypeError):
            header = hr.H(1, 50)
            del header
    def test_H_071(self):
        with self.assertRaises(TypeError):
            header = hr.H(1, 60.5)
            del header
    def test_H_072(self):
        with self.assertRaises(TypeError):
            header = hr.H(1, ["header part 1", "header part 2"])
            del header
    def test_H_073(self):
        with self.assertRaises(TypeError):
            para = hr.P("A paragraph.")
            header = hr.H(1, para)
            del header, para
    def test_H_080(self):
        with self.assertRaises(TypeError):
            header = hr.H(2, "Header text", id=50)
            del header

    def test_H_100(self):
        headers_and_p = [hr.H(i, self.strs_before[i-1]) for i in range(1, 6)]
        para = hr.P("\tText   under \n heading   \t5.    \n\t")
        headers_and_p.append(para)
        headers_and_p.append(hr.H(6, self.strs_after[5], alt='Some hover text'))
        strs_out, body = None, hr.Body(headers_and_p)
        with open(self.test_filename, 'w') as fobj:
            self.assertTrue(body.render(fobj, '  '))
        with open(self.test_filename, 'r') as f:
            strs_out = f.readlines()
            self.assertEqual(len(strs_out), 11)
            self.assertEqual(strs_out[0],  '<body>\n')
            self.assertEqual(strs_out[1], f'  <h1>{self.strs_after[0]}</h1>\n')
            self.assertEqual(strs_out[2], f'  <h2>{self.strs_after[1]}</h2>\n')
            self.assertEqual(strs_out[3], f'  <h3>{self.strs_after[2]}</h3>\n')
            self.assertEqual(strs_out[4], f'  <h4>{self.strs_after[3]}</h4>\n')
            self.assertEqual(strs_out[5], f'  <h5>{self.strs_after[4]}</h5>\n')
            self.assertEqual(strs_out[6], f'  <p>\n')
            self.assertEqual(strs_out[7], f'    Text under heading 5.\n')
            self.assertEqual(strs_out[8], f'  </p>\n')
            self.assertEqual(strs_out[9], 
                    f'  <h6 alt="Some hover text">{self.strs_after[5]}</h6>\n')
            self.assertEqual(strs_out[10],  '</body>\n')
        del strs_out, body, para, headers_and_p, f, fobj
        

        
        
        

        




if __name__ == '__main__':
    unittest.main()
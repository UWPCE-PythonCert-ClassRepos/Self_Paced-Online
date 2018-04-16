#!/usr/bin/env python3

import unittest
import html_render as hr

class ElementTestCase(unittest.TestCase):
    def setUp(self):
        self.e = hr.Element()
        hr.Element.tag = "html"
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
        del self.e
        del self.strs_before
        del self.strs_after

    def test_init_1(self):
        x = hr.Element(self.strs_before[0])
        self.assertEqual(x.contents, [self.strs_after[0]])
        del x
    def test_init_2(self):
        x = hr.Element(70)
        self.assertEqual(x.contents, [])
        del x
    def test_init_3(self):
        x = hr.Element('')
        self.assertEqual(x.contents, [])
        del x
    def test_init_4(self):
        x = hr.Element(self.strs_before[0])
        x.append(self.strs_before[1])
        self.assertEqual(x.contents, list(self.strs_after[:2]))
        del x

    def test_append_internal(self):
        self.assertEqual(len(self.strs_before), len(self.strs_after))
    def test_append_1(self):
        self.e.append(50)
        self.assertEqual(self.e.contents, [])
    def test_append_2(self):
        for i in range(len(self.strs_before)):
            self.e.append(self.strs_before[i])
            self.assertEqual(self.e.contents, list(self.strs_after[:i+1]))

    def test_render_1(self):
        self.assertFalse(self.e.render('', '  '))
    def test_render_2(self):
        self.assertFalse(self.e.render('Bogus2\\Bogus3\\Bogosity.txt', '  '))
    def test_render_3(self):
        self.assertFalse(self.e.render('R:\\Bogus2\\Bogus3\\Bogosity.txt', '  '))
    def test_render_4(self):
        self.assertFalse(self.e.render(100, '  '))
    def test_render_5(self):
        self.assertFalse(self.e.render('cannot_overwrite.txt', '  '))
    def test_render_100(self):
        self.assertTrue(self.render_helper('test_html_file.html', '', 'html'))
    def test_render_101(self):
        self.assertTrue(self.render_helper('test_html_file.html', '  ', 'html'))
    def test_render_102(self):
        self.assertTrue(self.render_helper('test_html_file.html', '    ', 'html'))
    def test_render_103(self):
        self.assertTrue(self.render_helper('test_html_file.html', 'dfafd', 'html'))
    def test_render_104(self):
        self.assertTrue(self.render_helper('test_html_file.html', '   -9 \n ', 'html'))
    def test_render_105(self):
        self.assertTrue(self.render_helper('test_html_file.html', '  0 \t   ', 'html'))
    def test_render_106(self):
        self.assertTrue(self.render_helper('test_html_file.html', ' \n  6 ', 'html'))
    def render_helper(self, filename, ind, element_tag):
        result = False
        for str in self.strs_before:
            self.e.append(str)
        try:
            fobj = open(filename, 'w')
        except FileNotFoundError:
            print(f"\n\tFile '{filename}' does not exist.\n")
        except PermissionError:
            print(f"Cannot write to file '{filename}'.")
        else:
            result = self.e.render(fobj, ind)
            if result:
                try:
                    ind = int(ind)
                except ValueError:
                    print(f"\n\tIllegal indent value '{ind}'' - "
                            "defaults to 2.\n")
                    ind = 2
                finally:
                    if ind <= 0:
                        ind = 2
                    with open(filename, 'r') as f:
                        self.strs_out = f.readlines()
                    # self.assertEqual(len(self.strs_out), 3)
                    self.assertEqual(self.strs_out[0], f"<{element_tag}>\n")
                    self.assertEqual(self.strs_out[-1], f"</{element_tag}>\n")
                    # self.assertEqual(self.strs_out[1], 
                    #         ' '*ind + ' '.join(self.strs_after) + ' \n')
            fobj.close()
        finally:
            return result

class Step2ElementTestCase(ElementTestCase):
    def setUp(self):
        self.html_element = hr.Html()
        self.body_element = hr.Body()
        self.p1_element = hr.P("hello")
        self.p2_element = hr.P()
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
                "I told you about..."
                "There's a somebody I'm longing to see",
                "Someone who'll watch over me",
                "I did it my way"
        )
    def tearDown(self):
        del self.html_element
        del self.p1_element
        del self.p2_element
        del self.body_element

    def test_render_P(self):
        para = hr.P(self.strs_before[0])
        for string in self.strs_before[1:]:
            para.append(string)
        self.assertEqual(para.contents, list(self.strs_after))
    def test_Body_element_1(self):
        bod = hr.Body(self.strs_before[0])
        for string in self.strs_before[1:]:
            bod.append(string)
        self.assertEqual(bod.contents, list(self.strs_after))
    def test_Html_element_1(self):
        pg = hr.Html(self.strs_before[0])
        for string in self.strs_before[1:]:
            pg.append(string)
        self.assertEqual(pg.contents, list(self.strs_after))
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


if __name__ == '__main__':
    unittest.main()
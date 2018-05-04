#!/usr/bin/env python3

import unittest, os
import html_render as hr

class consts():
    strs_before = (
            "  \n Why  am   \n\tI here?     \t",
            "\n\t  \n  Here's   that rainy   day...   \t  \n",
            "I told  you   about...\n",
            "    \n \t  \n  There's  a   somebody I'm longing  to   see\n",
            "   \n \t \t Someone  who'll \twatch\nover\nme   \t   ",
            "\tI\tdid\nit\t\tmy      \n\n\t\tway\t\t\n\t"
    )
    strs_after = (
            "Why am I here?", 
            "Here's that rainy day...",
            "I told you about...",
            "There's a somebody I'm longing to see",
            "Someone who'll watch over me",
            "I did it my way"
    )
    attrs_fail = {
        'id': 60,
        'alt': '  \t  \n \tFancy      \t\t   Pants   \n\n\t\n '
    }
    attrs_pass = {
        'id': 'Marker',
        'alt': '  \t  \n \tFancy      \t\t   Pants   \n\n\t\n '
    }
    random_tag = " \t SomeTagName \n "
    test_filename = "test_html_file_dennislee.html"


class ElementTestCase(unittest.TestCase):
    def setUp(self):
        """
        Initialize output string list, stream/file objects, and three
        test elements. Also make sure the test input and output string
        lists have the same number of items.
        """
        self.strs_out, self.file, self.fobj = None, None, None
        self.e1, self.e2, self.e3 = None, None, None
        self.assertEqual(len(consts.strs_before), len(consts.strs_after))        
    def tearDown(self):
        """Delete setup objects and test file (if necessary)."""
        del self.strs_out, self.file, self.fobj
        del self.e1, self.e2, self.e3
        if os.path.exists(consts.test_filename):
            os.remove(consts.test_filename)

    # Test initializer response with various (types of) content values
    def test_init_1(self):  # String content => normalized string content
        self.e1 = hr.Element(consts.strs_before[0])
        self.assertEqual(self.e1.contents, [consts.strs_after[0]])
    def test_init_2(self):  # Float content => type exception
        with self.assertRaises(TypeError):
            self.e1 = hr.Element(70.0)
    def test_init_3(self):  # Empty string => not added, no code break
        self.e1 = hr.Element('')
        self.assertEqual(self.e1.contents, [])
    def test_init_4(self):  # Whitespace => not added, no code break
        self.e1 = hr.Element('\t\n    ')
        self.assertEqual(self.e1.contents, [])
    def test_init_5(self):  # String content + append => 2-item string list
        self.e1 = hr.Element(consts.strs_before[0])
        self.e1.append(consts.strs_before[1])
        self.assertEqual(self.e1.contents, list(consts.strs_after[:2]))
    def test_init_6(self):  # No content => Empty content list
        self.e1 = hr.Element()
        self.assertEqual(self.e1.contents, [])
    def test_init_7(self):  # `None` passed => Empty content list
        self.e1 = hr.Element(None)
        self.assertEqual(self.e1.contents, [])
    # String list passed => Content is list of normalized strings
    def test_init_8(self):
        self.e1 = hr.Element(consts.strs_before)
        self.assertEqual(self.e1.contents, list(consts.strs_after))
    
    # Test initializer response to various attribute input
    def test_init_100(self):  # Attribute dict has int value => Type exception
        with self.assertRaises(TypeError):
            self.e1 = hr.Element(consts.strs_before[0], **consts.attrs_fail)
    # Int attribute value  passed as keyword argument => Type exception
    def test_init_101(self):
        with self.assertRaises(TypeError):
            self.e1 = hr.Element(consts.strs_before[0],
                    id=consts.attrs_fail['id'],
                    alt=consts.attrs_fail['alt'])
    # Attribute dict of strings passed with content => content and
    # attributes rendered with strings normalized, as expected
    def test_init_105(self):
        self.e1 = hr.Element(consts.strs_before[0], **consts.attrs_pass)
        self.e1.tag = consts.random_tag.strip()
        with open(consts.test_filename, 'w') as self.fobj:
            self.assertTrue(self.e1.render(self.fobj, '    '))
        with open(consts.test_filename, 'r') as self.file:
            str = self.file.read()
        self.assertEqual(str, '<SomeTagName id="Marker" alt="Fancy Pants">\n'
                f'    {consts.strs_after[0]}\n'
                '</SomeTagName>\n')
    # Attributes alone passed in initializer, with child strings
    # appended later => normalized attribute declarations and normalized
    # strings rendered, as expected
    def test_init_106(self):
        self.e1 = hr.Element(**consts.attrs_pass)
        self.e1.append(consts.strs_before[0])
        self.e1.append(consts.strs_before[1])
        self.e1.tag = consts.random_tag.strip()
        with open(consts.test_filename, 'w') as self.fobj:
            self.assertTrue(self.e1.render(self.fobj, '    '))
        with open(consts.test_filename, 'r') as self.file:
            str = self.file.read()
        self.assertEqual(str, '<SomeTagName id="Marker" alt="Fancy Pants">\n'
                f'    {consts.strs_after[0]} {consts.strs_after[1]}\n'
                '</SomeTagName>\n')
    # Attributes alone passed in initializer, with child strings/elements
    # appended later => normalized attribute declarations and normalized
    # strings/elements rendered, as expected
    def test_init_107(self):
        self.e1 = hr.Element(consts.strs_before[0], **consts.attrs_pass)
        self.e2 = hr.P(consts.strs_before[1])
        self.e1.append(self.e2)
        self.e1.append(consts.strs_before[2])
        self.e1.tag = consts.random_tag.strip()
        with open(consts.test_filename, 'w') as self.fobj:
            self.assertTrue(self.e1.render(self.fobj, '    '))
        with open(consts.test_filename, 'r') as self.file:
            str = self.file.read()
            self.assertEqual(str, '<SomeTagName id="Marker" alt="Fancy Pants">\n'
                    f'    {consts.strs_after[0]}\n'
                    '    <p>\n'
                    f'        {consts.strs_after[1]}\n'
                    '    </p>\n'
                    f'    {consts.strs_after[2]}\n'
                    '</SomeTagName>\n')

    # Test the `append` method with various (types of) values
    def test_append_1(self):  # Append an int to empty content => Type exception
        self.e1 = hr.Element()
        with self.assertRaises(TypeError):
            self.e1.append(50)
    # Append an int to existing content => Type exception
    def test_append_2(self):  
        self.e1 = hr.Element(consts.strs_before[0])
        with self.assertRaises(TypeError):
            self.e1.append(50)
    # Append strings to empty content => Normalized string list
    def test_append_3(self):  
        self.e1 = hr.Element()
        for i in range(len(consts.strs_before)):
            self.e1.append(consts.strs_before[i])
            self.e1.append("  ")
            self.assertEqual(self.e1.contents, list(consts.strs_after[:i+1]))
    # Append strings to existing string content => Normalized string list
    def test_append_4(self):
        self.e1 = hr.Element(consts.strs_before[0])
        for i in range(1, len(consts.strs_before)):
            self.e1.append(consts.strs_before[i])
            self.e1.append("  ")
            self.assertEqual(self.e1.contents, list(consts.strs_after[:i+1]))
    # Append strings to existing string list => Larger normalized string list
    def test_append_5(self):
        self.e1 = hr.Element(consts.strs_before[:2])
        self.e1.append(consts.strs_before[2:4])
        self.assertEqual(self.e1.contents, list(consts.strs_after[:4]))

    # Test the `append` method with various (types of) values
    def test_render_1(self):  # Empty output stream specified => Value exception
        self.e1 = hr.Element()
        with self.assertRaises(ValueError):
            self.e1.render('', '  ')
    # Element specified for output stream => Attribute exception
    def test_render_2(self):
        self.e1 = hr.Element()
        with self.assertRaises(AttributeError):
            self.e1.render(self.e1, '  ')
    # `render` method works successfully at indent = 0, 2, or 4 spaces
    def test_render_100(self):
        self.assertTrue(self.render_helper('', 'html'))
    def test_render_101(self):
        self.assertTrue(self.render_helper('  ', 'html'))
    def test_render_102(self):
        self.assertTrue(self.render_helper('    ', 'html'))
    # `render` results in a type error if indent is specified as an int value
    def test_render_103(self):
        with self.assertRaises(TypeError):
            self.render_helper(2, 'html')
    # `render` => value exception if the indent string contains printable chars
    def test_render_104(self):
        with self.assertRaises(ValueError):
            self.render_helper('dfafd', 'html')
    # `render` => value exception if the indent string contains tabs
    def test_render_105(self):
        with self.assertRaises(ValueError):
            self.render_helper('\t', 'html')
    def render_helper(self, ind, element_tag=''):
        """
        Internal helper function to wrap around the `render` method for
        a basic nonspecialized element.

        :ind:  The indentation between levels, as a string of spaces.

        :element_tag:  The element's tag name.

        :return:  `True` if successful; otherwise, `False`.
        """
        result, self.e1 = False, hr.Element()
        if element_tag:
            self.e1.tag = element_tag
        for str in consts.strs_before:
            self.e1.append(str)
        with open(consts.test_filename, 'w') as self.fobj:
            self.assertTrue(self.e1.render(self.fobj, ind))
        with open(consts.test_filename, 'r') as self.file:
            self.strs_out = self.file.readlines()
            self.assertEqual(len(self.strs_out), 3)  # Verify total lines
            self.assertEqual(self.strs_out[0], f"<{element_tag}>\n")
            self.assertEqual(self.strs_out[1], 
                    ind + ' '.join(consts.strs_after) + '\n')
            self.assertEqual(self.strs_out[-1], f"</{element_tag}>\n")
            result = True
        return result

    # Test P element init/append methods against the content list
    def test_P_element_1(self):
        self.e1 = hr.P()
        self.e1.append(consts.strs_before)
        self.assertEqual(self.e1.contents, list(consts.strs_after))
    def test_P_element_2(self):
        self.e1 = hr.P(consts.strs_before[0])
        for string in consts.strs_before[1:]:
            self.e1.append(string)
        self.assertEqual(self.e1.contents, list(consts.strs_after))
    # Test Body element init/append methods against the content list
    def test_Body_element_1(self):
        self.e1 = hr.Body()
        for string in consts.strs_before:
            self.e1.append(string)
        self.assertEqual(self.e1.contents, list(consts.strs_after))
    def test_Body_element_2(self):
        self.e1 = hr.Body(consts.strs_before[0])
        for string in consts.strs_before[1:]:
            self.e1.append(string)
        self.assertEqual(self.e1.contents, list(consts.strs_after))
    # Test Html element init/append methods against the content list
    def test_Html_element_1(self):
        self.e1 = hr.Html()
        for string in consts.strs_before:
            self.e1.append(string)
        self.assertEqual(self.e1.contents, list(consts.strs_after))
    def test_Html_element_2(self):
        self.e1 = hr.Html(consts.strs_before[0])
        for string in consts.strs_before[1:]:
            self.e1.append(string)
        self.assertEqual(self.e1.contents, list(consts.strs_after))
    # Test Head element w/appended Title element against rendering
    def test_Head_element_1(self):
        self.e2 = hr.Title('    \tSome \t marquee \t  text    \n')
        self.e1 = hr.Head(self.e2)
        with open(consts.test_filename, 'w') as self.fobj:
            self.assertTrue(self.e1.render(self.fobj, '    '))
        with open(consts.test_filename, 'r') as self.file:
            self.strs_out = self.file.readlines()
            self.assertEqual(len(self.strs_out), 3)  # Verify total lines
            self.assertEqual(self.strs_out[0], "<head>\n")
            self.assertEqual(self.strs_out[1], 
                    "    <title>Some marquee text</title>\n")
            self.assertEqual(self.strs_out[2], "</head>\n")

    # Test full HTML hierarchical document rendering
    def test_hierarchical_1(self):
        para1 = hr.P(consts.strs_before[0])
        para1.append(consts.strs_before[1])
        para2 = hr.P(consts.strs_before[2])
        para2.append(consts.strs_before[3])
        para3 = hr.P(consts.strs_before[4])
        para3.append(consts.strs_before[5])

        bod = hr.Body()
        bod.append(para1)
        bod.append(para2)
        bod.append(para3)
        
        pg = hr.Html(bod)

        with open(consts.test_filename, 'w') as self.fobj:
            self.assertTrue(pg.render(self.fobj, '    '))
        with open(consts.test_filename, 'r') as self.file:
            self.strs_out = self.file.readlines()
            self.assertEqual(len(self.strs_out), 14)  # Verify total lines
            self.assertEqual(self.strs_out[0], "<!DOCTYPE html>\n")
            self.assertEqual(self.strs_out[1], "<html>\n")
            self.assertEqual(self.strs_out[2], "    <body>\n")
            self.assertEqual(self.strs_out[3], "        <p>\n")
            self.assertEqual(self.strs_out[4], "            " +
                    consts.strs_after[0] + " " +
                    consts.strs_after[1] + "\n")
            self.assertEqual(self.strs_out[5], "        </p>\n")
            self.assertEqual(self.strs_out[6], "        <p>\n")
            self.assertEqual(self.strs_out[7], "            " +
                    consts.strs_after[2] + " " +
                    consts.strs_after[3] + "\n")
            self.assertEqual(self.strs_out[8], "        </p>\n")
            self.assertEqual(self.strs_out[9], "        <p>\n")
            self.assertEqual(self.strs_out[10], "            " +
                    consts.strs_after[4] + " " +
                    consts.strs_after[5] + "\n")
            self.assertEqual(self.strs_out[-3], "        </p>\n")
            self.assertEqual(self.strs_out[-2], "    </body>\n")
            self.assertEqual(self.strs_out[-1], "</html>\n")
        del pg, bod, para1, para2, para3

    # Test single-line tags
    def test_OneLineTag_1(self):  # Can't append child to a one-line tag
        self.e3 = hr.P(consts.strs_before[0])
        self.e2 = hr.Body(self.e3)
        self.e1 = hr.OneLineTag(self.e2)
        self.e1.tag = consts.random_tag.strip()
        with open(consts.test_filename, 'w') as self.fobj:
            with self.assertRaises(TypeError):
                self.e1.render(self.fobj, '    ')
    def test_OneLineTag_2(self):
        self.e2 = hr.P(consts.strs_before[0])
        self.e1 = hr.OneLineTag()
        self.e1.tag = consts.random_tag.strip()
        for str in consts.strs_before:
            self.e1.append(str)
        self.e1.append(self.e2)
        with open(consts.test_filename, 'w') as self.fobj:
            with self.assertRaises(TypeError):
                self.e1.render(self.fobj, '    ')
    # Test one-line tag rendering w/initialized content
    def test_OneLineTag_3(self):  
        self.e1 = hr.OneLineTag(consts.strs_before[0])
        self.e1.tag = consts.random_tag.strip()
        with open(consts.test_filename, 'w') as self.fobj:
            self.assertTrue(self.e1.render(self.fobj, '    '))
        with open(consts.test_filename, 'r') as self.file:
            str_out = self.file.read()
            self.assertEqual(str_out, "<{0}>{1}</{0}>\n".format(
                    self.e1.tag, consts.strs_after[0]))
    # Test one-line tag rendering w/appended content
    def test_OneLineTag_4(self):
        self.e1 = hr.OneLineTag()
        self.e1.tag = consts.random_tag.strip()
        for str in consts.strs_before:
            self.e1.append(str)
        with open(consts.test_filename, 'w') as self.fobj:
            self.assertTrue(self.e1.render(self.fobj, '    '))
        with open(consts.test_filename, 'r') as self.file:
            str_out = self.file.read()
            self.assertEqual(str_out, 
                    "<{0}>{1}</{0}>\n".format(
                    self.e1.tag, ' '.join(consts.strs_after)))
    # Test rendering of the `title` one-line element
    def test_Title_1(self):
        self.e1 = hr.Title()
        for str in consts.strs_before:
            self.e1.append(str)
        with open(consts.test_filename, 'w') as self.fobj:
            self.assertTrue(self.e1.render(self.fobj, '    '))
        with open(consts.test_filename, 'r') as self.file:
            str_out = self.file.read()
            self.assertEqual(str_out, "<{0}>{1}</{0}>\n".format(
                    "title", ' '.join(consts.strs_after)))

    # Test self-closing tags (containing no child text/elements)
    def test_SelfClosingTag_10(self):  # Rendering without attributes
        self.e1 = hr.SelfClosingTag()
        self.e1.tag = consts.random_tag.strip()
        with open(consts.test_filename, 'w') as self.fobj:
            self.assertTrue(self.e1.render(self.fobj, '    '))
        with open(consts.test_filename, 'r') as self.file:
            str_out = self.file.read()
            self.assertEqual(str_out, f"<SomeTagName />\n")
    def test_SelfClosingTag_20(self):  # Rendering with attributes
        self.e1 = hr.SelfClosingTag(**consts.attrs_pass)
        self.e1.tag = consts.random_tag.strip()
        with open(consts.test_filename, 'w') as self.fobj:
            self.assertTrue(self.e1.render(self.fobj, '    '))
        with open(consts.test_filename, 'r') as self.file:
            str_out = self.file.read()
            self.assertEqual(
                    str_out, '<SomeTagName id="Marker" alt="Fancy Pants" />\n')
    def test_SelfClosingTag_25(self):  # Within large doc hierarchy
        horizontal_rule = hr.Hr(**consts.attrs_pass)
        line_break = hr.Br(id='My'+consts.attrs_pass['id'],
                alt=consts.attrs_pass['alt']+' and Shirts')
        para = hr.P(consts.strs_before[0])
        para.append(line_break)
        para.append(consts.strs_before[1])
        body = hr.Body()
        body.append(horizontal_rule)
        body.append(para)
        with open(consts.test_filename, 'w') as self.fobj:
            self.assertTrue(body.render(self.fobj, '    '))
        with open(consts.test_filename, 'r') as self.file:
            self.strs_out = self.file.readlines()
            self.assertEqual(len(self.strs_out), 8)  # Verify total lines
            self.assertEqual(self.strs_out[0],  '<body>\n')
            self.assertEqual(self.strs_out[1],  '    <hr id="Marker" alt="Fancy Pants" />\n')
            self.assertEqual(self.strs_out[2],  '    <p>\n')
            self.assertEqual(self.strs_out[3], f'        {consts.strs_after[0]}\n')
            self.assertEqual(self.strs_out[4],  '        <br id="MyMarker" alt="Fancy Pants and Shirts" />\n')
            self.assertEqual(self.strs_out[5], f'        {consts.strs_after[1]}\n')
            self.assertEqual(self.strs_out[6],  '    </p>\n')
            self.assertEqual(self.strs_out[7],  '</body>\n')
        del horizontal_rule, line_break, para, body

    # Make sure the `br` self-closing tag can't take child text/elements
    def test_Br_1(self):
        with self.assertRaises(TypeError):
            self.e1 = hr.Br(consts.strs_before[0])
    def test_Br_2(self):
        with self.assertRaises(TypeError):
            self.e1 = hr.Br(consts.strs_before[0], **consts.attrs_pass)
    def test_Br_3(self):
        self.e1, self.e2 = hr.Br(), hr.Title()
        with self.assertRaises(TypeError):
            self.e1.append(self.e2)
    # Check rendering of `br` self-closing tag with or without attributes
    def test_Br_10(self):
        self.e1 = hr.Br()
        with open(consts.test_filename, 'w') as self.fobj:
            self.assertTrue(self.e1.render(self.fobj, '    '))
        with open(consts.test_filename, 'r') as self.file:
            str_out = self.file.read()
            self.assertEqual(str_out, '<br />\n')
    def test_Br_20(self):
        self.e1 = hr.Br(**consts.attrs_pass)
        with open(consts.test_filename, 'w') as self.fobj:
            self.assertTrue(self.e1.render(self.fobj, '    '))
        with open(consts.test_filename, 'r') as self.file:
            str_out = self.file.read()
            self.assertEqual(str_out, '<br id="Marker" alt="Fancy Pants" />\n')

    # Make sure the `hr` self-closing tag can't take child text/elements
    def test_Hr_1(self):
        self.e1, self.e2 = None, hr.Title()
        with self.assertRaises(TypeError):
            self.e1 = hr.Hr(self.e2)
    def test_Hr_2(self):
        self.e1, self.e2 = None, hr.Title()
        with self.assertRaises(TypeError):
            self.e1 = hr.Hr(self.e2, **consts.attrs_pass)
    def test_Hr_3(self):
        self.e1 = hr.Hr()
        with self.assertRaises(TypeError):
            self.e1.append(consts.strs_before[0])
    # Check rendering of `hr` self-closing tag with or without attributes
    def test_Hr_10(self):
        self.e1 = hr.Hr()
        with open(consts.test_filename, 'w') as self.fobj:
            self.assertTrue(self.e1.render(self.fobj, '    '))
        with open(consts.test_filename, 'r') as self.file:
            str_out = self.file.read()
            self.assertEqual(str_out, '<hr />\n')
    def test_Hr_20(self):
        self.e1 = hr.Hr(**consts.attrs_pass)
        with open(consts.test_filename, 'w') as self.fobj:
            self.assertTrue(self.e1.render(self.fobj, '    '))
        with open(consts.test_filename, 'r') as self.file:
            str_out = self.file.read()
            self.assertEqual(str_out, '<hr id="Marker" alt="Fancy Pants" />\n')

    # Test the `a` element class
    def test_A_201(self):  # Can't specify an int for the link text
        with self.assertRaises(TypeError):
            self.e1 = hr.A("   https://www.wikipedia.org/  ", 50)
    def test_A_202(self):  # Can't add additional attributes to `a` tag
        with self.assertRaises(TypeError):
            self.e1 = hr.A(consts.attrs_pass, 
                    '\t   \t  \n  Grand \t \tWiki   \t\n   \t')
    def test_A_203(self):  # Test rendering of a single `a` element
        self.e1 = hr.A("   https://www.wikipedia.org/  ", 
                '\t   \t  \n  Grand \t \tWiki   \t\n   \t')
        with open(consts.test_filename, 'w') as self.fobj:
            self.assertTrue(self.e1.render(self.fobj, '    '))
        with open(consts.test_filename, 'r') as self.file:
            str_out = self.file.read()
            self.assertEqual(str_out, 
                    '<a href="https://www.wikipedia.org/">Grand Wiki</a>\n')
    def test_A_204(self):  # Test `a` rendering within doc hierarchy
        self.e2 = hr.P(
                "  \t  Here's \t Britannica's  \nworst\t  nightmare: \n\n\t  ")
        self.e3 = hr.A("   https://www.wikipedia.org/  ", 
                '\t   \t  \n  Grand \t \tWiki   \t\n   \t')
        self.e2.append(self.e3)
        self.e2.append(" \t . \n    ")
        self.e1 = hr.Body(self.e2)
        with open(consts.test_filename, 'w') as self.fobj:
            self.assertTrue(self.e1.render(self.fobj, '   '))
        with open(consts.test_filename, 'r') as self.file:
            self.strs_out = self.file.readlines()
            self.assertEqual(len(self.strs_out), 7)  # Verify total lines
            self.assertEqual(self.strs_out[0], '<body>\n')
            self.assertEqual(self.strs_out[1], '   <p>\n')
            self.assertEqual(self.strs_out[2], 
                    "      Here's Britannica's worst nightmare:\n")
            self.assertEqual(self.strs_out[3], '      '
                    '<a href="https://www.wikipedia.org/">Grand Wiki</a>\n')
            self.assertEqual(self.strs_out[4], '      .\n')
            self.assertEqual(self.strs_out[5], '   </p>\n')
            self.assertEqual(self.strs_out[6], '</body>\n')

    # Test unordered list and list item rendering
    def test_Ul_100(self):
        self.e3 = hr.Br()
        self.e2 = [hr.Li(consts.strs_before[i]) for i in range(3)]
        self.e2.append(hr.Li(
                id=" \n \t First \n \n \t ", alt="  Hi \t\t there!  \n"))
        self.e2[3].append([consts.strs_before[3], self.e3, consts.strs_before[4]])
        self.e2.append(hr.Li(consts.strs_before[-1]))
        self.e1 = hr.Ul(**consts.attrs_pass)
        self.e1.append(self.e2)
        with open(consts.test_filename, 'w') as self.fobj:
            self.assertTrue(self.e1.render(self.fobj, '  '))
        with open(consts.test_filename, 'r') as self.file:
            self.strs_out = self.file.readlines()
            self.assertEqual(len(self.strs_out), 19)  # Verify total lines
            self.assertEqual(self.strs_out[0],   '<ul id="Marker" alt="Fancy Pants">\n')
            self.assertEqual(self.strs_out[1],   '  <li>\n')
            self.assertEqual(self.strs_out[2],  f'    {consts.strs_after[0]}\n')
            self.assertEqual(self.strs_out[3],   '  </li>\n')
            self.assertEqual(self.strs_out[4],   '  <li>\n')
            self.assertEqual(self.strs_out[5],  f'    {consts.strs_after[1]}\n')
            self.assertEqual(self.strs_out[6],   '  </li>\n')
            self.assertEqual(self.strs_out[7],   '  <li>\n')
            self.assertEqual(self.strs_out[8],  f'    {consts.strs_after[2]}\n')
            self.assertEqual(self.strs_out[9],   '  </li>\n')
            self.assertEqual(self.strs_out[10],  '  <li id="First" alt="Hi there!">\n')
            self.assertEqual(self.strs_out[11], f'    {consts.strs_after[3]}\n')
            self.assertEqual(self.strs_out[12],  '    <br />\n')
            self.assertEqual(self.strs_out[13], f'    {consts.strs_after[4]}\n')
            self.assertEqual(self.strs_out[14],  '  </li>\n')
            self.assertEqual(self.strs_out[15],  '  <li>\n')
            self.assertEqual(self.strs_out[16], f'    {consts.strs_after[5]}\n')
            self.assertEqual(self.strs_out[17],  '  </li>\n')
            self.assertEqual(self.strs_out[18],  '</ul>\n')

    # Make sure heading objects only work for levels 1-6 (ints)        
    def test_H_050(self):
        with self.assertRaises(ValueError):
            self.e1 = hr.H(7, "Some header")
    def test_H_051(self):
        with self.assertRaises(ValueError):
            self.e1 = hr.H(0, "Some header")
    def test_H_052(self):
        with self.assertRaises(ValueError):
            self.e1 = hr.H(-3, "Some header")
    def test_H_053(self):
        with self.assertRaises(ValueError):
            self.e1 = hr.H(10, "Some header")
    def test_H_060(self):
        with self.assertRaises(TypeError):
            self.e1 = hr.H(2.0, "Some header")
    def test_H_070(self):  # Can't specify an int for heading text
        with self.assertRaises(TypeError):
            self.e1 = hr.H(1, 50)
    def test_H_071(self):  # Can't specify a float for heading text
        with self.assertRaises(TypeError):
            self.e1 = hr.H(1, 60.5)
    def test_H_072(self):  # Can't specify a string list for heading text
        with self.assertRaises(TypeError):
            self.e1 = hr.H(1, ["header part 1", "header part 2"])
    def test_H_073(self):  # Can't specify an element as a heading child
        with self.assertRaises(TypeError):
            self.e2 = hr.P("A paragraph.")
            self.e1 = hr.H(1, self.e2)
    def test_H_080(self):  # Can't specify an int for a heading attribute value
        with self.assertRaises(TypeError):
            self.e1 = hr.H(2, "Header text", id=50)
    # Verify heading markup, content, and attribute text in a doc hierarchy
    def test_H_100(self):
        self.e2 = [hr.H(i, consts.strs_before[i-1]) for i in range(1, 6)]
        self.e3 = hr.P("\tText   under \n heading   \t5.    \n\t")
        self.e2.append(self.e3)
        self.e2.append(hr.H(6, consts.strs_after[5], alt='Some hover text'))
        self.e1 = hr.Body(self.e2)
        with open(consts.test_filename, 'w') as self.fobj:
            self.assertTrue(self.e1.render(self.fobj, '  '))
        with open(consts.test_filename, 'r') as self.file:
            self.strs_out = self.file.readlines()
            self.assertEqual(len(self.strs_out), 11)  # Verify total lines
            self.assertEqual(self.strs_out[0],  '<body>\n')
            self.assertEqual(self.strs_out[1], f'  <h1>{consts.strs_after[0]}</h1>\n')
            self.assertEqual(self.strs_out[2], f'  <h2>{consts.strs_after[1]}</h2>\n')
            self.assertEqual(self.strs_out[3], f'  <h3>{consts.strs_after[2]}</h3>\n')
            self.assertEqual(self.strs_out[4], f'  <h4>{consts.strs_after[3]}</h4>\n')
            self.assertEqual(self.strs_out[5], f'  <h5>{consts.strs_after[4]}</h5>\n')
            self.assertEqual(self.strs_out[6], f'  <p>\n')
            self.assertEqual(self.strs_out[7], f'    Text under heading 5.\n')
            self.assertEqual(self.strs_out[8], f'  </p>\n')
            self.assertEqual(self.strs_out[9], 
                    f'  <h6 alt="Some hover text">{consts.strs_after[5]}</h6>\n')
            self.assertEqual(self.strs_out[10],  '</body>\n')
        
    # Test `meta` self-closing element code
    def test_Meta_100(self):  # Can't initialize w/int content
        with self.assertRaises(TypeError):
            self.e1 = hr.Meta(50)
    def test_Meta_101(self):  # Can't initialize w/float content
        with self.assertRaises(TypeError):
            self.e1 = hr.Meta(70.5)
    def test_Meta_110(self):  # Can't initialize w/string content
        with self.assertRaises(TypeError):
            self.e1 = hr.Meta("UTF-8")
    def test_Meta_120(self):  # Can't append a string
        self.e1 = hr.Meta()
        with self.assertRaises(TypeError):
            self.e1.append("   Some \t text.   \n")
    def test_Meta_130(self):  # Can't append an element
        self.e2 = hr.P("\n    Nothing. \t\t")
        self.e1 = hr.Meta()
        with self.assertRaises(TypeError):
            self.e1.append(self.e2)
    # Verify `meta` rendering + attribute within its parent
    def test_Meta_200(self):  
        self.e2 = hr.Meta(charset="\t    UTF-8   \n")
        self.e1 = hr.Head(self.e2)
        with open(consts.test_filename, 'w') as self.fobj:
            self.assertTrue(self.e1.render(self.fobj, '     '))
        with open(consts.test_filename, 'r') as self.file:
            self.strs_out = self.file.readlines()
            self.assertEqual(len(self.strs_out), 3)  # Verify total lines
            self.assertEqual(self.strs_out[0], '<head>\n')
            self.assertEqual(self.strs_out[1], '     <meta charset="UTF-8" />\n')
            self.assertEqual(self.strs_out[2], '</head>\n')

    # Test a multilayered `html` document stream w/DOCTYPE declared
    def test_Html_with_doctype_100(self):
        import html_render as hr
        meta = hr.Meta(charset="\t    UTF-8   \n")
        title = hr.Title("\n\nRandom  \t   Page   \n\t   ")
        head = hr.Head([meta, title])
        li_1 = hr.Li("  First  item:  ")
        para = hr.P("\n\nExplanatory\t\ttext.\n\n", **consts.attrs_pass)
        link = hr.A("https://github.com/", "A useful site!")
        para.append(link)
        hr = hr.Hr()
        li_1.append([hr, para])
        import html_render as hr
        li_2 = hr.Li("Second")
        br = hr.Br()
        li_2.append([br, "item"])
        li_3 = hr.Li("Third item", onclick="\n\n\t  EventHandler()\t  \n")
        ul = hr.Ul([li_1, li_2, li_3])
        body = hr.Body(ul)
        html = hr.Html((head, body))
        with open(consts.test_filename, 'w') as self.fobj:
            self.assertTrue(html.render(self.fobj))
        with open(consts.test_filename, 'r') as self.file:
            self.strs_out = self.file.readlines()
            self.assertEqual(len(self.strs_out), 27)  # Verify total lines
            self.assertEqual(self.strs_out[ 0], '<!DOCTYPE html>\n')
            self.assertEqual(self.strs_out[ 1], '<html>\n')
            self.assertEqual(self.strs_out[ 2], '<head>\n')
            self.assertEqual(self.strs_out[ 3], '<meta charset="UTF-8" />\n')
            self.assertEqual(self.strs_out[ 4], '<title>Random Page</title>\n')
            self.assertEqual(self.strs_out[ 5], '</head>\n')
            self.assertEqual(self.strs_out[ 6], '<body>\n')
            self.assertEqual(self.strs_out[ 7], '<ul>\n')
            self.assertEqual(self.strs_out[ 8], '<li>\n')
            self.assertEqual(self.strs_out[ 9], 'First item:\n')
            self.assertEqual(self.strs_out[10], '<hr />\n')
            self.assertEqual(self.strs_out[11], '<p id="Marker" alt="Fancy Pants">\n')
            self.assertEqual(self.strs_out[12], 'Explanatory text.\n')
            self.assertEqual(self.strs_out[13], '<a href="https://github.com/">A useful site!</a>\n')
            self.assertEqual(self.strs_out[14], '</p>\n')
            self.assertEqual(self.strs_out[15], '</li>\n')
            self.assertEqual(self.strs_out[16], '<li>\n')
            self.assertEqual(self.strs_out[17], 'Second\n')
            self.assertEqual(self.strs_out[18], '<br />\n')
            self.assertEqual(self.strs_out[19], 'item\n')
            self.assertEqual(self.strs_out[20], '</li>\n')
            self.assertEqual(self.strs_out[21], '<li onclick="EventHandler()">\n')
            self.assertEqual(self.strs_out[22], 'Third item\n')
            self.assertEqual(self.strs_out[23], '</li>\n')
            self.assertEqual(self.strs_out[24], '</ul>\n')
            self.assertEqual(self.strs_out[25], '</body>\n')
            self.assertEqual(self.strs_out[26], '</html>\n')
        del meta, title, head, li_1, li_2, li_3, para, link, \
                hr, br, ul, body, html


if __name__ == '__main__':
    unittest.main()
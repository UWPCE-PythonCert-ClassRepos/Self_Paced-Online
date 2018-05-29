#!/usr/bin/env python3

import os
import unittest
import html_render

CLEANUP_TEST_FILES=True

def validate_output(file_out, want_lines):
    """validate_output parses a rendered file and validates its content."""

    # Extract got from file_out.
    got_lines = []
    try:
        f = open(file_out)
        got_lines = f.readlines()
        f.close()
    except:
        print('validate_output failed to validate %s: %s' %
              (file_out, sys.exc_info()[0]))
        return False

    # Check line counts.
    got_line_cnt = len(got_lines)
    want_line_cnt = len(want_lines)
    if (got_line_cnt != want_line_cnt):
        print('FAIL: %s has %s lines, expected %s lines.' %
              (file_out, got_line_cnt, want_line_cnt))
        return False

    # Check each line.
    good = True
    line_num = 0
    for got_line, want_line in zip(got_lines, want_lines):
        got_line = got_line.rstrip('\n')
        if (got_line != want_line) :
            print('FAIL at line %s: got \'%s\', expected \'%s\'' %
                  (line_num, got_line, want_line))
            good = False
        line_num += 1

    return good

def rm_test_file(file_out):
    try:
        if (CLEANUP_TEST_FILES):
            os.remove(file_out)
    except:
        pass

class TestTextWrapper(unittest.TestCase):
    def setUp(self):
        """setUp creates a file to back the TextWrapper class."""
        self.file_out = 'text_wrapper_test.txt'

    def tearDown(self):
        """tearDown deletes any files created by the tests."""
        rm_test_file(self.file_out)

    def testRender(self):
        """testRender validates a basic TextWrapper render operation."""
        given = 'hello TextWrapper'
        want = [given]

        got = open(self.file_out, 'w')
        html_render.TextWrapper(given).render(got)
        got.close()

        self.assertTrue(validate_output(self.file_out, want))

    def testRenderWithIndent(self):
        """testRenderWithIndent validates a rendering an indented string."""
        given = 'hello TextWrapper'
        want = ["\t%s" % given]

        got = open(self.file_out, 'w')
        html_render.TextWrapper(given).render(got, cur_ind='\t')
        got.close()

        self.assertTrue(validate_output(self.file_out, want))


class TestElement(unittest.TestCase):
    def setUp(self):
        """setUp creates a file to back the Element class."""
        self.file_out = 'element_test.txt'

    def tearDown(self):
        """tearDown deletes any files created by the tests."""
        rm_test_file(self.file_out)

    def testAppend(self):
        """testAppend validates appending an element to an Element object."""
        element = html_render.Element()
        element.append("a text element")
        element.append(html_render.Element("an object element"))

        self.assertIs(type(element.sub_elements), list)
        self.assertEqual(len(element.sub_elements), 2)
        self.assertEqual(element.sub_elements[0].text, "a text element")
        self.assertEqual(element.sub_elements[1].sub_elements[0].text, "an object element")

    def testRender(self):
        """testRender validates a basic Element render operation."""
        given = 'hello Element'
        want = [
            "<html>",
            "{}{}".format(html_render.Element().ind, given),
            "</html>",
        ]

        got = open(self.file_out, 'w')
        html_render.Element(given).render(got)
        got.close()

        self.assertTrue(validate_output(self.file_out, want))

class TestHtml(unittest.TestCase):
    def setUp(self):
        """setUp creates a file to back the Html class."""
        self.file_out = 'html_test.txt'

    def tearDown(self):
        """tearDown deletes any files created by the tests."""
        rm_test_file(self.file_out)

    def testRender(self):
        """testRender validates a basic TextHtml render operation."""
        given = 'hello Html'
        want = [
            "<!DOCTYPE html>",
            "<html>",
            "{}{}".format(html_render.Html().ind, given),
            "</html>",
        ]

        got = open(self.file_out, 'w')
        html_render.Html(given).render(got)
        got.close()

        self.assertTrue(validate_output(self.file_out, want))

class TestBody(unittest.TestCase):
    def setUp(self):
        """setUp creates a file to back the Html class."""
        self.file_out = 'body_test.txt'

    def tearDown(self):
        """tearDown deletes any files created by the tests."""
        rm_test_file(self.file_out)

    def testRender(self):
        """testRender validates a basic Body render operation."""
        given = 'hello Body'
        want = [
            "<body>",
            "{}{}".format(html_render.Body().ind, given),
            "</body>",
        ]

        got = open(self.file_out, 'w')
        html_render.Body(given).render(got)
        got.close()

        self.assertTrue(validate_output(self.file_out, want))

class TestP(unittest.TestCase):
    def setUp(self):
        """setUp creates a file to back the P class."""
        self.file_out = 'p_test.txt'

    def tearDown(self):
        """tearDown deletes any files created by the tests."""
        rm_test_file(self.file_out)

    def testRender(self):
        """testRender validates a basic Body render operation."""
        given = 'hello P'
        want = [
            "<p>",
            "{}{}".format(html_render.P().ind, given),
            "</p>",
        ]

        got = open(self.file_out, 'w')
        html_render.P(given).render(got)
        got.close()

        self.assertTrue(validate_output(self.file_out, want))

class TestHead(unittest.TestCase):
    def setUp(self):
        """setUp creates a file to back the Head class."""
        self.file_out = 'head_test.txt'

    def tearDown(self):
        """tearDown deletes any files created by the tests."""
        rm_test_file(self.file_out)

    def testRender(self):
        """testRender validates a basic Head render operation."""
        given = 'hello Head'
        want = [
            "<head>",
            "{}{}".format(html_render.Head().ind, given),
            "</head>",
        ]

        got = open(self.file_out, 'w')
        html_render.Head(given).render(got)
        got.close()

        self.assertTrue(validate_output(self.file_out, want))

class TestOneLineTag(unittest.TestCase):
    def setUp(self):
        """setUp creates a file to back the OneLineTag class."""
        self.file_out = 'one_line_tag_test.txt'

    def tearDown(self):
        """tearDown deletes any files created by the tests."""
        rm_test_file(self.file_out)

    def testRender(self):
        """testRender validates a basic OneLineTag render operation."""
        given = 'hello OneLineTag'
        want = ["<>{}</>".format(given)]

        got = open(self.file_out, 'w')
        html_render.OneLineTag(given).render(got, '', True)
        got.close()

        self.assertTrue(validate_output(self.file_out, want))

class TestTitle(unittest.TestCase):
    def setUp(self):
        """setUp creates a file to back the Title class."""
        self.file_out = 'title_test.txt'

    def tearDown(self):
        """tearDown deletes any files created by the tests."""
        rm_test_file(self.file_out)

    def testRender(self):
        """testRender validates a basic Title render operation."""
        given = 'hello Title'
        want = ["<title>{}</title>".format(given)]

        got = open(self.file_out, 'w')
        html_render.Title(given).render(got, '', True)
        got.close()

        self.assertTrue(validate_output(self.file_out, want))

class TestSelfClosingTag(unittest.TestCase):
    def setUp(self):
        """setUp creates a file to back the SelfClosingTag class."""
        self.file_out = 'self_closing_tag_test.txt'

    def tearDown(self):
        """tearDown deletes any files created by the tests."""
        rm_test_file(self.file_out)

    def testRender(self):
        """testRender validates a basic SelfClosingTag render operation."""
        want = ["<html />"]

        got = open(self.file_out, 'w')
        html_render.SelfClosingTag().render(got)
        got.close()

        self.assertTrue(validate_output(self.file_out, want))

class TestHr(unittest.TestCase):
    def setUp(self):
        """setUp creates a file to back the Hr class."""
        self.file_out = 'hr_test.txt'

    def tearDown(self):
        """tearDown deletes any files created by the tests."""
        rm_test_file(self.file_out)

    def testRender(self):
        """testRender validates a basic Hr render operation."""
        want = ["<hr />"]

        got = open(self.file_out, 'w')
        html_render.Hr().render(got)
        got.close()

        self.assertTrue(validate_output(self.file_out, want))

class TestBr(unittest.TestCase):
    def setUp(self):
        """setUp creates a file to back the Br class."""
        self.file_out = 'br_test.txt'

    def tearDown(self):
        """tearDown deletes any files created by the tests."""
        rm_test_file(self.file_out)

    def testRender(self):
        """testRender validates a basic Br render operation."""
        want = ["<br />"]

        got = open(self.file_out, 'w')
        html_render.Br().render(got)
        got.close()

        self.assertTrue(validate_output(self.file_out, want))

class TestA(unittest.TestCase):
    def setUp(self):
        """setUp creates a file to back the A class."""
        self.file_out = 'a_test.txt'

    def tearDown(self):
        """tearDown deletes any files created by the tests."""
        rm_test_file(self.file_out)

    def testRender(self):
        """testRender validates a basic A render operation."""
        given = 'hello A'
        given_link = 'a.com'
        want = ["<a href=\"{}\">{}</a>".format(given_link, given)]

        got = open(self.file_out, 'w')
        html_render.A(given_link, given).render(got)
        got.close()

        self.assertTrue(validate_output(self.file_out, want))

class TestUl(unittest.TestCase):
    def setUp(self):
        """setUp creates a file to back the Ul class."""
        self.file_out = 'ul_test.txt'

    def tearDown(self):
        """tearDown deletes any files created by the tests."""
        rm_test_file(self.file_out)

    def testRender(self):
        """testRender validates a basic Ul render operation."""
        given = 'hello Ul'
        want = [
            "<ul>",
            "{}{}".format(html_render.Ul().ind, given),
            "</ul>",
        ]

        got = open(self.file_out, 'w')
        html_render.Ul(given).render(got)
        got.close()

        self.assertTrue(validate_output(self.file_out, want))

class TestLi(unittest.TestCase):
    def setUp(self):
        """setUp creates a file to back the Li class."""
        self.file_out = 'li_test.txt'

    def tearDown(self):
        """tearDown deletes any files created by the tests."""
        rm_test_file(self.file_out)

    def testRender(self):
        """testRender validates a basic Li render operation."""
        given = 'hello Li'
        want = [
            "<li>",
            "{}{}".format(html_render.Li().ind, given),
            "</li>",
        ]

        got = open(self.file_out, 'w')
        html_render.Li(given).render(got)
        got.close()

        self.assertTrue(validate_output(self.file_out, want))

class TestH(unittest.TestCase):
    def setUp(self):
        """setUp creates a file to back the H class."""
        self.file_out = 'h_test.txt'

    def tearDown(self):
        """tearDown deletes any files created by the tests."""
        rm_test_file(self.file_out)

    def testRender(self):
        """testRender validates a basic H render operation."""
        given = 'hello H'
        given_level = 2
        want = ["<h2>{}</h2>".format(given)]

        got = open(self.file_out, 'w')
        html_render.H(given_level, given).render(got, '', True)
        got.close()

        self.assertTrue(validate_output(self.file_out, want))

class TestMeta(unittest.TestCase):
    def setUp(self):
        """setUp creates a file to back the Meta class."""
        self.file_out = 'meta_test.txt'

    def tearDown(self):
        """tearDown deletes any files created by the tests."""
        rm_test_file(self.file_out)

    def testRender(self):
        """testRender validates a basic Meta render operation."""
        want = ["<metacharset=UTF-8 />"]

        got = open(self.file_out, 'w')
        html_render.Meta(charset="UTF-8").render(got)
        got.close()

        self.assertTrue(validate_output(self.file_out, want))

if __name__ == '__main__':
    unittest.main()

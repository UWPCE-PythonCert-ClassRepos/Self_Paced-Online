#!/usr/bin/env python3
import unittest
import html_render as hr
import os
from os import path
import shutil
import tempfile


class html_render_tests(unittest.TestCase):

    test_dir = os.getcwd()

    # Initial setup of test values
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

    # Test html tag
    def test_html_tag(self):

        comp_string = "<!DOCTYPE html>\n<html>\n</html>\n"

        with open(path.join(self.test_dir, 'test.txt'), 'w') as f:
            test = hr.Html().render(f)

        with open(path.join(self.test_dir, 'test.txt')) as f:
            self.assertEqual(comp_string, f.read())

    # Test head tag
    def test_head_tag(self):
        comp_string = "<head>\n</head>\n"

        with open(path.join(self.test_dir, 'test.txt'), 'w') as f:
            test = hr.Head().render(f)

        with open(path.join(self.test_dir, 'test.txt')) as f:
            self.assertEqual(comp_string, f.read())

    # Test meta tag append
    def test_meta_tag(self):
        comp_string = '    <meta charset="UTF-8" /> \n'

        with open(path.join(self.test_dir, 'test.txt'), 'w') as f:
            test = hr.Meta(charset="UTF-8").render(f, "")

        with open(path.join(self.test_dir, 'test.txt')) as f:
            self.assertEqual(comp_string, f.read())

    # Test title tag append
    def test_title_tag(self):
        comp_string = '    <title>Title</title>\n'

        with open(path.join(self.test_dir, 'test.txt'), 'w') as f:
            test = hr.Title("Title").render(f, "")

        with open(path.join(self.test_dir, 'test.txt')) as f:
            self.assertEqual(comp_string, f.read())

    # Test head tag append
    def test_head_tag_append(self):
        comp_string = '<head>\n    <meta charset="UTF-8" /> \n</head>\n'

        with open(path.join(self.test_dir, 'test.txt'), 'w') as f:
            test = hr.Head()
            test.append(hr.Meta(charset="UTF-8"))
            test.render(f)

        with open(path.join(self.test_dir, 'test.txt')) as f:
            self.assertEqual(comp_string, f.read())

    # Test body tag
    def test_body_tag(self):
        comp_string = '<body>\n</body>\n'

        with open(path.join(self.test_dir, 'test.txt'), 'w') as f:
            test = hr.Body()
            test.render(f)

        with open(path.join(self.test_dir, 'test.txt')) as f:
            self.assertEqual(comp_string, f.read())

    # Test body tag
    def test_body_tag_append(self):
        comp_string = '<body>\n    Append Test\n</body>\n'

        with open(path.join(self.test_dir, 'test.txt'), 'w') as f:
            test = hr.Body()
            test.append("Append Test")
            test.render(f)

        with open(path.join(self.test_dir, 'test.txt')) as f:
            self.assertEqual(comp_string, f.read())

    # Test self-closing tag
    def test_sc_tags(self):
        comp_string = '<hr /> \n<br /> \n'

        with open(path.join(self.test_dir, 'test.txt'), 'w') as f:
            test = hr.Hr()
            test.indent = ""
            test.render(f, "")
            test = hr.Br()
            test.indent = ""
            test.render(f, "")

        with open(path.join(self.test_dir, 'test.txt')) as f:
            self.assertEqual(comp_string, str(f.read()))

    # Test anchor tag
    def test_a_tag(self):
        comp_string = '        <a href="http://google.com">google</a>\n'

        with open(path.join(self.test_dir, 'test.txt'), 'w') as f:
            test = hr.A("http://google.com", "google")
            test.indent = ""
            test.render(f, "")

        with open(path.join(self.test_dir, 'test.txt')) as f:
            self.assertEqual(comp_string, f.read())

    # Test Ul tag
    def test_ul_tag(self):
        comp_string = '<ul>\n</ul>\n'

        with open(path.join(self.test_dir, 'test.txt'), 'w') as f:
            test = hr.Ul()
            test.indent = ''
            test.render(f)

        with open(path.join(self.test_dir, 'test.txt')) as f:
            self.assertEqual(comp_string, f.read())

    # Test style append
    def test_ul_tag_style(self):
        comp_string = '<ul id="TheList" style="line-height:200%">\n</ul>\n'

        with open(path.join(self.test_dir, 'test.txt'), 'w') as f:
            test = hr.Ul(id="TheList", style="line-height:200%")
            test.indent = ''
            test.render(f)

        with open(path.join(self.test_dir, 'test.txt')) as f:
            self.assertEqual(comp_string, f.read())

    # Test Ul tag append li elements
    def test_ul_tag_append(self):
        comp_string = '<ul>\n<li>\n    Test 1\n</li>\n<li>\n    Test 2\n</li>\n</ul>\n'

        with open(path.join(self.test_dir, 'test.txt'), 'w') as f:
            test = hr.Ul()
            test.indent = ''
            li_1 = hr.Li("Test 1")
            li_2 = hr.Li("Test 2")
            li_1.indent = ""
            li_2.indent = ""
            test.append(li_1)
            test.append(li_2)
            test.render(f)

        with open(path.join(self.test_dir, 'test.txt')) as f:
            self.assertEqual(comp_string, f.read())

    # Cleanup
    def tearDown(self):
        # Remove the directory after the test
        f = open(path.join(self.test_dir, 'test.txt'), 'w')
        f.close()


if __name__ == '__main__':
    unittest.main()

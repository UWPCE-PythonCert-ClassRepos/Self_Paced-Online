# ------------------------------------------------- #
# Title: Lesson 7, pt 2/2, html render test
# Dev:   Craig Morton
# Date:  9/17/2018
# Change Log: CraigM, 9/17/2018, html render test
# ------------------------------------------------- #

from io import StringIO
import unittest
import html_render


class HtmlRenderTest(unittest.TestCase):

    def test_basic_tags(self):
        tags = ('Body', 'Head', 'Ul', 'Li')
        for t in tags:
            expected = '<{tag}>\n\n</{tag}>'.format(tag=t.lower())
            page = eval('html_render.{tag}()'.format(tag=t))
            rendered = StringIO()
            page.render(rendered)
            self.assertEqual(rendered.getvalue(), expected)

    def test_html_tag(self):
        expected = '<!DOCtype html>\n<html>\n\n</html>'
        page = html_render.Html()
        rendered = StringIO()
        page.render(rendered)
        self.assertEqual(rendered.getvalue(), expected)

    def test_one_line_tags(self):
        tags = ('Title', 'P')
        for t in tags:
            expected = '<{tag}></{tag}>'.format(tag=t.lower())
            page = eval('html_render.{tag}()'.format(tag=t))
            rendered = StringIO()
            page.render(rendered)
            self.assertEqual(rendered.getvalue(), expected)

    def test_levels(self):
        for level in range(1, 7):
            expected = '<h{level}></h{level}>'.format(level=level)
            page = eval('html_render.H({level})'.format(level=level))
            rendered = StringIO()
            page.render(rendered)
            self.assertEqual(expected, rendered.getvalue())
        self.assertRaises(AttributeError, html_render.H, 0)
        self.assertRaises(AttributeError, html_render.H, 7)

    def test_self_closing(self):
        tags = ('Hr', 'Br')
        for t in tags:
            expected = '<{tag}/>'.format(tag=t.lower())
            page = eval('html_render.{tag}()'.format(tag=t))
            rendered = StringIO()
            page.render(rendered)
            self.assertEqual(rendered.getvalue(), expected)
            self.assertRaises(TypeError, page.append, "Testing this")

    def test_meta_tag(self):
        expected = '<meta charset="UTF-8"/>'
        page = html_render.Meta("UTF-8")
        rendered = StringIO()
        page.render(rendered)
        self.assertEqual(rendered.getvalue(), expected)

    def test_anchor_tag(self):
        expected = '<a href="www.google.com"></a>'
        page = html_render.A("www.google.com")
        rendered = StringIO()
        page.render(rendered)
        self.assertEqual(rendered.getvalue(), expected)

    def test_content(self):
        expected = '<element>\nHello \n\n</element>'
        page = html_render.Element(content='Hello ')
        rendered = StringIO()
        page.render(rendered)
        self.assertEqual(rendered.getvalue(), expected)
        expected = '<element>\nHello \nworld\n\n</element>'
        page.append("world")
        rendered = StringIO()
        page.render(rendered)
        self.assertEqual(rendered.getvalue(), expected)
        expected = '<element>\nHello \nworld\n   <p>again</p>\n\n</element>'
        page.append(html_render.P("again"))
        rendered = StringIO()
        page.render(rendered)
        self.assertEqual(rendered.getvalue(), expected)


if __name__ == "__main__":
    unittest.main()


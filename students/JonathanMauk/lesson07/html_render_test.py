import unittest
import html_render as hr
from io import StringIO


class HtmlRenderingTests(unittest.TestCase):

    def test_element(self):
        element = hr.Element()
        self.assertEqual(element.content, [])

    def test_append(self):
        element1 = hr.Element()
        element1.append('Testing.')
        self.assertEqual(element1.content, ['Testing.'])
        element2 = hr.Element('Testing.')
        element2.append('1, 2, 3.')
        self.assertEqual(element2.content, ['Testing.', '1, 2, 3.'])

    def test_render(self):
        element = hr.Element('Testing.')
        f = StringIO()
        element.render(f)
        self.assertEqual(f.getvalue(), "<>\n" + element.indent + "Testing.\n</>\n")

    def test_title(self):
        title = hr.Title("A Title")
        f = StringIO()
        title.render(f)
        self.assertEqual(f.getvalue(), "<title>A Title</title>\n")

    def test_attributes(self):
        title = hr.Title("A Title", style="text-align: center; font-style: oblique;")
        f = StringIO()
        title.render(f)
        self.assertEqual(f.getvalue(), "<title style=\"text-align: center; font-style: oblique;\">A Title</title>\n")

    def test_break(self):
        br = hr.Br()
        f = StringIO()
        br.render(f)
        self.assertEqual(f.getvalue(), "<br />\n")

    def test_anchor(self):
        anchor = hr.A("http://www.google.com", "a link")
        f = StringIO()
        anchor.render(f)
        self.assertEqual(f.getvalue(), '<a href="http://www.google.com">a link</a>\n')


if __name__ == '__main__':
    unittest.main()

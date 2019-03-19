import unittest
from io import StringIO

import html_render as hr


class TestHtml(unittest.TestCase):

    @staticmethod
    def render_page(page, indent=None):
        """
        render the tree of elements

        This uses StringIO to render to memory, then dump to console and
        write to file -- very handy!
        """

        f = StringIO()
        if indent is None:
            page.render(f, "")
        else:
            page.render(f, indent)

        return f.getvalue()

    def test_render(self):
        element_render = hr.Element('Hello', style='font-size: 15px;')
        html_render = hr.Html('Hello')
        one_line_tag_render = hr.Title('Hello')
        self_closing_tag_render = hr.Hr()

        element_render = self.render_page(element_render).strip()
        html_render = self.render_page(html_render).strip()
        one_line_tag_render = self.render_page(one_line_tag_render).strip()
        self_closing_tag_render = self.render_page(self_closing_tag_render).strip()

        self.assertIn('style="font-size: 15px;"', element_render)
        self.assertTrue(element_render.startswith('<html'))
        self.assertTrue(html_render.startswith('<!DOCTYPE html>\n'))
        self.assertTrue('\n' not in one_line_tag_render)
        self.assertTrue(self_closing_tag_render.endswith('/>'))

    def test_append(self):
        subject = hr.Element()
        p = hr.P('Hello world')
        subject.append(p)
        subject.append('Another greeting.')
        subject.append(True)
        subject.append(1)

        self.assertEqual(len(subject.content), 2)

        subject.append('Yet another one.')

        self.assertEqual(len(subject.content), 3)

    def test_element(self):
        subject = hr.Element()
        subject.append(hr.P('hello world'))
        subject = self.render_page(subject).strip()

        self.assertTrue(subject.startswith('<html>'))
        self.assertTrue(subject.endswith('</html>'))
        self.assertIn('hello world', subject)

    def test_one_line_tag(self):
        subject = hr.OneLineTag()
        subject.tag = 'title'

        subject.append('Hello world.')
        subject = self.render_page(subject, "").strip()

        self.assertTrue('\n' not in subject)

    def test_self_closing_tag(self):
        subject = hr.Hr()
        subject = self.render_page(subject, "").strip()

        self.assertTrue(subject.endswith('/>'))

    def test_a(self):
        subject = hr.A('google', 'google.com')
        subject = self.render_page(subject, "").strip()

        self.assertIn("href=", subject)
        self.assertIn("google.com", subject)

    def test_h(self):
        h1 = hr.H(1, 'Heading 1')
        h3 = hr.H(3, 'Heading 3')
        h5 = hr.H(5, 'Heading 5')

        h1 = self.render_page(h1, "")
        h3 = self.render_page(h3, "")
        h5 = self.render_page(h5, "")

        self.assertTrue(h1.startswith("<h1>"))
        self.assertTrue(h3.startswith("<h3>"))
        self.assertTrue(h5.startswith("<h5>"))



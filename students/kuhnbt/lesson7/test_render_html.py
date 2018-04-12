import unittest
import html_render as hr
from io import StringIO

class HtmlTest(unittest.TestCase):
    def setUp(self):
        self.page = hr.Element()

    def test_append(self):
        self.page.append("Here's a new line")
        self.page.append('And another')
        expected_values = ["Here's a new line", "And another"]
        self.assertEqual(self.page.content, expected_values)

    def test_append_2(self):
        with self.assertRaises(TypeError):
            self.page.append(256)

    def test_render(self):
        self.page.content = ['Some content.', 'Some more content.']
        expected_text = "<>\n    Some content.\n    Some more content.\n"\
                        "</>"
        f = StringIO()
        self.page.render(f, 0)
        self.assertEqual(f.getvalue(), expected_text)

    def test_render_title(self):
        self.title = hr.Title('This is a test title')
        f = StringIO()
        self.title.render(f, 0)
        expected_text = '<title>This is a test title</title>'
        self.assertEqual(f.getvalue(), expected_text)

    def test_keywords(self):
        arguments = {'class': 'test class', 'id': 'test'}
        self.tag = hr.P('Test html', arguments)
        f = StringIO()
        self.tag.render(f, 0)
        expected_text = '<p class="test class" id="test">\n    Test html'\
            '\n</p>'
        self.assertEqual(f.getvalue(), expected_text)

    def test_keywords_type(self):
        with self.assertRaises(TypeError):
            self.tag = hr.P('Test html', keywords = "id='tag_id'")

    def test_self_closing_tag(self):
        with self.assertRaises(TypeError):
            self.tag = hr.SelfClosingTag(content = 'Test Content')

    def test_meta(self):
        f = StringIO()
        self.meta = hr.Meta(charset = "UTF-8")
        expected_text = '<meta charset="UTF-8" />'
        self.meta.render(f, 0)
        self.assertEqual(f.getvalue(), expected_text)

    def test_a(self):
        f = StringIO()
        self.a = hr.A(link='http://google.com', content='google link')
        self.a.render(f, 0)
        expected_text = '<a href="http://google.com">google link</a>'
        self.assertEqual(f.getvalue(), expected_text)
    
    def test_li(self):
        f = StringIO()
        self.li = hr.Li('list element')
        self.li.render(f, 0)
        self.assertEqual(f.getvalue(), '<li>list element</li>')

    def test_ul(self):
        f = StringIO()
        self.ul = hr.Ul(hr.Li('some content'))
        self.ul.render(f, 0)
        self.assertEqual(f.getvalue(), '<ul>\n    <li>some content</li>\n</ul>')    

    def test_header(self):
        f = StringIO()
        self.header = hr.H(3, 'header content')
        self.header.render(f, 0)
        self.assertEqual(f.getvalue(), '<h3>header content</h3>')

    def test_mixed_types(self):
        f = StringIO()
        self.h = hr.Html(content='Some text')
        for element in [hr.P('more text'), 
            hr.A('http://finance.yahoo.com', 'yahoo finance')]:
            self.h.append(element)
        self.h.render(f,0)
        expected_content = '<!DOCTYPE html>\n<html>\n    Some text\n    <p>\n'\
                           '        more text\n    </p>\n    <a href="http://finance.yahoo.com">yahoo finance</a>\n</html>'
        self.assertEqual(f.getvalue(), expected_content)
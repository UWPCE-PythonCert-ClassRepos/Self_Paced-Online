import unittest
import html_render as hr
from io import StringIO


class TestHtmlRender(unittest.TestCase):

    def test_element(self):
        test_element = hr.Element("test content")
        self.assertEqual(test_element.content, ["test content"])
        test_element.tag = "p"
        self.assertEqual(test_element.tag, 'p')
        test_element.tag = 'body'
        self.assertEqual(test_element.tag, 'body')

    def test_append(self):
        test_element = hr.Element("content1")
        test_element.append("content2")
        self.assertEqual(test_element.content, ["content1", "content2"])

    def test_style(self):
        test_element = hr.Element("test cotnent", style = 'font-color:red;')
        self.assertEqual(test_element.styles, {'style': 'font-color:red;'})

    def test_render(self):
        test_element = hr.Element("test content")
        test_element.tag = 'html'
        f = StringIO()
        test_element.render(f)
        self.assertEqual(f.getvalue(), "<html>\n" + test_element.indent + "test content\n</html>\n")

    def test_selfclosingtag(self):
        test_selfclosing = hr.SelfClosingTag()
        test_selfclosing.tag = 'br'
        f = StringIO()
        test_selfclosing.render(f)
        self.assertEqual(f.getvalue(), "<br />\n")
        test_selfclosing_attr = hr.SelfClosingTag(charset="UTF-8")
        test_selfclosing_attr.tag = 'meta'
        f = StringIO()
        test_selfclosing_attr.render(f)
        self.assertEqual(f.getvalue(), "<meta charset=\"UTF-8\" />\n")

    def test_onelinetag(self):
        test_onelinetag = hr.OneLineTag("This is Title")
        test_onelinetag.tag = 'title'
        f = StringIO()
        test_onelinetag.render(f)
        self.assertEqual(f.getvalue(), "<title>This is Title</title>\n")

    def test_atag(self):
        test_atag = hr.A("http://google.com", "Some link")
        f = StringIO()
        test_atag.render(f)
        self.assertEqual(f.getvalue(), "<a href=\"http://google.com\">\n" + test_atag.indent + "Some link\n</a>\n")

    def test_htag(self):
        test_htag = hr.H(2, "Header 2 Example")
        f = StringIO()
        test_htag.render(f)
        self.assertEqual(f.getvalue(), "<h2>Header 2 Example</h2>\n")

if __name__ == '__main__':
    unittest.main()

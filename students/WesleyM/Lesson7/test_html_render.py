import unittest
import html_render as hr
from io import StringIO

class TestHtmlRender(unittest.TestCase):
   
    def test_append(self):
        test_list = ['Some content.', 'Some more content.']
        test = hr.Element()
        test.append('Some content.')
        test.append('Some more content.')
        self.assertEqual(test.content, test_list)
   
    def test_element(self):
        test_element = hr.Element("Test Content")
        self.assertEqual(test_element.content, ["Test Content"])
        test_element.tag = "p"
        self.assertEqual(test_element.tag, 'p')
        test_element.tag = 'body'
        self.assertEqual(test_element.tag, 'body')
    
    def test_render(self):
        test_element = hr.Element("Test Content")
        test_element.tag = 'html'
        f = StringIO()
        test_element.render(f)
        self.assertEqual(f.getvalue(), "<html>\n" + test_element.indent + "Test Content\n</html>\n")
    
    def test_selfclosingtag(self):
        test_selfclosing = hr.SelfClosingTag()
        test_selfclosing.tag = 'br'
        f = StringIO()
        test_selfclosing.render(f)
        self.assertEqual(f.getvalue(), "<br />\n")

    def test_metatag(self):
        test_meta = hr.SelfClosingTag(charset="UTF-8")
        test_meta.tag = 'meta'
        f = StringIO()
        test_meta.render(f)
        self.assertEqual(f.getvalue(), "<meta charset=\"UTF-8\" />\n")

    def test_onelinetag(self):
        test_onelinetag = hr.OneLineTag("PythonClass - Session 6 example")
        test_onelinetag.tag = 'title'
        f = StringIO()
        test_onelinetag.render(f)
        self.assertEqual(f.getvalue(), "<title>PythonClass - Session 6 example</title>\n")

    def test_atag(self):
        test_atag = hr.A("http://google.com", "link to google")
        f = StringIO()
        test_atag.render(f)
        self.assertEqual(f.getvalue(), "<a href=\"http://google.com\">\n" + test_atag.indent + "link to google\n</a>\n")

    def test_htag(self):
        test_htag = hr.H(2, "The text of the header")
        f = StringIO()
        test_htag.render(f)
        self.assertEqual(f.getvalue(), "<h2>The text of the header</h2>\n")

if __name__ == "__main__":
    unittest.main()

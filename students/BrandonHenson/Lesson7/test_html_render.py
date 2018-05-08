# Brandon Henson
# 5/5/18
# Lesson 07 HTML Renderer
import unittest
import html_render as hr
import os
from io import StringIO
cwd = os.getcwd()


class TestHtmlRender(unittest.TestCase):

    def test_element(self):
        test_element = hr.Element('some stuff')
        self.assertEqual(test_element.content, ["some stuff"])

    def test_append(self):
        test = hr.Element('some stuff in here')
        test.append('some more stuff in here')
        self.assertEqual(test.content, ['some stuff in here', 'some more stuff in here'])

    def test_render(self):
        element = hr.Element("Test")
        element.tag = 'html'
        f = StringIO()
        element.render(f)
        self.assertEqual(f.getvalue(), "<html>\n" + element.indent + "Test\n</html>\n")
        element.tag = 'body'
        f = StringIO()
        element.render(f)
        self.assertEqual(f.getvalue(), "<body>\n" + element.indent + "Test\n</body>\n")
        element.tag = 'p'
        f = StringIO()
        element.render(f)
        self.assertEqual(f.getvalue(), "<p>\n" + element.indent + "Test\n</p>\n")
        element.tag = 'head'
        f = StringIO()
        element.render(f)
        self.assertEqual(f.getvalue(), "<head>\n" + element.indent + "Test\n</head>\n")
        assert os.path.isfile(cwd + '\\' + 'test_html_output1.html')
        assert os.path.isfile(cwd + '\\' + 'test_html_output2.html')
        assert os.path.isfile(cwd + '\\' + 'test_html_output3.html')
        assert os.path.isfile(cwd + '\\' + 'test_html_output4.html')
        assert os.path.isfile(cwd + '\\' + 'test_html_output5.html')
        assert os.path.isfile(cwd + '\\' + 'test_html_output6.html')
        assert os.path.isfile(cwd + '\\' + 'test_html_output7.html')
        assert os.path.isfile(cwd + '\\' + 'test_html_output8.html')

    def test_init(self):
        element = hr.Element('test', keyword='this is a test')
        self.assertEqual(element.content, ['test'])
        self.assertEqual(element.attributes, {'keyword': 'this is a test'})

    def test_selfclosingtag(self):
        test = hr.SelfClosingTag()
        test.tag = 'meta'
        f = StringIO()
        test.render(f)
        self.assertEqual(f.getvalue(), "<meta/>\n")

    def test_h(self):
        test = hr.H(1, "This is a test")
        f = StringIO()
        test.render(f)
        self.assertEqual(f.getvalue(), "<h1> This is a test  </h1>\n")


if __name__ == '__main__':
    unittest.main()

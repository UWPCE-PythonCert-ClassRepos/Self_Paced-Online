import unittest
import html_render as hr
from io import StringIO


class TestHtmlRender(unittest.TestCase):
    def test_1_Element(self):
        test1 = hr.Element('this is content', key='val')
        self.assertEqual(test1.content, ['this is content'])
        self.assertEqual(test1.attributes, {'key': 'val'})

    def test_2_append(self):
            test_1_element = hr.Body()
            test_1_element.append("content1")
            test_1_element.append("content2")
            self.assertEqual(test_1_element.content, ["content1", "content2"])

    def test_3_Title(self):
        f = StringIO()
        head = hr.Head()
        head.append(hr.Title("Test Title"))
        head.content[0].render(f)
        current_element = f.getvalue()
        expected_element = '<title>Test Title</title>\n'
        self.assertEqual(current_element, expected_element)

    def test_4_attributes(self):
        f = StringIO()
        par = hr.P("Paragrah", style="text-align: center; font-style: oblique;")
        par.render(f)
        actual = f.getvalue()
        expected = '<p style="text-align: center; font-style: oblique;">\n  Paragrah\n</p>\n'
        self.assertEqual(actual, expected)

    def test_5_SelfClosingTag(self):
        try:
            horizontal = hr.Hr('unexpected content')
        except TypeError:
            actual = 'TypeError'
        else:
            actual = 'OK'
        expected = 'TypeError'
        self.assertEqual(actual, expected)

    def test_6_A(self):
        f = StringIO()
        link = hr.A("http://google.com", "link")
        link.render(f)
        actual = f.getvalue()
        expected = '<a href="http://google.com">\n  link\n</a>\n'
        self.assertEqual(actual, expected)

    def test_7_H(self):
        f = StringIO()
        header = hr.H(2, "PythonClass - Class 6 example")
        header.render(f)
        actual = f.getvalue()
        expected = '<h2>PythonClass - Class 6 example</h2>\n'
        self.assertEqual(actual, expected)

    def test_8_Meta(self):
        f = StringIO()
        h = hr.Meta(charset="UTF-8")
        h.render(f)
        actual = f.getvalue()
        expected = '<meta charset="UTF-8" />\n'
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()

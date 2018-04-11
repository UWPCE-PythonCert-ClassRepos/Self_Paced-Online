import unittest
import html_render as hr
import os.path
import io
import sys
from io import StringIO


class TestHTMLRender(unittest.TestCase):

    def test_Element_render(self):
        f = StringIO()
        testelement = hr.Element()
        testelement.render(f)
        print(f.getvalue())
        self.assertEqual(f.getvalue(), "<tag>\n</tag>\n")

    def test_Element_append(self):
        f = StringIO()
        testelement = hr.Element()
        testelement.append('test1')
        testelement.append('test2')
        testelement.render(f)
        print(f.getvalue())
        self.assertEqual(f.getvalue(), "<tag>\ntest1\ntest2\n</tag>\n")

    def test_Html_render(self):
        f = StringIO()
        testelement = hr.Html()
        testelement.render(f)
        self.assertEqual(f.getvalue(), "<html>\n</html>\n")

    def test_Html_append(self):
        f = StringIO()
        testelement = hr.Html()
        testelement.append('test1')
        testelement.append('test2')
        testelement.render(f)
        self.assertEqual(f.getvalue(), "<html>\ntest1\ntest2\n</html>\n")

    def test_Body_render(self):
        f = StringIO()
        testelement = hr.Body()
        testelement.render(f)
        self.assertEqual(f.getvalue(), "<body>\n</body>\n")

    def test_Body_append(self):
        f = StringIO()
        testelement = hr.Body()
        testelement.append('test1')
        testelement.append('test2')
        testelement.render(f)
        self.assertEqual(f.getvalue(), "<body>\ntest1\ntest2\n</body>\n")

    def test_P_render(self):
        f = StringIO()
        testelement = hr.P()
        testelement.render(f)
        self.assertEqual(f.getvalue(), "<p>\n</p>\n")

    def test_P_append(self):
        f = StringIO()
        testelement = hr.P()
        testelement.append('test1')
        testelement.append('test2')
        testelement.render(f)
        self.assertEqual(f.getvalue(), "<p>\ntest1\ntest2\n</p>\n")

    def test_append_body_html(self):
        f = StringIO()
        testelement = hr.Html()
        body = hr.Body()
        testelement.append(body)
        testelement.render(f)
        print(f.getvalue())

    def test_append_p_body_html(self):
        f = StringIO()
        testelement = hr.Html()
        body = hr.Body()
        body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
                         "but this is enough  to show that we can do some text"))
        testelement.append(body)
        testelement.render(f)
        print(f.getvalue())

    def test_Title_render(self):
        f = StringIO()
        testelement = hr.Title()
        testelement.render(f)
        self.assertEqual(f.getvalue(), "<title></title>\n")

    def test_append_Title_string(self):
        f = StringIO()
        testelement = hr.Title("test")
        testelement.render(f)
        self.assertEqual(f.getvalue(), "<title>test</title>\n")

    def test_Head_render(self):
        f = StringIO()
        testelement = hr.Head()
        testelement.render(f)
        self.assertEqual(f.getvalue(), "<head>\n</head>\n")

    def test_append_Head_string(self):
        f = StringIO()
        testelement = hr.Head("test")
        testelement.render(f)
        self.assertEqual(f.getvalue(), "<head>\ntest\n</head>\n")

    def test_attributes_P(self):
        f = StringIO()
        testelement = hr.P("test", test="test")
        testelement.render(f)
        self.assertEqual(f.getvalue(), '<p test="test">\ntest\n</p>\n')

    def test_Hr_render(self):
        f = StringIO()
        testelement = hr.Hr()
        testelement.render(f)
        self.assertEqual(f.getvalue(), "<hr />\n")

    def test_attributes_Hr(self):
        f = StringIO()
        testelement = hr.Hr(test="test")
        testelement.render(f)
        self.assertEqual(f.getvalue(), '<hr test="test" />\n')

    def test_attributes_Hr(self):
        f = StringIO()
        testelement = hr.Hr("test")
        with self.assertRaises(TypeError):
            testelement.render(f)

    def test_A_render(self):
        f = StringIO()
        testelement = hr.A("http://google.com", "link")
        testelement.render(f)
        self.assertEqual(f.getvalue(), '<a href="http://google.com">link</a>\n')

    def test_H_render(self):
        f = StringIO()
        testelement = hr.H(2, "PythonClass - Class 6 example")
        testelement.render(f)
        self.assertEqual(f.getvalue(), '<h2>PythonClass - Class 6 example</h2>\n')

    def test_Ul_render(self):
        f = StringIO()
        testelement = hr.Ul(id="TheList", style="line-height:200%")
        testelement.render(f)
        self.assertEqual(f.getvalue(), '<ul id="TheList" style="line-height:200%">\n</ul>\n')

    def test_Li_render(self):
        f = StringIO()
        testelement = hr.Ul()
        testelement.append( hr.Li("test1") )
        testelement.render(f)
        self.assertEqual(f.getvalue(), '<ul>\n    <li>\n        test1\n    </li>\n</ul>\n')

if __name__ == '__main__':
    unittest.main()

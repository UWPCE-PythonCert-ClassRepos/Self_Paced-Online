import unittest
import html_render as hr


class ElementRenderTest(unittest.TestCase):
    """tests element render attributes"""

    def setUp(self):
        self.test = hr.Element(content=None)

    def test_element(self):
        self.assertEqual(self.test.tag, '')
        self.assertEqual(self.test.indent, '    ')
        self.assertEqual(self.test.content, [None])

    def test_element_append(self):
        self.test.append('new content')
        self.assertEqual(self.test.content, [None, 'new content'])

    def test_element_render(self):
        self.test.content = 'None'
        self.test.tag = 'html'
        self.assertEqual(self.test.render('file.txt', cur_ind=''),
                         ('<html>\n' + self.test.indent * '' +
                          'None\n' + '<\html>'))


class HTMLRenderTest(unittest.TestCase):
    """tests html render attributes"""

    def setUp(self):
        self.test = hr.Html(content=None)

    def test_html(self):
        # self.assertEqual(self.test.open_tag, '<html>')
        # self.assertEqual(self.test.close_tag, '</html>')
        self.test.append('new content')
        self.assertEqual(self.test.content, [None, 'new content'])


class BodyRenderTest(unittest.TestCase):
    """tests body render attributes"""

    def setUp(self):
        self.test = hr.Body(content=None)

    def test_body(self):
        # self.assertEqual(self.test.open_tag, '<body>')
        # self.assertEqual(self.test.close_tag, '</body>')
        self.test.append('new content')
        self.assertEqual(self.test.content, [None, 'new content'])


class ParaRenderTest(unittest.TestCase):
    """test p render attributes"""

    def setUp(self):
        self.test = hr.P(content=None)

    def test_p(self):
        # self.assertEqual(self.test.open_tag, '<p>')
        # self.assertEqual(self.test.close_tag, '</p>')
        self.test.append('new content')
        self.assertEqual(self.test.content, [None, 'new content'])

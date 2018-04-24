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
        self.assertEqual(self.test.tag, 'html')
        # self.assertEqual(self.test.close_tag, '</html>')
        self.test.append('new content')
        self.assertEqual(self.test.content, [None, 'new content'])


class BodyRenderTest(unittest.TestCase):
    """tests body render attributes"""

    def setUp(self):
        self.test = hr.Body(content=None)

    def test_body(self):
        self.assertEqual(self.test.tag, 'body')
        # self.assertEqual(self.test.close_tag, '</body>')
        self.test.append('new content')
        self.assertEqual(self.test.content, [None, 'new content'])


class ParaRenderTest(unittest.TestCase):
    """test p render attributes"""

    def setUp(self):
        self.test = hr.P(content=None)

    def test_p(self):
        self.assertEqual(self.test.tag, 'p')
        # self.assertEqual(self.test.close_tag, '</p>')
        self.test.append('new content')
        self.assertEqual(self.test.content, [None, 'new content'])


class HeadTest(unittest.TestCase):
    """test head render attributes"""

    def setUp(self):
        self.test = hr.Head(content=None)

    def test_head(self):
        self.assertEqual(self.test.tag, 'head')
        self.test.append('new content')
        self.assertEqual(self.test.content, [None, 'new content'])


class OneLineTagTest(unittest.TestCase):
    """test onelinetag render attributes"""

    def setUp(self):
        self.test = hr.OneLineTag(content=None)

    def test_olt(self):
        self.test.content = 'None'
        self.test.tag = 'olt'
        self.assertEqual(self.test.render('file.txt', cur_ind=''),
                         ('<olt>' + self.test.indent * '' +
                          'None' + '<\olt>'))


# class TitleTest(unittest.TestCase):
#     """test title render attributes"""

#     def setUp(self):
#         self.test = hr.Title(content=None)

#     def test_title(self):
#         self.assertEqual(self.test.tag, 'title')
#         self.test.append('new content')
#         self.assertEqual(self.content, [None, 'new content'])

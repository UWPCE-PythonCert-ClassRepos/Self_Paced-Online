import unittest
import html_render as hr
from io import StringIO


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
        self.f = StringIO()
        self.assertEqual(self.test.render(self.f, cur_ind=''),
                         ('<html>', 'None', '</html>'))


class HTMLRenderTest(unittest.TestCase):
    """tests html render attributes"""

    def setUp(self):
        self.test = hr.Html(content=None)

    def test_html(self):
        self.assertEqual(self.test.tag, 'html')
        self.test.append('new content')
        self.assertEqual(self.test.content, [None, 'new content'])


class BodyRenderTest(unittest.TestCase):
    """tests body render attributes"""

    def setUp(self):
        self.test = hr.Body(content=None)

    def test_body(self):
        self.assertEqual(self.test.tag, 'body')
        self.test.append('new content')
        self.assertEqual(self.test.content, [None, 'new content'])


class ParaRenderTest(unittest.TestCase):
    """test p render attributes"""

    def setUp(self):
        self.test = hr.P(
            style="text-align: center; font-style: oblique;")

    def test_p(self):
        self.assertEqual(self.test.tag, 'p')
        self.test.append('new content')
        self.assertEqual(self.test.content, [None, 'new content'])
        self.assertEqual(self.test.kwargs,
                         {'style': 'text-align: center; font-style: oblique;'})


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
        self.f = StringIO()
        self.assertEqual(('<olt>', 'None', '</olt>'),
                         self.test.render(self.f, cur_ind=''))


class TitleTest(unittest.TestCase):
    """test title render attributes"""

    def setUp(self):
        self.test = hr.Title(content=None)

    def test_title(self):
        self.assertEqual(self.test.tag, 'title')
        self.test.append('new content')
        self.assertEqual(self.test.content, [None, 'new content'])


class SelfClosingTagTest(unittest.TestCase):
    """test selfclosingtab render attributes"""

    def setUp(self):
        self.test = hr.SelfClosingTag()
        self.f = StringIO()

    def test_selfclosingtag(self):
        self.assertEqual(self.test.render(self.f, cur_ind=''),
                         '<sct />')


class HrTest(unittest.TestCase):
    """test hr render attributes"""

    def setUp(self):
        self.test = hr.Hr()

    def test_hr(self):
        self.assertEqual(self.test.tag, 'hr')
        self.assertEqual(self.test.content, [None])


class ATest(unittest.TestCase):
    """test anchor render attributes"""

    def setUp(self):
        self.test = hr.A(link='', content=None)
        self.f = StringIO()

    def test_a(self):
        self.assertEqual(self.test.tag, 'a')
        self.test.append('new content')
        self.assertEqual(self.test.content, [None, 'new content'])
        print('self.test.content contains:', self.test.content)
        self.test.link = 'http://duckduckgo.com'
        self.assertEqual(self.test.link, 'http://duckduckgo.com')
        self.assertEqual(self.test.render(self.f, cur_ind=''),
                         ("<a href=''>", [None, 'new content'], '</a>'))


class UlTest(unittest.TestCase):
    """test ul render attributes"""

    def setUp(self):
        self.test = hr.Ul(
            id='TheList', style='line-height:200%')

    def test_ul(self):
        self.assertEqual(self.test.tag, 'ul')
        self.test.append('new content')
        self.assertEqual(self.test.content, [None, 'new content'])
        self.assertEqual(self.test.kwargs,
                         {'id': 'TheList', 'style':
                          'line-height:200%'})


class LiTest(unittest.TestCase):
    """test li render attributes"""

    def setUp(self):
        self.test = hr.Li(content=None)

    def test_li(self):
        self.assertEqual(self.test.tag, 'li')
        self.test.append('new content')
        self.assertEqual(self.test.content, [None, 'new content'])


class HTest(unittest.TestCase):
    """test header render attributes"""

    def setUp(self):
        self.test = hr.H(integer=0, content=None)

    def test_h(self):
        self.assertEqual(self.test.tag, 'h')
        self.test.append('new content')
        self.assertEqual(self.test.content, [None, 'new content'])

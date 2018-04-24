import unittest
import html_render as hr
from io import StringIO

class TestHtmlRender(unittest.TestCase):

    def test_Element(self):
        test1 = hr.Element('this is content', key = 'val')
        self.assertEqual(test1.content, ['this is content'])
        self.assertEqual(test1.kwargs,{'key': 'val'})

    def test_append(self):
        test2 = hr.Element('first content')
        test2.append('some more content')
        self.assertEqual(test2.content, ['first content', 'some more content'])


    def test_render(self):

        test3 = hr.Element('Test for Render')
        test3.tag = 'p'
        f = StringIO()
        test3.render(f)
        self.assertEqual(f.getvalue(), f'<p>\n    Test for Render\n</p>\n')


    def test_OneLineTag(self):
        test4 = hr.OneLineTag('Test for OneLineTag')
        f = StringIO()
        test4.tag = 'p'
        test4.render(f,'')
        self.assertEqual(f.getvalue(),f'<p>    Test for OneLineTag</p>\n')


    def test_SelfClosingTag(self):
        test5 = hr.SelfClosingTag('Test for SelfClosingTag')
        f = StringIO()
        test5.tag = 'p'
        test5.render(f,'')
        self.assertEqual(f.getvalue(),f'<p>\n')


if __name__ == '__main__':
    unittest.main()

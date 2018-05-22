import unittest
import html_render as hr


class HtmlRenderingTests(unittest.TestCase):

    def test_element(self):
        element = hr.Element()
        self.assertEqual(element.content, [])

    def test_append(self):
        element = hr.Element()
        element.append('Testing.')
        self.assertEqual(element.content, ['Testing.'])


if __name__ == '__main__':
    unittest.main()

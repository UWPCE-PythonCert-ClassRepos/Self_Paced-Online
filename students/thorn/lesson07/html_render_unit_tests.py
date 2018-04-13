import unittest
import html_render as hr
from io import StringIO

class TagTests(unittest.TestCase):
    def test_html(self):
        ''' Test that it starts with <html> and ends with </html> '''
        e = hr.Element()
        test = hr.Html()
        e.render(hello)
        f = StringIO()
        test.render(f)
        lines = f.getvalue()
        lines.strip()
        print(lines)


class Step3Tests(unittest.TestCase):
    def test_head(self):
        ''' Test for proper head tag and that I remember how to make these. '''
        correct_tag = "head"
        self.assertEqual(hr.Head.tag, correct_tag)

    def test_title(self):
        ''' Test to make sure <title> tags are printed on the same line as their content as their super class OneLineTag dictates. '''
        test = hr.OneLineTag("One Line Test")
        test.tag = "title"
        f = StringIO()
        test.render(f)
        # Check for start and end with title
        self.assertEqual(f.getvalue()[:7], "<title>")        
        self.assertEqual(f.getvalue()[-9:], "</title>\n")


if __name__ == "__main__":
    unittest.main()
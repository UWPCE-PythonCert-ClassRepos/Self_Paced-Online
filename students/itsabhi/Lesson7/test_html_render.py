import html_render as hr
import unittest
from unittest.mock import patch
import os


class HtmlRenderTestCases(unittest.TestCase):

    def setUp(self):
        # Invoked before each test method
        self.test_class = hr.Element()
        self.tag = ""
        self.cur_ind = "    "
        self.another_attrib_key = ""
        self.another_attrib_value = ""

    def test_init_empty_content(self):
        # Tests base class init method: initializing Element object with empty content
        result = self.test_class.content
        self.assertListEqual([], result)

    def test_init_some_content_string(self):
        # Tests base class init method: initializing Element object with some string
        test_class_w_content = hr.Element("Here is a line of text.\n")
        result_content = test_class_w_content.content
        self.assertListEqual(["Here is a line of text.\n"], result_content)

    def test_init_w_kwargs(self):
        # Tests base class init method: initializing Element object with additional keyword arguments
        test_class_w_content_kwargs = hr.Element("Here is a line of text", style="color: red")
        result_attrib_key = test_class_w_content_kwargs.another_attrib_key
        result_attrib_val = test_class_w_content_kwargs.another_attrib_value
        self.assertDictEqual({"style": "color: red"}, {result_attrib_key: result_attrib_val})

    def test_append(self):
        # Tests base class append method: appending content to Element object
        self.test_class.append("Here, we append some content.\n")
        result_content = self.test_class.content
        self.assertListEqual(["Here, we append some content.\n"], result_content)

    def test_opening_tag_w_attribute(self):
        # Tests base class opening_tag_w_attribute method
        self.test_class.tag = "xyz"
        self.test_class.another_attrib_key = "style"
        self.test_class.another_attrib_value = "font-style: oblique;"
        result = self.test_class.opening_tag_w_attribute(self.cur_ind)
        self.assertEqual("    <xyz style:\"font-style: oblique;\">", result)

    def test_render_w_opt_attr(self):
        # Tests base class render method IF Element object has optional attributes.
        # Output file is created in current working directory
        f = open("test_renderfile.txt", "w")
        self.test_class.tag = "xyz"
        self.test_class.another_attrib_key = "style"
        self.test_class.another_attrib_value = "font-style: oblique;"
        self.test_class.render(f)
        self.assertIn('test_renderfile.txt', os.listdir())

    def test_render_wo_opt_attr(self):
        # Tests base class render method IF Element object has NO optional attributes.
        # Output file is created in current working directory
        f = open("test_renderfile.txt", "w")
        self.test_class.tag = "xyz"
        self.test_class.render(f)
        self.assertIn('test_renderfile.txt', os.listdir())

    def test_HTML_obj(self):
        # Tests HTML tag
        html_obj = hr.Html()
        self.assertEqual(html_obj.tag, "html")

    def test_Body_obj(self):
        # Tests body tag
        body_obj = hr.Body()
        self.assertEqual(body_obj.tag, "body")

    def test_P_obj(self):
        # Tests p tag
        p_obj = hr.P()
        self.assertEqual(p_obj.tag, "p")

    def test_Head_obj(self):
        # Tests head tag
        head_obj = hr.Head()
        self.assertEqual(head_obj.tag, "head")

    def test_Title_obj(self):
        # Tests Title tag
        title_obj = hr.Title()
        self.assertEqual(title_obj.tag, "Title")

    def test_selfclosingtag_obj(self):
        # Tests content is an empty list
        selfclosingtag_obj = hr.SelfClosingTag()
        self.assertListEqual(selfclosingtag_obj.content, [])

    def test_selfclosingtag_obj_TypeError(self):
        # Tests SelfClosingTag object cannot be initialized with content
        with self.assertRaises(TypeError):
            hr.SelfClosingTag("some_text")

    def test_hr_obj(self):
        # Tests hr tag
        hr_obj = hr.Hr()
        self.assertEqual(hr_obj.tag, "hr /")

    def test_br_obj(self):
        # Tests br tag
        br_obj = hr.Br()
        self.assertEqual(br_obj.tag, "br /")

    def test_a_obj(self):
        # Tests "a" tag
        a_obj = hr.A("www.cnn.com", "Click here for news")
        self.assertEqual(a_obj.tag, "a")

    def test_a_obj_hypertext(self):
        # Tests "A" object created with hypertext link
        a_obj = hr.A("www.cnn.com", "Click here for news")
        self.assertDictEqual({a_obj.another_attrib_key: a_obj.another_attrib_value}, {"href": "www.cnn.com"})
        self.assertListEqual(a_obj.content, ["Click here for news"])

    def test_ul_obj(self):
        # Tests ul tag
        ul_obj = hr.Ul()
        self.assertEqual(ul_obj.tag, "ul")

    def test_li_obj(self):
        # Tests li tag
        li_obj = hr.Li()
        self.assertEqual(li_obj.tag, "li")

    def test_meta_obj(self):
        # Tests meta tag
        meta_obj = hr.Meta()
        self.assertEqual(meta_obj.tag, "meta charset=\"UTF-8\" /")

    def test_h_obj(self):
        # Tests header obj
        h_obj = hr.H(3, "Testing Python class exercise")
        self.assertEqual(h_obj.tag, "h3")
        self.assertListEqual(h_obj.content, ["Testing Python class exercise"])


if __name__ == '__main__':
    unittest.main()
    
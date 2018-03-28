from html_render import * 
import unittest

class test_element(unittest.TestCase):

    

    def test_html(self):
        html = Html()
        assert html.opening_tag == "<!DOCTYPE html>\n<html>\n"
        assert html.closing_tag == "</html>\n"
        assert html.attr_str == ""

    def test_body(self):
        body = Body()
        tag = body.tag
        cur_ind = body.cur_ind 
        assert body.opening_tag == f"{cur_ind}<{tag}>\n"
        assert body.closing_tag == f"{cur_ind}</{tag}>\n"
        assert body.attr_str == ""

    def test_p(self):
        p = P()
        tag = p.tag
        cur_ind = p.cur_ind
        assert p.opening_tag == f"{cur_ind}<{tag}>\n"
        assert p.closing_tag == f"{cur_ind}</{tag}>\n"
        assert p.attr_str == "" 

    def test_head(self):
        head = Head()
        tag = head.tag
        cur_ind = head.cur_ind
        assert head.opening_tag == f"{cur_ind}<{tag}>\n"
        assert head.closing_tag == f"{cur_ind}</{tag}>\n"
        assert head.attr_str == "" 


    def test_title(self):
        """ also tests OneLineTag """
        t = Title()
        tag = t.tag
        cur_ind = t.cur_ind
        t.append('test')
        assert t.one_line_tag == f"{cur_ind}<{tag}>test</{tag}>\n"

    def test_hr(self):
        hr = Hr()
        tag = hr.tag
        cur_ind = hr.cur_ind
        assert hr.opening_tag == f"{cur_ind}<{tag}>\n"
        assert hr.closing_tag == f"{cur_ind}</{tag}>\n"
        assert hr.attr_str == ""

    def test_br(self):
        br = Br()
        tag = br.tag
        cur_ind = br.cur_ind
        assert br.opening_tag == f"{cur_ind}<{tag}>\n"
        assert br.closing_tag == f"{cur_ind}</{tag}>\n"
        assert br.attr_str == ""

    def test_a(self):
        link = 'http://www.google.com'
        a = A(link,content=None)
        tag = a.tag
        cur_ind = a.cur_ind
        attr_str = a.attr_str
        assert a.opening_tag == f"{cur_ind}<{tag} {attr_str}>\n"
        assert a.closing_tag == f"{cur_ind}</{tag}>\n"
        assert a.attr_str == f"href=\"{link}\""

    def test_ul(self):
        ul = Ul()
        tag = ul.tag
        cur_ind = ul.cur_ind
        assert ul.opening_tag == f"{cur_ind}<{tag}>\n"
        assert ul.closing_tag == f"{cur_ind}</{tag}>\n"
        assert ul.attr_str == ""

    def test_li(self):
        li = Li()
        tag = li.tag
        cur_ind = li.cur_ind
        assert li.opening_tag == f"{cur_ind}<{tag}>\n"
        assert li.closing_tag == f"{cur_ind}</{tag}>\n"
        assert li.attr_str == ""
 
    def test_h(self):
        h = H(2,None)
        assert h.tag == "h2"
        tag = h.tag
        cur_ind = h.cur_ind
        assert h.opening_tag == f"{cur_ind}<{tag}>\n"
        assert h.closing_tag == f"{cur_ind}</{tag}>\n"
        assert h.attr_str == ""

    def test_meta(self):
        """ also tests self closing tag """
        meta = Meta()
        tag = meta.tag
        cur_ind = meta.cur_ind
        attr_str = meta.attr_str
        assert meta.closed_tag == f"{cur_ind}<{tag} {attr_str} />\n"
        #assert meta.closing_tag == f"{cur_ind}</{tag}>\n"

if __name__ == '__main__':
    unittest.main()
 

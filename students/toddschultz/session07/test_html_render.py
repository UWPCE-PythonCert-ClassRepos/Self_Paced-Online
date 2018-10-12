import html_render as hr
from io import StringIO

def test_p():
    ptag = hr.Element("I did not like this assignment at all.")
    ptag.tag = 'html'
    x = StringIO()
    ptag.render(x)
    assert x.getvalue() == "<html>\nI did not like this assignment at all.\n</html>\n"

def test_html():
    htmltag = hr.Element("And here is another piece of text")
    htmltag.tag = 'html'
    x = StringIO()
    htmltag.render(x)
    assert x.getvalue() == "<html>\nAnd here is another piece of text\n</html>\n"

def test_body():
    bodytag = hr.Element()
    bodytag.tag = "body"
    x = StringIO()
    bodytag.render(x)
    assert x.getvalue() == "<body>\n</body>\n"

def test_head():
    headtag = hr.Element()
    headtag.tag = "head"
    x = StringIO()
    headtag.render(x)
    assert x.getvalue() == "<head>\n</head>\n"

def test_title():
    titletag = hr.Element("PythonClass = Revision 1087:")
    titletag.tag = "title"
    x = StringIO()
    titletag.render(x)
    assert x.getvalue() == "<title>\nPythonClass = Revision 1087:\n</title>\n"

def test_hr():
    hrtag = hr.SelfClosingTag()
    hrtag.tag = "hr"
    x = StringIO()
    hrtag.render(x)
    assert x.getvalue() == "<hr>\n"

def test_br():
    brtag = hr.SelfClosingTag()
    brtag.tag = "br"
    x = StringIO()
    brtag.render(x)
    assert x.getvalue() == "<br>\n"

def test_a():
    atag = hr.Element()
    atag.tag = "a"
    x = StringIO()
    atag.render(x)
    assert x.getvalue() == "<a>\n</a>\n"

def test_ul():
    ultag = hr.Element()
    ultag.tag = "ul"
    x = StringIO()
    ultag.render(x)
    assert x.getvalue() == "<ul>\n</ul>\n"

def test_li():
    litag = hr.Element()
    litag.tag = "li"
    x = StringIO()
    litag.render(x)
    assert x.getvalue() == "<li>\n</li>\n"

def test_h():
    htag = hr.OneLineTag()
    htag.tag = "h"
    x = StringIO()
    htag.render(x)
    assert x.getvalue() == "<h></h>\n"

def test_meta():
    metatag = hr.SelfClosingTag()
    metatag.tag = "ul"
    x = StringIO()
    metatag.render(x)
    assert x.getvalue() == "<ul>\n"









# tests for html_render using pytest

import html_render
from io import StringIO

def test_Element_append():
    sample = html_render.Element("a")
    sample.append("b")
    assert sample.contentList == ["a", "b"]


def test_Element_render():  # using body subclass as simple content to test render function with
    sample = html_render.Body()
    f = StringIO()
    sample.render(f)
    g = f.getvalue()
    assert g == "<body>\n</body>\n"


def test_Html_render():
    sample = html_render.Html()
    f = StringIO()
    sample.render(f)
    g = f.getvalue()
    assert g == "<!DOCTYPE html><html>\n</html>\n"


def test_OneLineTag_render(): #using title subclass as simple content to test render function with
    sample = html_render.Title()
    f = StringIO()
    sample.render(f)
    g = f.getvalue()
    assert g == "<title></title>\n"


def test_SelfClosingTag_render(): #using hr subclass as simple content to test render function with
    sample = html_render.Hr()
    f = StringIO()
    sample.render(f)
    g = f.getvalue()
    assert g == "<hr />\n"


def test_A_render():
    sample = html_render.A("google.com", "google")
    f = StringIO()
    sample.render(f)
    g = f.getvalue()
    assert g == "<a href=\"google.com\">google</a>"


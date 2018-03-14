import html_render as hr
from io import StringIO

def test_step1():
    """
    Step 1 Tests
    """
    f = StringIO()
    a = hr.Element("Test_A")
    a.render(f, "    ")
    assert "html" == a.tag
    assert 0 == a.indent
    assert ("Test_A",) == a.substance
    assert ("<html>\n    Test_A\n</html>\n") == f.getvalue()
    
    g = StringIO()
    a.append("Test_B")
    a.render(g, "    ")
    assert ("Test_A", "Test_B") == a.substance
    assert ("<html>\n    Test_A\n    Test_B\n</html>\n") == g.getvalue()


def test_step2():
    f = StringIO()
    a = hr.Html()
    b = hr.Body()
    p = hr.P()

    assert "html" == a.tag
    assert "body" == b.tag
    assert "p" == p.tag
    p.append("Test")
    b.append(p)
    assert ("Test",) == p.substance
    b.render(f, "    ")
    print(f.getvalue())
    assert "<body>\n    <p>\n        Test\n    </p>\n</body>\n" == f.getvalue()

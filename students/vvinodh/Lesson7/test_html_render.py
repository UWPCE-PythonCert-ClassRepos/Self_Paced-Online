import html_render as hr

# Test Step One


def test_html_class_creation():

    page = hr.Html()

    assert page.open_tag == ("<html>")
    assert page.close_tag == ("</html>")

# Test Step Two


def test_body_p_creation():

    page = hr.Html()
    body = hr.Body()
    p = hr.P("And the base keeps running, running...")

    assert p.content[0] == ("And the base keeps running, running...")
    assert p.open_tag == ("<p>")

    body.append(p)

    assert body.content[1].content[0] == (
        "And the base keeps running, running...")
    assert body.open_tag == ("<body>")

    page.append(body)

    assert page.content[1].content[1].content[0] == (
        "And the base keeps running, running...")
    assert page.open_tag == ("<html>")

# Test Step Three


def test_single_line_tags():

    head = hr.Head()
    title = hr.Title("PythonClass = Revision 1087:")

    assert title.content == ("PythonClass = Revision 1087:")
    assert title.open_tag == ("<title>")
    assert head.open_tag == ("<head>")

    head.append(title)

    assert head.content[1].content == ("PythonClass = Revision 1087:")

# Test Step Four


def test_tag_attributes():

    p = hr.P("Here is a paragraph of text -- there could be more of them, "
             "but this is enough  to show that we can do some text",
             style="text-align: center; font-style: oblique;")

    assert p.open_tag == (
        '<p style="text-align: center; font-style: oblique;">')
    assert p.content[0] == ("Here is a paragraph of text -- there"
                            " could be more of them,"
                            " but this is enough  to show that we"
                            " can do some text")

# Test Step Five


def test_self_closing_tags():

    horiz_rule = hr.Hr()
    line_break = hr.Br()

    assert horiz_rule.tag == ("<hr />")
    assert line_break.tag == ("<br />")

# Test Step Six


def test_hyperlinks():

    a = hr.A("http://google.com", "link")

    assert a.open_tag == ('<a href="http://google.com">')
    assert a.content[0] == ("link")

# Test Step Seven


def test_lists():

    u_list = hr.Ul(id="TheList", style="line-height:200%")


    u_list.append(hr.Li("The first item in a list"))
    u_list.append(hr.Li("This is the second item", style="color: red"))

    assert u_list.content[1].content[0] == ("The first item in a list")
    assert u_list.content[2].content[0] == ("This is the second item")

# Test Step Eight


def test_doc_meta_tags():
    """A function to test the added meta self-closing tag."""
    page = hr.Html()
    head = hr.Head()

    head.append(hr.Meta(charset="UTF-8"))

    assert head.content[1].tag == ('<meta charset="UTF-8" />')


print("All tests have passed!")

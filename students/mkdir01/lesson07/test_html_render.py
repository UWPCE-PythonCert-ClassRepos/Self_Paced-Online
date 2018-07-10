#!/usr/bin/env python

from io import StringIO
import html_render as hr


def render_page(page, filename, indent=None):
    f = StringIO()
    if indent is None:
        page.render(f)
    else:
        page.render(f, indent)

    print(f.getvalue())
    with open(filename, 'w') as outfile:
        outfile.write(f.getvalue())


def test_Element():
    page = hr.Element()
    render_page(page, "page.html")
    testdata = open("page.html").read()
    assert testdata == "<html>\n</html>"


def test_Element_test_Content():
    page = hr.Element()
    page.append("Test 1")
    render_page(page, "page.html")
    testdata = open("page.html").read()
    assert testdata == "<html>\n    Test 1\n</html>"


# Step 1
#########
def test_Element_real_Content():
    page = hr.Element()
    page.append("Here is a paragraph of text -- there could be more of them, "
            "but this is enough  to show that we can do some text")
    page.append("And here is another piece of text -- you should be able to add any number")
    render_page(page, "page.html")
    testdata = open("page.html").read()
    assert testdata == "<html>\n    Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text\n    And here is another piece of text -- you should be able to add any number\n</html>"


def test_Html():
    page = hr.Html()
    render_page(page, "page.html")
    testdata = open("page.html").read()
    assert testdata == "<html>\n</html>"


def test_Body():
    body = hr.Body()
    testdata = body.content
    assert testdata == "<body>\n</body>"


def test_Html_Body():
    page = hr.Html()
    body = hr.Body()
    page.append(body)
    render_page(page, "page.html")
    testdata = open("page.html").read()
    assert testdata == "<html>\n    <body>\n    </body>\n</html>"

def test_P():
    para = hr.P()
    testdata = para.content
    assert testdata == "<p>\n</p>"


def test_P_test_Content():
    para = hr.P("Test 2")
    testdata = para.content
    assert testdata == "<p>\n    Test 2\n</p>"


def test_Body_test_Content():
    body = hr.Body()
    body.append(hr.P("Test 3"))
    testdata = body.content
    assert testdata == "<body>\n    <p>\n        Test 3\n    </p>\n</body>"


def test_Body_P_test_Content():
    body = hr.Body()
    body.append(hr.P("Test 4"))
    body.append(hr.P("Test 5"))
    testdata = body.content
    assert testdata == "<body>\n    <p>\n        Test 4\n    </p>\n    <p>\n        Test 5\n    </p>\n</body>"


def test_Html_Body_P_test_Content():
    page = hr.Html()
    body = hr.Body()
    body.append(hr.P("Test 4"))
    body.append(hr.P("Test 5"))
    page.append(body)
    render_page(page, "page.html")
    testdata = open("page.html").read()
    assert testdata == "<html>\n    <body>\n        <p>\n            Test 4\n        </p>\n        <p>\n            Test 5\n        </p>\n    </body>\n</html>"


# Step 2
##########
def test_Html_Body_P_real_Content():
    page = hr.Html()
    body = hr.Body()
    body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
                  "but this is enough  to show that we can do some text"))
    body.append(hr.P("And here is another piece of text -- you should be able to add any number"))
    page.append(body)
    render_page(page, "page.html")
    testdata = open("page.html").read()
    assert testdata == "<html>\n    <body>\n        <p>\n            Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text\n        </p>\n        <p>\n            And here is another piece of text -- you should be able to add any number\n        </p>\n    </body>\n</html>"


def test_Head():
    head = hr.Head()
    testdata = head.content
    assert testdata == "<head>\n</head>"


def test_Title():
    title = hr.Title()
    testdata = title.content
    assert testdata == "<title>\n</title>"


def test_Title_test_Content():
    title = hr.Title("Test 6")
    testdata = title.content
    assert testdata == "<title>Test 6</title>"


def test_Head_Title_test_Content():
    head = hr.Head()
    head.append(hr.Title("Test 7"))
    testdata = head.content
    assert testdata == "<head>\n    <title>Test 7</title>\n</head>"


def test_Html_Head_Title_test_Content():
    page = hr.Html()
    head = hr.Head()
    head.append(hr.Title("Test 8"))
    page.append(head)
    render_page(page, "page.html")
    testdata = open("page.html").read()
    assert testdata == "<html>\n    <head>\n        <title>Test 8</title>\n    </head>\n</html>"


def test_Html_Head_Title_Body_P_test_Content():
    page = hr.Html()
    head = hr.Head()
    head.append(hr.Title("Test 9"))
    page.append(head)
    body = hr.Body()
    body.append(hr.P("Test 10"))
    page.append(body)
    render_page(page, "page.html")
    testdata = open("page.html").read()
    assert testdata == "<html>\n    <head>\n        <title>Test 9</title>\n    </head>\n    <body>\n        <p>\n            Test 10\n        </p>\n    </body>\n</html>"


def test_Html_Head_Title_Body_P_test_Content_2():
    page = hr.Html()
    head = hr.Head()
    head.append(hr.Title("Test 11"))
    page.append(head)
    body = hr.Body()
    body.append(hr.P("Test 12"))
    body.append(hr.P("Test 13"))
    page.append(body)
    render_page(page, "page.html")
    testdata = open("page.html").read()
    assert testdata == "<html>\n    <head>\n        <title>Test 11</title>\n    </head>\n    <body>\n        <p>\n            Test 12\n        </p>\n        <p>\n            Test 13\n        </p>\n    </body>\n</html>"


# Step 3
##########
def test_Html_Head_Title_Body_P_real_Content():
    page = hr.Html()
    head = hr.Head()
    head.append(hr.Title("PythonClass = Revision 1087:"))
    page.append(head)
    body = hr.Body()
    body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
                     "but this is enough  to show that we can do some text"))
    body.append(hr.P("And here is another piece of text -- you should be able to add any number"))
    page.append(body)
    render_page(page, "page.html")
    testdata = open("page.html").read()
    assert testdata == "<html>\n    <head>\n        <title>PythonClass = Revision 1087:</title>\n    </head>\n    <body>\n        <p>\n            Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text\n        </p>\n        <p>\n            And here is another piece of text -- you should be able to add any number\n        </p>\n    </body>\n</html>"


def test_P_test_Content():
    para = hr.P(style="Test 14")
    testdata = para.content
    assert testdata == "<p style=\"Test 14\">\n</p>"


def test_P():
    para = hr.P()
    testdata = para.content
    assert testdata == "<p>\n</p>"


def test_P_test_Content_style():
    para = hr.P("Test 15", style="Test 16")
    testdata = para.content
    assert testdata == "<p style=\"Test 16\">\n    Test 15\n</p>"


def test_Body_P_test_Content_style():
    body = hr.Body()
    body.append(hr.P("Test 17", style="Test 18"))
    testdata = body.content
    assert testdata == "<body>\n    <p style=\"Test 18\">\n        Test 17\n    </p>\n</body>"


def test_Html_Body_P_test_Content_style():
    page = hr.Html()
    body = hr.Body()
    body.append(hr.P("Test 19", style="Test 20"))
    page.append(body)
    render_page(page, "page.html")
    testdata = open("page.html").read()
    assert testdata == "<html>\n    <body>\n        <p style=\"Test 20\">\n            Test 19\n        </p>\n    </body>\n</html>"


def test_Html_Head_Title_Body_P_test_Content_style():
    page = hr.Html()
    head = hr.Head()
    head.append(hr.Title("Test 21"))
    page.append(head)
    body = hr.Body()
    body.append(hr.P("Test 22", style="Test 23"))
    page.append(body)
    render_page(page, "page.html")
    testdata = open("page.html").read()
    assert testdata == "<html>\n    <head>\n        <title>Test 21</title>\n    </head>\n    <body>\n        <p style=\"Test 23\">\n            Test 22\n        </p>\n    </body>\n</html>"


# Step 4
##########
def test_Html_Head_Title_Body_P_real_Content_style():
    page = hr.Html()
    head = hr.Head()
    head.append(hr.Title("PythonClass = Revision 1087:"))
    page.append(head)
    body = hr.Body()
    body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
                     "but this is enough  to show that we can do some text",
                     style="text-align: center; font-style: oblique;"))
    page.append(body)
    render_page(page, "page.html")
    testdata = open("page.html").read()
    assert testdata == "<html>\n    <head>\n        <title>PythonClass = Revision 1087:</title>\n    </head>\n    <body>\n        <p style=\"text-align: center; font-style: oblique;\">\n            Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text\n        </p>\n    </body>\n</html>"


def test_Hr():
    horiz = hr.Hr()
    testdata = horiz.content
    assert testdata == "<hr />"


def test_Body_Hr():
    body = hr.Body()
    horiz = hr.Hr()
    body.append(horiz)
    testdata = body.content
    assert testdata == "<body>\n    <hr />\n</body>"


def test_Body_Hr_2():
    body = hr.Body()
    body.append(hr.Hr())
    testdata = body.content
    assert testdata == "<body>\n    <hr />\n</body>"


def test_Body_P_Hr_test_Content_style():
    body = hr.Body()
    body.append(hr.P("Test 24", style="Test 25"))
    body.append(hr.Hr())
    testdata = body.content
    assert testdata == "<body>\n    <p style=\"Test 25\">\n        Test 24\n    </p>\n    <hr />\n</body>"


def test_Html_Boidy_P_Hr_test_Content_style():
    page = hr.Html()
    body = hr.Body()
    body.append(hr.P("Test 26", style="Test 27"))
    body.append(hr.Hr())
    page.append(body)
    render_page(page, "page.html")
    testdata = open("page.html").read()
    assert testdata == "<html>\n    <body>\n        <p style=\"Test 27\">\n            Test 26\n        </p>\n        <hr />\n    </body>\n</html>"


def test_Html_Head_Title_Body_P_Hr_test_Content_style():
    page = hr.Html()
    head = hr.Head()
    head.append(hr.Title("Test 28"))
    page.append(head)
    body = hr.Body()
    body.append(hr.P("Test 29", style="Test 30"))
    body.append(hr.Hr())
    page.append(body)
    render_page(page, "page.html")
    testdata = open("page.html").read()
    assert testdata == "<html>\n    <head>\n        <title>Test 28</title>\n    </head>\n    <body>\n        <p style=\"Test 30\">\n            Test 29\n        </p>\n        <hr />\n    </body>\n</html>"

# Step 5
#########
def test_Html_Head_Title_Body_P_Hr_real_Content_style():
    page = hr.Html()
    head = hr.Head()
    head.append(hr.Title("PythonClass = Revision 1087:"))
    page.append(head)
    body = hr.Body()
    body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
                     "but this is enough  to show that we can do some text",
                     style="text-align: center; font-style: oblique;"))
    body.append(hr.Hr())
    page.append(body)
    render_page(page, "page.html")
    testdata = open("page.html").read()
    assert testdata == "<html>\n    <head>\n        <title>PythonClass = Revision 1087:</title>\n    </head>\n    <body>\n        <p style=\"text-align: center; font-style: oblique;\">\n            Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text\n        </p>\n        <hr />\n    </body>\n</html>"


def test_Body_test_Content_2():
    body = hr.Body()
    body.append("Test 31")
    testdata = body.content
    assert testdata == "<body>\n    Test 31\n</body>"

def test_A_test_Content():
    anchor = hr.A("Test 31_a", "Test 31_b")
    testdata = anchor.content
    assert testdata == "<a href=\"Test 31_a\">Test 31_b</a>"


def test_Body_A_test_Content():
    body = hr.Body()
    body.append( hr.A("Test 32", "Test 33") )
    testdata = body.content
    assert testdata == "<body>\n    <a href=\"Test 32\">Test 33</a>\n</body>"

def test_Body_A_test_Content_2():
    body = hr.Body()
    body.append("Test 34 ")
    body.append( hr.A("Test 35", "Test 36") )
    body.append(" Test 37")
    testdata = body.content
    assert testdata == "<body>\n    Test 34 \n    <a href=\"Test 35\">Test 36</a>\n     Test 37\n</body>"

def test_Html_Body_A_test_Content():
    page = hr.Html()
    body = hr.Body()
    body.append("Test 38 ")
    body.append( hr.A("Test 39", "Test 40") )
    body.append(" Test 41")
    page.append(body)
    render_page(page, "page.html")
    testdata = open("page.html").read()
    assert testdata == "<html>\n    <body>\n        Test 38 \n        <a href=\"Test 39\">Test 40</a>\n         Test 41\n    </body>\n</html>"

def test_Html_Head_Title_Body_P_Hr_A_test_Content():
    page = hr.Html()
    head = hr.Head()
    head.append(hr.Title("Test 42"))
    page.append(head)
    body = hr.Body()
    body.append(hr.P("Test 43", style="Test 44"))
    body.append(hr.Hr())
    body.append("Test 45 ")
    body.append( hr.A("Test 46", "Test 47") )
    body.append(" Test 48")
    page.append(body)
    render_page(page, "page.html")
    testdata = open("page.html").read()
    assert testdata == "<html>\n    <head>\n        <title>Test 42</title>\n    </head>\n    <body>\n        <p style=\"Test 44\">\n            Test 43\n        </p>\n        <hr />\n        Test 45 \n        <a href=\"Test 46\">Test 47</a>\n         Test 48\n    </body>\n</html>"

# Step 6
#########
def test_Html_Head_Title_Body_P_Hr_A_real_Content():
    page = hr.Html()
    head = hr.Head()
    head.append(hr.Title("PythonClass = Revision 1087:"))
    page.append(head)
    body = hr.Body()
    body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
                     "but this is enough  to show that we can do some text",
                     style="text-align: center; font-style: oblique;"))
    body.append(hr.Hr())
    body.append("And this is a ")
    body.append( hr.A("http://google.com", "link") )
    body.append("to google")
    page.append(body)
    render_page(page, "page.html")
    testdata = open("page.html").read()
    assert testdata == "<html>\n    <head>\n        <title>PythonClass = Revision 1087:</title>\n    </head>\n    <body>\n        <p style=\"text-align: center; font-style: oblique;\">\n            Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text\n        </p>\n        <hr />\n        And this is a \n        <a href=\"http://google.com\">link</a>\n        to google\n    </body>\n</html>"

def test_H_test_Content():
    heading = hr.H(2, "Test 49")
    testdata = heading.content
    assert testdata == "<h2>Test 49</h2>"

def test_Body_H_test_Content():
    body = hr.Body()
    body.append( hr.H(2, "Test 50") )
    testdata = body.content
    assert testdata == "<body>\n    <h2>Test 50</h2>\n</body>"

def test_Ul_test_Content_style():
    unordered = hr.Ul(id="Test 51", style="Test 52")
    testdata = unordered.content
    assert testdata == "<ul id=\"Test 51\" style=\"Test 52\">\n</ul>"

def test_Body_Ul_test_Content_style():
    body = hr.Body()
    unordered = hr.Ul(id="Test 53", style="Test 54")
    body.append(unordered)
    testdata = body.content
    assert testdata == "<body>\n    <ul id=\"Test 53\" style=\"Test 54\">\n    </ul>\n</body>"

def test_Li():
    item = hr.Li()
    testdata = item.content
    assert testdata == "<li>\n</li>"

def test_Li_test_Content():
    item = hr.Li()
    item.append("Test 55")
    testdata = item.content
    assert testdata == "<li>\n    Test 55\n</li>"

def test_Lt_test_Content_style():
    item = hr.Li()
    item.append("Test 55_a", style="Test 55_b")
    testdata = item.content
    assert testdata == "<li style=\"Test 55_b\">\n    Test 55_a\n</li>"

def test_Ul_Li_A_test_Content_id_style():
    unordered = hr.Ul(id="Test 56", style="Test 57")
    item = hr.Li()
    item.append("Test 58")
    item.append( hr.A("Test 59", "Test 60") )
    item.append(" Test 61")
    unordered.append(item)
    testdata = unordered.content
    assert testdata == "<ul id=\"Test 56\" style=\"Test 57\">\n    <li>\n        Test 58\n        <a href=\"Test 59\">Test 60</a>\n         Test 61\n    </li>\n</ul>"

def test_Ul_Li_A_test_Content_id_style_2():
    unordered = hr.Ul(id="Test 62", style="Test 63")
    unordered.append( hr.Li("Test 64") )
    unordered.append( hr.Li("Test 65", style="Test 66") )
    item = hr.Li()
    item.append("Test 67")
    item.append( hr.A("Test 68", "Test 69") )
    item.append(" Test 70")
    unordered.append(item)
    testdata = unordered.content
    assert testdata == "<ul id=\"Test 62\" style=\"Test 63\">\n    <li>\n        Test 64\n    </li>\n    <li style=\"Test 66\">\n        Test 65\n    </li>\n    <li>\n        Test 67\n        <a href=\"Test 68\">Test 69</a>\n         Test 70\n    </li>\n</ul>"

def test_Html_Body_Ul_Li_A_test_Content_id_style():
    page = hr.Html()
    body = hr.Body()
    unordered = hr.Ul(id="Test 71", style="Test 72")
    unordered.append( hr.Li("Test 73") )
    unordered.append( hr.Li("Test 74", style="Test 75") )
    item = hr.Li()
    item.append("Test 76")
    item.append( hr.A("Test 77", "Test 78") )
    item.append(" Test 79")
    unordered.append(item)
    body.append(unordered)
    page.append(body)
    testdata = page.content
    assert testdata == "<html>\n    <body>\n        <ul id=\"Test 71\" style=\"Test 72\">\n            <li>\n                Test 73\n            </li>\n            <li style=\"Test 75\">\n                Test 74\n            </li>\n            <li>\n                Test 76\n                <a href=\"Test 77\">Test 78</a>\n                 Test 79\n            </li>\n        </ul>\n    </body>\n</html>"

# Step 7
#########
def test_Html_Body_Ul_Li_A_real_Content_id_style():
    page = hr.Html()
    head = hr.Head()
    head.append(hr.Title("PythonClass = Revision 1087:"))
    page.append(head)
    body = hr.Body()
    body.append( hr.H(2, "PythonClass - Class 6 example") )
    body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
                     "but this is enough  to show that we can do some text",
                     style="text-align: center; font-style: oblique;"))
    body.append(hr.Hr())
    list = hr.Ul(id="TheList", style="line-height:200%")
    list.append( hr.Li("The first item in a list") )
    list.append( hr.Li("This is the second item", style="color: red") )
    item = hr.Li()
    item.append("And this is a ")
    item.append( hr.A("http://google.com", "link") )
    item.append("to google")
    list.append(item)
    body.append(list)
    page.append(body)
    render_page(page, "page.html")
    testdata = open("page.html").read()
    assert testdata == "<html>\n    <head>\n        <title>PythonClass = Revision 1087:</title>\n    </head>\n    <body>\n        <h2>PythonClass - Class 6 example</h2>\n        <p style=\"text-align: center; font-style: oblique;\">\n            Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text\n        </p>\n        <hr />\n        <ul id=\"TheList\" style=\"line-height:200%\">\n            <li>\n                The first item in a list\n            </li>\n            <li style=\"color: red\">\n                This is the second item\n            </li>\n            <li>\n                And this is a \n                <a href=\"http://google.com\">link</a>\n                to google\n            </li>\n        </ul>\n    </body>\n</html>"

def test_Meta_test_Content_charset():
    meta = hr.Meta(charset="Test 80")
    testdata = meta.content
    assert testdata == "<meta charset=\"Test 80\" />"

def test_Head_Meta_test_Content_charset():
    head = hr.Head()
    head.append( hr.Meta(charset="Test 81") )
    testdata = head.content
    assert testdata == "<head>\n    <meta charset=\"Test 81\" />\n</head>"

# Step 8
########
def test_Html_Head_Meta_Title_Body_H_P_Hr_Ul_Li_A_real_Content_charset_style_id():
    page = hr.Html()
    head = hr.Head()
    head.append( hr.Meta(charset="UTF-8") )
    head.append(hr.Title("PythonClass = Revision 1087:"))
    page.append(head)
    body = hr.Body()
    body.append( hr.H(2, "PythonClass - Example") )
    body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
                     "but this is enough  to show that we can do some text",
                     style="text-align: center; font-style: oblique;"))
    body.append(hr.Hr())
    list = hr.Ul(id="TheList", style="line-height:200%")
    list.append( hr.Li("The first item in a list") )
    list.append( hr.Li("This is the second item", style="color: red") )
    item = hr.Li()
    item.append("And this is a ")
    item.append( hr.A("http://google.com", "link") )
    item.append("to google")
    list.append(item)
    body.append(list)
    page.append(body)
    render_page(page, "page.html")
    testdata = open("page.html").read()
    assert testdata == "<html>\n    <head>\n        <meta charset=\"UTF-8\" />\n        <title>PythonClass = Revision 1087:</title>\n    </head>\n    <body>\n        <h2>PythonClass - Example</h2>\n        <p style=\"text-align: center; font-style: oblique;\">\n            Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text\n        </p>\n        <hr />\n        <ul id=\"TheList\" style=\"line-height:200%\">\n            <li>\n                The first item in a list\n            </li>\n            <li style=\"color: red\">\n                This is the second item\n            </li>\n            <li>\n                And this is a \n                <a href=\"http://google.com\">link</a>\n                to google\n            </li>\n        </ul>\n    </body>\n</html>"


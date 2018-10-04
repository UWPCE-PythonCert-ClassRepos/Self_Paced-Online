
def test_render_element():
    e = Element("this is some text")
    e.append("And this is some more text")

    file_contents = render_result(e).strip()
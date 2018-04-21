from html_render import Element


def test_type_Element():
    test_element = Element()
    assert isinstance(test_element, Element) is True

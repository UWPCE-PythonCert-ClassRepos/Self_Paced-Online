import pytest
import html_render as h

def test_element():
    test_element = h.Element()
    test_element.append("This is content.")
    test_element.append("This is more content.")
    assert test_element.content[0] == "This is content."
    assert test_element.content[1] == "This is more content."


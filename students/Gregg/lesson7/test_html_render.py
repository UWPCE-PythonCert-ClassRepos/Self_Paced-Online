import html_render as hr
import pytest

def test_element_init():
    element = hr.Element()
    assert(element.content == [])
    test_string = "test string"
    element = hr.Element(test_string)
    assert(element.content == [test_string])
    fail_items = [(), [], {}, set(), 3, False]
    for item in fail_items:
        with pytest.raises(TypeError):
            element = hr.Element(item)


def test_element_append():
    init_string = "init string"
    element = hr.Element()
    test_strings = ["test1", 'test2', 'test3']
    for idx, test_string in enumerate(test_strings):
        element.append(test_string)
        assert(element.content == test_strings[:idx+1])
    fail_items = [(), [], {}, set(), None, 3]
    for item in fail_items:
        with pytest.raises(TypeError):
            element.append(item)


def test_element_render():
    test_string = "test string"
    element = hr.Element(test_string)
    element.append(test_string)
    goal_string = "<html>\n    {0}{0}\n</html>".format(test_string)
    out_file = 'test.txt'
    element.render(out_file)
    with open(out_file) as test_out:
        assert goal_string in test_out.read()

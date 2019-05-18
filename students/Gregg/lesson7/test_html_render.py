import html_render as hr


def test_element_init():
    element = hr.Element()
    assert(elemet.string_list == [])
    test_string = "test string"
    element = hr.Element(test_string)
    assert(elemet.string_list == [test_string])
    fail_items = [(), [], {}, set(), None, 3, False]
    for item in fail_items:
        with pytest.raises(TypeError):
            element = hr.Element(item)


def test_element_append():
    init_string = "init string"
    element = hr.Element()
    test_strings = ["test1", 'test2', 'test3']
    for idx, string in enumerate(test_strings):
        element.append(test_string)
        assert(elemet.string_list == test_strings[:i+1])
    fail_items = [(), [], {}, set(), None, 3]
    for item in fail_items:
        with pytest.raises(TypeError):
            element.append(item)


def test_element_render():
    test_string = "test string"
    element = hr.Element(test_string)
    element.append(test_string)
    goal_string = r"<html>\\{}{}}\\n<\html>".formt(test_string)
    with open('test.txt') as test_out:
        element.render(test_out)
        assert test_out

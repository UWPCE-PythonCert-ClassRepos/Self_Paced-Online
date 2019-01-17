# open a terminal window
# cd lesson7
# pytest test_html_unit_tests.py

import pytest
import html_render as hr
import py
import hashlib
import os

tmp_directory = "{}\\".format(os.getcwd())


"""
assert that render page functions correctly
"""

def test_0():
    page_test = hr.Element()
    page_test.append("Lorem ipsum dolor sit amet")
    hr.render_page(page_test, "test_0_render_class.htm")
    test_file = f"{tmp_directory}test_0_render_class.htm"
    hash_object_open = hashlib.md5()
    with open(test_file, 'rb') as afile:
        buf = afile.read()
        hash_object_open.update(buf)
    assert hash_object_open.hexdigest() == "b6d4bc719c12230e96a0d3e63ad30da7"

"""
assert that Html class builds correctly against a hash of a known good file
"""

def test_1():
    page_test = hr.Html()
    hr.render_page(page_test, "test_1_html_class.htm")
    test_file = f"{tmp_directory}test_1_html_class.htm"
    hash_object_open = hashlib.md5()
    with open(test_file, 'rb') as afile:
        buf = afile.read()
        hash_object_open.update(buf)
    assert hash_object_open.hexdigest() == "94a82dd9d4d963d9be87a510eef281f6"


"""
assert that Head class (including Title and Meta tags) builds correctly against a hash of a known good file
"""

def test_2():
    page_test = hr.Html()
    head = hr.Head()
    head.append(hr.Meta(charset="UTF-8"))
    head.append(hr.Title("Lorem ipsum dolor sit amet"))
    page_test.append(head)
    hr.render_page(page_test, "test_2_head_class.htm")
    test_file = f"{tmp_directory}test_2_head_class.htm"
    hash_object_open = hashlib.md5()
    with open(test_file, 'rb') as afile:
        buf = afile.read()
        hash_object_open.update(buf)
    assert hash_object_open.hexdigest() == "b362162f7599ff8217d0b5e8e5598849"


"""
assert that Body class builds correctly against a hash of a known good file
"""

def test_3():
    page_test = hr.Html()
    body = hr.Body()
    page_test.append(body)
    hr.render_page(page_test, "test_3_body_class.htm")
    test_file = f"{tmp_directory}test_3_body_class.htm"
    hash_object_open = hashlib.md5()
    with open(test_file, 'rb') as afile:
        buf = afile.read()
        hash_object_open.update(buf)
    assert hash_object_open.hexdigest() == "27895e07b6faa150ae55ad2043947abe"


"""
assert that P (paragraph) class builds correctly against a hash of a known good file
"""

def test_4():
    page_test = hr.Html()
    body = hr.Body()
    body.append(hr.P("Lorem ipsum dolor sit amet", style="text-align: center; font-style: oblique;"))
    page_test.append(body)
    hr.render_page(page_test, "test_4_p_class.htm")
    test_file = f"{tmp_directory}test_4_p_class.htm"
    hash_object_open = hashlib.md5()
    with open(test_file, 'rb') as afile:
        buf = afile.read()
        hash_object_open.update(buf)
    assert hash_object_open.hexdigest() == "6aed2d9ebf983a50a4a444607b0bca93"


"""
assert that Hr (horizontal rule) class builds correctly against a hash of a known good file
"""

def test_5():
    page_test = hr.Html()
    body = hr.Body()
    body.append(hr.Hr())
    page_test.append(body)
    hr.render_page(page_test, "test_5_hr_class.htm")
    test_file = f"{tmp_directory}test_5_hr_class.htm"
    hash_object_open = hashlib.md5()
    with open(test_file, 'rb') as afile:
        buf = afile.read()
        hash_object_open.update(buf)
    assert hash_object_open.hexdigest() == "e19ef5bfaf2983b57fc6cbeeb6e55341"


"""
assert that A (anchor tag) class builds correctly against a hash of a known good file
"""

def test_6():
    page_test = hr.Html()
    body = hr.Body()
    body.append(hr.A("http://google.com", "google"))
    page_test.append(body)
    hr.render_page(page_test, "test_6_a_class.htm")
    test_file = f"{tmp_directory}test_6_a_class.htm"
    hash_object_open = hashlib.md5()
    with open(test_file, 'rb') as afile:
        buf = afile.read()
        hash_object_open.update(buf)
    assert hash_object_open.hexdigest() == "d174a8ea530d2ccfb72865019ea63646"


"""
assert that UI and LI classes build correctly against a hash of a known good file
"""

def test_7():
    page_test = hr.Html()
    body = hr.Body()
    list = hr.Ul(id="TheList", style="line-height:200%")
    list.append(hr.Li("The first item in a list"))
    list.append(hr.Li("This is the second item", style="color: red"))
    item = hr.Li()
    body.append(list)
    page_test.append(body)
    hr.render_page(page_test, "test_7_UILI_class.htm")
    test_file = f"{tmp_directory}test_7_UILI_class.htm"
    hash_object_open = hashlib.md5()
    with open(test_file, 'rb') as afile:
        buf = afile.read()
        hash_object_open.update(buf)
    assert hash_object_open.hexdigest() == "0f69f655f2b48ba2739fbdcab16cb612"

#test class SelfClosingTag(Element):
#class Singleton(Element):






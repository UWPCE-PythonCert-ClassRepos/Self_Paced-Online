"""
    Author is Antonio V. Alvillar
    Self-Paced-Online Python 210 UWPCE
    January 16th 2019
"""

'''
This is a testing class that will be used when running pytest and test
for the objects to be created from either the subclass calls or direct
element initializers. There are several redundencies checked against as
the classes were being developed. Unfortunately I was unsure if it would be
possible to use pytest and assert statements for the render functionality.
'''

import html_render as hr

#Test an empty Element object
def test_empty_element():
    empty = hr.Element()
    assert empty.tag == '', ('empty: Tag Failure')
    assert empty.indentation == 4, ('empty: Indentation Failure')
    assert empty.attrs == {}, ('empty: Attrs Failure')
    assert empty.contents == [], ('empty: Contents Failure')

#Test an Element object with an initial value and appending
def test_initial_element():
    initial = hr.Element('initial string')
    assert initial.contents == ['initial string'], ('initial: Content Failure')
    initial.append('append')
    assert initial.contents == ['initial string', 'append'], ('append: Content Failure')

#Test an initial Element object with a style attribute
def test_attrs_element():
    attrs_initial = hr.Element('new string', style="text-align: center")
    assert attrs_initial.attrs == {'style': 'text-align: center'}, ('Style Dict: Attrs Failure')

#Test the Tag sub-classes of html, body, p, and head
def test_tags_element():
    html_element = hr.Html('html content')
    assert html_element.tag == 'html', ('HTML tag Failure')
    assert html_element.indentation == 4, ('Html: Indentation Failure')
    assert html_element.contents == ['html content'], ('Html: Contents Failure')
    body_element = hr.Body()
    assert body_element.tag == 'body', ('Body tag Failure')
    assert body_element.indentation == 4, ('Body: Indentation Failure')
    body_element.append('body append')
    assert body_element.contents == ['body append'], ('Body: Contents Failure')
    p_element = hr.P('initial', style="text-align: right")
    assert p_element.tag == 'p', ('P tag Failure')
    assert p_element.indentation == 4, ('P: Indentation Failure')
    p_element.append('appended')
    assert p_element.contents == ['initial', 'appended'], ('P initial and append: Contents Failure')
    assert p_element.attrs == {'style': 'text-align: right'}, ('P Dict: Attrs Failure')
    head_element = hr.Head('head content')
    assert head_element.tag == 'head', ('Head tag Failure')
    assert head_element.indentation == 4, ('Head: Indentation Failure')
    assert head_element.contents == ['head content'], ('Head: Contents Failure')

#Test onelinetag, title, and selfclosingtag classes
def test_subclasses():
    onelinetag = hr.OneLineTag()
    assert onelinetag.tag == '', ('onelinetag: Tag Failure')
    title_tag = hr.Title('Title Of')
    assert title_tag.tag == 'title', ('Title: Tag Failure')
    assert title_tag.contents == ['Title Of'], ('Title: Content Failure')
    self_closing = hr.SelfClosingTag('SCT')
    assert self_closing.tag == '', ('SelfClosingTag: Tag Failure')
    assert self_closing.contents == ['SCT'], ('SelfClosingTag: Content Failure')

#Testing the tags that subclass from the self closing tag class
def test_self_closing_tags():
    hr_tag = hr.Hr()
    assert hr_tag.tag == 'hr', ('Hr: tag failure')
    br_tag = hr.Br('BR Value')
    assert br_tag.contents == ['BR Value'], ('Br: contents failure')
    assert br_tag.tag == 'br', ('Br: tag failure')
    meta_tag = hr.Meta()
    assert meta_tag.tag == 'meta', ('Meta: tag failure')

#Test the unordered list and list sub classes/tags.
def test_list_tags():
    ul_tag = hr.Ul(id="myUnorderedList", style="line-height:250%")
    assert ul_tag.tag == 'ul', ('Ul: tag failure')
    assert ul_tag.attrs == {'id': 'myUnorderedList', 'style': 'line-height:250%'}, ('Ul: Attrs failure')
    li_tag = hr.Li(id="myList", style="line-height:25%")
    assert li_tag.tag == 'li', ('Ul: tag failure')
    assert li_tag.attrs == {'id': 'myList', 'style': 'line-height:25%'}, ('Li: Attrs failure')

#Test the header and level as well as link attributes that had their own initializers.
def test_header_links():
    h_tag = hr.H(3, "Testing H = 3")
    assert h_tag.tag == 'h3', ('H: tag failure')
    assert h_tag.contents == ['Testing H = 3'], ('H: content failure')
    link_tag = hr.A("http://google.com", "link")
    assert link_tag.tag == 'a', ('A: tag failure')
    assert link_tag.contents == ['link'], ('A link: content failure')
    assert link_tag.attrs == {'href': 'http://google.com'}, ('attrs: link failure')

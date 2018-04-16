#!/usr/bin/env python


import html_render as hr


def test_element():
    test1 = hr.Element('intro', color = 'blue')
    test1.append('test text')
    assert 'test text' and 'intro' in test1.content


def test_onelinetag():
    test2 = hr.OneLineTag('intro2')
    test2.append('test text2')
    assert 'test text2' and 'intro2' in test2.content

def test_selfclosingtag():
    test3 = hr.SelfClosingTag('intro3')
    test3.append('test text3')
    assert 'test text3' and 'intro3' in test3.content


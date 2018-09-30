# Description: html Tester
# Author: Andy Kwok
# Last Updated: 9/7/2018
# ChangeLog: Initialization

#!/usr/bin/env python3

import pytest
import html_render
from io import StringIO

def test_Element():
    eval = html_render.Element()
    eval.append('TESTING')
    f = StringIO()
    eval.render(f)
    actual = f.getvalue()
    expected = '<html>\n    TESTING\n</html>\n' 
    assert actual == expected
    
def test_Body():
    eval = html_render.Body()
    eval.append('TESTING')
    f = StringIO()
    eval.render(f)
    actual = f.getvalue()
    expected = '<body>\n    TESTING\n</body>\n'
    assert actual == expected
    
def test_Head():
    eval = html_render.Head()
    eval.append('TESTING')
    top_eval = html_render.Html()
    top_eval.append(eval)
    f = StringIO()
    top_eval.render(f)
    actual = f.getvalue()
    expected = '<!DOCTYPE html>\n<html>\n<head>\n    TESTING\n</head>\n</html>\n'
    assert actual == expected
    
def test_P():
    eval = html_render.P('TESTING', style='TESTING2')
    f = StringIO()    
    eval.render(f)
    actual = f.getvalue()
    expected = '<p style="TESTING2">\n    TESTING\n</p>\n'
    assert actual == expected
    
def test_Title():
    eval = html_render.Title('TESTING')
    f = StringIO()    
    eval.render(f)
    actual = f.getvalue()
    expected = '<title>TESTING</title>\n'
    assert actual == expected

def test_Hr():    
    eval = html_render.Hr()
    f = StringIO()    
    eval.render(f)
    actual = f.getvalue()
    expected = '<hr />\n'
    assert actual == expected    

def test_A():
    eval = html_render.A('TESTING', 'TESTING2')
    f = StringIO()    
    eval.render(f)
    actual = f.getvalue()
    expected = '<a href="TESTING">\n    TESTING2\n</a>\n'
    assert actual == expected       
    
def test_H():
    eval = html_render.H(2, 'TESTING')
    f = StringIO()    
    eval.render(f)
    actual = f.getvalue()
    expected = '<h2>TESTING</h2>\n'
    assert actual == expected      

def test_Meta():
    eval = html_render.Meta(charset="TESTING")
    f = StringIO()    
    eval.render(f)
    actual = f.getvalue()
    expected = '<meta charset="TESTING" />\n'
    assert actual == expected   

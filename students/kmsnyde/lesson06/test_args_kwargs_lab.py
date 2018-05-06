# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 10:47:25 2018

@author: Karl M. Snyder
"""

"""Test driven development for args / kwargs lab 2"""

from args_kwargs_lab import colors

colors1 = ('red', 'blue', 'yellow', 'chartreuse')
colors2 = ('gray', 'light pink')
dict1 = {'fore_color': "cool blue", 'visited_color': 'cast iron'}
dict2 = {'back_color': 'creme', 'link_color': 'purple'}

#def test_1():
#    assert colors(*colors1) == (colors1, {})
#
#def test_2():
#    assert colors(*colors1[:2], **dict1) == ('red', 'blue', dict1.values())
#    
#def test_3():
#    assert colors(*colors2, **dict2) == ('gray', 'light pink', 'creme', 'purple')
    
def test_1():
    assert colors('red', 'blue', 'yellow', 'chartreuse') == \
    (('red', 'blue', 'yellow', 'chartreuse'), {})

def test_2():
    assert colors(link_color='red', back_color='blue') == \
    ((), {'link_color':'red', 'back_color':'blue'})
    
def test_3():
    assert colors('purple', link_color='red', back_color='blue') == \
    (('purple',), {'link_color':'red', 'back_color':'blue'})
    
regular = ('red', 'blue')
links = {'link_color': 'chartreuse'}

def test_4():
    assert colors(*regular, **links) == (('red', 'blue',), {'link_color': 'chartreuse'})
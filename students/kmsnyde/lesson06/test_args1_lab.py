# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 10:25:57 2018

@author: Karl M. Snyder
"""

"""Test driven development for args / kwargs lab"""

from args1_lab import colors

def test_1():
    assert colors('red', 'blue', 'yellow', 'chartreuse') == \
    ('red', 'blue', 'yellow', 'chartreuse')

def test_2():
    assert colors(link_color='red', back_color='blue') == \
    ('calico', 'blue', 'red', 'ruby')
    
def test_3():
    assert colors('purple', link_color='red', back_color='blue') == \
    ('purple', 'blue', 'red', 'ruby')
    
regular = ('red', 'blue')
links = {'link_color': 'chartreuse'}

def test_4():
    assert colors(*regular, **links) == ('red', 'blue', 'chartreuse', 'ruby')
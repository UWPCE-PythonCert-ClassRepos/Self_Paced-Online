# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:02:49 2018

@author: Laura.Fiorentino
"""


import html_render

class Element():
    def test_append(self):
        test1 = html_render.Element('test1')
        self.append_element(test1, 'test2')
        assert test2 == ['test1' 'test2']

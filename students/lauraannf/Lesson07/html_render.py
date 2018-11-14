# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:01:24 2018

@author: Laura.Fiorentino
"""


class Element():
    tag = 'html'
    indentation = '     '

    def __init__(self, content=None):
        if content is None:
            self.content = []
        else:
            self.content = [content]

    def append_element(self, content):
        self.content.append_element(content)

    def render_element(self, file_out, cur_ind=''):
        file_out.write('{}<{}>\n'.format(cur_ind, self.tag))
        for item in self.content:
            file_out.write(self.content)
        file_out.write('{}/<{}>'.format(cur_ind, self.tag))

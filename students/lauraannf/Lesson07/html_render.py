# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:01:24 2018

@author: Laura.Fiorentino
"""


class Element():
    def __init__(self, tag='html', indentation='     ', content=None):
        self.tag = tag
        self.indentation = indentation
        if content is None:
            self.content = []
        else:
            self.content = [content]

    def append(self, new_content):
        self.content.append(new_content)

    def render(self, file_out, cur_ind=''):
        file_out.write('{}<{}>\n'.format(cur_ind, self.tag))
        for item in self.content:
            file_out.write(item)
        file_out.write('\n{}</{}>'.format(cur_ind, self.tag))

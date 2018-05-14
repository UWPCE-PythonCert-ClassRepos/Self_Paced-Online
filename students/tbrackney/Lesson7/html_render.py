#!/usr/bin/env python3
"""
File Name: html_render.py
Author: Travis Brackney
Class: Python 201 - Self paced online
Date Created 5/12/2018
Python Version: 3.6.4
"""

''' Class for rendering html page'''


class Element():
    tag = None
    i_string = '    '
    indent = 0

    def __init__(self, content=None):
        if content is None:
            self.content = []
        else:
            self.content = [content]

    def append(self, new_content):
        if (self.content):
            self.content.append(new_content)
        else:
            self.content = [new_content]

    def render(self, file_out, curr_ind=None):
        file_out.write(f'{i_string * indent}<{self.tag}>\n')
        file_out.write(self.i_string * (indent + 1))
        for c in self.content:
            if issubclass(type(c), Element):
                c.render(file_out, (indent + 1))
            elif (c[-1:] is '.'):
                file_out.write(c + ' ')
            else:
                file_out.write(c + '. ')
        file_out.write('\n')
        file_out.write(f'</{self.tag}>\n')


class Html(Element):
    tag = 'html'


class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'

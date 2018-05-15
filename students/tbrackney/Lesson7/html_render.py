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

    def __init__(self, *args, **kwargs):
        self.content = []
        if len(args) is not 0:
            for arg in args:
                self.content.append(arg)
        self.keywords = kwargs

    def append(self, *args):
        for content in args:
            self.content.append(content)

    def render(self, file_out, curr_ind=0):
        file_out.write(f'{self.i_string * curr_ind}')
        if len(self.keywords) is 0:
            file_out.write(f'<{self.tag}>\n')
        else:
            file_out.write(f'<{self.tag} ')
            for key, val in self.keywords.items():
                file_out.write(f'{key}="{val}"')
            file_out.write('>\n')
        file_out.write(self.i_string * (curr_ind + 1))
        for c in self.content:
            if issubclass(type(c), Element):
                c.render(file_out, (curr_ind + 1))
            elif (c[-1:] is '.'):
                file_out.write(c + ' ')
            else:
                file_out.write(c + '. ')
        file_out.write('\n')
        file_out.write(f'{curr_ind * self.i_string}</{self.tag}>\n')


class Html(Element):
    tag = 'html'


class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'


class Head(Element):
    tag = 'head'


class OneLineTag(Element):

    def __init__(self, content=None):
        self.content = content

    def render(self, file_out, curr_ind=0):
        file_out.write(f'{self.i_string * curr_ind}<{self.tag}>{self.content}</{self.tag}>\n')


class Title(OneLineTag):
    tag = 'title'

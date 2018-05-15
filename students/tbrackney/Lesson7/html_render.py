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

    def open_tag(self, indent=0, new_lines=True):
        spaces = f'{self.i_string * indent}'
        keywords = ''
        tag = f'<{self.tag}'
        if len(self.keywords) > 0:
            for key, val in self.keywords.items():
                keywords += f' {key}="{val}"'
        close = '>'
        if new_lines:
            close += '\n'
        return ''.join([spaces, tag, keywords, close])

    def close_tag(self, indent=0, new_lines=True):
        if new_lines:
            return ''.join(['\n', f'{indent * self.i_string}</{self.tag}>\n'])
        else:
            return f'</{self.tag}>\n'

    def render(self, file_out, curr_ind=0):
        file_out.write(self.open_tag(curr_ind))
        file_out.write(self.i_string * (curr_ind + 1))
        for c in self.content:
            if issubclass(type(c), Element):
                c.render(file_out, (curr_ind + 1))
            elif (c[-1:] is '.'):
                file_out.write(c + ' ')
            else:
                file_out.write(c + '. ')
        file_out.write(self.close_tag(curr_ind))


class Html(Element):
    tag = 'html'


class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'


class Head(Element):
    tag = 'head'


class OneLineTag(Element):
    def __init__(self, *args, **kwargs):
        self.content = []
        if len(args) is not 0:
            for arg in args:
                self.content.append(arg)
        self.keywords = kwargs

    def render(self, file_out, curr_ind=0):
        file_out.write(self.open_tag(curr_ind, False))
        for c in self.content:
            file_out.write(f'{c}')
        file_out.write(self.close_tag(curr_ind, False))


class Title(OneLineTag):
    tag = 'title'


class SelfClosingTag(Element):
    def __init__(self, content=None):
        if content:
            raise TypeError('SelfClosingTag takes no content')

    def render(self, file_out, curr_ind=0):
        file_out.write(f'{self.i_string * curr_ind}<{self.tag} />\n')


class Hr(SelfClosingTag):
    tag = 'hr'


class Br(SelfClosingTag):
    tag = 'br'

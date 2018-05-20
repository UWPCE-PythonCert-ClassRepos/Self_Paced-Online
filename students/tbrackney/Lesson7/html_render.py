#!/usr/bin/env python3
"""
File Name: html_render.py
Author: Travis Brackney
Class: Python 201 - Self paced online
Date Created 5/12/2018
Python Version: 3.6.4
"""

''' '''


class Element():
    """Class for rendering html page"""
    tag = None
    i_string = '    '
    indent = 0
    new_lines = True
    keywords = ''

    def __init__(self, *args, **kwargs):
        self.content = []
        if len(args) is not 0:
            for arg in args:
                self.content.append(arg)
        self.keywords = kwargs

    def append(self, *args):
        for arg in args:
            self.content.append(arg)

    def open_tag(self, indent=0):
        """writes the opening of any xml tag"""
        spaces = f'{self.i_string * indent}'
        tag = f'<{self.tag}'
        keywords = ''
        if len(self.keywords) > 0:
            for key, val in self.keywords.items():
                keywords += f' {key}="{val}"'
        close = '>'
        if self.new_lines:
            close += '\n'
        return ''.join(['\n', spaces, tag, keywords, close])

    def close_tag(self, indent=0):
        """writes the closing xml tag"""
        if self.new_lines:
            return ''.join(['\n', f'{indent * self.i_string}</{self.tag}>\n'])
        else:
            return f'</{self.tag}>\n'

    def render(self, file_out, curr_ind=0):
        """Writes the output of each element to the output stream"""
        file_out.write(self.open_tag(curr_ind))
        file_out.write(self.i_string * (curr_ind + 1))
        for c in self.content:
            if issubclass(type(c), Element):
                c.render(file_out, (curr_ind + 1))
            else:
                file_out.write(c + ' ')
        file_out.write(self.close_tag(curr_ind))


class Html(Element):
    tag = 'html'

    def render(self, file_out):
        file_out.write('<!DOCTYPE html>\n')
        Element.render(self, file_out)


class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'


class Head(Element):
    tag = 'head'


class OneLineTag(Element):
    def render(self, file_out, curr_ind=0):
        self.new_lines = False
        file_out.write(self.open_tag(curr_ind))
        for c in self.content:
            file_out.write(f'{c}')
        file_out.write(self.close_tag(curr_ind))


class Title(OneLineTag):
    new_lines = False
    tag = 'title'


class SelfClosingTag(Element):
    def __init__(self, content=None, **kwargs):
        if content:
            raise TypeError('SelfClosingTag takes no content')
        self.keywords = kwargs

    def render(self, file_out, curr_ind=0):
        file_out.write(f'{self.i_string * curr_ind}')
        file_out.write(f'<{self.tag} ')
        if len(self.keywords) > 0:
            for key, val in self.keywords.items():
                file_out.write(f'{key}="{val}"')
        file_out.write('/>\n')


class Hr(SelfClosingTag):
    tag = 'hr'


class Br(SelfClosingTag):
    tag = 'br'


class A(OneLineTag):
    tag = 'a'

    def __init__(self, *args, **kwargs):
        kwargs['href'] = args[0]
        Element.__init__(self, *args[1:], **kwargs)


class Ul(Element):
    tag = 'ul'


class Li(Element):
    tag = 'li'


class H(OneLineTag):
    def __init__(self, *args, **kwargs):
            self.tag = f'h{int(args[0])}'
            Element.__init__(self, *args[1:], **kwargs)


class Meta(SelfClosingTag):
    tag = 'meta'

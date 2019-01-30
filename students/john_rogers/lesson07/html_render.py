#!/usr/bin/env python3
"""
html_render.py: using classes to render HTML
Author: JohnR
Version: .2
Last updated: 1/29/2019
Notes:
"""


class Element(object):
    """
    create base class for adding html tags and text strings to a file
    """
    tag = 'html'
    indent = ' ' * 4

    def __init__(self, content=None):
        self.content = [content] if content else []

    def append(self, data):
        self.content.append(data)

    def render(self, file_out, cur_ind=''):
        file_out.write(cur_ind + f'<{self.tag}>\n')

        for item in self.content:
            try:
                item.render(file_out)
            except AttributeError:
                file_out.write(f'{item}\n')

        file_out.write(cur_ind + f'</{self.tag}>\n')


class Html(Element):
    tag = 'html'


class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'P'


class Head(Element):
    pass


class Hr(Element):
    pass


class Li(Element):
    pass


class Ul(Element):
    pass


#!/usr/bin/env python3
"""
html_render.py: using classes to render HTML
Author: JohnR
Version: .1
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
                file_out.write(cur_ind + self.indent + item + '\n')
            except Exception as e:
                print(e)

        file_out.write(cur_ind + f'</{self.tag}>\n')


class Html(Element):
    pass


class Body(Element):
    pass


class Head(Element):
    pass


class Hr(Element):
    pass


class Li(Element):
    pass


class Ul(Element):
    pass


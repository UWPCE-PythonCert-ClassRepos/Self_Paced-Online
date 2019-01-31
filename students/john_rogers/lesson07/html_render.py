#!/usr/bin/env python3
"""
html_render.py: using classes to render HTML
Author: JohnR
Version: .5
Last updated: 1/29/2019
Notes:
"""


class Element(object):
    """
    create base class for adding html tags and text strings to a file
    """
    tag = ''
    indent = ' ' * 4

    def __init__(self, content=None, **kwargs):
        self.content = [content] if content else []
        self.kwargs = kwargs

    def append(self, data):
        self.content.append(data)

    def render(self, file_out, cur_ind=''):
        """
        Render content with html tags in place
        :param file_out: file to write to
        :param cur_ind: current indentation level
        :return: none
        """
        file_out.write(cur_ind + f'<{self.tag}')

        for key, value in self.kwargs.items():
            file_out.write(f' {key}="{value}"')
        file_out.write('>\n')

        for item in self.content:
            try:
                item.render(file_out)
            except AttributeError:
                file_out.write(f'{item}\n')

        file_out.write(cur_ind + f'</{self.tag}>\n')


class OneLineTag(Element):

    def render(self, file_out, cur_ind=''):
        """
        Render a string with tags on a single line
        :param file_out: file to write to
        :param cur_ind: indentation level
        :return: none
        """
        file_out.write(cur_ind + f'<{self.tag}')

        for key, value in self.kwargs.items():
            file_out.write(f'{key}="{value}"')
        file_out.write('>')

        for item in self.content:
            try:
                item.render(file_out)
            except AttributeError:
                file_out.write(f'{item}')

        file_out.write(cur_ind + f'</{self.tag}>')


class SelfClosingTag(Element):
    """
    override the render method to render just the one tag and attributes
    """

    # cut and paste from above; customize this and look for ways to
    # eliminate repeated code; look at @staticmethod ?
    def render(self, file_out, cur_ind=''):
        file_out.write(cur_ind + f'<{self.tag}')

        for key, value in self.kwargs.items():
            file_out.write(f'{key}="{value}"')
        file_out.write('>')

        for item in self.content:
            try:
                item.render(file_out)
            except AttributeError:
                file_out.write(f'{item}')

        file_out.write(cur_ind + f'</{self.tag}>')


class Title(OneLineTag):
    tag = 'title'


class Html(Element):
    tag = 'html'


class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'P'


class Head(Element):
    tag = 'head'


class Hr(OneLineTag):
    tag = 'hr'


class Br(OneLineTag):
    tag = 'br'

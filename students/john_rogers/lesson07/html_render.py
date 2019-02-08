#!/usr/bin/env python3
"""
html_render.py: using classes to render HTML
Author: JohnR
Version: 1.0
Last updated: 2/04/2019
Notes:
"""


class Element(object):
    """
    create base class for adding html tags and text strings to a file
    """
    tag = ''
    indent = ' '

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
        Element.add_values(self, file_out)
        file_out.write('>\n')
        Element.add_items(self, file_out)
        file_out.write(cur_ind + f'</{self.tag}>\n')

    def add_items(self, file_out):
        """
        Add in items with a new line
        :param file_out: file to write to
        :return: None
        """
        for item in self.content:
            try:
                item.render(file_out)
            except AttributeError:
                file_out.write(f'{item}\n')

    def add_items_no_line(self, file_out):
        """
        Add in items without a new line
        :param file_out: file to write to
        :return: None
        """
        for item in self.content:
            try:
                item.render(file_out)
            except AttributeError:
                file_out.write(f'{item}')

    def add_values(self, file_out):
        """
        use a dict to capture kwargs
        :param file_out: file to write to
        :return: None
        """
        for key, value in self.kwargs.items():
            file_out.write(f' {key}="{value}"')


class Ul(Element):
    tag = 'ul'


class Li(Element):
    tag = 'li'


class A(Element):
    """
    Create a link to a given website
    """
    tag = 'a'

    def __init__(self, content, link):
        super().__init__(link, href=content)


class OneLineTag(Element):

    def render(self, file_out, cur_ind=''):
        """
        Render a string with tags on a single line
        :param file_out: file to write to
        :param cur_ind: indentation level
        :return: none
        """
        file_out.write(cur_ind + f'<{self.tag}')
        Element.add_values(self, file_out)
        file_out.write('>')
        Element.add_items_no_line(self, file_out)
        file_out.write(cur_ind + f'</{self.tag}>\n')


class Ul(Element):
    """ unordered list """
    tag = 'ul'


class Li(Element):
    """ element of a list """
    tag = 'li'


class H(OneLineTag):
    """  use a custom header size """
    def __init__(self, level, content=None, **kwargs):
        super().__init__(content=content, **kwargs)
        self.tag = f'h{level}'


class SelfClosingTag(Element):
    """ render just one tag and attributes """
    def __init__(self, content=None, **kwargs):
        if content:
            raise TypeError
        self.kwargs = kwargs

    def render(self, file_out, cur_ind='  '):
        file_out.write(cur_ind + f'<{self.tag}')
        Element.add_values(self, file_out)
        file_out.write('>\n')


class Meta(SelfClosingTag):
    tag = 'meta'


class Html(Element):
    """ create a DOCTYPE tag at top of page """
    tag = 'html'

    def render(self, file_out, cur_ind=''):
        file_out.write('<!DOCTYPE html>\n')
        Element.render(self, file_out, cur_ind='')


class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'P'


class Head(Element):
    tag = 'head'


class Title(OneLineTag):
    tag = 'title'


class Hr(SelfClosingTag):
    tag = 'hr'


class Br(SelfClosingTag):
    tag = 'br'

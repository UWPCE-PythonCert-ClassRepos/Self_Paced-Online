#!/usr/bin/env python

"""This module renders the HTML codes."""


class Element:
    """Base class."""

    tag = 'html'
    ind = '    '

    def __init__(self, content=None, **attrs):
        """Initialize the object with instance attributes."""
        if content:
            self.contents = [content]
        else:
            self.contents = []
        self.attrs = attrs

    def append(self, content):
        """Append the content."""
        self.contents.append(content)

    def render(self, file_out, cur_ind=''):
        """Render the element."""
        self.add_attrs(file_out, cur_ind)
        file_out.write('>\n')

        for content in self.contents:
            try:
                content.render(file_out, f'{cur_ind}{self.ind}')
            except AttributeError:
                file_out.write(f'{cur_ind}{self.ind}{str(content)}\n')
        file_out.write(f'{cur_ind}</{self.tag}>\n')

    def add_attrs(self, file_out, cur_ind):
        """Add attributes."""
        file_out.write(f'{cur_ind}<{self.tag}')
        for k, v in self.attrs.items():
            file_out.write(' {}="{}"'.format(k, v))


class Html(Element):
    tag = 'html'

    def render(self, file_out, cur_ind=''):
        file_out.write(f'{cur_ind}<!DOCTYPE html>\n')
        super().render(file_out, cur_ind)


class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'


class Head(Element):
    tag = 'head'


class OneLineTag(Element):
    def render(self, file_out, cur_ind=''):
        """Render the element on a single line."""
        self.add_attrs(file_out, cur_ind)
        file_out.write(f'>{str(self.contents[0])}</{self.tag}>\n')


class Title(OneLineTag):
    tag = 'title'


class SelfClosingTag(Element):
    def render(self, file_out, cur_ind=''):
        self.add_attrs(file_out, cur_ind)
        file_out.write(' />\n')


class Hr(SelfClosingTag):
    tag = 'hr'


class Br(SelfClosingTag):
    tag = 'br'


class A(OneLineTag):
    tag = 'a'

    def __init__(self, link, content):
        super().__init__(content, href=link)


class Ul(Element):
    tag = 'ul'


class Li(Element):
    tag = 'li'


class H(OneLineTag):
    def __init__(self, level, content):
        super().__init__(content)
        self.tag = f'h{level}'


class Meta(SelfClosingTag):
    tag = 'meta'

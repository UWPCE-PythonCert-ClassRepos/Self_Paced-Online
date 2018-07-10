#!/usr/bin/env python3

## Student:  Roy Tate (githubtater)


class Element:
    '''Takes content (string, a list, etc) and an HTML element, or tag, and renders the html code,
    with indentation, to a file to be displayed in a browser.'''
    tag = ''
    indent = '    '  # 4 spaces for indentation

    def __init__(self, content=None, **kwargs):
        if content:
            self.content = [content]
        else:
            self.content = []
        self.kwargs = kwargs

    def append(self, content):
            self.content.append(content)

    def render(self, file_out, cur_ind=''):
        file_out.write(cur_ind + '<{}'.format(self.tag))
        for key, value in self.kwargs.items():
            file_out.write(' {}="{}"'.format(key, value))
        file_out.write('>\n')
        for item in self.content:
            if isinstance(item, Element):
                item.render(file_out, cur_ind + self.indent)
            else:
                file_out.write(cur_ind + self.indent + item + '\n')
        file_out.write(cur_ind + '</{}>\n'.format(self.tag))


class Html(Element):
    tag='html'

    def render(self, file_out, cur_ind=''):
        '''Override Element.render'''
        file_out.write('<!DOCTYPE html>\n')
        Element.render(self, file_out, cur_ind='')


class Title(Element):
    tag = 'title'


class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'


class Head(Element):
    tag = 'head'


class OneLineTag(Element):

    def render(self, file_out, cur_ind=''):
        '''override Element.render to generate the correct tags for <br>, etc.'''
        file_out.write(cur_ind + '<{}'.format(self.tag))
        for key, value in self.kwargs.items():
            file_out.write(' {}="{}"'.format(key, value))
        file_out.write('>\n')
        for item in self.content:
            if isinstance(item, Element):
                item.render(file_out, cur_ind + self.indent)
            else:
                file_out.write(cur_ind + self.indent + item + '\n')
        file_out.write(cur_ind + '</{}>\n'.format(self.tag))


class A(OneLineTag):
    tag = 'a'
    def __init__(self, link, content):
        super().__init__(content, href=link)

class H(OneLineTag):
    def __init__(self, level, content, **kwargs):
        Element.__init__(self, content, **kwargs)
        self.level = level
        self.tag = 'h{}'.format(level)


class SelfClosingTag(Element):
    def __init__(self, content=None, **kwargs):
        if content:
            raise TypeError('Error: class SelfClosingTag does not take content')
        self.kwargs = kwargs

    def render(self, file_out, cur_ind=''):
        file_out.write(cur_ind + '<{}'.format(self.tag))
        for key, value in self.kwargs.items():
            file_out.write(' {}="{}"'.format(key, value))
        file_out.write(' />\n')


class Hr(SelfClosingTag):
    tag = 'hr'


class Br(SelfClosingTag):
    tag = 'br'

class Meta(SelfClosingTag):
    tag = 'meta'


class Ul(Element):
    tag = 'ul'


class Li(Element):
    tag = 'li'
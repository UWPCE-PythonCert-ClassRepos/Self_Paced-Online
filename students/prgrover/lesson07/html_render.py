#!/usr/bin/env python3

class Element:
    """
    Base class for rendering an HTML element
    """

    tag = 'html'
    indent = '    ' #4 space characters

    def __init__(self, content=None, **kwargs):
        self.attributes = kwargs
        self.content = []
        if content:
            self.append(content)


    def append(self, content):
        if hasattr(content, 'render'):
            self.content.append(content)
        else:
            self.content.append(TextWrapper(str(content)))


    #Per Step 4 - next four methods are an attempt to refactor common parts into separate methods
    def render(self, file_out, cur_ind=""):
        self.make_open_tag(file_out, cur_ind)
        for markup in self.content:
            markup.render(file_out, cur_ind + self.indent)
            file_out.write('\n')
        close_tag = '{}</{}>'.format(cur_ind, self.tag)
        file_out.write(close_tag)


    def make_open_tag(self, file_out, cur_ind="", one_line=False):
        open_tag = self.get_open_tag()
        if one_line == True:
            file_out.write(cur_ind + open_tag)            
        else:
            file_out.write(cur_ind + open_tag + '\n')


    def get_open_tag(self):
        open_tag = '<{}{}>'.format(self.tag, self.get_keywords())    
        return open_tag


    def get_keywords(self):
        keywords = ""
        for key, val in self.attributes.items():
            keywords += ' {}="{}"'.format(key, val)
        return keywords


class TextWrapper:

    def __init__(self, text):
        self.text = text

    def render(self, file_out, current_ind=""):
        file_out.write(current_ind)
        file_out.write(self.text)


class OneLineTag(Element):

    def render(self, file_out, cur_ind=""):
        self.make_open_tag(file_out, cur_ind, one_line=True)
        for markup in self.content:
            markup.render(file_out)
        close_tag = '</{}>'.format(self.tag)
        file_out.write(close_tag)


class SelfClosingTag(Element):

    def get_open_tag(self):
        open_tag = '<{}'.format(self.tag) + self.get_keywords() + ' />'
        return open_tag

    def render(self, file_out, cur_ind=""):
        self.make_open_tag(file_out, cur_ind, one_line=True)


class Html(Element):
    tag = 'html'

    def render(self, file_out, cur_ind=""):
        file_out.write(cur_ind + "<!DOCTYPE html>\n")
        Element.render(self, file_out, cur_ind=cur_ind)


class Body(Element):
    tag = 'body'

class P(Element):
    tag = 'p'

class Head(Element):
    tag = 'head'

class Title(OneLineTag):
    tag = 'title'

class Hr(SelfClosingTag):
    tag = 'hr'

class Br(SelfClosingTag):
    tag = 'br'

class A(OneLineTag):
    tag = 'a'

    def __init__(self, link=None, content=None, **kwargs):
        Element.__init__(self, content, href=link, **kwargs)


class Ul(Element):
    tag = 'ul'

class Li(Element):
    tag = 'li'

class H(OneLineTag):
    tag = 'h'

    def __init__(self, level, content=None, **kwargs):
        self.tag = 'h' + str(int(level))
        Element.__init__(self, content, **kwargs)

class Meta(SelfClosingTag):
    tag = 'meta'

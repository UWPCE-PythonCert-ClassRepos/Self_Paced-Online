#!/usr/bin/env python3


class Element:
    '''A class to render an HTML element'''

    tag_name = ''
    indents = 4

    def __init__(self, content=None):
        self.content = []
        if content:
            self.content.append(content)

    def append(self, content):
        '''Appends strings to content'''
        self.content.append(content)

    def render(self, file_out, cur_ind=""):
        next_ind = cur_ind + (" " * self.indents)
        if self.tag_name == 'html':
            file_out.write("{}<!DOCTYPE html>\n".format(cur_ind))
        file_out.write("{}<{}>\n".format(cur_ind, self.tag_name))
        for item in self.content:
            if isinstance(item, str):
                file_out.write('{}{}\n'.format(next_ind, item))
            else:
                item.render(file_out, next_ind)
        file_out.write("{}</{}>\n".format(cur_ind, self.tag_name))


class Html(Element):
    '''A class for an element with an HTML tag'''

    tag_name = 'html'

    def __init__(self, content=None):
        Element.__init__(self, content)
        self.content = []
        if content:
            self.content.append(content)


class Head(Element):
    '''A class for an element with a body tag'''

    tag_name = 'head'

    def __init__(self, content=None):
        Element.__init__(self, content)
        self.content = []
        if content:
            self.content.append(content)


class Body(Element):
    '''A class for an element with a body tag'''

    tag_name = 'body'

    def __init__(self, content=None):
        Element.__init__(self, content)
        self.content = []
        if content:
            self.content.append(content)


class P(Element):
    '''A class for an element with a body tag'''

    tag_name = 'p'

    def __init__(self, content=None):
        Element.__init__(self, content)
        self.content = []
        if content:
            self.content.append(content)


class OneLineTag(Element):
    '''A class for an element with a body tag'''

    tag_name = ''

    def __init__(self, content=None):
        Element.__init__(self, content)
        self.content = []
        if content:
            self.content.append(content)

    def render(self, file_out, cur_ind=""):
        file_out.write("{}<{}>".format(cur_ind, self.tag_name))
        for item in self.content:
            if isinstance(item, str):
                file_out.write('{}'.format(item))
            else:
                item.render(file_out)
        file_out.write("</{}>\n".format(self.tag_name))


class Title(OneLineTag):
    '''A class for an element with a body tag'''

    tag_name = 'title'

    def __init__(self, content=None):
        Element.__init__(self, content)
        self.content = []
        if content:
            self.content.append(content)

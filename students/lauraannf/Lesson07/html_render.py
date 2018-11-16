# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:01:24 2018

@author: Laura.Fiorentino
"""


class Element():
    tag = 'html'
    indentation = '     '

    def __init__(self, content=None, **kwargs):
        self.__dict__.update(kwargs)
        if content is None:
            self.content = []
        else:
            self.content = [content]

    def append(self, new_content):
        self.content.append(new_content)

    def render(self, file_out, cur_ind=''):
        file_out.write('{}<{}>\n'.format(cur_ind, self.tag))
        for item in self.content:
            # file_out.write(item)
            try:
                item.render(file_out)
            except AttributeError:
                file_out.write(item)
            file_out.write('\n')
        file_out.write('{}</{}>'.format(cur_ind, self.tag))


class Html(Element):
    tag = 'html'


class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'


class Head(Element):
    tag = 'head'


class OneLineTag(Element):
    def render(self, file_out, cur_ind=''):
        file_out.write('{}<{}>'.format(cur_ind, self.tag))
        file_out.write(self.content[0])
        file_out.write('{}</{}>'.format(cur_ind, self.tag))

    def append(self, content):
        raise NotImplementedError


class Title(OneLineTag):
    tag = 'title'

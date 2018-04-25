#!/usr/bin/env python3

# file: html_render.py

# define class 'Element':
class Element:

    tag = 'element'
    i_level = 0

    # define attributes:
    def __init__(self, content=None):
        self.content = [content] if content else []
    
    # define method append:
    def append(self, stuff):
        self.content.append(stuff)

    # define method render:
    # def render(self, io, cur_ind=''):
    def render(self, io, ind):
        io.write('<{}>\n'.format(self.tag))
        for i in self.content:
            # if isinstance(i, Element):
            if hasattr(i, 'render'):
                # i.render(io)
                i.render(io, ind)
            else:
                line = '{}{}\n'.format(ind, i)
                io.write(line)
        io.write('</{}>\n'.format(self.tag))
        

class Html(Element):
    # self.tag = 'html'
    tag = 'html'
    #def __init__(self, tagtype='html', i_level=1, content=None):
    #    self.tag = tagtype
    #    self.indent = i_level
    #    self.content = [content] if content else []


class Body(Element):
    # self.tag = 'body'
    tag = 'body'
    #def __init__(self, tagtype='body', i_level=2, content=None):
    #    self.tag = tagtype
    #    self.indent = i_level
    #    self.content = [content] if content else []


class P(Element):
    # self.tag = 'p'
    tag = 'p'
    #def __init__(self, tagtype='p', i_level=3, content=None):
    #    self.tag = tagtype
    #    self.indent = i_level
    #    self.content = [content] if content else []


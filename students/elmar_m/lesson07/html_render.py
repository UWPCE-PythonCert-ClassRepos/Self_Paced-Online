#!/usr/bin/env python3

# file: html_render.py

# define class 'Element':
class Element:

    # define attributes:
    tag = 'element'
    i_level = 0

    def __init__(self, content=None):
        self.content = [content] if content else []
    
    # define method append:
    def append(self, stuff):
        self.content.append(stuff)

    # define method render:
    def render(self, io, ind):
        # io.write('<{}>\n'.format(self.tag))
        if self.tag == 'html':
            io.write('<!DOCTYPE html>\n')
            io.write('<{}>\n'.format(self.tag))
        else:
            io.write('<{}>\n'.format(self.tag))
            
        for i in self.content:
            if hasattr(i, 'render'):
                i.render(io, ind)
            else:
                line = '{}{}\n'.format(ind, i)
                io.write(line)
        io.write('</{}>\n'.format(self.tag))
        

class Html(Element):
    tag = 'html'


class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'


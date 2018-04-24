#!/usr/bin/env python3

# file: html_render.py

# define class 'Element':
class Element:
    # define attributes:
    def __init__(self, tagname='element', i_level=0, content=None):
        self.tag = tagname
        self.indent = i_level
        self.content = [content] if content else []
    
    # define method append:
    def append(self, stuff):
        self.content.append(stuff)

    # define method render:
    def render(self, io, cur_ind=''):
        io.write('<{}>\n'.format(self.tag))
        for i in self.content:
            line = '{}{}\n'.format(cur_ind, i)
            io.write(line)
        io.write('</{}>\n'.format(self.tag))
        

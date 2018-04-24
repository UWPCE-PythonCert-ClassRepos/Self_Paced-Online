#!/usr/bin/env python3

# file: html_render.py

# define class 'Element':
class Element:
    # define attributes:
    def __init__(self, tagname='', indentation=0, content=[]):
        self.tagname = tagname
        self.indentation = indentation
    
    # define method append:
    def append(self, *args):
        # myoutput = []
        # pass
        # content = []
        for i in args:
            content.append(i)

    # define method render:
    def render(self, io, content):
        io.write(content) 

    
        

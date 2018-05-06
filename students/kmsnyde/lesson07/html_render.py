# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 18:24:32 2018

@author: Karl M. Snyder
"""

#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""

#adding "textwrapper" per guidance: Ahead of Time Option
class TextWrapper:
    """ A simple wrapper that creates a class with a render method
    for simple text"""
    def __init__(self, text):
        self.text = text
        
    def render(self, out_file, cur_ind=''):
        out_file.write(cur_ind + self.text)

# This is the framework for the base class
class Element(object):
    
    tag = 'html'
    indent = ' ' * 4 #indent at 4

    def __init__(self, content=None, **attrs):
        #set content as list if provided, else empty list
        self.content = []
        self.attrs = attrs
        if content:
            self.append(content)
        
    #Trying part 2 of guidance; tried "isinstacne but failed
    def append(self, new_content):
       if hasattr(new_content, 'render'):
           self.content.append(new_content)
       else:
           self.content.append(TextWrapper(str(new_content)))

    def render(self, out_file, cur_ind=''):
        out_file.write('{}<{}'.format(cur_ind, self.tag))
        
        for k,v in self.attrs.items():
            out_file.write(' {}={}'.format(k, v))
            
        out_file.write('>\n')
        
        try:
            for x in self.content:
                x.render(out_file, cur_ind + self.indent)
                out_file.write('\n')
        
            out_file.write('{}</{}>'.format(cur_ind, self.tag))
        except (AttributeError, TypeError):
            print("Content not allowed for SelfClosingTags.")

class Html(Element):
    tag = "html"
    
    def render(self, out_file, cur_ind=''):
        out_file.write('<!DOCTYPE hmtl>\n')
        Element.render(self, out_file, cur_ind='')
    
class Body(Element):
    tag = 'body'
        
class P(Element):
    tag = 'p'
    
class Head(Element):
    tag = 'head'

# overwrite render() to remove "\n" and enable one line
class OneLineTag(Element):
    def render(self, out_file, cur_ind=''):
        out_file.write('{}<{}>{}'.format(cur_ind, self.tag, self.indent))
        for x in self.content:
            x.render(out_file)
        out_file.write('{}</{}>'.format(self.indent, self.tag))
        
class Title(OneLineTag):
    tag = 'title'

class SelfClosingTag(Element):
    def __init__(self, **attrs):
        self.attrs = attrs
                
    def render(self, out_file, cur_ind=''):
        out_file.write('{}<{}'.format(cur_ind, self.tag))
        for k,v in self.attrs.items():
            out_file.write(' {}={}'.format(k, v))
        out_file.write(' />')
        
        
class Hr(SelfClosingTag):
    tag = 'hr'
    
class Br(SelfClosingTag):
    tag = 'br'

class A(Element):
    tag = 'a'
    def __init__(self, link, content):
        Element.__init__(self, content, href=link)
        
class Ul(Element):
    tag = 'ui'
    
class Li(Element):
    tag = 'li'
    
class H(OneLineTag):
    def __init__(self, content, level, **attrs):
        self.level = level
        self.tag = 'h{}'.format(level)
        OneLineTag.__init__(self, content, **attrs)
        
class Meta(SelfClosingTag):
    tag = 'meta'
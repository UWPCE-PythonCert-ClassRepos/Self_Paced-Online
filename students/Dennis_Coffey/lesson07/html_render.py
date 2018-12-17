# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 21:13:15 2018

@author: dennis
"""

"""HTML renderer for Lesson 07"""

class Element():
    tag = '' # Element type
    indent = 0 # Indent of tag
    inline = False # Defines whether content is to be displayed on same line
    empty = False  # Defines whether tag is an empty tag
    def __init__(self, content=None, **kwargs):
        self.content_list = []
        self.kwargs = kwargs
        if content:
            self.content_list.append(content)
        
    def append(self, content):
        self.content_list.append(content)
        
    def starttag(self, tag):
        if tag:
            tag = ' ' * self.indent + '<' + tag
            if self.kwargs:
                attribute = ''
                for k in self.kwargs:
                    attribute += ' ' + k + '=\"' + self.kwargs[k] + '\"'
                tag += attribute
            tag += '>'
        return tag
        
    def endtag(self, tag):
        if tag:
            tag = ' ' * self.indent + '</' + tag + '>'
        return tag
        
    def render(self, output_file, indent=0):
        # Render opening tag
        output_file.write(self.starttag(self.tag))
        if not self.inline and not self.empty:
            output_file.write('\n')
        
        # Render content
        if self.content_list:
            for item in self.content_list:
                if type(item) == str:
                    output_file.write(item)
                else:
                    item.render(output_file, indent + 4)
                if not self.inline:
                    output_file.write('\n')
                
        # Render closing tag
        if not self.empty:
            output_file.write(self.endtag(self.tag))
        
class Html(Element):
    tag = 'html'
    indent = 0
    
#    def render(self, output_file, indent=0):
#        output_file.write('<!DOCTYPE html>\n')
#        super().render(output_file, indent)        

    
class Body(Element):
    tag = 'body'
    indent = 0
    
class P(Element):
    tag = 'p'
    indent = 0
    
class Head(Element):
    tag = 'head'
    indent = 0
    
class Title(Element):
    tag = 'title'
    indent = 0
    inline = True
    
class SelfClosingTag(Element):
    
    def __init__(self, content=None, **kwargs):
        self.kwargs = kwargs
        if content:
            raise TypeError('Content is not allowed for Self Closing Tag elements')

    def render(self, output_file, indent=0):
        # Render opening tag
        output_file.write('<' + self.tag)
        
        # Render attribute
        if self.kwargs:
            attribute = ''
            for k in self.kwargs:
                attribute += ' ' + k + '=\"' + self.kwargs[k] + '\"'
            output_file.write(attribute)
                
        # Render closing tag
        output_file.write(' />')
    
class Hr(SelfClosingTag):
    tag = 'hr'
    indent = 0
    empty = True
    
class Br(SelfClosingTag):
    tag = 'br'
    indent = 0
    
class Meta(SelfClosingTag):
    tag = 'meta'
    indent = 0

class A(Element):
    tag = 'a'
    indent = 0
    inline = True
    def __init__(self, link, content, **kwargs):
        self.content_list = []
        self.kwargs = kwargs
        self.kwargs['href'] = link
        if content:
            self.content_list.append(content)

class H(Element):
    tag = 'h'
    indent = 0
    inline = True
    def __init__(self, level, content, **kwargs):
        self.content_list = []
        self.kwargs = kwargs
        self.tag = self.tag + str(level)
        if content:
            self.content_list.append(content)

class Ul(Element):
    tag = 'ul'
    indent = 0
    
class Li(Element):
    tag = 'li'
    indent = 0
    
    
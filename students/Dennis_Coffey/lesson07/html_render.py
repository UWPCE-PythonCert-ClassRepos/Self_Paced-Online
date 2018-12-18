# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 21:13:15 2018

@author: dennis
"""

"""HTML renderer for Lesson 07"""

# Base element class
class Element():
    tag = '' # Element type
    indent_size = ' '* 4 # Indent of tag
#    indent_size = ''* 4 # Use this cause no indent for Steps 1-8
    inline = False # Defines whether content is to be displayed on same line
    empty = False  # Defines whether tag is an empty tag
    def __init__(self, content=None, **kwargs):
        self.content_list = []
        self.kwargs = kwargs
        if content:
            self.content_list.append(content)
        
    # Append content
    def append(self, content):
        self.content_list.append(content)
        
    # Start tag for element
    def starttag(self, tag, indent):
        if tag:
            tag = self.indent_size * indent + '<' + tag
            if self.kwargs:
                attribute = ''
                for k in self.kwargs:
                    attribute += ' ' + k + '=\"' + self.kwargs[k] + '\"'
                tag += attribute
            tag += '>'
        return tag
        
    # End tag for element
    def endtag(self, tag, indent):
        if tag and not self.inline:
            tag = self.indent_size * indent + '</' + tag + '>'
        elif tag:
            tag = '</' + tag + '>'
        return tag
        
    # Generate start tag, content and closing tag
    def render(self, output_file, indent=0):
        # Render opening tag
        output_file.write(self.starttag(self.tag, indent))
        if not self.inline and not self.empty:
            output_file.write('\n')
        
        # Render content
        if self.content_list:
            for item in self.content_list:
                if type(item) == str:
                    if self.inline:
                        output_file.write(item)
                    else:
                        output_file.write(self.indent_size * indent + item)
                else:
                    item.render(output_file, indent + 1)
                if not self.inline:
                    output_file.write('\n')
                
        # Render closing tag
        if not self.empty:
            output_file.write(self.endtag(self.tag, indent))
        
# html tag
class Html(Element):
    tag = 'html'
    
    # Overwrite Element render method to add <!DOCTYPE html> before html tag
    # Comment out next 3 lines of code to not add <!DOCTYPE html> so that Steps 1-8
    # assert statements will pass
    def render(self, output_file, indent=0):
        output_file.write('<!DOCTYPE html>\n')
        super().render(output_file, indent)        

# body tag
class Body(Element):
    tag = 'body'
    
# paragraph tag
class P(Element):
    tag = 'p'
    
# head tag
class Head(Element):
    tag = 'head'
    
# title tag
class Title(Element):
    tag = 'title'
    inline = True
    
# tag with no content
class SelfClosingTag(Element):
    
    def __init__(self, content=None, **kwargs):
        self.kwargs = kwargs
        if content:
            raise TypeError('Content is not allowed for Self Closing Tag elements')

    def render(self, output_file, indent=0):
        # Render opening tag
        output_file.write(self.indent_size * indent + '<' + self.tag)
        
        # Render attribute
        if self.kwargs:
            attribute = ''
            for k in self.kwargs:
                attribute += ' ' + k + '=\"' + self.kwargs[k] + '\"'
            output_file.write(attribute)
                
        # Render closing tag
        output_file.write(' />')
    
# horizontal ruler tag
class Hr(SelfClosingTag):
    tag = 'hr'
    empty = True
    
# br/ tag
class Br(SelfClosingTag):
    tag = 'br'
    
# meta tag
class Meta(SelfClosingTag):
    tag = 'meta'

# a tag
class A(Element):
    tag = 'a'
    inline = True
    def __init__(self, link, content, **kwargs):
        self.content_list = []
        self.kwargs = kwargs
        self.kwargs['href'] = link
        if content:
            self.content_list.append(content)

# header tag
class H(Element):
    tag = 'h'
    inline = True
    def __init__(self, level, content, **kwargs):
        self.content_list = []
        self.kwargs = kwargs
        self.tag = self.tag + str(level)
        if content:
            self.content_list.append(content)

# unordered list tag
class Ul(Element):
    tag = 'ul'
    
# list tag
class Li(Element):
    tag = 'li'
       
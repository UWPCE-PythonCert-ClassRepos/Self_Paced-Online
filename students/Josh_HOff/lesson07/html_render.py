#!/usr/bin/env python3
import copy

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    
    indent = ''
    tag = 'html'

    def __init__(self, content=None, **kwargs):
#        print(f'{Element.indent}hi')
        self.test_dict = copy.deepcopy(kwargs)
        if content is None:
            self.contents = []
        else:
            self.contents = [content]

    def append(self, new_content):
        self.contents.append(new_content)

    def _opentag(self, out_file):
        pass        
        
    def render(self, out_file, cur_ind=''):
        if self.tag == 'html':
            out_file.write(f'<!DOCTYPE html>\n')
        open_tag = [f'{Element.indent}<{self.tag}']
        for key, value in self.test_dict.items():
            open_tag.append(f' {key}="{value}"')
        open_tag.append('>\n')
        out_file.write(''.join(open_tag))
        Element.indent += '    '
        for content in self.contents:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(f'{Element.indent}{content}')
                out_file.write('\n')
        Element.indent = (len(Element.indent) - 4) * ' '
        out_file.write(f'{Element.indent}</{self.tag}>\n')

        
                
        
class Body(Element):

    tag = 'body'
    
    
class Html(Element):

    tag = 'html'
    
class P(Element):

    tag = 'p'
    

class Head(Element):

    tag = 'head'
    
    
class OneLineTag(Element):

    def render(self, out_file, cur_ind=''):
        out_file.write(f'{Element.indent}<{self.tag}>')        
        out_file.write(self.contents[0])
        out_file.write(f'</{self.tag}>\n')
    def append(self, content):
        raise NotImplementedError
    
    
class Title(OneLineTag):

    tag = 'title'
    

class SelfClosingTag(Element):
    def __init__(self, content=None, **kwargs):
        if self.tag == 'meta charset="UTF-8"':
            kwargs = {}
        self.test_dict = copy.deepcopy(kwargs)
        if content is not None:
            raise TypeError('SelfClosingTag can not contain any content')
        super().__init__(content=content, **kwargs)
    
    def render(self, out_file, cur_ind=''):
        open_tag = [f'{Element.indent}<{self.tag}']
        for key, value in self.test_dict.items():
            open_tag.append(f' {key}="{value}"')
        out_file.write(''.join(open_tag))
        for content in self.contents:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
        out_file.write(f' />\n')
        
        
    def append(self, *args):
        raise TypeError('You can not add content to a SelfClosingTag')
        
        
class Hr(SelfClosingTag):

    tag = 'hr'
    
    
class Br(SelfClosingTag):

    tag = 'br'
    
    
class A(OneLineTag):

    tag = 'a'
    
    def __init__(self, link, content=None, **kwargs):
        self.test_dict = copy.deepcopy(kwargs)
        kwargs['href'] = link
        super().__init__(content, **kwargs)

    def render(self, out_file, cur_ind=''):
        Element.indent += '    '
        open_tag = [f'<{self.tag}']
        for key, value in self.test_dict.items():
            open_tag.append(f' {key}="{value}">')
        out_file.write(''.join(open_tag))
        for content in self.contents:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
        Element.indent = (len(Element.indent) - 4) * ' '
        out_file.write(f'</{self.tag}> ')
        
        
class Ul(Element):

    tag = 'ul'
    
    def render(self, out_file, cur_ind=''):
        open_tag = [f'{Element.indent}<{self.tag}']
        for key, value in self.test_dict.items():
            open_tag.append(f' {key}="{value}"')
        open_tag.append('>\n')
        out_file.write(''.join(open_tag))
        for content in self.contents:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
                out_file.write('\n')
        out_file.write(f'{Element.indent}</{self.tag}>\n')

    
    
class Li(Element):

    tag = 'li'
    def render(self, out_file, cur_ind=''):
        Element.indent += '    '
        open_tag = [f'{Element.indent}<{self.tag}']
        for key, value in self.test_dict.items():
            open_tag.append(f' {key}="{value}"')
        open_tag.append('>')
        out_file.write(''.join(open_tag))
        for content in self.contents:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
        Element.indent = (len(Element.indent) - 4) * ' '
        out_file.write(f'</{self.tag}>\n')
            
    
class H(OneLineTag):
    
    def __init__(self, level, content=None, **kwargs):
        self.tag = f'h{level}'
        super().__init__(content, **kwargs)
        
    def render(self, out_file, cur_ind=''):
        out_file.write(f'{Element.indent}<{self.tag}>')        
        out_file.write(self.contents[0])
        out_file.write(f'</{self.tag}>\n')


class Meta(SelfClosingTag):

    tag = 'meta charset="UTF-8"'
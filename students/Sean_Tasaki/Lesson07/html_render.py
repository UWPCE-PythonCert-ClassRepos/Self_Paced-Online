#!/usr/bin/env python3

"""
Sean Tasaki
6/10/2018
Lesson07.html_render
"""

# Step 1
class Element:
    tag_name = ''
    indent = '    '
    test = 'test'
    def __init__(self, content=None, **style):
        self.style = style
        if content:
            self.content = [content]
        else:
            self.content = []


    def append(self, words):
        self.content.append(words)
    
    def render(self, fileout, cur_ind=''):
        fileout.write(cur_ind + "<{}".format(self.tag_name))

        if self.style is not False:
            for key, value in self.style.items():  
                fileout.write(' {}="{}"'.format(key,value))
        fileout.write(">\n")

        for item in self.content:
            
            if hasattr(item, 'render'):
                item.render(fileout, cur_ind + self.indent)
            else: 
                fileout.write(cur_ind + self.indent + item)
                fileout.write("\n")     
        fileout.write(cur_ind + "</{}>\n".format(self.tag_name))
        

        

# Step 2
class Html(Element):
    tag_name = 'html'
    def render(self, fileout, cur_ind = ''):
        fileout.write(cur_ind + '<!DOCTYPE html>\n')
        Element.render(self, fileout, cur_ind)

class Body(Element):
    tag_name = 'body'

class P(Element):
    tag_name = 'p'

class Head(Element):
    tag_name = 'head'

class OneLineTag(Element):
    def render(self, fileout, cur_ind = ''):
        fileout.write(cur_ind + "<{}".format(self.tag_name))

        if self.style is not False:
            for key, value in self.style.items():  
                fileout.write(' {}="{}"'.format(key,value))
        fileout.write(">")

        for item in self.content:
            if hasattr(item, 'render'):
                item.render(fileout)
            else: 
                fileout.write(item) 
        fileout.write("</{}>\n".format(self.tag_name))

class Title(OneLineTag):
    tag_name = 'title'

class SelfClosingTag(Element):
    tag_name = ''
    
    # Self closing tags cannot accept content. Raise Error if there is content
    def __init__(self, content=None, **style):
        if content is not None:
            raise TypeError('SelfClosingTag may not have any content')
        else:
            super().__init__(**style)

    def render(self,fileout,cur_ind):
        fileout.write(cur_ind + '<{}'.format(self.tag_name,))
        if self.style is not False:
            for key, val in self.style.items():
                fileout.write( ' {}="{}"'.format(key, val))
        fileout.write(' />\n')

class Hr(SelfClosingTag):
    # <hr /> tags
    tag_name = 'hr'


class Br(SelfClosingTag):
    # <br /> tags
    tag_name = 'br'

class A(OneLineTag):
    # <a link /a> tags
    tag_name = 'a'
    def __init__(self, link, content):
        super().__init__(content, href = link)

class Ul(Element):
    # unordered list tag
    tag_name = 'ul'

class Li(Element):
    # list item tag
    tag_name = 'li'

class H(OneLineTag):
    tag_name = 'h'
    def __init__(self, level, content):
        self.tag_name = H.tag_name + str(level)
        super().__init__(content)

class Meta(SelfClosingTag):
    # <meta /> tags
    tag_name = 'meta'


#Lesson 7 Assignment 1
#HTML Render
#Jason Virtue 03/02/2019
#UW Self Paced Python Course

#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""

# This is the framework for the base class
class Element(object):

    tag = 'html'
    indent = ''

    def __init__(self, content=None, **kwargs):
        if content is None:
            self.content = []
        else:
            self.content = [content]
        self.attrs = kwargs

    def append(self, new_content):
        self.content.append(new_content)

    def render(self, file_out, cur_ind=''):
        file_out.write(cur_ind + '<{}'.format(self.tag))
        for attr_name, attr_value in self.attrs.items():
            file_out.write(' {} = "{}"'.format(attr_name,attr_value))
        file_out.write('>\n')

        for item in self.content:
            try:
                item.render(file_out)
            except AttributeError:
                file_out.write(str(item)+'\n')
        file_out.write('</{}>\n'.format(self.tag))

class Html(Element):
    tag = 'html'

    def render(self, file_out, cur_ind=''):
        file_out.write('<!DOCTYPE html>\n')
        super().render(file_out, cur_ind='')

class OneLineTag(Element):
    def render(self, file_out, cur_ind=''):
        file_out.write(cur_ind + '<{}>'.format(self.tag))
        for item in self.content:
            try:
                item.render(file_out)
            except AttributeError:
                file_out.write(str(item))
        file_out.write('</{}>\n'.format(self.tag))

class SelfClosingTag(Element):
    def render(self, file_out, cur_ind=''):
        file_out.write(cur_ind + '<{}'.format(self.tag))
        for attr_name, attr_value in self.attrs.items():
            file_out.write(' {} = "{}"'.format(attr_name, attr_value))
        file_out.write(' />\n')


class Body(Element):
    tag = 'body'

class P(Element):
    tag = 'p'

class Head(Element):
    tag = 'head'

class Title(OneLineTag):
    tag = "title"

class Hr(SelfClosingTag):
    tag = "hr"

class Br(SelfClosingTag):
    tag = "br"

class A(Element):
    tag = 'a'
    def __init__(self, link, content):
        super().__init__(content, href=link)

class Ul(Element):
    tag = "ul"

class Li(Element):
    tag = "li"

class H(OneLineTag):
    tag = 'h'

    def __init__(self,header_level, content):
        self.tag = 'h'+ str(header_level)
        super().__init__(content)

class Meta(SelfClosingTag):
    tag ="meta"
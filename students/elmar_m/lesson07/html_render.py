#!/usr/bin/env python3

'''
file: html_render.py
elmar_m / 22e88@mailbox.org
Lesson07: HTML renderer
'''

class Element:
    tag = 'element'
    props = []
    propstring = ''

    def __init__(self, content=None, **kwargs):       
        self.content = [content] if content else []  
        self.attrs = kwargs
        self.tagopen = self.tag

        if self.attrs:
            for key, value in self.attrs.items():
                self.props.append('{}="{}"'.format(key,value))
            self.propstring = ' '.join(self.props)
            self.tagopen = '{} {}'.format(self.tag, self.propstring)

    def append(self, stuff):
        self.content.append(stuff)

    def render(self, io, ind):
        io.write('<{}>\n'.format(self.tagopen))
        for i in self.content:
            if hasattr(i, 'render'):
                i.render(io, ind)
            else:
                line = '{}{}\n'.format(ind, i)
                io.write(line)
        io.write('</{}>\n'.format(self.tag))


class Html(Element):
    tag = 'html'
    def render(self, io, ind):
        io.write('<!DOCTYPE html>\n')
        Element.render(self, io, ind)


class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'
    props = []
    propstring = ''


class Head(Element):
    tag = 'head'


class Title(Element):
    tag = 'title'
    def __init__(self, text):
        self.text = text
    def render(self, io, ind):
        io.write('<{}>{}</{}>\n'.format(self.tag, self.text, self.tag))


class SelfClosingTag(Element):
    def render(self, io, ind):
        closing = '/'
        io.write('<{} {}>\n'.format(self.tagopen, closing))


class Meta(SelfClosingTag):
    tag = 'meta'
    props = []
    propstring = ''
    

class Hr(SelfClosingTag):
    tag = 'hr'


class A(Element):
    tag = 'a'
    def __init__(self, target, linktext):
        self.target = target
        self.link = linktext
        self.targetstring = 'href={}'.format(self.target)

    def render(self, io, ind):
        io.write('{}<{} {}>{}</{}>\n'.format(ind, self.tag, self.targetstring, self.link, self.tag))


class H(Element):
    tag = 'h'
    def __init__(self, size, text):
        self.size = size
        self.text = text
    def render(self, io, ind):
        io.write('<{}{}>{}</{}{}>\n'.format(self.tag, self.size, self.text, self.tag, self.size))


class Ul(Element):
    tag = 'ul'
    props = []
    propstring = ''
 

class Li(Ul):
    tag = 'li'
    props = []
    propstring = ''


#!/usr/bin/env python3

'''
file: html_render.py
elmar_m / 22e88@mailbox.org
Lesson07: HTML renderer
'''

class Element:
    tag = 'element'

    def __init__(self, content=None):       # wird erzeugt und kann schon content uebergeben bekommen, 
        self.content = [content] if content else []  #  siehe Step2 body.append(hr.P("blabla...")

    def append(self, stuff):
        self.content.append(stuff)

    def render(self, io, ind):
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
    def render(self, io, ind):
        io.write('<!DOCTYPE html>\n')
        Element.render(self, io, ind)


class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'
    def __init__(self, content=None, **kwargs):   
        self.content = [content] if content else []
        if 'style' in kwargs.keys():
            s = kwargs['style']
            self.style = str('style="' + s + '"')
    def render(self, io, ind):
        io.write('<{} {}>\n'.format(self.tag, self.style))
        for i in self.content:
                line = '{}{}\n'.format(ind, i)
                io.write(line)
        io.write('</{}>\n'.format(self.tag))


class Head(Element):
    tag = 'head'


class Title(Element):
    tag = 'title'
    def __init__(self, text):
        self.text = text
    def render(self, io, ind):
        io.write('<{}>{}</{}>\n'.format(self.tag, self.text, self.tag))


class SelfClosingTag(Element):
    def __init__(self):     # if erroneously given a second argument ('content'), 
        pass                # a TypeError will be raised
    def render(self, io, ind):
        closing = '/'
        io.write('<{} {}>\n'.format(self.tag, closing))


class Meta(SelfClosingTag):
    props = []
    propstring = ''
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            self.props.append('{}="{}"'.format(key,value))

        self.propstring = ' '.join(self.props)
        self.tag = 'meta ' + self.propstring
    

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
    def __init__(self, content=None, **kwargs):       
        self.content = [content] if content else []
        props = []
        for key, value in kwargs.items():
            props.append('{}="{}"'.format(key,value))
        self.propstring = ' '.join(props)

    def append(self, stuff):
        self.content.append(stuff)

    def render(self, io, ind):
        io.write('<{} {}>\n'.format(self.tag, self.propstring))
        for i in self.content:
            if hasattr(i, 'render'):
                i.render(io, ind)
            else:
                line = '{}{}\n'.format(ind, i)
                io.write(line)
        io.write('</{}>\n'.format(self.tag))
 

class Li(Ul):
    tag = 'li'


#!/usr/bin/env python
# coding: utf-8

# Goal: to create a set of classes to render html pages
import os

class Element:
    #
    tag = "html"
    indent =  "  "
    #
    def __init__(self, content = None, **kwargs):
        self.styles = kwargs
        if content is None:
            self.content = []
        else:
            self.content = [content]
    #
    def append(self, content_add):
        self.content.append(content_add)
    #
    def render(self, file_out, cur_ind = ""):
        #
        file_out.write(cur_ind + "<{}".format(self.tag))
        #
        for key, value in self.styles.items():
            file_out.write(' {}="{}"'.format(key,value))
        #
        file_out.write(">\n")
        #
        for item in self.content:
            if isinstance(item, Element):
                item.render(file_out, cur_ind + self.indent)
            else:
                file_out.write(cur_ind + self.indent + item)
                file_out.write("\n")
                #
        file_out.write(cur_ind + "</{}>\n".format(self.tag))


class Html(Element):
    tag = 'html'
    def render(self, file_out, cur_ind = ""):
        file_out.write("<!DOCTYPE html>\n")
        Element.render(self, file_out, cur_ind = "")

class Body(Element):
    tag = 'body'

class P(Element):
    tag = 'p'
#

class Head(Element):
    tag = 'head'


class SelfClosingTag(Element):
    def __init__(self, **kwargs):
        self.styles = kwargs
    def render(self, file_out, cur_ind=""):
        file_out.write(cur_ind + "<{}".format(self.tag))
        for key, value in self.styles.items():
            file_out.write(' {}="{}"'.format(key,value))
        file_out.write(" />\n")

class OneLineTag(Element):
    def render(self, file_out, cur_ind=""):
        file_out.write(cur_ind + "<{}".format(self.tag))
        for key, value in self.styles.items():
            file_out.write(' {}="{}"'.format(key, value))
        file_out.write(">")
        for item in self.content:
            if isinstance(item, Element):
                item.render(file_out, cur_ind + self.indent)
            else:
                file_out.write(item)
        file_out.write("</{}>\n".format(self.tag))

class Title(OneLineTag):
    tag = 'title'

class Meta(SelfClosingTag):
    tag = 'meta'

class Hr(SelfClosingTag):
    tag = 'hr'

class Br(SelfClosingTag):
    tag = 'br'

class A(Element):
    tag = 'a'
    def __init__(self, link, content):
        Element.__init__(self, content, href=link)

class Ul(Element):
    tag = 'ul'

class Li(Element):
    tag = 'li'

class H(OneLineTag):
    def __init__(self, size, content, **kwargs):
        OneLineTag.__init__(self, content, **kwargs)
        self.size = size
        self.tag = "h{}".format(size)

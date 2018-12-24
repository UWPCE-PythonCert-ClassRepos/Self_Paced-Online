"""
Author: Alyssa Hong
Date: 12/18/2018
Update:
Lesson7 Assignments > HTML Renderer.
"""



#!/usr/bin/env python3

"""
a simple script can run and test your html rendering classes.

Uncomment the steps as you add to your rendering.

"""
import os


class Element:

    tag = "html"
    indent = "  "

    def __init__(self, content=None, **style):
        self.content = [content] if content else[]
        self.styles = style

    def append(self, new_content):
        self.content.append(new_content)

    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind + "<{}".format(self.tag))

        for key, value in self.styles.items():
            out_file.write(' {}="{}"'.format(key,value))
        out_file.write(">\n")

        for item in self.content:
            if isinstance(item, Element):
                item.render(out_file, cur_ind + self.indent)
            else:
                out_file.write(cur_ind + self.indent + item)
                out_file.write("\n")

        out_file.write(cur_ind + "</{}>\n".format(self.tag))


class Html(Element):
    tag = 'html'

    def render(self, out_file, cur_ind=""):
        out_file.write("<!DOCTYPE html>\n")
        Element.render(self, out_file, cur_ind="")


class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'


class Head(Element):
    tag = 'head'


class SelfClosingTag(Element):

    def __init__(self, **style):
        self.styles = style

    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind + "<{}".format(self.tag))
        for key, value in self.styles.items():
            out_file.write(' {}="{}"'.format(key,value))
        out_file.write(" />\n")


class OneLineTag(Element):

    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind + "<{}".format(self.tag))

        for key, value in self.styles.items():
            out_file.write(' {}="{}"'.format(key, value))
        out_file.write(">")

        for item in self.content:
            if isinstance(item, Element):
                item.render(out_file, cur_ind + self.indent)
            else:
                out_file.write(item)
        out_file.write("</{}>\n".format(self.tag))


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

    def __init__(self, size, content, **style):
        OneLineTag.__init__(self, content, **style)
        self.size = size
        self.tag = "h{}".format(size)

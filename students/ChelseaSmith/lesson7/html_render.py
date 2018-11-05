#!/usr/bin/env python3

from io import StringIO

#  a series of classes used to generate html


class Element:
    tag = ""
    indent = " "

    def __init__(self, content=None, **kwargs):
        self.content = content
        self.kwargs = kwargs
        if self.content != None:
            self.contentList = [content]
        else:
            self.contentList = []


    def append(self, addon):
        self.contentList.append(addon)

    def render(self, file_out, cur_ind = 0):
        file_out.write(f"{(self.indent * cur_ind)}<{self.tag}")
        if type(self.kwargs) == dict:
            for k in self.kwargs:
                file_out.write(f" {k}=\"{self.kwargs[k]}\"")   # note: kwargs had 3 empty values in it that prevented me from using for k, v format
        file_out.write(f">\n")
        if self.contentList:
            for item in self.contentList:
                if type(item) == str:
                    file_out.write(item)
                else:
                    new_ind = cur_ind +1
                    item.render(file_out, new_ind)
        file_out.write(f"{(self.indent * cur_ind)}</{self.tag}>\n")


class Html(Element):
    tag = "html"

    def render(self, file_out):
        file_out.write(f"<!DOCTYPE html>")
        Element.render(self, file_out)


class Body(Element):
    tag = "body"


class P(Element):
    tag = "p"


class Head(Element):
    tag = "head"


class OneLineTag(Element):
    def render(self, file_out, cur_ind = 0):
        file_out.write(f"{(self.indent * cur_ind)}<{self.tag}")
        if type(self.kwargs) == dict:
            for k in self.kwargs:
                file_out.write(
                    f" {k}=\"{self.kwargs[k]}\"")
        file_out.write(f">")
        if self.contentList:
            for item in self.contentList:
                if type(item) == str:
                    file_out.write(item)
                else:
                    new_ind = cur_ind + 1
                    item.render(file_out, new_ind)
        file_out.write(f"</{self.tag}>\n") # indenting removed for prettier html


class Title(OneLineTag):
    tag = "title"


class SelfClosingTag(Element):
    def render(self, file_out, cur_ind = 0):
        file_out.write(f"{(self.indent * cur_ind)}<{self.tag}")
        if type(self.kwargs) == dict:
            for k in self.kwargs:
                file_out.write(f" {k}=\"{self.kwargs[k]}\"")
        file_out.write(f" />\n")
        if self.contentList:
            for item in self.contentList:
                new_ind = cur_ind +1
                item.render(file_out, new_ind)


class Hr(SelfClosingTag):
    tag = "hr"


class Br(SelfClosingTag):
    tag = "br"


class A(Element):
    tag = "a"

    def __init__(self, link, content):
        Element.__init__(self, content, href = link)


    def render(self, file_out, cur_ind = 0):
        file_out.write(f"{(self.indent * cur_ind)}<{self.tag}")
        if type(self.kwargs) == dict:
            for k in self.kwargs:
                file_out.write(
                    f" {k}=\"{self.kwargs[k]}\"")
        file_out.write(f">")
        if self.contentList:
            for item in self.contentList:
                if type(item) == str:
                    file_out.write(item)
                else:
                    new_ind = cur_ind + 1
                    item.render(file_out, new_ind)
        file_out.write(f"{(self.indent * cur_ind)}</{self.tag}>") # newline removed for prettier html formatting


class Ul(Element):
    tag = "ul"


class Li(OneLineTag): #changed superclass for prettier html formatting
    tag = "li"


class H(OneLineTag):
    def __init__(self, level, content):
        OneLineTag.__init__(self, content)
        self.tag = f"h{level}"


class Meta(SelfClosingTag):
    tag = "meta"

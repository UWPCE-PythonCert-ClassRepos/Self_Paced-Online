#!/usr/bin/env python3
class Element:
    tag = ""
    indent = " "

    def __init__(self, content=None, **kwargs):
        self.indent = 4
        if content:
            self.content = [content]
        else:
            self.content = []
        self.html_options = kwargs

    def append(self, p_content):
        return self.content.append(p_content)

    def render(self, file_out, cur_ind=" "):
        file_out.write(f"<{self.tag}")
        for k in self.html_options:
            file_out.write(f" {k}={self.html_options[k]}")
        file_out.write(f"> ")
        file_out.write("\n")

        for item in range(len(self.content)):
            if isinstance(self.content[item], Element):
                self.content[item].render(file_out)
            else:
                file_out.write(self.content[item])
                file_out.write("\n")
        file_out.write(f"<\\{self.tag}>")
        file_out.write("\n")


class Html(Element):
    tag = "html"

    def render(self,file_out,cur_ind=" "):
        file_out.write(f"<!DOCTYPE html>")
        file_out.write("\n")
        Element.render(self, file_out,cur_ind=" ")
        file_out.write("\n")


class Body(Element):
    tag = "body"


class P(Element):
    tag = "p"


class Head(Element):
    tag = "head"


class OneLineTag(Element):
    tag = "head"

    def render(self, file_out, cur_ind = ""):
        file_out.write(f"<{self.tag}>")
        file_out.write(f"<\\{self.tag}>")


class Title(Element):
    tag = "title"


class Hr(Element):
    tag = "hr"

    def render(self, file_out, cur_ind=""):
        file_out.write(f"<{self.tag}/>")


class Br(Element):
    tag = "br"

    def render(self, file_out, cur_ind=""):
        file_out.write(f"<{self.tag}/>")


class A(Element):
    tag = "a"

    def __init__(self, link, content, **kwargs):
        Element.__init__(self, content, **kwargs)


class Ul(Element):
    tag = "ul"


class Li(Element):
    tag = "li"


class H(OneLineTag):
    tag = "h"

    def __init__(self, number, content):
        OneLineTag.__init__(self, Element)
        self.number = number

    def render(self, file_out, cur_ind = ""):
        file_out.write(f"<{self.tag}{self.number}>")
        file_out.write(f"<\\{self.tag}>")


class Meta(Element):

    tag = "meta"

    def render(self, file_out, cur_ind=""):
        file_out.write(f"<{self.tag}  charset=\"UTF-8\"/>")
        file_out.write("\n")



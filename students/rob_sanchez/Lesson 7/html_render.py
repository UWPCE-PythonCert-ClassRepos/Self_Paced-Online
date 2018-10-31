#!/usr/bin/env python3


# Class for rendering an html elements
class Element:
    tag = ""
    ind_level = 4
    indent = " " * ind_level

    def __init__(self, content=None, **kwargs):

        self.kwargs = dict(kwargs)

        if content is None:
            self.content = []
        else:
            self.content = [content]

    def append(self, content):
        self.content.append(content)

    # renders the tag and the strings in the content
    def render(self, file_out, ind_level=ind_level):
        styles = ""
        for key, value in self.kwargs.items():
            style_tag = ' {}="{}"'
            styles = styles + style_tag.format(key, value)

        open_tag = "{}<{}{}>\n"
        close_tag = "{}</{}>\n"

        file_out.write(open_tag.format(self.indent, self.tag, styles))

        for values in self.content:
            if hasattr(values, "render"):
                values.render(file_out, ind_level=self.indent)
            else:
                file_out.write(" "*4 + self.indent + str(values) + "\n")

        file_out.write(close_tag.format(self.indent, self.tag))


class Html(Element):
    tag = "html"
    indent = ""

    def render(self, file_out, ind_level=0):
        initial_tag = "<!DOCTYPE html>\n"
        file_out.write(initial_tag)
        Element.render(self, file_out)


class Body(Element):
    tag = "body"
    indent = ""


class P(Element):
    tag = "p"


class Head(Element):
    tag = "head"
    indent = ""


class OneLineTag(Element):

    def render(self, file_out, ind_level):
        open_tag = "{}<{}>"
        close_tag = "</{}>\n"

        file_out.write(open_tag.format(self.indent, self.tag))

        for values in self.content:
            file_out.write(str(values))

        file_out.write(close_tag.format(self.tag))


class Title(OneLineTag):
    tag = "title"


class SelfClosingTag(Element):
    def __init__(self, content=None, **kwargs):
        self.kwargs = kwargs
        if content is not None:
            raise TypeError("Self closing tags must be empty!")

    def render(self, file_out, ind_level):
        sc_tag = "{}<{}{} /> \n"
        styles = ""
        for key, value in self.kwargs.items():
            style_tag = ' {}="{}"'
            styles = styles + style_tag.format(key, value)

        file_out.write(sc_tag.format(self.indent, self.tag, styles))


class Hr(SelfClosingTag):
    tag = "hr"


class Br(SelfClosingTag):
    tag = "br"


class A(Element):
    tag = "a"
    addtl = " " * 8

    def __init__(self, link, content):
        Element.__init__(self, content, href=link)

    def render(self, file_out, ind_level):
        open_tag = '{}<{}{}>{}'
        style_tag = ' href="{}"'.format(self.kwargs['href']) if ("href" in self.kwargs) else ''
        close_tag = '</{}>\n'

        for val in self.content:
            file_out.write(open_tag.format(self.indent+self.addtl, self.tag,
                           style_tag.format(self.kwargs), val))

        file_out.write(close_tag.format(self.tag))


class Ul(Element):
    tag = "ul"


class Li(Element):
    tag = "li"
    indent = " " * 8


class H(OneLineTag):

    def __init__(self, level, content, **kwargs):
        OneLineTag.__init__(self, content, **kwargs)
        self.tag = "h" + str(level)


class Meta(SelfClosingTag):
    tag = "meta"

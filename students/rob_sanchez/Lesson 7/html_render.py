#!/usr/bin/env python3


# Class for rendering an html element
class Element:
    tag = ""

    def __init__(self, content=None, **kwargs):

        self.kwargs = dict(kwargs)

        if content is None:
            self.content = []
        else:
            self.content = [content]

    def append(self, content):
        self.content.append(content)

    # renders the tag and the strings in the content
    def render(self, file_out, cur_ind=""):
        attrs = ""
        for key, value in self.kwargs.items():
            style_tag = ' {}="{}"'
            attrs = attrs + style_tag.format(key, value)

        open_tag = "{}<{}{}>\n"
        close_tag = "{}</{}>\n"

        file_out.write(open_tag.format(cur_ind, self.tag, attrs))

        for values in self.content:
            if hasattr(values, "render"):
                values.render(file_out, cur_ind)
            else:
                file_out.write(cur_ind + str(values) + "\n")

        file_out.write(close_tag.format(cur_ind, self.tag))


class Html(Element):
    tag = "html"

    def render(self, file_out, cur_ind=""):
        initial_tag = "<!DOCTYPE html>\n"
        file_out.write(initial_tag)
        Element.render(self, file_out, cur_ind)


class Body(Element):
    tag = "body"


class P(Element):
    tag = "p"


class Head(Element):
    tag = "head"


class OneLineTag(Element):

    def render(self, file_out, cur_ind=""):
        open_tag = "{}<{}>"
        close_tag = "{}</{}>\n"

        file_out.write(open_tag.format(cur_ind, self.tag))

        for values in self.content:
            file_out.write(cur_ind + str(values))

        file_out.write(close_tag.format(cur_ind, self.tag))


class Title(OneLineTag):
    tag = "title"


class SelfClosingTag(Element):
    def __init__(self, content=None, **kwargs):
        self.kwargs = kwargs
        if content is not None:
            raise TypeError("Self closing tags must be empty!")

    def render(self, file_out, cur_ind=""):
        sc_tag = "{}<{}{} /> \n"
        attrs = ""
        for key, value in self.kwargs.items():
            style_tag = ' {}="{}"'
            attrs = attrs + style_tag.format(key, value)

        file_out.write(sc_tag.format(cur_ind, self.tag, attrs))


class Hr(SelfClosingTag):
    tag = "hr"


class Br(SelfClosingTag):
    tag = "br"


class A(Element):
    tag = "a"

    def __init__(self, link, content):
        Element.__init__(self, content, href=link)

    def render(self, file_out, cur_ind=""):
        style_tag = ' href="{}"'.format(self.kwargs['href']) if ("href" in self.kwargs) else ''
        open_tag = '{}<{}{}>{}'
        close_tag = '</{}>\n'

        for val in self.content:
            file_out.write(open_tag.format(cur_ind, self.tag, style_tag.format(self.kwargs), val))

        file_out.write(close_tag.format(self.tag))


class Ul(Element):
    tag = "ul"


class Li(Element):
    tag = "li"


class H(OneLineTag):

    def __init__(self, level, content, **kwargs):
        OneLineTag.__init__(self, content, **kwargs)
        self.tag = "h" + str(level)


class Meta(SelfClosingTag):
    tag = "meta"

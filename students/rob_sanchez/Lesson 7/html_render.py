#!/usr/bin/env python3


# Class for rendering an html element
class Element:
    tag = ""
    one_line = "False"

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
        style_tag = " style={}".format(self.kwargs['style']) if ("style" in self.kwargs) else ""
        open_tag = "{}<{}{}>\n" if (self.one_line == "False") else "{}<{}>"
        close_tag = "{}</{}>\n"

        file_out.write(open_tag.format(cur_ind, self.tag, style_tag))

        for values in self.content:
            if hasattr(values, "render"):
                values.render(file_out, cur_ind)
            else:
                if (self.one_line == "False"):
                    file_out.write(cur_ind + str(values) + "\n")
                else:
                    file_out.write(cur_ind + str(values))

        file_out.write(close_tag.format(cur_ind, self.tag))


class Html(Element):
    tag = "html"
    one_line = "False"

    def render(self, file_out, cur_ind=""):
        initial_tag = "<!DOCTYPE html>\n"
        file_out.write(initial_tag)
        Element.render(self, file_out, cur_ind)


class Body(Element):
    tag = "body"
    one_line = "False"


class P(Element):
    tag = "p"
    one_line = "False"


class Head(Element):
    tag = "head"
    one_line = "False"


class Title(Element):
    tag = "title"
    one_line = "True"


class OneLineTag(Element):
    def render(self, file_out, cur_ind=""):
        open_tag = "{}<{}>"
        close_tag = "{}</{}>"
        file_out.write(open_tag.format(cur_ind, self.tag))
        for values in self.content:
            if hasattr(values, "render"):
                values.render(file_out, cur_ind)
            else:
                file_out.write(cur_ind + str(values) + "\n")
        file_out.write(close_tag.format(cur_ind, self.tag))

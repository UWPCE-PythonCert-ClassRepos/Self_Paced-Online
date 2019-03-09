#!/usr/bin/env python3
class Element:
    tag = ""

    def __init__(self, content=None):
        self.indent = 4
        if content:
            self.content = [content]
        else:
            self.content = []

    def append(self, p_content):
        return self.content.append(p_content)

    def render(self, file_out, cur_ind = ""):
        file_out.write(f"<{self.tag}>")

        for _ in range(len(self.content)):
            if isinstance(self.content[_], Element):
                self.content[_].render(file_out)
            else:
                file_out.write(self.content[_])
                file_out.write(". ")
                file_out.write("\n")
        file_out.write(f"<\\{self.tag}>")


class Html(Element):
    tag = "html"


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






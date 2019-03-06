#!/usr/bin/env python3

# Step 1
class Element:
    tag = "html"
    indent = "  "

    def __init__(self, content=None, **kwargs):
        self.content = []
        self.kwargs = {}

        if content:
            self.content.append(content)
        if kwargs:
            self.kwargs = kwargs

    def append(self, new_content):
        self.content.append(new_content)

    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind + f"<{self.tag}")

        for key, value in self.kwargs.items():
            out_file.write(f' {key} = "{value}"')
        out_file.write(">\n")

        for item in self.content:
            if isinstance(item, Element):
                item.render(out_file, cur_ind + self.indent)
            else:
                out_file.write(cur_ind + self.indent + item)
                out_file.write("\n")

        out_file.write(cur_ind + f"</{self.tag}>\n")


# Step 2
class Html(Element):
    tag = "html"

    # Step 8
    def render(self, out_file, cur_ind=""):
        out_file.write("<!DOCTYPE html>\n")
        Element.render(self, out_file, cur_ind)


class Body(Element):
    tag = "body"


class P(Element):
    tag = "p"


# Step 3
class Head(Element):
    tag = "head"


class OneLineTag(Element):
    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind + f"<{self.tag}")

        for key, value in self.kwargs.items():
            out_file.write(f' {key} = "{value}"')
        out_file.write(">")

        for item in self.content:
            if isinstance(item, Element):
                item.render(out_file, cur_ind + self.indent)
            else:
                out_file.write(item)

        out_file.write(f"</{self.tag}>\n")


class Title(OneLineTag):
    tag = "title"


# Step 5
class SelfClosingTag(Element):
    def render(self, out_file, cur_ind="", **kwargs):
        self.kwargs = kwargs

        out_file.write(cur_ind + f"<{self.tag}")

        for key, value in self.kwargs.items():
            out_file.write(f' {key} = "{value}"')

        out_file.write(" />\n")


class Meta(SelfClosingTag):
    tag = "meta"


class Hr(SelfClosingTag):
    tag = "hr"


class Br(SelfClosingTag):
    tag = "br"


# Step 6
class A(Element):
    tag = "a"

    def __init__(self, link, content):
        Element.__init__(self, content, href=link)


# Step 7
class Ul(Element):
    tag = "ul"


class Li(Element):
    tag = "li"


class H(OneLineTag):
    def __init__(self, size, content, **kwargs):
        OneLineTag.__init__(self, content, **kwargs)
        self.size = size
        self.tag = f"h{size}"

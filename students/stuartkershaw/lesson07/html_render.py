#!/usr/bin/env python3


class TextWrapper:
    """
    A simple wrapper that creates a class with a render method
    for simple text
    """
    def __init__(self, text):
        self.text = text

    def render(self, file_out, cur_ind=""):
        file_out.write(cur_ind)
        file_out.write(
            f"{self.text}\n"
        )


class Element:
    tag_name = ''
    indentation = 4

    def __init__(self, content=None):
        self.content = [] if content is None else [TextWrapper(content)]

    def append(self, content):
        if isinstance(content, str):
            self.content.append(TextWrapper(content))
        else:
            self.content.append(content)

    def render(self, file_out, cur_ind=""):
        self.file_out = file_out
        self.cur_ind = cur_ind

        self.file_out.write(f"{self.cur_ind}<{self.tag_name}>\n")

        for el in self.content:
            el.render(self.file_out, self.cur_ind)

        self.file_out.write(f"{self.cur_ind}</{self.tag_name}>")

        if not self.tag_name == 'html':
            self.file_out.write("\n")


class Html(Element):
    tag_name = 'html'


class Body(Element):
    tag_name = 'body'


class P(Element):
    tag_name = 'p'

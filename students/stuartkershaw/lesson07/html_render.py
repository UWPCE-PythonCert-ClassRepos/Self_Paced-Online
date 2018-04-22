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
    cur_tree_level = [0]

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

        if self.tag_name not in ['', 'html']:
            self.cur_tree_level[0] += 1
            self.file_out.write(
                " " * self.cur_tree_level[0] * self.indentation
            )

        if not self.tag_name == '':
            self.file_out.write(f"<{self.tag_name}>\n")

        for el in self.content:
            el.render(self.file_out, self.cur_ind)

        if self.tag_name not in ['', 'html']:
            self.file_out.write(
                " " * self.cur_tree_level[0] * self.indentation
            )

        if not self.tag_name == '':
            self.file_out.write(f"</{self.tag_name}>")

        if self.tag_name not in ['', 'html']:
            self.cur_tree_level[0] -= 1
            self.file_out.write("\n")


class Html(Element):
    tag_name = 'html'


class Body(Element):
    tag_name = 'body'


class P(Element):
    tag_name = 'p'

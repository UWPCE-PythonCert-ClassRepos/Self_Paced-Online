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
            f"{self.text}"
        )


class Element:
    tag_name = ''
    indentation = 4
    cur_tree_level = [0]

    def __init__(self, content=None, **kwargs):
        self.content = [] if content is None else [TextWrapper(content)]
        self.kwargs = kwargs

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
            self.file_out.write(f"<{self.tag_name}")

            if self.kwargs:
                for key, value in self.kwargs.items():
                    self.file_out.write(f" {key}=\"{value}\"")

            self.file_out.write(f">\n")

        for el in self.content:
            el.render(
                self.file_out,
                " " * (self.cur_tree_level[0] + 1) * self.indentation
            )

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


class Head(Element):
    tag_name = 'head'


class OneLineTag(Element):
    def render(self, file_out, cur_ind=""):
        self.file_out = file_out
        self.cur_ind = cur_ind

        self.file_out.write(
            " " * (self.cur_tree_level[0] + 1) * self.indentation
        )

        self.file_out.write(f"<{self.tag_name}")

        if self.kwargs:
            for key, value in self.kwargs.items():
                self.file_out.write(f" {key}=\"{value}\"")

        self.file_out.write(f">")

        for el in self.content:
            el.render(self.file_out)

        self.file_out.write(f"</{self.tag_name}>\n")


class Title(OneLineTag):
    tag_name = 'title'


class P(OneLineTag):
    tag_name = 'p'


class SelfClosingTag(Element):
    def render(self, file_out, cur_ind=""):
        self.file_out = file_out
        self.cur_ind = cur_ind

        self.file_out.write(
            " " * (self.cur_tree_level[0] + 1) * self.indentation
        )

        self.file_out.write(f"<{self.tag_name}")

        if self.kwargs:
            for key, value in self.kwargs.items():
                self.file_out.write(f" {key}=\"{value}\"")

        try:
            if len(self.content):
                raise TypeError
            self.file_out.write(f" />\n")
        except TypeError:
            print('This element does not accept nested content.')


class Hr(SelfClosingTag):
    tag_name = 'hr'

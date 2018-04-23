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

    def generate_spacing(self, tree_level):
        self.tree_level = tree_level

        return " " * self.tree_level * self.indentation

    def apply_attributes(self, attrs):
        self.attrs = attrs

        for key, value in self.attrs.items():
            self.file_out.write(f" {key}=\"{value}\"")

    def render(self, file_out, cur_ind=""):
        self.file_out = file_out
        self.cur_ind = cur_ind

        if self.tag_name not in ['', 'html']:
            self.cur_tree_level[0] += 1
            self.file_out.write(
                self.generate_spacing(self.cur_tree_level[0])
            )

        if not self.tag_name == '':
            self.file_out.write(f"<{self.tag_name}")

            if self.kwargs:
                self.apply_attributes(self.kwargs)

            self.file_out.write(f">\n")

        for el in self.content:
            el.render(
                self.file_out,
                self.generate_spacing(self.cur_tree_level[0] + 1)
            )

        if self.tag_name not in ['', 'html']:
            self.file_out.write(
                self.generate_spacing(self.cur_tree_level[0])
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
            self.generate_spacing(self.cur_tree_level[0] + 1)
        )

        self.file_out.write(f"<{self.tag_name}")

        if self.kwargs:
            self.apply_attributes(self.kwargs)

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
            self.generate_spacing(self.cur_tree_level[0] + 1)
        )

        self.file_out.write(f"<{self.tag_name}")

        if self.kwargs:
            self.apply_attributes(self.kwargs)

        try:
            if len(self.content):
                raise TypeError
            self.file_out.write(f" />\n")
        except TypeError:
            print('This element does not accept nested content.')


class Hr(SelfClosingTag):
    tag_name = 'hr'

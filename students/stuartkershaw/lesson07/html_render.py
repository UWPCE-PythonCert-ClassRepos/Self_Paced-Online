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
    ignored_tag_spacing = ['', 'a', 'html']

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

        if self.tag_name not in self.ignored_tag_spacing:
            self.cur_tree_level[0] += 1
            self.file_out.write(
                self.generate_spacing(self.cur_tree_level[0])
            )

        if not self.tag_name == '':
            self.file_out.write(f"<{self.tag_name}")

            if self.kwargs:
                self.apply_attributes(self.kwargs)

            self.file_out.write(f">")

            if not self.tag_name == 'a':
                self.file_out.write(f"\n")

        for el in self.content:
            el.render(self.file_out)

        if self.tag_name not in self.ignored_tag_spacing:
            self.file_out.write(
                self.generate_spacing(self.cur_tree_level[0])
            )

        if not self.tag_name == '':
            self.file_out.write(f"</{self.tag_name}>")

        if self.tag_name not in self.ignored_tag_spacing:
            self.cur_tree_level[0] -= 1
            self.file_out.write("\n")


class Html(Element):
    tag_name = 'html'

    def render(self, file_out, cur_ind=""):
        self.file_out = file_out
        self.cur_ind = cur_ind

        self.file_out.write('<!DOCTYPE html>\n')

        Element.render(self, self.file_out, self.cur_ind)


class Body(Element):
    tag_name = 'body'


class Head(Element):
    tag_name = 'head'


class OneLineTag(Element):
    def render(self, file_out, cur_ind="", level=None):
        self.file_out = file_out
        self.cur_ind = cur_ind
        self.level = level

        self.file_out.write(
            self.generate_spacing(self.cur_tree_level[0] + 1)
        )
        self.file_out.write(f"<{self.tag_name}")

        if self.kwargs:
            if not self.tag_name == "h":
                self.apply_attributes(self.kwargs)
            else:
                self.file_out.write(f"{self.kwargs['level']}")

        self.file_out.write(f">")

        for el in self.content:
            el.render(self.file_out)

        self.file_out.write(f"</{self.tag_name}")

        if self.kwargs.get("level"):
            self.file_out.write(f"{self.kwargs.get('level')}")

        self.file_out.write(">\n")


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


class Br(SelfClosingTag):
    tag_name = 'br'


class A(Element):
    tag_name = 'a'

    def __init__(self, link, content):
        self.link = link
        self.content = content
        self.attributes = {'href': self.link}

        Element.__init__(self, content=self.content, **self.attributes)


class Ul(Element):
    tag_name: 'ul'


class Li(Element):
    tag_name: 'li'


class H(OneLineTag):
    tag_name = 'h'

    def __init__(self, level, content):
        self.level = level
        self.content = content
        self.attributes = {'level': self.level}

        OneLineTag.__init__(self, content=self.content, **self.attributes)


class Meta(SelfClosingTag):
    tag_name = 'meta'

    def __init__(self, **kwargs):
        self.attributes = kwargs

        SelfClosingTag.__init__(self, **self.attributes)

#!/usr/bin/env python3

class TextWrapper:
    """
    A simple wrapper that creates a class with a render method
    for simple text -- like the one in the lecture notes!
    """

    def __init__(self, text):
        self.text = text

    def render(self, file_out, cur_ind=''):
        file_out.write(cur_ind)
        file_out.write(self.text)

class Element:
    tag = "html"
    cur_ind = ''
    def __init__(self, content=None, **kwargs):
        self.attrs = kwargs
        self.content = []
        if content:
            self.content.append(content)
    def append(self, content):
        if hasattr(content, 'render'):
            self.content.append(content)
        else:
            self.content.append(TextWrapper(str(content)))
    def add_attrs(self, file_out, cur_ind=cur_ind):
        file_out.write("{}<{}".format(cur_ind, self.tag))
        for k, v in self.attrs.items():
            file_out.write(' {}="{}"'.format(k, v))
        file_out.write('>\n')
    def render(self, file_out, cur_ind=cur_ind):
        # file_out.write("<{}>\n".format(self.tag))
        self.add_attrs(file_out, cur_ind)
        for contents in self.content:
            try:
                contents.render(file_out)
            except AttributeError:
                file_out.write(str(contents) + "\n")
        file_out.write("{}</{}>\n".format(cur_ind, self.tag))


class OneLineTag(Element):
    cur_ind = ''
    def render(self, file_out, cur_ind=cur_ind):
        self.add_attrs(file_out, cur_ind)
        for contents in self.content:
            try:
                contents.render(file_out)
            except AttributeError:
                file_out.write(str(contents))
        file_out.write(" </{}>".format(self.tag))

class Html(Element):
    tag = 'html'
    cur_ind = ''
    def render(self, file_out, cur_ind=cur_ind):
        file_out.write(cur_ind + "<!DOCTYPE html>\n")
        super().render(file_out, cur_ind=cur_ind)
class Body(Element):
    tag = "body"
class P(Element):
    tag = "p"
class Head(Element):
    tag = "head"
class Title(OneLineTag):
    tag = "title"
class SelfClosingTag(Element):
    def render(self, file_out, cur_ind=''):
        self.add_attrs(file_out, cur_ind)
class Hr(SelfClosingTag):
    tag = "hr"
class Br(SelfClosingTag):
    tag = "br"
class A(OneLineTag):
    tag = 'a'
    def __init__(self, link, *args, **kwargs):
        kwargs['href'] = link
        super().__init__(*args, **kwargs)
class Ul(Element):
    tag = 'ul'
class Li(Element):
    tag = 'li'
class H(OneLineTag):
    def __init__(self, level, content):
        super().__init__(content)
        self.tag = 'h{}'.format(level)
class Meta(SelfClosingTag):
    tag = 'meta'
#!/usr/bin/env python3


"""
Lesson7 - HTML Renderer
"""


class Element:
    'Generates HTML tags, content, and attributes'

    version = '0.1'
    indent = '  '
    tag = ''

    def __init__(self, content=None, **kwargs):
        self.content = [] if content is None else [content]
        self.atts = kwargs if kwargs else ''
        self.tag = self.tag if self.tag else 'html'

    @staticmethod
    def format_atts(atts=None):
        if atts:
            s = ''.join(' {}="{}"'.format(k, v) for k, v in atts.items())
        else:
            s = ''
        return s

    def append(self, content):
        self.content.append(content)

    def render(self, file_out, cur_ind=""):
        atts = self.format_atts(self.atts)
        file_out.write("{}<{}{}>\n".format(cur_ind, self.tag, atts))
        for node in self.content:
            if isinstance(node, Element):
                node.render(file_out, cur_ind + self.indent)
            else:
                if self.tag == 'a':
                    file_out.write('{}{}\n'.format(cur_ind, node))
                else:
                    file_out.write(self.indent)
                    file_out.write('{}{}\n'.format(cur_ind, node))
        file_out.write("{}</{}>\n".format(cur_ind, self.tag))


class Html(Element):
    tag = 'html'

    def __init__(self, content=None, **kwargs):
        super().__init__(**{'lang': 'en'})

    def render(self, file_out, cur_ind=""):
        file_out.write("<!DOCTYPE html>\n")
        super().render(file_out, cur_ind)


class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'


class Head(Element):
    tag = 'head'


class OneLineTag(Element):
    tag = ''

    def render(self, file_out, cur_ind=""):
        atts = Element.format_atts(self.atts)
        file_out.write("{}<{}{}>".format(cur_ind, self.tag, atts))
        file_out.write('{}'.format(self.content[0]))
        file_out.write("</{}>\n".format(self.tag))


class Title(OneLineTag):
    tag = 'title'


class SelfClosingTag(Element):

    def __init__(self, content=None, **kwargs):
        self.content = content
        self.atts = kwargs if kwargs else ''
        if content:
            raise TypeError

    def render(self, file_out, cur_ind=""):
        atts = Element.format_atts(self.atts)
        file_out.write("{}<{}{} />\n".format(cur_ind, self.tag, atts))


class Hr(SelfClosingTag):
    tag = 'hr'


class Br(SelfClosingTag):
    tag = 'br'


class A(Element):
    tag = 'a'

    def __init__(self, href, content):
        self.href = href
        self.content = content
        super().__init__(content=content, **{'href': self.href})


class Ul(Element):
    tag = 'ul'


class Li(Element):
    tag = 'li'


class H(OneLineTag):

    def __init__(self, size, content, **kwargs):
        self.tag = 'h{}'.format(size)
        self.content = content
        self.kwargs = kwargs
        super().__init__(content, **kwargs)


class Meta(SelfClosingTag):
    tag = 'meta'

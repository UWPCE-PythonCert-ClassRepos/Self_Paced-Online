#!/usr/bin/env python3


class Element:
    """Base class to run functions"""
    tag = "html"
    indent = "    "

    def __init__(self, content=None, **kwargs):
        if content is None:
            self.content = []
        else:
            self.content = [content]
        self.atrbs = kwargs

    def append(self, content_str):
        """append content to the element class object"""
        self.content.append(content_str)

    def render(self, resp, cur_ind=0):
        """general render for html file"""
        resp.write(f'{cur_ind*self.indent}<{self.tag}{self.extra_attrib()}>\n')
        for item in self.content:
            try:
                item.render(resp, cur_ind+1)
            except AttributeError:
                resp.write((cur_ind + 1) * self.indent + str(item) + '\n')
        resp.write(f'{cur_ind * self.indent}</{self.tag}>\n')

    def extra_attrib(self):
        atb = ''
        if self.atrbs:
            for key, value in self.atrbs.items():
                atb += f' {key}="{value}";'
        return str(atb)


class OneLineTag(Element):

    def render(self, resp, cur_ind=0):
        ax = f'{(cur_ind) * self.indent}<{self.tag}>{self.content[0]}\
              {self.extra_attrib()}</{self.tag}>\n'
        resp.write(ax)


class H(OneLineTag):

    def __init__(self, level, desc):
        super().__init__(content=desc)
        self.tag = f'h{level}'


class SelfClosingTag(Element):

    def render(self, resp, cur_ind=0):
        resp.write(f'{(cur_ind) * self.indent}<{self.tag}\
                   {self.extra_attrib()} />\n')


class Html(Element):
    tag = 'html'

    def render(self, resp, cur_ind=0):
        file_out.write(cur_ind + "<!DOCTYPE html>\n")
        super().render(resp, cur_ind)


class A(Element):
    tag = 'a'

    def __init__(self, link, desc):
        super().__init__(content=desc, href=link)


class Ul(Element):
    tag = 'ul'


class Li(Element):
    tag = 'li'


class Head(Element):
    tag = 'head'


class Html(Element):
    tag = 'html'


class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'


class Title(OneLineTag):
    tag = 'title'


class Hr(SelfClosingTag):
    tag = 'hr'


class Br(SelfClosingTag):
    tag = 'br'


class Meta(SelfClosingTag):
    tag = 'meta'

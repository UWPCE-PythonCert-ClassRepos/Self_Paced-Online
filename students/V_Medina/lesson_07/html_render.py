#!/usr/bin/env python3

class Element():
    tag = ""
    indent = "    "

    def __init__(self, content=None, **kwargs):
        # self.contentList = []
        self.content = content
        self.attr = kwargs
        if self.content is not None:
            self.contentList = [content]
        else:
            self.contentList = []

    def append(self, new_str):
        self.contentList.append(new_str)

    def render(self, file_out, cur_ind=""):
        cur_ind += self.indent
        file_out.write('{}<{}'.format(cur_ind, self.tag))
        for key, value in self.attr.items():
            file_out.write(' {}="{}"'.format(key, value))
        file_out.write('>\n')
        for content in self.contentList:
            try:
                content.render(file_out)
            except AttributeError:
                file_out.write(content)

        file_out.write('</{}>\n'.format(self.tag))


class Html(Element):
    tag = "html"

    def render(self, file_out, cur_ind=""):
        file_out.write("<!DOCTYPE html>\n")
        Element.render(self, file_out, cur_ind)


class Body(Element):
    tag = "body"


class P(Element):
    tag = "p"


class Head(Element):
    tag = "head"


class OneLineTag(Element):
    tag = ""
    indent = "    "

    def append(self, new_str):
        self.contentList.append(new_str)

    def render(self, file_out, cur_ind=""):
        cur_ind += self.indent
        for content in self.contentList:
            file_out.write('{}<{}'.format(cur_ind, self.tag))
            for key, value in self.attr.items():
                file_out.write(' {}="{}"'.format(key, value))
            file_out.write('>')
            try:
                content.render(file_out)
            except AttributeError:
                file_out.write(content)
            file_out.write('</{}>\n'.format(self.tag))


class Title(OneLineTag):
    tag = "title"


class SelfClosingTag(Element):
    tag = ""
    indent = "    "

    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError('Content is not allowed for a self closing tag')
        super().__init__(content, **kwargs)

    def render(self, file_out, cur_ind=""):
        cur_ind += self.indent
        file_out.write('{}<{} />'.format(cur_ind, self.tag))
        for content in self.contentList:
            try:
                content.render(file_out)
            except AttributeError:
                file_out.write(content)
        file_out.write('\n')

    def append(self, new_str):
        raise TypeError('Content is not allowed for a self closing tag')


class Hr(SelfClosingTag):
    tag = 'hr'


class Br(SelfClosingTag):
    tag = 'br'


class Ul(Element):
    tag = 'ul'


class Li(Element):
    tag = 'li'


class H(OneLineTag):

    def __init__(self, level, content=None, **kwargs):
        tag = 'h'
        self.tag = tag + str(level)
        super().__init__(content, **kwargs)


class A(OneLineTag):
    tag = "a"

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)





class Meta(SelfClosingTag):
    tag = "meta"

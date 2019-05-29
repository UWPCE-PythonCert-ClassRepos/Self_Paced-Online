#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""
# This is the framework for the base class
class Element(object):
    tag = "html"
    indent = "    "

    def __init__(self, content=None, **kwargs):
        self.attributes = kwargs
        self.contents = []
        if content:
            self.contents.append(content)

    def append(self, new_content):
        # if hasattr(new_content, 'render'):
        #     self.contents.append(new_content)
        # else:
        self.contents.append(new_content)

    def _open_tag(self):
        tag = f"<{self.tag}"
        if self.attributes:
            for attr in self.attributes.keys():
                tag += (f" {attr}=\"{self.attributes[attr]}\"")
        tag += ('>')
        return tag

    def _close_tag(self):
        return f"</{self.tag}>"
        
    def render(self, out_file, cur_ind=''):
        # out_file.write("just something as a place holder...")
        out_file.write(cur_ind + self._open_tag() + '\n')
        for content in self.contents:
            try:
                content.render(out_file, cur_ind + self.indent)
            except AttributeError:
                out_file.write(cur_ind + self.indent + content)
            out_file.write('\n')
        out_file.write(cur_ind + self._close_tag())

class Html(Element):
    tag = 'html'
    def render(self, out_file, cur_ind=''):
        out_file.write(cur_ind + "<!DOCTYPE html>\n")
        super().render(out_file, cur_ind=cur_ind)

class Body(Element):
    tag = 'body'

class P(Element):
    tag = 'p'

class Head(Element):
    tag = 'head'

class OneLineTag(Element):
    def render(self, out_file, cur_ind=''):
        # out_file.write(f"<{self.tag}>")
        # out_file.write(content)
        # out_file.write(f"</{self.tag}>")
        # out_file.write(f"<{self.tag}>{self.contents[0]}</{self.tag}>\n")

        out_file.write(cur_ind + self._open_tag())
        for content in self.contents:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
        out_file.write(self._close_tag())

            
    def append(self,content):
        raise NotImplementedError

class Title(OneLineTag):
    tag = 'title'

class SelfClosingTag(Element):
    def __init__(self, content=None, **kwargs):
        self.attributes = kwargs
        if content != None:
            raise TypeError

    def append(self, new_content):
        raise TypeError

    def render(self,out_file, cur_ind='' ):
        # out_file.write(f"<{self.tag}")
        # if self.attributes:
        #     for attr in self.attributes.keys():
        #         out_file.write(f" {attr}={self.attributes[attr]};")
        # out_file.write(" />")
        out_file.write(cur_ind + self._open_tag()[:-1] + ' />\n')

class Hr(SelfClosingTag):
    tag = 'hr'

class Br(SelfClosingTag):
    tag = 'br'

class A(OneLineTag):
    tag = 'a'
    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)

class Ul(Element):
    tag = 'ul'

class Li(Element):
    tag = 'li'

class H(OneLineTag):
    tag = 'H'
    def __init__(self, level, *args, **kwargs):
        self.tag = f'h{int(level)}'
        super().__init__(*args, **kwargs)

class Meta(SelfClosingTag):
    tag = 'meta'


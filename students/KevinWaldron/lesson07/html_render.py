#!/usr/bin/env python3

class Element:
    """ Defines a basic html element type

    An html element consists of an open tag potentially containing attributes followed by content and finally a closing tag

    """

    tag = 'html'
    indent = 4

    def __init__(self, content=None, **kwargs):
        self.content = []
        if content is not None:
            self.append(content)
        self.attributes = kwargs

    def append(self, append_content):
        """ Append content to the element, content can be either a string or another element """
        if isinstance(append_content, str):
            self.content.append(TextElement(append_content))
        else:
            self.content.append(append_content)

    def render_tag_attrs(self, file_out, cur_ind="", end_of_tag=""):
        """ Render the opening tag followed by any attribtues and finally the end_of_tag"""
        file_out.write(cur_ind + f"<{self.tag}")
        for k , v in self.attributes.items():
            file_out.write(f" {k}=\"{v}\"")
        file_out.write(f"{end_of_tag}>")

    def render(self, file_out, cur_ind=""):
        """ Renders the html element in including tag, attributes, and content """
        self.render_tag_attrs(file_out, cur_ind)
        next_ind = cur_ind + (Element.indent * ' ')
        for v in self.content:
            file_out.write("\n")
            v.render(file_out, next_ind)
        file_out.write("\n" + cur_ind + f"</{self.tag}>")

class TextElement(Element):
    """ An element that contains only a text value """
    def __init__(self, text):
        self.text = text

    def append(self, append_content):
        """ Overridden append method that raise an exception since this type doesn't supprt content """
        raise TypeError("TextElement do not support content")

    def render(self, file_out, cur_ind=""):
        """ Render the text value """
        file_out.write(cur_ind + self.text)

class Body(Element):
    """ A body tag """
    tag = 'body'

class Html(Element):
    """ An html tag """
    tag = 'html'

    def render(self, file_out, cur_ind=""):
        """ Render method that adds a DOCTYPE tag first """
        file_out.write("<!DOCTYPE html>\n")
        Element.render(self, file_out, cur_ind)

class P(Element):
    """ A paragraph tag """
    tag = 'p'

class Head(Element):
    """ A head tag """
    tag = 'head'

class OneLineTag(Element):
    """ An html tag that renders everything on a single line """
    def render(self, file_out, cur_ind=""):
        self.render_tag_attrs(file_out, cur_ind);
        for v in self.content:
            v.render(file_out, "")
        file_out.write(f"</{self.tag}>")

class Title(OneLineTag):
    """ A title tag """
    tag = 'title'

class SelfClosingTag(Element):
    """ A self closing html tag, requires no closing tag and supports no content """

    def __init__(self, **kwargs):
        self.attributes = kwargs

    def append(self, append_content):
        """ Overridden append method that raise an exception since this type doesn't supprt content """
        raise TypeError("SelfClosingTag do not support content")

    def render(self, file_out, cur_ind=""):
        """ Renders out the tag, attributes, and closing > """
        self.render_tag_attrs(file_out, cur_ind, end_of_tag=" /")

class Hr(SelfClosingTag):
    """ A horizaontal rule tag """
    tag = 'hr'

class Br(SelfClosingTag):
    """ A line break tag """
    tag = 'br'

class A(OneLineTag):
    """ An anchor tag """
    tag = 'a'

    def __init__(self, link, content=None):
        link_ref = {"href":link}
        Element.__init__(self, content, **link_ref)

class Ul(Element):
    """ An unordered list tag """
    tag = 'ul'

class Li(Element):
    """ A list item tag """
    tag = 'li'

class H(OneLineTag):
    """ A header tag """
    def __init__(self, level, content=None):
        self.tag = 'h' + str(level)
        Element.__init__(self, content)

class Meta(SelfClosingTag):
    """ A meta tag """
    tag = 'meta'

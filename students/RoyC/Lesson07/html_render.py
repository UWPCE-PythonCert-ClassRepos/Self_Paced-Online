#!/usr/bin/env python3

class Element:
    """
    An element represents one level of html tag, which can contain more nested elements
    """
    tag = ""
    indent = 4
    
    def __init__(self, content=None, **kwargs):
        """
        Optional content is the next element nested under this one
        """
        self.content = []
        if not content is None:
            self.append(content)
        self.attr = kwargs
        
    def append(self, content):
        """
        Content to be appended is either an Element or a string, which will be used
        to append a new TextElement
        """
        if isinstance(content, str):
            self.content.append(TextEntry(content))
        else:
            self.content.append(content)
        
    def render(self, file_out, cur_ind=""):
        """
        Renders opening tag, followed by nested elements and closing tag
        """
        file_out.write(cur_ind + "<{}".format(self.tag))
        for key, val in self.attr.items():
            file_out.write(" {}=\"{}\"".format(key, val))
        file_out.write(">")
        sub_ind = cur_ind + (Element.indent * ' ')
        for entry in self.content:
            file_out.write("\n")
            entry.render(file_out, cur_ind + self.indent * " ")
        file_out.write("\n")
        file_out.write(cur_ind + "</{}>".format(self.tag))
        
class Html(Element):
    """
    An HTML tag element
    """
    tag = "html"
    
    def render(self, file_out, cur_ind=""):
        file_out.write("<!DOCTYPE html>\n")
        Element.render(self, file_out, cur_ind)

class Body(Element):
    """
    A body tag element
    """
    tag = "body"
    
class P(Element):
    """
    A paragraph tag element
    """
    tag = "p"
    
class Head(Element):
    """
    A head tag element
    """
    tag = "head"
    
class Ul(Element):
    """
    An unordered list tag element
    """
    tag = "ul"
    
class Li(Element):
    """
    A list item tag element
    """
    tag = "li"
    
class TextEntry(Element):
    """
    Lowest level of Element, used for plain text line entry
    """

    def __init__(self, text):
        self.text = text
        
    def append(self, content):
        # this is the lowest level Element, append is not applicable
        raise TypeError("TextEntry element does not support lower-level elements")
        
    def render(self, file_out, cur_ind=""):
        file_out.write(cur_ind + self.text)
    
class OneLineTag(Element):
    """
    An element that renders on one line
    """
    
    def render(self, file_out, cur_ind=""):
        """
        Same render as Element without line feeds
        """
        file_out.write(cur_ind + "<{}".format(self.tag))
        for key, val in self.attr.items():
            file_out.write(" {}=\"{}\"".format(key, val))
        file_out.write(">")
        sub_ind = (Element.indent * ' ')
        for entry in self.content:
            entry.render(file_out, "")
        file_out.write("</{}>".format(self.tag))
        
class Title(OneLineTag):
    """
    A one-line title tag element
    """
    tag = "title"
    
class A(OneLineTag):
    """
    An anchor tag element with an embedded link
    """
    tag = "a"
    
    def __init__(self, link, content=None):
        link_arg = {"href": link}
        Element.__init__(self, content, **link_arg)
    
class H(OneLineTag):
    """
    A one-line header tag element
    """
    def __init__(self, level, content=None):
        self.tag = "h{}".format(str(level))
        Element.__init__(self, content)
    
class SelfClosingTag(Element):
    """
    A self-closing tag element
    """
    def render(self, file_out, cur_ind=""):
        file_out.write(cur_ind + "<{}".format(self.tag))
        for key, val in self.attr.items():
            file_out.write(" {}=\"{}\"".format(key, val))
        file_out.write(" />")
        
class Hr(SelfClosingTag):
    """
    A horizontal rule tag element
    """
    tag = "hr"
    
class Br(SelfClosingTag):
    """
    A line break tag element
    """
    tag = "br"

class Meta(SelfClosingTag):
    """
    A meta tag element
    """
    tag = "meta"

    


#!/usr/bin/env python3
# Ian Letourneau
# 5/30/2018

from io import StringIO

"""A script to define classes to later be initialized by the
run_html_render.py script."""


class Element:
    """Parent class for all html elements to be created."""

    def __init__(self, open_tag="<html>",
                 close_tag="</html>", content=None, **kwargs):
        """Constructor for Element objects.

        :param open_tag="<html>": set opening tag parameter to html
        should none be given 

        :param close_tag="</html>": set closing tag parameter to html
        should none be given 

        :param content=None: set content value to NoneType if no 
        content associated"""

        self.open_tag = open_tag
        self.close_tag = close_tag
        self.content = [content]
        # Loop through input keywords to incoporate into element
        # attributes.
        if kwargs:
            self.open_tag = open_tag.strip(">")
            for key in kwargs:
                self.open_tag += ' {}="{}"'.format(key, kwargs[key])
            self.open_tag += ">"

    def append(self, content=None):
        """A function to append objects or strings to higher level
        html element objects."""
        if hasattr(content, 'render') and self.content:
            self.content.append(content)
        elif hasattr(content, 'render'):
            self.content = content
        elif content and self.content:
            self.content += content
        elif content:
            self.content = content

    def render(self, file_out, cur_ind=""):
        """A function to render page elements into stringIO object, 
        creating html file with associated elements and formatting."""
        self.cur_ind = "\n" + cur_ind
        file_out.write(self.cur_ind)
        file_out.write(self.open_tag)
        for obj in range(len(self.content)):
            if self.content[obj]:
                if hasattr(self.content[obj], 'render'):
                    self.content[obj].render(file_out, (cur_ind + "    "))
                else:
                    file_out.write(self.content[obj])
        file_out.write(self.cur_ind + self.close_tag)


class Html(Element):
    """Html subclass of Element. Changes tags to 'html' tags."""

    def __init__(self):
        """Html object constructor."""
        open_tag = "<html>"
        close_tag = "</html>"
        Element.__init__(self, open_tag, close_tag)

    def render(self, file_out, cur_ind=""):
        """Render overide function to add DOCTYPE to top of page
        and then continue on to nromal render() processing."""
        file_out.write("<!DOCTYPE html>")
        super(Html, self).render(file_out)


class Body(Element):
    """Body subclass of Element. Changes tags to 'body' tags."""

    def __init__(self):
        """Body object constructor."""
        open_tag = "<body>"
        close_tag = "</body>"
        Element.__init__(self, open_tag, close_tag)


class P(Element):
    """Paragraph subclass of Element. Changes tags to 'p' tags."""

    def __init__(self, content=None, **attributes):
        """Paragraph object constructor."""
        open_tag = "<p>"
        close_tag = "</p>"
        Element.__init__(self, open_tag, close_tag, content, **attributes)


class Head(Element):
    """Head subclass of Element. Changes tags to 'head' tags."""

    def __init__(self):
        """Head object constructor."""
        open_tag = "<head>"
        close_tag = "</head>"
        Element.__init__(self, open_tag, close_tag)


class OneLineTag(Element):
    """Subclass of Element for tags that are called in-line
    and are not subject to normal render process."""

    def __init__(self, open_tag, close_tag, content=None):
        """OneLineTag object constructor."""
        self.open_tag = open_tag
        self.close_tag = close_tag
        self.content = content

        def render(self, file_out, cur_ind):
            """OneLineTag render function override."""
            file_out.write("{} {} {}".format(
                self.open_tag, self.content, self.close_tag))


class Title(OneLineTag):
    """Title subclass of OnelineTag. Changes tags to 'title' tags."""

    def __init__(self, content=None):
        """Title object constructor."""
        open_tag = "<title>"
        close_tag = "</title>"
        OneLineTag.__init__(self, open_tag, close_tag, content)


class H(OneLineTag):
    """Heading subclass of OnelineTag. Changes tags to 'h' tags."""

    def __init__(self, size, content=None):
        """Headign object constructor. Pulls in a given size to adjust
        size of heading. (<h2>, <h3>, etc.)"""
        open_tag = "<h{}>".format(size)
        close_tag = "</h{}>".format(size)
        OneLineTag.__init__(self, open_tag, close_tag, content)


class SelfClosingTag(Element):
    """Subclass of Element for tags that are opened and closed with one
    line and are not subject to normal render process."""

    def __init__(self, tag):
        """SelfClosingTag object constructor."""
        self.tag = tag

    def render(self, file_out, cur_ind):
        """SelfClosingTag render function override."""
        file_out.write(self.tag)


class Hr(SelfClosingTag):
    """Horizontal rule subclass of SelfClosingTag. Changes tag to 
    '<hr />' tags."""

    def __init__(self):
        """Horizontal rule object constructor."""
        tag = "<hr />"
        SelfClosingTag.__init__(self, tag)


class Br(SelfClosingTag):
    """Line break subclass of SelfClosingTag. Changes tag to 
    '<br />' tags."""

    def __init__(self):
        """Line break object constructor."""
        tag = "<br />"
        SelfClosingTag.__init__(self, tag)


class Meta(SelfClosingTag):
    """Meta subclass of SelfClosingTag. Changes tag to 
    <meta /> with an added charset value if given for encoding."""

    def __init__(self, charset):
        """Meta object constructor."""
        tag = '<meta charset="{}" />'.format(charset)
        SelfClosingTag.__init__(self, tag)


class A(Element):
    """Subclass of element. Changes tags to 'a' tags to allow
    links within the render."""

    def __init__(self, link, content):
        """A object constructor formats open tag to include
        given hyperlink and word to be hyperlinked."""
        open_tag = '<a href="{}">'.format(link)
        close_tag = "</a>"
        Element.__init__(self, open_tag, close_tag, content)


class Ul(Element):
    """Unordered list subclass of element. Changes tags to 'ul'
    tags."""

    def __init__(self, **kwargs):
        """Unordered list object constructor. Allows for Element
        attributes to be included in object creation."""
        open_tag = "<ul>"
        close_tag = "</ul>"
        Element.__init__(self, open_tag, close_tag, **kwargs)


class Li(Element):
    """List item subclass of Element. Changes tags to 'li'
    tags."""

    def __init__(self, content=None, **kwargs):
        """List item object constructor. Allows for Element
        attributes to be included in object creation."""
        open_tag = "<li>"
        close_tag = "</li>"
        Element.__init__(self, open_tag, close_tag, content, **kwargs)

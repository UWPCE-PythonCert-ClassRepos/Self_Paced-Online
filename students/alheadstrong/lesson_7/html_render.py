#!/usr/bin/env python3
import itertools


"""
A class-based system for rendering html.
"""

# This is the framework for the base class
class Element(object):
    """Base level object, not intended to be used alone."""

    tag = 'html'
    indent = '   '

    def __init__(self, content=None, **attributes):
        if content:
            self.content = [self.indent + content]
        else:
            self.content = []
        self.attributes = ''
        for key in attributes.keys():
            self.attributes += ' ' + key + '="' + attributes[key]+'"'


    def append(self, new_content):
        """Using append to render nested classes as they are appended."""
        try:
            nc = new_content.render_in_place()
            self.content += nc
        except AttributeError:
            self.content += [self.indent+new_content]


    def render(self, out_file):
        """Call render_in_place, flatten list, join with new line and write to outfile"""
        f = self.render_in_place()
        f = self.flatten(f)
        f = '\n'.join(f)
        out_file.write(f)

    def flatten(self, x):
        """From nested list return all items in 1D list."""
        result = []
        for i in x:
            if isinstance(i, str):
                result += [i]
            else:
                result.extend(self.flatten(i))
        return result

    def render_in_place(self):
        """Add tags, formatting and content"""
        rlist = [self.indent + '<' + self.tag + self.attributes + '>']
        for i in self.content:
            rlist += [self.indent+i]
        rlist += [self.indent + '</' + self.tag + '>']
        return rlist

class Html(Element):
    """Fist, instantiating class for HTML. Html tags are not indented, but
    render in place has been modified to allow a single string of content
    to be indented."""
    tag = 'html'
    indent = ''

    def render_in_place(self):
        """Over-write render_in_place to add Doctype. If a single string is passed in to
        the HTML object,it will get an indent, but this should be unusual."""
        rlist = []
        rlist += ['<!DOCTYPE html>']
        if len(self.content) == 1:
            self.content = [Element.indent + self.content[0]]
        rlist.extend([Element.render_in_place(self)])
        return rlist


class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'


class Head(Element):
    tag = 'head'


class OneLineTag(Element):
    """Base class for elements rendered on a single line."""
    def render_in_place(self):
        fstring = self.indent + '<' + self.tag + self.attributes + '>'
        for _ in self.content:
            fstring += '{}'
        fstring += '</' + self.tag + '>'
        return [fstring.format(*self.content)]


class Title(OneLineTag):
    tag = 'title'


class SelfClosingTag(Element):
    """Base class for elements with a single tag."""
    def __init__(self, **attributes):
        Element.__init__(self, content=None, **attributes)

        self.attributes = ''
        for key in attributes.keys():
            self.attributes += ' ' + key + '="' + str(attributes[key])+'"'

    def render_in_place(self):
        return [self.indent + '<' + self.tag + self.attributes + '/>']


class Hr(SelfClosingTag):
    tag = 'hr'


class Br(SelfClosingTag):
    tag = 'br'


class A(Element):
    """Class for the addition of links."""
    tag = 'a'

    def __init__(self, link, content):
        Element.__init__(self)
        self.link = link
        self.content = content

    def render_in_place(self):
        return [self.indent + '<' + self.tag + ' href=' + '"' + self.link + '"' '>' + self.content +
                '</' + self.tag + '>']


class Ul(Element):
    tag = 'ul'


class Li(Element):
    tag= 'li'


class H(OneLineTag):
    tag= 'h'

    def __init__(self, level, content):
        OneLineTag.__init__(self)
        self.content = content
        self.tag = H.tag + str(level)


class Meta(SelfClosingTag):
    tag= 'meta'


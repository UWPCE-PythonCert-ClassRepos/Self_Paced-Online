#!/usr/bin/env python3

class Element():
    """Generic html element."""
    indent_size = 4
    tag_types = ['html', 'body', 'p', 'head', 'title', 'hr', 'br', 'a', 'ul',
                 'li', 'h', 'meta']
    tag_type = 0

    def __init__(self, content=None, **kwargs):
        if content is None:
            self.content = []
        else:
            self.content = [content]
        self.attrs = kwargs

    def indent(self, status=True):
        """Turn indentation on (True) or off (False)"""
        if status:
            self.indent_size = 4
        else:
            self.indent_size = 0
        try:
            for c in self.content:
                if issubclass(type(c), Element):
                    c.indent(status)
        except AttributeError:
            pass

    def __str__(self):
        return self.tag()

    def append(self,newcontent):
        """Append new string or element to element's content list."""
        self.content.append(newcontent)

    def render(self, out_file, cur_ind=0):
        """
        Apply appropriate tags and indentation and output Element content to
        an open writable object.
        """
        out_file.write(self.tag(cur_ind))

    def apply_tag(self, cur_ind=0, tlist=None):
        """Return a list of html-tagged blocks of text. Apply tags and in-tag
        indentation to a string or Element object."""
        if tlist is None:
            tlist = []
        if isinstance(self,SelfClosingTag):
            tlist.append(self.closetag(cur_ind))
        else:
            tlist.append(self.opentag(cur_ind))
            for c in self.content:
                if isinstance(c, Element):
                    c.apply_tag(cur_ind+1, tlist)
                else:
                    tlist.append(self.line(c,cur_ind))
            tlist.append(self.closetag(cur_ind))
        return tlist

    def tag(self, cur_ind=0):
        """Returns a string of html-tagged text. Wrapper on apply_tag
        that returns a string instead of a list."""
        return ''.join(self.apply_tag(cur_ind))

    def opentag(self, ci):
        """Returns an open tag with indentation ci."""
        return ci * self.indent_size * ' ' + '<' + \
            self.tag_types[self.tag_type] + self.stattr() + '>\n'

    def closetag(self, ci):
        """Returns a close tag with indentation ci."""
        return ci * self.indent_size * ' ' + '</' + \
            self.tag_types[self.tag_type] + '>\n'

    def line(self, c, ci):
        """Returns a block of text with indentation and newlines."""
        return (ci + 1)*self.indent_size * ' ' + c + '\n'

    def stattr(self):
        """Returns a string of the user-specified attrs."""
        return ''.join([' ' + k + '="' + v + '"' for k,v in self.attrs.items()
            if k]) if self.attrs else ''

class Html(Element):
    tag_type = 0

    def render(self, out_file, cur_ind=0):
        """
        Apply appropriate tags and indentation and output Element content to
        an open writable object.
        """
        out_file.write('<!DOCTYPE html>\n' + self.tag(cur_ind))

class Body(Element):
    tag_type = 1

class P(Element):
    tag_type = 2

class Head(Element):
    tag_type = 3

class OneLineTag(Element):
    def opentag(self, ci):
        """Returns an open tag with indentation ci."""
        return ci * self.indent_size * ' ' + '<' + \
            self.tag_types[self.tag_type] + self.stattr() + '>'

    def closetag(self, ci):
        """Returns a close tag with indentation ci."""
        return '</' + self.tag_types[self.tag_type] + '>\n'

    def line(self, c, ci):
        """Returns a block of text with indentation and newlines."""
        return c

class Title(OneLineTag):
    tag_type = 4

class SelfClosingTag(Element):
    class ContentError(Exception):
        """Throw an error if user attempts to add content to SelfClosingTag
        instance"""
        expression = 'Content cannot be added to a SelfClosingTag'

    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise self.ContentError
        self.attrs = kwargs

    def append(self,newcontent):
        raise self.ContentError

    def closetag(self, ci):
        """Returns a close tag with indentation ci."""
        return ci * self.indent_size * ' ' + '<' + \
            self.tag_types[self.tag_type] + self.stattr() + ' />\n'

class Hr(SelfClosingTag):
    tag_type = 5

class Br(SelfClosingTag):
    tag_type = 6

class A(OneLineTag):
    """Html link element"""
    tag_type = 7

    def __init__(self, link, content):
        self.link = link
        self.attrs = {'href': link}
        self.content = [content]

class Ul(Element):
    """Html unordered list."""
    tag_type = 8

class Li(Element):
    """Html list element."""
    tag_type = 9

class H(OneLineTag):
    """Html header element"""
    tag_type = 10

    def __init__(self, level, content=None, **kwargs):
        if content is None:
            self.content = []
        else:
            self.content = [content]
        self.attrs = kwargs
        self.level = int(level)

    def opentag(self, ci):
        """Returns an open tag with indentation ci."""
        return ci * self.indent_size * ' ' + '<' + \
            self.tag_types[self.tag_type] + str(self.level) + self.stattr() + \
            '>'

    def closetag(self, ci):
        """Returns a close tag with indentation ci."""
        return '</' + self.tag_types[self.tag_type] + str(self.level) + '>\n'

class Meta(SelfClosingTag):
    """Html meta tag type"""
    tag_type = 11

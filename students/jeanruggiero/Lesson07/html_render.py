#!/usr/bin/env python3

class Element():

    indent_size = 4
    tag_types = ['html', 'body', 'p', 'head', 'title', 'hr', 'br']

    tag_type = 0

    def __init__(self, content=None, **kwargs):
        if content is None:
            self.content = []
        else:
            self.content = [content]

        self.attrs = kwargs

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
        return ' ' + ''.join([k + '="' + v + '"' for k,v in self.attrs.items()
            if k]) if self.attrs else ''



class Html(Element):
    tag_type = 0

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
            self.tag_types[self.tag_type] + ' />\n'


class Hr(SelfClosingTag):
    tag_type = 5

class Br(SelfClosingTag):
    tag_type = 6

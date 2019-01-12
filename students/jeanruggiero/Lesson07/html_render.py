#!/usr/bin/env python3

class Element():

    indent_size = 4
    tag_types = ['html', 'body', 'p', 'head', 'meta', 'title']

    tag_type = 0

    def __init__(self, content=None):
        if content is None:
            self.content = []
        else:
            self.content = [content]

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
            self.tag_types[self.tag_type] + '>\n'

    def closetag(self, ci):
        """Returns a close tag with indentation ci."""
        return ci * self.indent_size * ' ' + '</' + \
            self.tag_types[self.tag_type] + '>\n'

    def line(self, c, ci):
        """Returns a block of text with indentation and newlines."""
        return (ci + 1)*self.indent_size * ' ' + c + '\n'



class Html(Element):

    tag_type = 0


class Body(Element):

    tag_type = 1

class P(Element):

    tag_type = 2

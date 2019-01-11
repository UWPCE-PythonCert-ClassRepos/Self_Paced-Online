#!/usr/bin/env python3

class Element():

    indent_size = 4
    tag_types = ['html', 'head', 'meta', 'title']

    def __init__(self, content=[], tag_type=0):
        if not content:
            self.content = []
        else:
            self.content = [content]
        self.tag_type = tag_type

    def __str__(self):
        return ''.join([self.tag(c) for c in self.content])

    def append(self,newcontent):
        """Append new string to element's content list."""
        self.content.append(newcontent)

    def render(self, out_file, cur_ind=0):
        """
        Apply appropriate tags and indentation and output Element content to
        an open writable file-like object.
        """
        out_file.write(''.join([self.tag(c,cur_ind) for c in self.content]))

    def tag(self, c, cur_ind=0):
        """Apply tags and in-tag indentation to a string."""
        t = self.tag_types[self.tag_type]
        ind = self.indent_size
        return '<' + t + '>\n' + ' '*(ind) + c + '\n<\\' + t + '>\n'

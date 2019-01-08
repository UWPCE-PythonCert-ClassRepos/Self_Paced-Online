#!/usr/bin/env python3.7

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag = 'html'

    def __init__(self, content=None):
        if content is not None:
            self.contents = [content]
            print("contents is:", self.contents)
        else:
            self.contents = []

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file):
        # loop through the list of contents:
        for content in self.contents:
            out_file.write("<{}>\n".format(self.tag))
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
            out_file.write("\n")
            out_file.write("</{}>\n".format(self.tag))

"""
# This is the old render...

    def render(self, out_file):
        # loop through the list of contents:
        out_file.write("<{}>\n".format(self.tag))
        for content in self.contents:
            out_file.write(content)
            out_file.write("\n")
        out_file.write("</{}>\n".format(self.tag))


# The next render...

    def render(self, out_file):
    # loop through the list of contents:
    for content in self.contents:
        out_file.write("<{}>\n".format(self.tag))
        # out_file.write(content)
        content.render(out_file)
        out_file.write("\n")
        out_file.write("</{}>\n".format(self.tag))

"""


class Body(Element):
    tag = 'body'

class Html(Element):
    tag = 'html'

class P(Element):
    tag = 'p'

class Head(Element):
    tag = 'head'

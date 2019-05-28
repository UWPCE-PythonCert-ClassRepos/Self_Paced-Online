#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag = "html"

    def __init__(self, content=None):
        if content == None:
            self.contents = []
        else:
            self.contents = [content]

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file, **attrs):
        # out_file.write("just something as a place holder...")
        out_file.write(f"<{self.tag}>\n")
        for content in self.contents:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
            out_file.write('\n')
        out_file.write(f"</{self.tag}>")

class Html(Element):
    tag = 'html'

class Body(Element):
    tag = 'body'

class P(Element):
    tag = 'p'

class Head(Element):
    tag = 'head'

class OneLineTag(Element):
    def render(self, out_file, **attrs):
        # out_file.write(f"<{self.tag}>")
        # out_file.write(content)
        # out_file.write(f"</{self.tag}>")
        out_file.write(f"<{self.tag}>{self.contents[0]}</{self.tag}>\n")

            
    def append(self,content):
        raise NotImplementedError

class Title(OneLineTag):
    tag = 'title'

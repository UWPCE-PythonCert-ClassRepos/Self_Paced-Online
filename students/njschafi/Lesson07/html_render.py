#!/usr/bin/env python3

# NEIMA SCHAFI, LESSON 7 Assignment - HTML RENDERER

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    """Main class for object"""
    tag = 'html'
    indent = '   '

    def __init__(self, content=None, **kwargs):
        """Default Object initializer"""
        if content is not None:
            self.stuff = [content]
        elif content is None:
            self.stuff = []
        self.attributes = kwargs

    def append(self, new_content):
        """Appends new material to object content list"""
        self.stuff.append(new_content)

    def render(self, out_file, cur_int=""):
        """Renders content and tags to text and writes to file"""
        out_file.write(cur_int + '<{}'.format(self.tag))
        for key, value in self.attributes.items():
            out_file.write(' {}="{}"'.format(key, value))
        out_file.write('>\n')
        for item in self.stuff:
            if isinstance(item, Element):
                item.render(out_file, cur_int + self.indent)
                out_file.write('\n')
            else:
                out_file.write(cur_int + self.indent + item + '\n')
        out_file.write(cur_int + '</{}>'.format(self.tag))


class Html(Element):
    tag = 'html'

    def render(self, out_file, cur_int=""):
        out_file.write(cur_int + "<!DOCTYPE html>\n")
        Element.render(self, out_file, cur_int)


class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'


class Head(Element):
    tag = 'head'


class OneLineTag(Element):
    """Subclass of Element that allows for one line tagging"""

    def render(self, out_file, cur_int=""):
        """Renders contents and tags onto a single line"""
        out_file.write(cur_int + '<{}'.format(self.tag))
        for key, value in self.attributes.items():
            out_file.write(' {}="{}"'.format(key, value))
        out_file.write('>')
        for item in self.stuff:
            out_file.write(item)
        out_file.write('</{}>'.format(self.tag))

    def append(self, content):
        raise NotImplementedError


class Title(OneLineTag):
    tag = 'title'


class SelfClosingTag(Element):
    """Subclass of Element that allows for self closing tags"""

    def render(self, out_file, cur_int=""):
        """Renders contents for self closing tags"""
        # raise an exception if there is content
        out_file.write(cur_int + '<{}'.format(self.tag))
        for key, value in self.attributes.items():
            out_file.write(' {}="{}"'.format(key, value))
        if self.stuff:
            raise TypeError
        out_file.write(' />')


class Hr(SelfClosingTag):
    tag = 'hr'


class Br(SelfClosingTag):
    tag = 'br'


class A(OneLineTag):
    tag = 'a'

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)


class Ul(Element):
    tag = 'ul'


class Li(Element):
    tag = 'li'


class H(OneLineTag):
    tag = 'h'

    def __init__(self, level, content=None, **kwargs):
        super().__init__(content, **kwargs)
        self.level = level
        self.tag = ('h{}'.format(level))


class Meta(SelfClosingTag):
    tag = 'meta'

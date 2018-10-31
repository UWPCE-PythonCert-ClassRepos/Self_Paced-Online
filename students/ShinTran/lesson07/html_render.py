'''
Shin Tran
Python 210
Assignment 7
'''

#!/usr/bin/env python3

# A class-based system for rendering html.


# This is the framework for the base class
class Element(object):

    _Indent = '    '    # Default indent of 4 spaces
    tag = 'html'        # Default tag name set to 'html'

    # Initializes the program, if there's no content, returns an empty list
    # the style parameter is for formatting a specific tag 
    def __init__(self, content=None, **style):
        self.style = style
        if content != None:
            self.content_list = [content]
        else:
            self.content_list = []

    # Adds the tags and content to a list
    def append(self, new_content):
        self.content_list.append(new_content)

    # Prints out the opening and closing tags and content to a user specified html file
    # Indentation and formatting will depend on what parameter(s) are passed in
    def render(self, out_file, indent = ''):
        out_file.write(indent + "<{}{}>\n".format(self.tag, self.style_string()))
        for item in self.content_list:
            if hasattr(item, 'render'):
                item.render(out_file, self._Indent + indent)
            else:
                out_file.write(self._Indent + indent + item + "\n")
        out_file.write(indent + "</{}>\n".format(self.tag))

    # If attributes are passed in, it'll be formatted into a string
    # This method will retrn the formatted string
    # That string will be placed in a specified tag
    def style_string(self):
        string = ''
        if self.style:
            for k, v in self.style.items():
                string += ' {}="{}"'.format(k, v)
        return string

# Html tag that extends Element
# Prints out a Doctype tag at the beginning of the output file 
class Html(Element):
    tag = 'html'
    def render(self, out_file, indent = ''):
        out_file.write("<!DOCTYPE html>\n")
        super().render(out_file, indent)

# Body tag that extends Element
class Body(Element):
    tag = 'body'

# P tag that extends Element
class P(Element):
    tag = 'p'

# Head tag that extends Element
class Head(Element):
    tag = 'head'

# One lined tag that extends Element
# Prints everything in one line instead of one item per line
# E.g., <tag> content </tag>
class OneLineElement(Element):
    def render(self, out_file, indent = ''):
        out_file.write(indent + "<{}{}>".format(self.tag, self.style_string()))
        for item in self.content_list:
            if hasattr(item, 'render'):
                item.render(out_file,indent)
            else:
                out_file.write(item)
        out_file.write("</{}>\n".format(self.tag))

# Title tag extends OneLineElement
class Title(OneLineElement):
    tag = 'title'

# Self closing tag that doesn't have an opening tag
# E.g., < tag />
class SelfClosing(Element):
    def render(self, out_file, indent = ''):
        for item in self.content_list:
            if hasattr(item, 'render'):
                item.render(out_file, self._Indent + indent)
            else:
                out_file.write(self._Indent + indent + item + "\n")
        out_file.write(indent + "<{}{} />\n".format(self.tag, self.style_string()))

# Br tag that extends SelfClosing
class Br(SelfClosing):
    tag = 'br'

# Hr tag that extends SelfClosing
class Hr(SelfClosing):
    tag = 'hr'

# A tag that extends OneLineElement
# Includes a hyperlink with the content
class A(OneLineElement):
    tag = 'a'
    def __init__(self, link, content):
        super().__init__(content, href = link)

# Ul tag that extends Element
class Ul(Element):
    tag = 'ul'

# Li tag that extends Element
class Li(Element):
    tag = 'li'

# H tag that extends OneLineElement
# Takes in an int as a parameter and is used in the h tag
# E.g., <h9> content</h9>
class H(OneLineElement):
    tag = 'h'
    def __init__(self, head_int, content):
        self.tag = 'h' + str(head_int)
        super().__init__(content)

# Meta tag that extends SelfClosing
class Meta(SelfClosing):
    tag = 'meta'
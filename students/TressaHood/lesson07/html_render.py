#!/usr/bin/env python3

"""
Lesson 07, HTML rendering/class assignment
A class-based system for rendering html
"""


def style_format(dict=None):
    """Creating a helper style function that puts the style elements into a list, and then
    iterates through them depending on how many
    :return: the formated string for style options
    """
    style_options = []

    if dict is not None:
        for k, v in dict.items():
            style_options.append(" {}=\"{}\"".format(k, v))
    return " ".join(style_options)


class TextWrapper:
    """
    A wrapper function that wraps text for out put
    """

    def __init__(self, text):
        self.text = text

    def render(self, file_out, cur_ind=""):
        file_out.write(cur_ind)
        file_out.write(self.text)


class Element(object):
    """The base class for the entire project
    :attribute tag: the tag for the type of formatting necessary, defaults to 'html'
    :attribute indent: the number of indents for the html
    """

    tag = "html"
    indent = 4 * " "

    def __init__(self, content=None, **kwargs):
        """this function initializes
        """

        if content is not None:
            self.contents = [content]
        else:
            self.contents = []

        # set the kwargs for style
        self.kwargs = kwargs

    def append(self, new_content):
        """This function appends new content/list/string"""
        self.contents.append(new_content)

    def render(self, out_file, cur_ind=""):
        """This function renders the html page"""
        new_ind = cur_ind + self.indent
        out_file.write(
            "{}<{}{}>\n".format(
                cur_ind,
                self.tag,
                style_format(
                    self.kwargs)))

        # loop through it and have a try/catch block for errors
        for content in self.contents:
            try:
                content.render(out_file, new_ind)
            except AttributeError:
                out_file.write("{}{}\n".format(new_ind, str(content)))
        out_file.write("{}</{}>\n".format(cur_ind, self.tag))


class Html(Element):
    """Class that changes the tag to html"""

    # add the render attribute
    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind + "<!DOCTYPE html>\n")
        Element.render(self, out_file, cur_ind=cur_ind)


class Body(Element):
    """Class that changes the tag to body"""

    tag = "body"


class P(Element):
    """Class that changes the tag to paragraphs"""

    tag = "p"


class Head(Element):
    """Class that changes the tag to header"""

    tag = "head"


class OneLineTag(Element):
    """Class that adapts for one line tags"""

    def render(self, out_file, cur_ind="", **kwargs):

        # set new indents
        new_ind = cur_ind + self.indent

        # write to file
        out_file.write(
            "{}<{}{}>".format(
                cur_ind,
                self.tag,
                style_format(
                    self.kwargs)))

        # iterate through catching error
        for content in self.contents:
            try:
                content.render(out_file, new_ind)
            except AttributeError:
                out_file.write(str(content) + " ")

        out_file.write("</{}>\n".format(self.tag))


class Title(OneLineTag):
    """Class that changes one line tag to title"""
    tag = "title"


class A(OneLineTag):
    """Class that changes one line tag to a, for links"""
    tag = "a"

    def __init__(self, link, content):
        """this function initializes"""
        OneLineTag.__init__(self, href=link, content=content)


class Ul(Element):
    """Class that changes tag to ul"""
    tag = "ul"


class Li(Element):
    """Class that changes tag to li"""
    tag = "li"


class SelfClosingTag(Element):
    """Class that changes tag a closing tag"""

    def render(self, out_file, cur_ind='', **kwargs):
        """this function renders the new formating for closing tags"""
        out_file.write("{}<{}{} />\n".format(cur_ind,
                                             self.tag, style_format(self.kwargs)))


class Br(SelfClosingTag):
    """Class that changes the closing tag to breaks"""
    tag = "br"


class Meta(SelfClosingTag):
    """Class that changes the closing tag to meta"""
    tag = "meta"


class Hr(SelfClosingTag):
    """Class that changes the closing tag to hr"""
    tag = "hr"


class H(OneLineTag):
    """Class that changes the one line tag to deal with different levels of paragraphs"""

    def __init__(self, l, content):
        """this function initializes"""
        OneLineTag.__init__(self, content=content)
        self.tag = "h{}".format(l)

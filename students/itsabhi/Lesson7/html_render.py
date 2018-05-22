#!/usr/bin/env python3


class Element:

    tag = ""
    indent = "   "

    def __init__(self, content=None, **kwargs):
        # Takes optional keyword arguments that can be used to initialize additional element parameters like font etc.
        if isinstance(content, str):
            # Initializes a list with the content
            self.content = [str(content)]
            for key in kwargs:
                self.another_attrib_key = key
                self.another_attrib_value = kwargs[key]
        else:
            self.content = []

    def append(self, add_content):
        self.content.append(add_content)

    def render(self, file_out, cur_ind=""):
        # Goes through the content list and renders each list item. If the item is an Element object,
        # then it does recursive call to render method, else for string object it writes to file.

        # Uncomment below line for Step 1
        # self.tag = "html"
        f = file_out
        if hasattr(self, "another_attrib_value"):
            f.write(self.opening_tag_w_attribute(cur_ind) + '\n')
        else:
            f.write(cur_ind+'<' + self.tag + '>' + '\n')
        for component in self.content:
            try:
                component.render(file_out, cur_ind+self.indent)
            except AttributeError:
                f.write(cur_ind+component)
                f.write('\n')
        f.write(cur_ind+'<\\'+self.tag+'>'+'\n')

    def opening_tag_w_attribute(self, cur_ind):
        tag_str = cur_ind+'<'+self.tag+' '+self.another_attrib_key+':'+'"'+self.another_attrib_value+'"'+'>'
        return tag_str


class Html(Element):
    tag = "html"

    def render(self, file_out, cur_ind=""):
        f = file_out
        f.write('<!DOCTYPE html>'+'\n')
        Element.render(self, f)


class Body(Element):
    tag = "body"


class P(Element):
    tag = "p"


class Head(Element):
    tag = "head"


class OneLineTag(Element):

    def render(self, file_out, cur_ind=""):
        # Renders everything on one line
        f = file_out

        # Ignore below line, this was used in Step 4
        # f.write('<' + self.tag + '>')
        if hasattr(self, "another_attrib_value"):
            # Ignore below line, this was used in Step 3
            # f.write('<'+self.tag+' '+self.another_attrib_key+':'+'"'+self.another_attrib_value+'"'+'>')
            f.write(self.opening_tag_w_attribute(cur_ind))
        else:
            f.write(cur_ind+'<' + self.tag + '>')
        for component in self.content:
            try:
                component.render(file_out, cur_ind)
            except AttributeError:
                f.write(component)
        f.write('<\\' + self.tag + '>' + '\n')


class Title(OneLineTag):

    tag = "Title"


class SelfClosingTag(Element):

    def __init__(self, content=None, **kwargs):
        # Raises a TypeError if object being initialized with content
        if isinstance(content, str):
            raise TypeError('Do not set content for SelfClosingTag objects.')
        else:
            self.content = []

    def render(self, file_out, cur_ind=""):
        #Overrides the base class render() by omitting the render of 'end' tag
        f = file_out
        if hasattr(self, "another_attrib_value"):
            f.write(self.opening_tag_w_attribute(cur_ind))
        else:
            f.write(cur_ind+'<' + self.tag + '>' + '\n')
        for component in self.content:
            try:
                component.render(file_out)
            except AttributeError:
                f.write(component)


class Hr(SelfClosingTag):

    tag = "hr /"


class Br(SelfClosingTag):

    tag = "br /"


class A(Element):
# Creates 'A' tag by calling the base class init method and parsing the hypertext as optional keyword attributes
    tag = "a"

    def __init__(self, link, content):
        # Overrides the Element init method
        hypertext = link
        content = content
        kwargs = {"href": hypertext}
        Element.__init__(self, content, **kwargs)


class Ul(Element):

    tag = "ul"


class Li(Element):

    tag = "li"


class H(OneLineTag):

    tag = "h"

    def __init__(self, header_level, content):
        #Creates Header tag (eg. h1, h2 etc.) by calling the base class init method
        self.tag += str(header_level)
        kwargs = {}
        OneLineTag.__init__(self, content, **kwargs)


class Meta(SelfClosingTag):

    tag = "meta charset=\"UTF-8\" /"


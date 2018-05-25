class Element:
    """Base class to run functions"""
    tag = ""
    indent = "  "

    def __init__(self, content=None, **kwargs):
        self.content = []
        if content: self.content.append(content)
        self.attributes = kwargs

    def append(self, content):
        """append content to the element class object"""
        self.content.append(content)

    def render(self, file_out, cur_ind=0):
        """general render for html file"""
        tagstring = (cur_ind*self.indent) + "<{}".format(self.tag)
        if self.attributes:
            for key, value in self.attributes.items():
                tagstring += " {}=\"{}\"".format(key, value)
        tagstring += ">\n"
        file_out.write(tagstring)
        for item in self.content:
            try:
                item.render(file_out, cur_ind + 1)
            except AttributeError:
                file_out.write((cur_ind*self.indent) + "{}\n".format(item))
        file_out.write((cur_ind*self.indent) + "</{}>\n".format(self.tag))


class OneLineTag(Element):
    """Single line Element sublclass"""

    def render(self, file_out, cur_ind=0):
        """unique render for single line element"""
        tagstring = (cur_ind*self.indent) + "<{}".format(self.tag)
        if self.attributes:
            for key, value in self.attributes.items():
                tagstring += " {}=\"{}\"".format(key, value)
        tagstring += ">"
        file_out.write(tagstring)
        for item in self.content:
            file_out.write(item)
        file_out.write("</{}>\n".format(self.tag))


class SelfClosingTag(Element):
    """Self closing format tags with no content"""

    def __init__(self, **kwargs):
        self.attributes = kwargs

    def render(self, file_out, cur_ind=0):
        """unique render for self closing tags"""
        tagstring = (cur_ind*self.indent) + "<{}".format(self.tag)
        for key, value in self.attributes.items():
            tagstring += " {}=\"{}\"".format(key, value)
        tagstring += ">\n"
        file_out.write(tagstring)


class Html(Element):
    tag = 'html'

    def render(self, file_out, cur_ind=0):
        file_out.write("<!DOCTYPE html>\n")
        Element.render(self, file_out, cur_ind=0)


class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'


class Head(Element):
    tag = 'head'


class Title(OneLineTag):
    tag = "title"


class Hr(SelfClosingTag):
    tag = 'hr'


class Br(SelfClosingTag):
    tag = 'br'


class A(OneLineTag):
    tag = "a"

    def __init__(self, link, content):
        self.attributes = {"href": link}
        self.content = []
        if content: self.content.append(content)


class Ul(Element):
    tag = "ul"


class Li(Element):
    tag = "li"


class H(OneLineTag):

    def __init__(self, size, content, **kwargs):
        OneLineTag.__init__(self, content, **kwargs)
        self.size = size
        self.tag = "h{}".format(size)


class Meta(SelfClosingTag):
    tag = 'meta'

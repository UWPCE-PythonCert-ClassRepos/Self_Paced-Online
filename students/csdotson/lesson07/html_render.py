class Element:
    """Create an Element class for rendering an html element"""
    tag_name = "html"
    indentation = ""

    def __init__(self, content=None, **attrs):
        self.content = [content] if content else []
        self.attributes = attrs
        if isinstance(self, SelfClosingTag):
            if self.content:
                raise TypeError("Self closing tag cannot have content")

    def append(self, content_to_add):
        if isinstance(content_to_add, str):
            self.content.append(TextWrapper(content_to_add))
        else:
            self.content.append(content_to_add)

    def render(self, file_out, cur_ind=""):
        if self.attributes:
            for key, value in self.attributes.items():
                file_out.write("<"+self.tag_name+f" {key}=\"{value}\""+">\n")
        else:
            file_out.write("<"+self.tag_name+">\n")
        for elem in self.content:
            if isinstance(elem, str):
                elem = TextWrapper(elem)
            elem.render(file_out)
        file_out.write("</"+self.tag_name+">\n")


class Html(Element):
    tag_name = 'html'


class Head(Element):
    tag_name = 'head'


class Body(Element):
    tag_name = 'body'


class P(Element):
    tag_name = 'p'


class OneLineTag(Element):
    def render(self, file_out, cur_ind=""):
        open_tag = "<"+self.tag_name+">"
        close_tag = "</"+self.tag_name+">\n"
        file_out.write(open_tag + self.content[0] + close_tag)


class Title(OneLineTag):
    tag_name = 'title'


class SelfClosingTag(Element):
    def render(self, file_out, cur_ind=""):
        tag = "<"+self.tag_name+">\n"
        file_out.write(tag)


class Hr(SelfClosingTag):
    tag_name = 'hr'


class Br(SelfClosingTag):
    tag_name = 'br'


class TextWrapper:
    """
    A simple wrapper that creates a class with a render method
    for simple text
    """
    def __init__(self, text):
        self.text = text

    def render(self, file_out, cur_ind=""):
        # file_out.write(cur_ind)
        file_out.write(self.text)

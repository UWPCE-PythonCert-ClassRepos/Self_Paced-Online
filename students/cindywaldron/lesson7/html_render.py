#!/usr/bin/env python3

class Element:
    """Base class"""
    tag = "html"
    # indent 4 spaces
    indent = 4

    def __init__(self, content=None, **kwargs):
        self.a_list = []
        # there is  content
        if content is not None:
            # append content to a_list
            self.a_list.append(content)
        self.kwargs = kwargs

    def append(self, sub_element):
        self.a_list.append(sub_element)

    def render(self, file_out, cur_ind=""):
        # new indentation
        new_ind = cur_ind + ' '*self.indent
        file_out.write(cur_ind + "<{}".format(self.tag))
        for k, v in self.kwargs.items():
            file_out.write(" {}=\"{}\"".format(k, v))
        file_out.write(">\n")
        for item in self.a_list:
            if isinstance(item, str):
                file_out.write(new_ind + "{}\n".format(item))
            else:
                item.render(file_out, new_ind)

        file_out.write(cur_ind + "</{}>\n".format(self.tag))

class Html(Element):
    """Html subclass of Element"""
    tag = "html"

    def render(self, file_out, cur_ind=""):
        file_out.write("<!DOCTYPE html>\n")
        super().render(file_out,cur_ind)

class Body(Element):
    """Body subclass of Element"""
    tag = "body"

class P(Element):
    """P subclass of Element"""
    tag = "p"

class Head(Element):
    """Head subclass of Element"""
    tag = "head"

class OneLineTag(Element):
    """subclass of Element, tags + content are in one line"""
    def __init__(self, content, **kwargs):
        self.a_list = []
        if content is not None:
            self.a_list.append(content)
        self.kwargs = kwargs

    def render(self,file_out, cur_ind=""):
        file_out.write(cur_ind + "<{}".format(self.tag))
        for k, v in self.kwargs.items():
            file_out.write(" {}=\"{}\"".format(k, v))
        file_out.write(">")

        for item in self.a_list:
            if isinstance(item, str):
                file_out.write("{}".format(item))

        file_out.write("</{}>\n".format(self.tag))

class Title(OneLineTag):
    """Title subclass of OneLineTag"""
    tag = "title"

class SelfClosingTag(Element):
    """SelfClosingTag subclass of Element"""
    tag = ''

    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def append(self, sub_element):
        # raise TypeError is content is given
        raise TypeError

    def render(self, file_out, cur_ind=""):
        file_out.write(cur_ind + "<{}/> \n".format(self.tag))

class Hr(SelfClosingTag):
    tag = "hr"

class Br(SelfClosingTag):
    tag = "br"

class A(OneLineTag):
    tag = 'a'

    def __init__(self, link, content = None):
        super().__init__(content, **{"href":link})

class Ul(Element):
    """Ul subclass of Element"""
    tag = 'ul'

class Li(Element):
    """Li subclass of Element"""
    tag = 'li'

class H(OneLineTag):
    """H subclass of OneLineTag"""
    tag = ''

    def __init__(self, level, content=None):
        super().__init__(content)
        self.tag = "h{}".format(level)

class Meta(SelfClosingTag):
    """Meta subclass of SelfClosingTag"""
    tag = "meta charset"

    def render(self, file_out, cur_ind=""):
        file_out.write(cur_ind + "<{}=\"UTF-8\" /> \n".format(self.tag))
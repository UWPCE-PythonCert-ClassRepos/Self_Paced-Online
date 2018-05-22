class Element:

    tag = ''
    indent = '    '

    def __init__(self, content=None, **kwargs):
        if content is None:
            self.content = []
        else:
            self.content = [content]
        self.kwargs = kwargs

    def append(self, content):
        self.content.append(content)

    def render(self, file_out, cur_ind=""):
        file_out.write(cur_ind + "<{}".format(self.tag))
        for key, value in self.kwargs.items():
            file_out.write(' {}="{}"'.format(key, value))
        file_out.write(">\n")
        for item in self.content:
            if isinstance(item, Element):
                item.render(file_out, cur_ind + self.indent)
            else:
                file_out.write(cur_ind + self.indent + item + "\n")
        file_out.write(cur_ind + "</{}>\n".format(self.tag))


class Html(Element):

    tag = 'html'


class Body(Element):

    tag = 'body'


class P(Element):

    tag = 'p'


class Head(Element):

    tag = 'head'


class OneLineTag(Element):

    def render(self, file_out, cur_ind=""):
        file_out.write(cur_ind + "<{}".format(self.tag))
        for key, value in self.kwargs.items():
            file_out.write(' {}="{}"'.format(key, value))
        file_out.write(">")
        for item in self.content:
            if isinstance(item, Element):
                item.render(file_out)
            else:
                file_out.write(item)
        file_out.write("</{}>\n".format(self.tag))


class Title(OneLineTag):

    tag = 'title'


class SelfClosingTag(Element):

    def __init__(self, content=None, **kwargs):
        if content:
            raise TypeError('Error: the SelfClosingTag type does not take content.')
        self.kwargs = kwargs

    def render(self, file_out, cur_ind=""):
        file_out.write(cur_ind + "<{}".format(self.tag))
        for key, value in self.kwargs.items():
            file_out.write(' {}="{}"'.format(key, value))
        file_out.write(" />\n")


class Hr(SelfClosingTag):

    tag = 'hr'


class Br(SelfClosingTag):

    tag = 'br'


class A(OneLineTag):

    tag = 'a'

    def __init__(self, link, content):
        super().__init__(content, href=link)

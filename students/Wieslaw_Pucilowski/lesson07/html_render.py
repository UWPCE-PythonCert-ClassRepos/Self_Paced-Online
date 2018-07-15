
__author__ = 'Wieslaw Pucilowski'


class Element:
    tag = ""
    indent = "  "

    def __init__(self, content=None, **attributes):
        self.content = [content] if content else []
        self.attributes = attributes

    def append(self, element):
        # can be a string or element
        self.content.append(element)

    def render(self, file_out, cur_ind=""):
        file_out.write(cur_ind + '<{}'.format(self.tag,))
        for key, val in self.attributes.items():
            file_out.write(' {}="{}"'.format(key, val))
        file_out.write('>\n')
        for item in self.content:
            if isinstance(item, Element):
                # threads the state (intend depth)
                # through each recursive call,
                # cur_ind += self.indent
                item.render(file_out, cur_ind + self.indent)
            else:
                file_out.write(cur_ind + self.indent + item)
                file_out.write("\n")
        file_out.write(cur_ind + '</{}>\n'.format(self.tag))


class Html(Element):
    tag = 'html'

    def render(self, file_out, cur_ind=''):
        file_out.write('<!DOCTYPE html>\n')
        Element.render(self, file_out, cur_ind='')


class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'


class OneLineTag(Element):
    def render(self, file_out, cur_ind=""):
        file_out.write(cur_ind + "<{}".format(self.tag))
        for key, value in self.attributes.items():
            file_out.write(' {}="{}"'.format(key, value))
        file_out.write(">")  # no new line
        for item in self.content:
            if isinstance(item, Element):
                item.render(file_out, cur_ind + self.indent)
            else:
                file_out.write(item)
        file_out.write("</{}>\n".format(self.tag))


class Title(OneLineTag):
    tag = 'title'


class Head(Element):
    tag = 'head'


class SelfClosingTag (Element):
    # no content, __init__ overwriten
    def __init__(self, **attributes):
        self.attributes = attributes

    def render(self, file_out, cur_ind=""):
        file_out.write(cur_ind + "<{}".format(self.tag))
        for key, value in self.attributes.items():
            file_out.write(' {}="{}"'.format(key, value))
        file_out.write(" />\n")


class Hr(SelfClosingTag):
    tag = 'hr'


class Br(SelfClosingTag):
    tag = 'br'


class A(Element):
    tag = 'a'

    # mind order first link, then content and no attributes
    # hr.A("http://google.com", "link") kwargs h
    def __init__(self, link, content=None):
        # kwargs href="http://google.com"
        Element.__init__(self, content, href=link)


class Ul(Element):
    tag = 'ul'


class Li(Element):
    tag = 'li'


class H(OneLineTag):
    def __init__(self, level, content, **attributes):
        self.level = level
        self.tag = "h{}".format(level)
        self.content = [content] if content else []
        self.attributes = attributes


class Meta(SelfClosingTag):
    tag = 'meta'

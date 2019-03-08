class Element:
    """Class an Element class for rendering an html element"""
    tag = "html"
    indentation = " "

    def __init__(self, content=None, **attributes):
        if not content:
            self.content = []
        else:
            self.content = [content]
        self.attributes = attributes

    def append(self, item):
        # Only allow adding Elements or strings.
        if isinstance(item, Element) or isinstance(item, str):
            self.content.append(item)

    def render(self, file_out, cur_ind=" "):
        file_out.write(cur_ind + '<{}'.format(self.tag))
        for key, val in self.attributes.items():
            file_out.write(' {}="{}"'.format(key, val))
        file_out.write('>\n')

        for item in self.content:
            if isinstance(item, Element):
                item.render(file_out, cur_ind + self.indentation)
            elif isinstance(item, str):
                file_out.write(cur_ind + self.indentation + item + '\n')
            else:
                continue

        file_out.write(cur_ind + '</{}>\n'.format(self.tag))


class Html(Element):
    tag = 'html'

    def render(self, file_out, cur_ind=" "):
        file_out.write(cur_ind + "<!DOCTYPE html>\n")
        Element.render(self, file_out, cur_ind=" ")


class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'


class Head(Element):
    tag = 'head'


class OneLineTag(Element):
    def render(self, file_out, cur_ind=" "):
        file_out.write(cur_ind + '<{}'.format(self.tag))
        for key, val in self.attributes.items():
            file_out.write(' {}="{}"'.format(key, val))
        file_out.write('>')

        for item in self.content:
            if isinstance(item, Element):
                item.render(file_out, cur_ind + self.indentation)
            else:
                file_out.write(item)
        file_out.write('</{}>\n'.format(self.tag))


class Title(OneLineTag):
    tag = 'title'


class SelfClosingTag(Element):
    def render(self, file_out, cur_ind=" "):
        file_out.write(cur_ind + '<{}'.format(self.tag, ))
        for key, val in self.attributes.items():
            file_out.write(' {}="{}"'.format(key, val))
        file_out.write('/>\n')


class Hr(SelfClosingTag):
    tag = 'hr'


class Br(SelfClosingTag):
    tag = 'br'


class A(OneLineTag):
    tag = "a"

    def __init__(self, link, content):
        super().__init__(content, href=link)


class Ul(Element):
    tag = 'ul'


class Li(Element):
    tag = 'li'


class H(OneLineTag):
    tag = 'h'

    def __init__(self, level, content):
        super().__init__(content)
        self.tag = 'h{}'.format(level)


class Meta(SelfClosingTag):
    tag = 'meta'


# Brandon Henson
# 5/5/18
# Lesson 07 HTML Renderer




class Element:
    tag = ''
    indent = ' '

    def __init__(self, content=None, **attributes):
        self.attributes = attributes
        if content:
            self.content = [content]
        else:
            self.content = []

    def append(self, content):
        self.content.append(content)

    def render(self, file_out, cur_ind=''):
        file_out.write(f'{cur_ind}<{self.tag}{self.format_attributes()}>\n')

        for i in self.content:
            if hasattr(i, 'render'):
                i.render(file_out, cur_ind + self.indent)
            else:
                file_out.write(cur_ind + self.indent + str(i) + '\n')

        file_out.write(cur_ind + f'</{self.tag}>\n')

    def format_attributes(self):
        if self.attributes:
            attributes = ' ' + ' '.join(f'{k}="{v}"' for k, v in self.attributes.items())
        else:
            attributes = ''
        return attributes


class Html(Element):
    tag = 'html'


class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'


class Head(Element):
    tag = 'head'


class OneLineTag(Element):
    def render(self, file_out, cur_ind=''):
        file_out.write(f'{cur_ind}<{self.tag}{self.format_attributes()}> ')
        for i in self.content:
            if hasattr(i, 'render'):
                i.render(file_out, cur_ind + self.indent)
            else:
                file_out.write(str(i) + '  ')
        file_out.write(f'</{self.tag}>\n')


class Title(OneLineTag):
    tag = 'title'


class SelfClosingTag(Element):
    def render(self, file_out, cur_ind=''):
        file_out.write(f'{cur_ind}<{self.tag}{self.format_attributes()}/>\n')


class Hr(SelfClosingTag):
    tag = 'hr'


class Br(SelfClosingTag):
    tag = 'br'


class A(Element):
    tag = 'a'

    def __init__(self, link, content):
        super().__init__(content, href=link)


class Ul(Element):
    tag = 'ui'


class Li(Element):
    tag = 'li'


class H(OneLineTag):
    def __init__(self, level, content):
        super().__init__(content)
        self.tag = f'h{level}'


class Meta(SelfClosingTag):
    tag = 'meta'

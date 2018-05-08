# Lesson 07: Html Render
# Natalie Rodriguez
# May 01, 2018


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
        file_out.write(f'{cur_ind}<{self.tag}{self.fmt_attrs()}>\n')

        for item in self.content:
            if hasattr(item, 'render'):
                item.render(file_out, cur_ind + self.indent)
            else:
                file_out.write(cur_ind + self.indent + str(item) + '\n')

        file_out.write(cur_ind + f'</{self.tag}>\n')

    def fmt_attrs(self):
        if self.kwargs:
            attrs = ' ' + ' '.join(f'{k}="{v}"' for k, v in self.kwargs.items())
        else:
            attrs = ''
        return attrs

    def add_kwargs(self, file_out, cur_ind):
        file_out.write(f'{cur_ind}<{self.tag}')
        for k, v in self.kwargs.items():
            file_out.write(' {}="{}"'.format(k, v))


class Html(Element):
    tag = 'html'

    def render(self, file_out, cur_ind=''):
        file_out.write(f'{cur_ind}<!DOCTYPE html>\n')
        super().render(file_out, cur_ind)


class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'


class Head(Element):
    tag = 'head'


class OneLineTag(Element):

    def render(self, file_out, cur_ind=''):
        file_out.write('{}<{}>'.format(cur_ind, self.tag))

        for item in self.content:
            if hasattr(item, 'render'):
                item.render(file_out, cur_ind + self.indent)
            else:
                file_out.write(item)
        file_out.write('</{}>\n'.format(self.tag))


class Title(OneLineTag):
    tag = 'title'


class SelfClosingTag(Element):
    def render(self, file_out, cur_ind=''):
        self.add_kwargs(file_out, cur_ind)
        file_out.write(' />\n')


class Hr(SelfClosingTag):
    tag = 'hr'


class Br(SelfClosingTag):
    tag = 'br'


class A(Element):
    tag = 'a'

    def __init__(self, link, content):
        Element.__init__(self, content, href=link)


class Ul(Element):
    tag = 'ul'


class Li(Element):
    tag = 'li'


class H(OneLineTag):
    def __init__(self, level, content=None):
        super().__init__(content)
        self.tag = f'h{level}'


class Meta(SelfClosingTag):
    tag = 'meta'
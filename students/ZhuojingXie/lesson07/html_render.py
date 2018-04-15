class Element:
    tag = ''
    indent = '    '

    def __init__(self, content=None,**kwargs):
        if content is None:
            self.content = []
        else:
            self.content = [content]
        self.kwargs = kwargs


    def append(self, content):
        self.content.append(content)


    def render(self, file_out, cur_ind=''):

        file_out.write(cur_ind + '<{}'.format(self.tag,))
        for key, val in self.kwargs.items():
            file_out.write(' {}="{}"'.format(key, val))
        file_out.write('>\n')


        for item in self.content:
            try:
                file_out.write(cur_ind + self.indent + item)
                file_out.write('\n')
            except TypeError: #must be str, not Body
                item.render(file_out, cur_ind + self.indent)

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


class Head(Element):
    tag = 'head'

class OneLineTag(Element):
    def render(self,file_out,cur_ind):
        file_out.write(cur_ind + '<{}>'.format(self.tag))

        for item in self.content:
            try:
                file_out.write(cur_ind + self.indent + item)
                file_out.write('')
            except TypeError: #must be str, not Body
                item.render(file_out, cur_ind + self.indent)

        file_out.write(cur_ind + '</{}>\n'.format(self.tag))

class Title(OneLineTag):
    tag = 'title'


class SelfClosingTag(Element):
    def render(self,file_out,cur_ind):
        file_out.write(cur_ind + '<{}'.format(self.tag,))
        for key, val in self.kwargs.items():
            file_out.write(' {}="{}"'.format(key, val))
        file_out.write('>\n')

class Hr(SelfClosingTag):
    tag = 'hr'


class Br(SelfClosingTag):
    tag = 'br'

class A(Element):
    tag ='a'

    def __init__(self, link, content):
        super().__init__(content,href=link)


class Ul(Element):
    tag = 'ul'

class Li(Element):
    tag = 'li'

class H(OneLineTag):
    tag = 'h'

    def __init__(self, h, content, **kwargs):
        super().__init__(content, **kwargs)
        self.h = h
        self.tag = '{}{}'.format(self.tag, self.h)

class Meta(SelfClosingTag):
    tag = 'meta'

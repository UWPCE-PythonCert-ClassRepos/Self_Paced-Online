class Element:
    tag = 'html'
    indent = 4

    def __init__(self, content=None, **kwargs):
        if content is None:
            self.content = []
        else:
            self.content = [content]
        self.attr = kwargs

    def append(self, string):
        self.content.append(string)

    def render(self, file_out, cur_ind=None):
        self.render_open_tag(file_out, cur_ind, self.attr)
        file_out.write('\n')
        ind = 0 if cur_ind is None else cur_ind
        for item in self.content:
            if hasattr(item, 'render'):
                item.render(file_out, ind + 1)
            else:
                file_out.write(self.conv_ind(ind + 1) + item + '\n')
        file_out.write(self.conv_ind(cur_ind))
        self.render_close_tag(file_out)

    def render_open_tag(self, file_out, cur_ind=None, attr={}):
        file_out.write(self.conv_ind(cur_ind) + '<' + self.tag)
        for key, value in attr.items():
            file_out.write(' ' + key + '="' + value + '"')
        file_out.write('>')

    def conv_ind(self, cur_ind):
        return '' if cur_ind is None else cur_ind * ' ' * self.indent

    def render_close_tag(self, file_out):
        file_out.write('</' + self.tag + '>\n')


class Html(Element):
    tag = 'html'


class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'


class Head(Element):
    tag = 'head'


class OneLineTag(Element):
    def render(self, file_out, cur_ind=None):
        self.render_open_tag(file_out, cur_ind, self.attr)
        for item in self.content:
            file_out.write(item)
        self.render_close_tag(file_out)


class Title(OneLineTag):
    tag = 'title'


class SelfClosingTag(Element):
    def __init__(self):
        pass

    def render(self, file_out, cur_ind=None):
        self.render_open_tag(file_out, cur_ind)
        file_out.write('\n')


class Hr(SelfClosingTag):
    tag = 'hr /'


class Br(SelfClosingTag):
    tag = 'br /'


class A(OneLineTag):
    tag = 'a'

    def __init__(self, link, content):
        Element.__init__(self, content, href=link)

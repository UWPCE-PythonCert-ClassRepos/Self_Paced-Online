class Element:
    tag = 'html'
    indent = 0

    def __init__(self, content=None, **kwargs):
        if content is None:
            self.content = []
        else:
            self.content = [content]
        self.attr = kwargs 

    def append(self, string):
        self.content.append(string)

    def render(self, file_out, cur_ind=None):
        cur_ind = 0 if cur_ind is None else cur_ind
        ind = cur_ind * '    '
        file_out.write(ind + '<' + self.tag)
        for key, value in self.attr.items():
            file_out.write(' ' + key + '="' + value + '"')
        file_out.write('>\n')
        for item in self.content:
            if hasattr(item, 'render'):
                item.render(file_out, cur_ind + 1)
            else:
                file_out.write(ind + '    ' + item + '\n')
        file_out.write(ind + '</' + self.tag + '>\n')


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
        cur_ind = 0 if cur_ind is None else cur_ind
        ind = cur_ind * '    '
        file_out.write(ind + '<' + self.tag + '>')
        for item in self.content:
            file_out.write(item)
        file_out.write('</' + self.tag + '>\n')


class Title(OneLineTag):
    tag = 'title'

class Element:
    indent = '    '
    tag = ''
    left = '<'
    right = '>'

    def __init__(self, content=None, **kwargs):
        self.content = [content] if content else []
        self.html_data = kwargs

    def append(self, data):
        self.content.append(data)

    def render(self, file_out, cur_indent=''):
        file_out.write('{}{}{}'.format(cur_indent, self.left, self.tag))  # noqa: E501
        for k, v in self.html_data.items():
            file_out.write(' {}="{}"'.format(k, v))
        file_out.write('{}\n'.format(self.right))
        for contents in self.content:
            if isinstance(contents, Element):
                contents.render(file_out, cur_indent + self.indent)
            else:
                file_out.write(cur_indent + self.indent + contents)
                file_out.write('\n')
        file_out.write(cur_indent + "{}/{}{}\n".format(self.left, self.tag, self.right))  # noqa: E501


class Html(Element):
    tag = 'html'


class P(Element):
    tag = 'p'


class Body(Element):
    tag = 'body'


class Head(Element):
    tag = 'head'


class OneLineTag(Element):
    def render(self, file_out, cur_indent=''):
        file_out.write('{}{}{}{} '.format(cur_indent, self.left, self.tag, self.right))  # noqa: E501
        for contents in self.content:
            if isinstance(contents, Element):
                contents.render(file_out, cur_indent + self.indent)
            else:
                file_out.write(cur_indent + self.indent + contents)
                file_out.write(' ')
        file_out.write(cur_indent + "{}/{}{}\n".format(self.left, self.tag, self.right))  # noqa: E501


class Title(OneLineTag):
    tag = 'title'

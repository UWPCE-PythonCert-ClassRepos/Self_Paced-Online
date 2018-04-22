class Element(object):
    """renders an html element"""

    tag = ''
    indent = '    '

    def __init__(self, content=None):
        self.content = [content]

    def append(self, new_string):
        return self.content.append(new_string)

    def render(self, file_out, cur_ind=''):
        self.open_tag = '<' + self.tag + '>'
        self.close_tag = '</' + self.tag + '>'
        file_out.write(self.open_tag + '\n')
        for item in self.content:
            if item is None:
                file_out.write(cur_ind)
            elif type(item) == str:
                file_out.write(cur_ind * 3 + item + '\n')
                file_out.write(cur_ind * 2 + self.close_tag + '\n')
            else:
                item.render(file_out, cur_ind)
        if self.tag != 'html' and self.tag != 'p':
            file_out.write(cur_ind + self.close_tag + '\n')
        elif self. tag == 'html':
            file_out.write(self.close_tag)


class Html(Element):
    """renders html"""
    tag = 'html'


class Body(Element):
    """renders body"""
    tag = 'body'


class P(Element):
    """renders p"""
    tag = 'p'

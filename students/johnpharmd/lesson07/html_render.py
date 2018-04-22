class Element(object):
    """renders an html element"""

    tag = ''
    indent = '    '

    def __init__(self, content=None):
        self.content = [content]

    def append(self, new_string):
        # self.content = '<br>'.join([self.content, new_string])
        return self.content.append(new_string)

    def render(self, file_out, cur_ind=''):
        self.open_tag = '<' + self.tag + '>'
        self.close_tag = '</' + self.tag + '>'
        file_out.write(self.open_tag + '\n')
        # print('self.content ==', self.content)
        for item in self.content:
            if item is None:
                file_out.write(cur_ind + '')
            elif type(item) == str:
                file_out.write(cur_ind + item + '\n')
            else:
                item.render(file_out)
        file_out.write(self.close_tag + '\n')


class Html(Element):
    """renders html"""

    tag = 'html'
    # def __init__(self, content=''):
    #     self.open_tag = '<html>'
    #     self.close_tag = '</html>'
    #     self.content = [content]


class Body(Element):
    """renders body"""

    tag = 'body'
    # def __init__(self, content=''):
    #     self.open_tag = '<body>'
    #     self.close_tag = '</body>'
    #     self.content = [content]


class P(Element):
    """renders p"""

    tag = 'p'
    # def __init__(self, content=''):
    #     self.open_tag = '<p>'
    #     self.close_tag = '</p>'
    #     self.content = [content]

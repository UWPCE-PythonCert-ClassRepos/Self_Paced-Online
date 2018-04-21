class Element(object):
    """renders an html element"""

    tag = ''
    indent = '    '

    def __init__(self, content=''):
        self.open_tag = '<' + self.tag + '>'
        self.close_tag = '</' + self.tag + '>'
        self.content = [content]

    def append(self, new_string):
        # self.content = '<br>'.join([self.content, new_string])
        return self.content.append(new_string)

    def render(self, file_out, cur_ind=''):
        file_out.write(self.open_tag)
        print('open_tag ==', self.open_tag)
        print('self.content ==', self.content)
        for l in self.content:
            for s in l:
                file_out.write(cur_ind + s + '\n')
        file_out.write(self.close_tag)


class Html(Element):
    """renders html"""

    def __init__(self, content=''):
        self.open_tag = '<html>'
        self.close_tag = '</html>'
        self.content = [content]


class Body(Element):
    """renders body"""

    def __init__(self, content=''):
        self.open_tag = '<body>'
        self.close_tag = '</body>'
        self.content = [content]


class P(Element):
    """renders p"""

    def __init__(self, content=''):
        self.open_tag = '<p>'
        self.close_tag = '</p>'
        self.content = [content]

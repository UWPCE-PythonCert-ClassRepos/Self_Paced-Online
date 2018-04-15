class Element(object):
    """renders an html element"""

    tag = ''
    indent = ''

    def __init__(self, content=None):
        self.content = content
        self.content_list = [content]

    def render(self, cur_ind=''):
        return ('<{}>\n' + ' ' * int(cur_ind) + '{}\n'
                + '<\\{}>').format(self.tag,
                                   self.content, self.tag).strip('\'')


if __name__ == '__main__':
    e1 = Element()
    e1.tag = 'html'
    print(e1.render(cur_ind='4'))

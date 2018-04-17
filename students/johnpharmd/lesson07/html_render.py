class Element(object):
    """renders an html element"""

    tag = ''
    indent = 1

    def __init__(self, content=''):
        self.content = content

    def append(self, new_string):
        self.content = ' '.join([self.content, new_string])
        return self.content

    def render(self, file_out, cur_ind=''):
        output = (('<{}>\n' + self.indent * cur_ind + '{}\n'
                  + '<\\{}>').format(self.tag, self.content,
                                     self.tag).strip('\''))
        file_out.write(output)

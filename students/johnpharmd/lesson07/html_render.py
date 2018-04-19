class Element(object):
    """renders an html element"""

    tag = ''
    indent = 1

    def __init__(self, content=''):
        self.content = content
        self.content_list = ['<' + self.tag + '>', self.content,
                             '<\\' + self.tag + '>']

    def append(self, new_string):
        self.content = ' '.join([self.content, new_string])
        return self.content

    def render(self, file_out, cur_ind=''):
        output = (('<{}>\n' + self.indent * cur_ind + '{}\n'
                  + '<\\{}>').format(self.tag, self.content,
                                     self.tag).strip('\''))
        # https://stackoverflow.com/questions/4369159/replace-n-with-br
        file_out.write(output.replace('\n', '<br />'))

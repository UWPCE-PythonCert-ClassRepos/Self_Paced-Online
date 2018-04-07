class Element:
    indent = '    '

    def __init__(self, content=None):
        self.content = [content] if content else []

    def append_to_content(self, data):
        self.content.append(data)

    def render(self, file_out, cur_indent=''):
        x = ''
        file_out.write('{}<html>\n'.format(cur_indent))
        file_out.write('{}{}'.format(cur_indent, self.indent))
        for contents in self.content:
            x += contents
            x += ' '
        x += '\n'
        str_to_write = '{}'.format(cur_indent) + x
        file_out.write(str_to_write)
        file_out.write('{}<\html>\n'.format(cur_indent))

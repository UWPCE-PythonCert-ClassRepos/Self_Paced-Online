class Element():
    tag_name = 'html'
    indentation = 4

    def __init__(self, content = None):
        if content:
            self.content = content
        else:
            self.content = []
        self.text = None

    def append(self, new_content):
        self.content.append(new_content)

    def render(self, file_out, cur_ind=' '):
        self.text = '<' + self.tag_name + '>\n' + cur_ind*self.indentation +\
                    ' '.join([i for i in self.content]) + \
                     '\n</' + self.tag_name + '>'
class Element:
    """Creates html code for given inputs"""
    tag = 'html'

    def __init__(self, content = None):
        if content == None:
            self.contents = []
        else:
            self.contents = [content]

    def append(self, some_string):
        self.contents.append(some_string)

    def render(self, file_out):
            file_out.write("<{}>\n".format(self.tag))
            for content in self.contents:
                file_out.write(content)
                file_out.write('\n')
            file_out.write("<\{}>\n".format(self.tag))




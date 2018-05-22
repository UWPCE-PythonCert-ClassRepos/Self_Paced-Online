class Element:

    tag = 'html'
    indent = '    '

    def __init__(self, content=None, **kwargs):
        if content is None:
            self.content = []
        else:
            self.content = [content]
        self.kwargs = kwargs

    def append(self, content):
        self.content.append(content)

    def render(self, file_out, cur_ind=""):
        file_out.write(cur_ind + "<{}>\n".format(self.tag))
        for item in self.content:
            if isinstance(item, Element):
                item.render(file_out, cur_ind + self.indent)
            else:
                file_out.write(cur_ind + self.indent + item)
                file_out.write("\n")
        file_out.write(cur_ind + "</{}>\n".format(self.tag))

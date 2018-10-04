
class Element():
    tag = 'html'
    indent = ""

    def __init__(self, content=None):
        if content is None:
            self.content = []
        else:
            self.content = [content]

    def append(self, content_str):
        self.content.append(content_str)

    def render(self, file_out, cur_ind=""):
        file_out.write("<{}>\n".format(self.tag))
        for item in self.content:
            file_out.write("{}\n".format(item))
        file_out.write("</{}>\n".format(self.tag))

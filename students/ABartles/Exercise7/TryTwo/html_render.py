

class Element():
    tag = ""
    indent = "    "

    def __init__(self, content=None):
        if content is None:
            self.content = []
#        else:
#            self.content = content

    def append(self, str):
        self.content.append(str)

    def render(self, file_out, cur_int=""):
        file_out.write("<{}>\n".format(self.tag))
        for item in self.content:
           file_out.write("{}{}\n".format(self.indent, item))
        file_out.write("<{}\\>\n".format(self.tag))

class Html(Element):
    tag = "html"

class Body(Element):
    tag = "body"

class P(Element):
    tag = "p"

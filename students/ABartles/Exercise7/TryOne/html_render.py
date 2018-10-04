
class Element(object):
    tag = ""
    indent = "    "

    def __init__(self, content=None):
        if content == None:
            self.content = []
        else:
            self.content = [content]

    def append(self, str):
        self.content.append(str)

    def render(self, file_out, cur_indent=""):
        file_out.write("{}<{}>\n".format(cur_indent, self.tag))
        for item in self.content:
            file_out.write("{}{}{}\n".format(cur_indent, self.indent, item))
        file_out.write("{}<{}{}>\n".format(cur_indent, "\\", self.tag))



class Html(Element):
    tag = "html"

class Body(Element):
    tag = "body"

class P(Element):
    tag = "p"

class Element:
    tag = "html"
    indent = "    "*0

    def __init__(self, content=None):
        self.substance = () if content is None else (content,)

    def render(self, file_out, cur_ind=""):
        file_out.write(self.indent+'<'+self.tag+">\n")
        for x in self.substance:
            file_out.write(self.indent+cur_ind+x+'\n')
        file_out.write(self.indent+"</"+self.tag+">\n")

    def append(self, text):
        mutable_content = list(self.substance)
        mutable_content.append(text)
        self.substance = tuple(mutable_content)

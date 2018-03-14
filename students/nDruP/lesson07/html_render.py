class Element:
    tag = "html"
    indent = 0

    def __init__(self, content=None):
        self.substance = () if content is None else (content,)

    def render(self, file_out, cur_ind=""):
        file_out.write((self.indent*cur_ind)+'<'+self.tag+">\n")
        for x in self.substance:
            if issubclass(type(x), Element):
                x.indent = self.indent + 1
                x.render(file_out, cur_ind)
            elif type(x) is str:
                file_out.write((cur_ind*(self.indent+1))+str(x)+'\n')
        file_out.write((self.indent*cur_ind)+"</"+self.tag+">\n")

    def append(self, text):
        mutable_content = list(self.substance)
        mutable_content.append(text)
        self.substance = tuple(mutable_content)


class Html(Element):
    pass


class Body(Element):
    tag = "body"
    pass


class P(Element):
    tag = "p"
    pass
